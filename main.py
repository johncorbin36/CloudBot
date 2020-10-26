import datetime
import random
import time
from func import follow_func, driver_func, database_func, like_func

'''
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
        follow_func.follow_users(self.browser)

    # Unfollow function
    def start_unfollow_run(self):
        unfollow.start_unfollow_run(self.browser)

    # Comment function
    #def start_comment_run(self):
        #comment.start_comment_run(self.browser)

    # Watch stories function
    def start_watching_stories(self):
        stories.start_watching_stories(self.browser)


# Assign bot
bot = CloudBot()

'''

# i = 0
#while i != 3:

driver = driver_func.start_driver()
follow_func.follow_users(driver)
like_func.like_posts(driver)

    # start_liking_posts()
    #bot.start_watching_stories()
    # print('Run completed at:' + str(datetime.datetime.now().hour) + ' ' + str(datetime.datetime.now().minute))

    # bot.browser.get('https://google.com')
    # timeVar = random.randint(3600, 7200)
    # print('Continuing run in ' + str(timeVar) + ' seconds.')
    # time.sleep(timeVar)

    # i += 1

#bot.browser.close()
