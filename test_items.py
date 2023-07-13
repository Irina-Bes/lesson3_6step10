from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button(browser):
    browser.get(link)
    browser.find_element(By.XPATH, "//button[@type='submit']")