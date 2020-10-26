import sys
import os


# Function to check for action blocks
def exists(driver):

    # Check for "content restriction" action block
    try:
        text = 'We restrict certain activity to protect our community. Tell us if you think we made a mistake.'
        driver.find_element_by_xpath('//div[contains(text(), "' + text + '")]')
        handler(driver)
    except:
        return


# Function to handle action blocks
def handler(driver):
    print('Action block located, ending process.')
    driver.close()
    os.remove('cookies.pkl')
    sys.exit()
