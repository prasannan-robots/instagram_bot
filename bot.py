from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time
import os
from mailer import Mailer



#path to your workspace
set_workspace(path=None)

def job():
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
  mail = Mailer(email='vinayakarobotics@gmail.com',
              password='Vrprasanna@2005')
  mail.send(receiver='prasannanatarajan3595@gmail.com',  # Email From Any service Provider
          no_reply='noreplay@example.com', # Redirect receiver to another email when try to reply.
          subject='Logged In Instagram',
          message='Logged in from Insta')
  with smart_run(session):
      session.like_by_feed(amount=100, randomize=True, interact=True,unfollow=False)
      session.like_by_tags(["memes", "sinclairlab","python","neuralnetworks","space"], amount=5)
      session.set_dont_like(["naked", "nsfw"])

schedule.every().day.at("12:35").do(job)
schedule.every().day.at("17:30").do(job)
schedule.every().day.at("20:25").do(job)

while True:
  schedule.run_pending()
  time.sleep(10)

