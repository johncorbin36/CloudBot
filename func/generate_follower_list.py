import time
from config import follow_config
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# Generates new list of followers from set target, saves to list as txt file
def get_followers(browser, target):

    # Define vars
    actions = ActionChains(browser)
    actions.send_keys(Keys.LEFT_CONTROL, Keys.ARROW_DOWN)

    # Get user page
    browser.get('https://www.instagram.com/' + target + '/')
    time.sleep(3)

    # Load user followers
    browser.find_element_by_xpath('//*[@href="/' + target + '/followers/"]').click()
    time.sleep(5)

    # Load elements
    users = []
    while len(users) < follow_config['max_follow_list']:
        browser.execute_script('''
                               var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                               fDialog.scrollTop = fDialog.scrollHeight
                               ''')
        time.sleep(3)
        users = browser.find_elements_by_xpath('//*[@class="FPmhX notranslate  _0imsa "]')

    # Save user names to text file
    file = open('followerLists/' + target + '_users.txt', 'w')
    for user in users:
        username = user.get_attribute('title')
        file.write(username + '\n')

    file.close()
