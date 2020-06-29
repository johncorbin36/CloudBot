import os
from func import follow_user, generate_follower_list
from config import follow_config


# Function to follow users, keeps count of total users followed and reads/writes to target followers file
def start_follow_run(browser):

    # Check if target list exists
    if os.path.exists('followerLists/' + follow_config['follow_target'] + '_users.txt'):
        print('Target list exists, starting follow run.')
    else:
        print('Target list does not exist, generating new list.')
        generate_follower_list.get_followers(browser, follow_config['follow_target'])

    # Open target follower list
    file = open('followerLists/' + follow_config['follow_target'] + '_users.txt', 'r')

    # Start following users
    i = 0
    remaining_users = []
    for user in file:
        if i <= follow_config['max_follows'] - 1:
            i = follow_user.follow(browser, user, i)
        else:
            remaining_users.append(user)

    browser.get('https://www.google.com')
    print('Max follows reached, generating new follower list.')

    # Closing file and deleting it for updated list
    file.close()
    os.remove('followerLists/' + follow_config['follow_target'] + '_users.txt')

    # Generate new follow list without already followed users if users still exist in list
    if len(remaining_users) > 0:
        # Generate new follow list
        f = open('followerLists/' + follow_config['follow_target'] + '_users.txt', 'w')
        for user in remaining_users:
            f.write(user)
        print('Complete, generated new file with remaining users successfully.')
        f.close()
    else:
        print('Complete, no users to follow remaining.')
