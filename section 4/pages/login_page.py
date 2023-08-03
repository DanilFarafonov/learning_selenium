from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # корректный url адрес
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK).get_attribute('href')
        assert login_link in self.browser.current_url

    def should_be_login_form(self):
        # есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)
