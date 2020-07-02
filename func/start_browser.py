import os
import pickle
from selenium import webdriver
from config import login
from func import create_cookies


# Function to start selenium and return browser
def start_browser():

    # Startup firefox browser
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", login['user_agent'])
    browser = webdriver.Firefox(profile)
    browser.get('https://www.instagram.com/')

    # Check if cookies file exists. If not, creates one. If so, load cookies.
    if not os.path.exists("cookies.pkl"):
        browser = create_cookies.create_cookies(browser)
    else:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)

    # Refresh and return
    browser.get('https://www.instagram.com/')
    return browser

# Write function for seperate browsers and generate seperate cookies