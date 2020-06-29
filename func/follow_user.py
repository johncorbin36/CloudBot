import time
from config import follow_config


# Function to follow individual user, returns total successful follows 
def follow(browser, user, count):

    # Get user profile
    browser.get('https://www.instagram.com/' + user + '/')
    time.sleep(2)

    # Check if already following
    try:
        browser.find_element_by_xpath("//button[text()='Following']")
        print('"Following" button located, returning.')
        return count
    except:
        print('"Following" button not located, resuming.')

    # Find 'requested' button if it exists
    try:
        browser.find_element_by_xpath("//button[text()='Requested']")
        print('"Request" button located, returning.')
        return count
    except:
        print('"Request" button not located, resuming.')

    # Find 'follow back' button if it exists
    try:
        browser.find_element_by_xpath("//button[text()='Follow Back']")
        print('"Follow Back" button located, returning.')
        return count
    except:
        print('"Follow Back" button not located, resuming.')

    # Check if user does not exist
    try:
        browser.find_element_by_xpath("//*[text()='Sorry, this page isn't available.']")
        print('User does not exist or page is not available, returning.')
        return count
    except:
        print('User does exist and page is available, resuming.')

    # Follow user
    try:
        browser.find_element_by_xpath("//*[text()='Follow']").click()
        time.sleep(3)
        print('Successfully followed user: ' + user)
    except:
        print('Failed to follow user, returning.')
        return count

    # Increase count and return
    count += 1
    return count
