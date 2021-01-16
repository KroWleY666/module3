import pytest
from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"  # есть кнопка
#link = "http://selenium1py.pythonanywhere.com/catalogue/hackers-painters_185/"  # нет кнопки

def test_should_be_add_to_card_button(browser):
	browser.get(link)
	browser.implicitly_wait(5)
	
	time.sleep(30)
	button = browser.find_element_by_css_selector(".btn.btn-primary.btn-add-to-basket")
	assert button is not None, "Should be a button"