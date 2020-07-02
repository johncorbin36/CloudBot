import time
from config import unfollow_config


def start_unfollow_run(browser):

    # Get user profile and open following
    browser.get('https://www.instagram.com/' + unfollow_config['unfollow_target'] + '/')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@href="/' + unfollow_config['unfollow_target'] + '/following/"]').click()
    time.sleep(3)

    # Open unfollow blacklist and save names to array
    file = open('config/unfollow_blacklist.txt', 'r')
    blacklisted_users = []
    for user in file:
        blacklisted_users.append(user)
    file.close()

    # Load all elements to unfollow
    elements = []
    while len(elements) < unfollow_config['max_unfollows']:
        elements = browser.find_elements_by_xpath('//button[contains(text(), "Following")]')
        browser.execute_script('''
                               var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                               fDialog.scrollTop = fDialog.scrollHeight
                               ''')

    # Save username elements and unfollow button elements to list
    username = browser.find_elements_by_xpath('//*[@class="FPmhX notranslate  _0imsa "]')
    unfollow_button = browser.find_elements_by_xpath('//button[contains(text(), "Following")]')

    # Start to unfollow individual users
    count = 0
    while count != unfollow_config['max_unfollows']:
        count = unfollow_user(browser, count, blacklisted_users, username, unfollow_button)
        print('Unfollowed ' + str(count) + ' users out of ' + str(unfollow_config['max_unfollows']) + '.')

    # Finish
    browser.get('https://www.google.com')


# Function to unfollow individual user
def unfollow_user(browser, count, blacklisted_users, username, unfollow_button):

    # Save unfollow target username
    target = str(username[count].text)

    # Check if user is blacklisted
    for user in blacklisted_users:
        if user == target:
            print('User is blacklisted, returning.')
            return count

    # Unfollow user
    unfollow_button[count].click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@class="aOOlW -Cab_   "]').click()
    time.sleep(2)

    # Return
    print('Successfully unfollowed user: ' + target)
    count += 1
    return count
