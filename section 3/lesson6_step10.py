import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def test_add_to_cart_btn_exists(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    browser.get(link)
    try:
        browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    except NoSuchElementException:
        print('Кнопка "Добавить в корзину" отсутствует')
        pytest.fail()

# example: pytest -browser_name=firefox --language=en 'section 3/lesson6_step10.py'