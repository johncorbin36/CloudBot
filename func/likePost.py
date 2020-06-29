import time
from config import like_config


# Likes individual post and returns total likes
def like_post(browser, count, actions):

    # Check if post embed has closed
    if browser.current_url == 'https://www.instagram.com/explore/tags/' + like_config['tag_target'] + '/':
        posts = []
        while len(posts) < count + 12:
            browser.execute_script('''
                                   var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                                   fDialog.scrollTop = fDialog.scrollHeight
                                   ''')
            time.sleep(3)
            posts = browser.find_elements_by_xpath('//*[@class="_9AhH0"]')
        posts[count + 12].click()

    # Check for unlike button
    try:
        browser.find_element_by_xpath('//*[@aria-label="Unlike"]')
        print('Post already liked.')
        time.sleep(3)
        actions.perform()
        time.sleep(3)
        return count
    except:
        print('Post not liked, continuing.')

    # Like photo
    browser.find_element_by_xpath('//button[@class="wpO6b "]').click()
    count += 1

    # Get next post and return
    print('Post liked successfully. ' + str(count) + ' post(s) in total.')
    time.sleep(3)
    actions.perform()
    time.sleep(3)
    return count
