import time
import pickle
from config import login
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to log in user and create cookies, accounts for 2factor auth
def create_cookies(browser):

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
