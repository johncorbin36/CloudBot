def startLikeRun(browser):
    import time
    from func import likePost
    from random import randint
    from config import likeConfig
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains

    # Define vars
    actions = ActionChains(browser)
    actions.send_keys(Keys.ARROW_RIGHT)

    # Get page and wait for content to load
    browser.get('https://www.instagram.com/explore/tags/' + likeConfig['tagTarget'] + '/')
    time.sleep(5)
    browser.find_element_by_xpath('//*[@class="_9AhH0"]').click()

    # Skip trending posts
    i = 0
    while i != 9:
        actions.perform()
        time.sleep(.2)
        i += 1
    time.sleep(3)

    # Generate random number of likes
    low = likeConfig['likeLimit'] - 5
    high = likeConfig['likeLimit'] + 5
    limit = randint(low, high)
    print('Liking ' + str(limit) + ' photos.')

    # Start liking posts
    count = 0
    while count < limit:
        count = likePost.likePost(browser, count, actions)

    # Redirect browser back to homepage
    browser.get('https://www.instagram.com')
