def startBrowser():
    from selenium import webdriver
    from config import login
    from func import createCookies
    import os, pickle

    # Startup browser
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", login['userAgent'])
    browser = webdriver.Firefox(profile)
    browser.get('https://www.instagram.com/')

    # Check if cookies file exists. If not, creates one. If so, load cookies.
    if not os.path.exists("cookies.pkl"):
        browser = createCookies.createCookies(browser)
    else:
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)

    return browser
