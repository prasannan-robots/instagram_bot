"""Scheduled InstaPy session: likes posts from your feed and a few hashtags.

Environment: INSTA_USERNAME, INSTA_PASSWORD; optional MAIL_ADDRESS,
MAIL_PASSWORD and MAIL_TO for a "logged in" email.

Note: InstaPy is no longer maintained and may fail against current
Instagram; see README.
"""

import os
import time

import schedule
from instapy import InstaPy, set_workspace, smart_run

set_workspace(path=None)

TAGS = ["memes", "sinclairlab", "python", "neuralnetworks", "space"]


def notify():
    address, password, to = os.getenv("MAIL_ADDRESS"), os.getenv("MAIL_PASSWORD"), os.getenv("MAIL_TO")
    if not (address and password and to):
        return
    from mailer import Mailer

    # Separate mail credentials: this used to reuse the Instagram password.
    Mailer(email=address, password=password).send(
        receiver=to, no_reply="noreply@example.com",
        subject="Logged in to Instagram", message="The InstaPy session started.",
    )


def job():
    session = InstaPy(username=os.environ["INSTA_USERNAME"], password=os.environ["INSTA_PASSWORD"],
                      headless_browser=True)
    with smart_run(session):  # smart_run logs in and always ends the session
        session.set_quota_supervisor(
            enabled=True,
            sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
            sleepyhead=True,
            stochastic_flow=True,
            peak_likes_daily=100,
            peak_comments_daily=2,
            peak_follows_daily=None,
            peak_unfollows_daily=None,
            peak_server_calls_daily=4700,
        )
        # Filters must be set before liking; they used to be set afterwards.
        session.set_dont_like(["naked", "nsfw"])
        notify()
        session.like_by_feed(amount=100, randomize=True, interact=True, unfollow=False)
        session.like_by_tags(TAGS, amount=5)


if __name__ == "__main__":
    for at in ("12:35", "17:30", "20:25"):
        schedule.every().day.at(at).do(job)
    while True:
        schedule.run_pending()
        time.sleep(10)
