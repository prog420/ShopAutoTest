import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_presense_of_add_to_basket_button_on_item_page(browser):
    browser.get(link)
    time.sleep(5)
    browser.implicitly_wait(5)
    assert browser.find_element(
        By.XPATH, 
        '//button[contains(@class, "btn-add-to-basket") and @type="submit"]'
    ).is_displayed() == True, "Missed Button 'Add to basket'"