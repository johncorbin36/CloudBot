from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Wait for element to appear in page
def wait_for_element(driver, ele_type, identifier):

    while True:

        # Wait till element can be clicked
        if ele_type == 'ID':
            try:
                element = WebDriverWait(driver, 240).until(
                    ec.element_to_be_clickable((By.ID, identifier))
                )
            finally:
                print('Element ready.')
                break

        # Wait till element can be clicked
        if ele_type == 'NAME':
            try:
                element = WebDriverWait(driver, 240).until(
                    ec.element_to_be_clickable((By.NAME, identifier))
                )
            finally:
                print('Element ready.')
                break

        # Wait till element can be clicked
        if ele_type == 'CLASS_NAME':
            try:
                element = WebDriverWait(driver, 240).until(
                    ec.element_to_be_clickable((By.CLASS_NAME, identifier))
                )
            finally:
                print('Element ready.')
                break

        # Wait till element can be clicked
        if ele_type == 'LINK_TEXT':
            try:
                element = WebDriverWait(driver, 240).until(
                    ec.element_to_be_clickable((By.LINK_TEXT, identifier))
                )
            finally:
                print('Element ready.')
                break

        # Wait till element can be clicked
        if ele_type == 'XPATH':
            try:
                element = WebDriverWait(driver, 240).until(
                    ec.element_to_be_clickable((By.XPATH, identifier))
                )
            finally:
                print('Element ready.')
                break

        # Wait till element can be clicked
        if ele_type == 'XPATH_RETURN_BOOL':
            try:
                element = WebDriverWait(driver, 10).until(
                    ec.element_to_be_clickable((By.XPATH, identifier))
                )
                print('Element located.')
                return True
            except:
                return False
