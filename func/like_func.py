import time
from func import action_block_func, wait_func, database_func
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Like multiple posts
def like_posts(driver):

    # Handle multiple tags
    tags = database_func.get_config_value('tag_targets', 'like_config')
    tags = tags.split(', ')
    print(tags)
    likes_per_tag = database_func.get_config_value('limit', 'like_config') / int(len(tags))

    # For each tag
    for tag in tags:

        # Get page and wait for content to load
        driver.get('https://www.instagram.com/explore/tags/' + tag + '/')

        # Skip trending posts
        wait_func.wait_for_element(driver, 'CLASS_NAME', '_9AhH0')
        trending = driver.find_elements_by_xpath('//*[@class="_9AhH0"]')
        trending[9].click()

        # Generate random number of likes
        low = likes_per_tag - database_func.get_config_value('standard_deviation', 'like_config')
        high = likes_per_tag + database_func.get_config_value('standard_deviation', 'like_config')
        limit = randint(round(low), round(high))
        print('Liking ' + str(limit) + ' photos in tag: ' + tag)

        # Start liking posts
        count = 0
        users = []
        zero_count = 0
        while count < limit:

            # Like individual post
            count, users = like_post(driver, count, users, tag)

            # Check if count increased
            if count == 0:
                zero_count += 1
            if zero_count == 10:
                print('Action blocked. Returning.')
                # Call action block function
                return

    # Redirect driver back to homepage
    driver.get('https://www.instagram.com')


# Likes individual post and returns total likes
def like_post(driver, count, users, tag):

    # Set selenium actions
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_RIGHT)

    # Check if post embed has closed
    if driver.current_url == 'https://www.instagram.com/explore/tags/' + tag + '/':
        print('Post embed was closed, returning to previous post.')
        driver.find_element_by_xpath('//*[@class="_9AhH0"]').click()
        i = 0
        while i != count + 12:
            time.sleep(.2)
            actions.perform()
            i += 1
        print('Successfully returned to previous post, resuming with likes.')
        time.sleep(5)

    # Check for unlike button
    try:
        driver.find_element_by_xpath('//*[@aria-label="Unlike"]')
        print('Post already liked.')
        time.sleep(3)
        actions.perform()
        time.sleep(3)
        return count, users
    except:
        print('Post not liked, continuing.')

    # Count times username has appeared (if it has appeared at all)
    time.sleep(2)
    try:
        username = driver.find_element_by_xpath('//*[@class="sqdOP yWX7d     _8A5w5   ZIAjV "]').text
    except:
        username = ''
        print('Failed to gather username.')
    limit_counter = 0
    for user in users:
        if user == username:
            limit_counter += 1

    # Check if username entries pass max limit
    if limit_counter >= database_func.get_config_value('like_per_user_limit', 'like_config'):
        print('Max likes for this users posts reached, continuing to the next post.')
        time.sleep(3)
        actions.perform()
        time.sleep(3)
        return count, users
    else:
        users.append(username)

    # Like photo
    try:
        driver.find_element_by_xpath('//*[@aria-label="Like"]').click()
        count += 1
    except:
        actions.perform()
        time.sleep(10)

    # Check for action block
    action_block_func.exists(driver)

    # Get next post and return
    print('Post liked successfully. ' + str(count) + ' post(s) in total.')
    time.sleep(3)
    actions.perform()
    time.sleep(3)
    return count, users
