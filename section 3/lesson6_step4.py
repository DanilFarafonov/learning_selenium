import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math


url_list = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


@pytest.fixture(scope='function')
def browser_step4():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestParametrisation:

    @pytest.mark.parametrize('urls', url_list)
    def test_logining(self, browser, urls):
        link = urls
        browser.get(link)
        btn_login = WebDriverWait(browser, 15)\
            .until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a.navbar__auth_login')))
        btn_login.click()

        WebDriverWait(browser, 10) \
            .until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.box')))

        browser.find_element(By.NAME, 'login').send_keys('login')
        browser.find_element(By.NAME, 'password').send_keys('password')
        browser.find_element(By.CSS_SELECTOR, 'button.sign-form__btn.button_with-loader').click()

        # ввел так как скрипт начинал писать в форму, не завершив авторизацию. Подумать как заменить
        time.sleep(10)

        text_area = WebDriverWait(browser, 10) \
            .until(ec.presence_of_element_located((By.CSS_SELECTOR, 'textarea.ember-text-area')))
        answer = math.log(int(time.time()))
        text_area.send_keys(answer)
        btn_submit = WebDriverWait(browser, 10) \
            .until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
        btn_submit.click()
        correct_message = WebDriverWait(browser, 10) \
            .until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div.smart-hints.ember-view > p')))
        assert correct_message.text == 'Correct!'
