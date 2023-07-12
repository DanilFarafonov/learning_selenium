import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, 'firstname').send_keys('Danil')
    browser.find_element(By.NAME, 'lastname').send_keys('Farafonov')
    browser.find_element(By.NAME, 'email').send_keys('pochta')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'lesson2_step8.txt')
    browser.find_element(By.NAME, 'file').send_keys(file_path)

    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    time.sleep(10)
    browser.quit()
