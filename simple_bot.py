from instapy import InstaPy
import os

session = InstaPy(username=os.getenv("username"), password=os.getenv("password"), headless_browser=True).login()
session.set_quota_supervisor(enabled=True,
                            sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                            sleepyhead=True,
                            stochastic_flow=True,
                            peak_likes_daily=100,
                            peak_comments_daily=2,
                            peak_follows_daily=None,
                            peak_unfollows_daily=None,
                            peak_server_calls_daily=4700)
session.like_by_feed(amount=100, randomize=True, interact=True,unfollow=False)
session.like_by_tags(["memes", "sinclairlab","python","neuralnetworks","space"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.end()