import time
import datetime
import random
import os
import asyncio
from func import like, start_browser, follow


# Bot container
class CloudBot:
    def __init__(self):
        # Start browser
        self.browser = start_browser.start_browser()

    # Like function
    def start_liking_posts(self):
        like.start_like_run(self.browser)

    # Follow function
    def start_following_users(self):
        follow.start_follow_run(self.browser)


# Assign bot
bot = CloudBot()
bot.start_liking_posts()
print('Completed at ' + str(datetime.datetime.now()))
bot.start_following_users()
print('Completed at ' + str(datetime.datetime.now()))
