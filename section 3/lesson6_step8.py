import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser_step8():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

# command to run: pytest -v --tb=line --reruns 1 'section 3/lesson6_step8.py'