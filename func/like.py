import time
from func import like_post
from random import randint
from config import like_config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Manages like run, counts likes, calls like_post
def start_like_run(browser):

    # Define vars
    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)

    # Get page and wait for content to load
    browser.get('https://www.instagram.com/explore/tags/' + like_config['tag_target'] + '/')
    time.sleep(5)

    # Skip trending posts
    trending = browser.find_elements_by_xpath('//*[@class="_9AhH0"]')
    trending[9].click()
    time.sleep(3)

    # Generate random number of likes
    low = like_config['like_limit'] - 5
    high = like_config['like_limit'] + 5
    limit = randint(low, high)
    print('Liking ' + str(limit) + ' photos.')

    # Start liking posts
    count = 0
    while count < limit:
        count = like_post.like_post(browser, count, actions)

    # Redirect browser back to homepage
    browser.get('https://www.instagram.com')
