import time, datetime, random, os
from func import like, startBrowser, createCookies

# Startup web driver, set cookies and user agent
browser = startBrowser.startBrowser()
browser.get('https://www.instagram.com/')

# Check if cookies needs to be generated
if not os.path.exists('cookies.pkl'):
    browser = createCookies.createCookies(browser)

# Start like run
i = 0
maxRuns = 3
while i != maxRuns:
    like.startLikeRun(browser)
    print('Completed at ' + str(datetime.datetime.now()))
    i += 1
    time.sleep(random.randint(3600, 4500))

# Close browser
browser.close()
