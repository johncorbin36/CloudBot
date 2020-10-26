import time
import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Start selenium as firefox driver
def start_driver():

    # Startup firefox browser
    profile = webdriver.FirefoxProfile()
    # profile.set_preference("general.useragent.override", login['user_agent'])
    driver = webdriver.Firefox(profile)
    driver.get('https://www.instagram.com/')

    # Check if cookies file exists
    if not os.path.exists("cookies.pkl"):
        print('NOT TRUE')
        #driver = create_cookies.create_cookies(driver)
    else:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

    # Refresh and return
    driver.refresh()
    return driver


# Login to instagram
#def login():


# Function to log in user and create cookies, accounts for 2factor auth
# def create_cookies(browser):

    '''
    # Login to Instagram
    browser.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)
    login_username = browser.find_element_by_name('username')
    login_username.send_keys(login['username'])
    login_password = browser.find_element_by_name('password')
    login_password.send_keys(login['password'])
    time.sleep(1)
    login_password.send_keys(Keys.RETURN)
    time.sleep(5)

    # Allow for user to enter 2Factor authenticator if applicable
    try:
        wait = WebDriverWait(browser, 300)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Not Now"]')))
        print('Located button to not save information to browser, proceeding.')
        browser.find_element_by_xpath('//button[text()="Not Now"]').click()
        time.sleep(2)
    except:
        print('Returning, button not located.')

    # Create pickle file for cookies
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))
    return browser


# Function to return random user agent
def random_user_agent():
    print('Holder')

# Function to complete 2Factor authentication
'''

def create_cookies():
    print('Create cookies')
