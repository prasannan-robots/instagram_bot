from instapy import InstaPy
import os


session = InstaPy(username=os.getenv("username"), password=os.getenv("password")).login()
session.set_quota_supervisor(enabled=True,
                            sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                            sleepyhead=True,
                            stochastic_flow=True,
                            peak_likes_daily=100,
                            peak_comments_daily=2,
                            peak_follows_daily=None,
                            peak_unfollows_daily=402,
                            peak_server_calls_daily=4700)
session.set_delimit_liking(enabled=True, max_likes=None, min_likes=30)
session.set_relationship_bounds(min_posts=10,
                                 max_posts=None)

                                 
session.login()
session.accept_follow_requests(amount=100, sleep_delay=1)
session.like_by_feed(amount=100, randomize=True, interact=True)

session.like_by_tags(["memes", "sinclairlab","python","neuralnetworks","space"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=10)
session.set_do_comment(True, percentage=20)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()
