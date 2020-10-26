import random
import time
from func import database_func, wait_func


# Follow multiple users from follow list in database
def follow_users(driver):

    # Get followers list
    conn = database_func.connect_to_db()
    followers = conn.execute('SELECT username FROM follow_list').fetchall()
    conn.close()

    # Check if list is great enough to follow enough users
    if not len(followers) > database_func.get_config_value('limit_follows', 'follow_config'):
        add_to_follow_list(driver, database_func.get_config_value('target_list', 'follow_config'), len(followers))

    # Get all users from follow list and set variables for follow iterations
    all_users = database_func.get_column_data('username', 'follow_list')
    skipped_users = []
    followed_users = []

    # Follow users from list
    i = 0
    while len(followed_users) != database_func.get_config_value('limit_follows', 'follow_config'):

        # Attempt to follow user
        print('Attempting to follow user: ' + all_users[i][0])
        follow_result = follow_user(driver, all_users[i][0])

        # Add user to followed list or skip list
        if follow_result:
            followed_users.append(all_users[i][0])
        else:
            skipped_users.append(all_users[i][0])

        # Print remaining users to follow
        print('Number of users left to follow: ' +
              str(database_func.get_config_value('limit_follows', 'follow_config')))

        # Increase iteration
        i += 1

    # Delete followed and skipped users from database
    users_to_remove = followed_users + skipped_users
    database_func.remove_list_from_db(users_to_remove, 'follow_list', 'username')


# Add users to the follow list in sql database
def add_to_follow_list(driver, target, users_in_follow_list):

    # Get user page
    driver.get('https://www.instagram.com/' + target + '/')
    wait_func.wait_for_element(driver, 'XPATH', '//*[@href="/' + target + '/followers/"]')

    # Get user followers
    driver.find_element_by_xpath('//*[@href="/' + target + '/followers/"]').click()

    # Gather users to add to follow list
    users = []
    while len(users) < database_func.get_config_value('limit_get_followers', 'follow_config') - users_in_follow_list:
        driver.execute_script('''
                                   var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                   fDialog.scrollTop = fDialog.scrollHeight
                                   ''')
        users = driver.find_elements_by_xpath('//*[@class="FPmhX notranslate  _0imsa "]')

    # Get user name from each element
    user_names = []
    for user in users:
        username = user.get_attribute('title')
        user_names.append(username)

    # Scramble list (following users the bot does not follow users in the same order they were gathered)
    random.shuffle(user_names)

    # Write users to follow list
    database_func.write_list_to_db(user_names, 'follow_list', 'username')


# Follow individual user
def follow_user(driver, username):

    # Get user profile
    driver.get('https://www.instagram.com/' + username + '/')

    # Wait for cool down
    time.sleep(database_func.get_config_value('cool_down', 'follow_config'))

    # If follow button is located
    if wait_func.wait_for_element(driver, 'XPATH_RETURN_BOOL', "//*[text()='Follow']"):

        # Check if profile is private
        follow_buttons = driver.find_elements_by_xpath("//*[text()='Follow']")
        print(len(follow_buttons))
        if len(follow_buttons) == 1 or len(follow_buttons) == 11:

            # Try to follow user
            try:
                driver.find_element_by_xpath("//*[text()='Follow']").click()
                print('Successfully followed user: ' + username + '\n')
                time.sleep(3)
            except:
                print('Failed to follow user, returning.' + '\n')
                return False

        else:
            print('Skipping user: ' + username + '.' + '\n')
            return False

    else:
        return False

    # WRITE METHOD TO VERIFY USER WAS FOLLOWED SUCCESSFULLY

    # Return
    return True
