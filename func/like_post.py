import time
from config import like_config


# Likes individual post and returns total likes
def like_post(browser, count, actions, users):

    # Check if post embed has closed
    if browser.current_url == 'https://www.instagram.com/explore/tags/' + like_config['tag_target'] + '/':
        print('Post embed was closed, returning to previous post.')
        browser.find_element_by_xpath('//*[@class="_9AhH0"]').click()
        i = 0
        while i != count + 12:
            time.sleep(.2)
            actions.perform()
            i += 1
        print('Successfully returned to previous post, resuming with likes.')
        time.sleep(5)

    # Check for unlike button
    try:
        browser.find_element_by_xpath('//*[@aria-label="Unlike"]')
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
        username = browser.find_element_by_xpath('//*[@class="sqdOP yWX7d     _8A5w5   ZIAjV "]').text
    except:
        username = ''
        print('Failed to gather username.')
    limit_counter = 0
    for user in users:
        if user == username:
            limit_counter += 1

    # Check if username entries pass max limit
    if limit_counter >= like_config['like_per_user_limit']:
        print('Max likes for this users posts reached, continuing to the next post.')
        time.sleep(3)
        actions.perform()
        time.sleep(3)
        return count, users
    else:
        users.append(username)

    # Like photo
    browser.find_element_by_xpath('//button[@class="wpO6b "]').click()
    count += 1

    # Get next post and return
    print('Post liked successfully. ' + str(count) + ' post(s) in total.')
    time.sleep(3)
    actions.perform()
    time.sleep(3)
    return count, users
