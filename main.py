import datetime
import random
import time
from func import like, start_browser, follow, unfollow


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

    # Unfollow function
    def start_unfollow_run(self):
        unfollow.start_unfollow_run(self.browser)


# Assign bot
bot = CloudBot()
i = 0
while i != 3:
    bot.start_liking_posts()
    print('Completed at ' + str(datetime.datetime.now()))
    #bot.start_following_users()
    #print('Completed at ' + str(datetime.datetime.now()))
    bot.start_unfollow_run()
    print('Completed at ' + str(datetime.datetime.now()))

    timeVar = random.randint(3600, 4500)
    print('Continuing run in ' + str(timeVar) + ' seconds.')
    time.sleep(timeVar)

    i += 1

bot.browser.close()
