from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_contains_add_button(browser):
	browser.get(link)
	time.sleep(30)
	try:
		browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
		button = True
	except:
		button = False
	assert button, "Button not found :("
