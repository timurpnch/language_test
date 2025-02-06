from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_button(browser):
    browser.get(link)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    assert add_to_basket_button


