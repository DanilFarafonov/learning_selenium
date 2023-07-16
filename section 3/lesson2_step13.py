import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationWithRequiredFields(unittest.TestCase):

    def test_link_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, 'input:required.first')
        last_name = browser.find_element(By.CSS_SELECTOR, 'input:required.second')
        email = browser.find_element(By.CSS_SELECTOR, 'input:required.third')

        first_name.send_keys('Ivan')
        last_name.send_keys('Petrov')
        email.send_keys('petvan')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # находим элемент, содержащий текст
        welcome_text_elt = WebDriverWait(browser, 5)\
            .until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)

    def test_link_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        first_name = browser.find_element(By.CLASS_NAME, 'input:required.first')
        last_name = browser.find_element(By.CLASS_NAME, 'input:required.second')
        email = browser.find_element(By.CLASS_NAME, 'input:required.third')

        first_name.send_keys('Ivan')
        last_name.send_keys('Petrov')
        email.send_keys('petvan')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # находим элемент, содержащий текст
        welcome_text_elt = WebDriverWait(browser, 5) \
            .until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
