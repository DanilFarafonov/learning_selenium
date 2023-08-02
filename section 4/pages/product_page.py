from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_btn()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Отсутствует кнопка 'Добавить в корзину'"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Отсутствует наименование товара"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Отсутствует цена товара"

    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        self.browser.execute_script('return arguments[0].scrollIntoView(true);', add_to_basket_btn)
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        product_name_added_to_basket = self.browser. \
            find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_TO_BASKET).text
        basket_sum = self.browser.find_element(*ProductPageLocators.BASKET_SUM).text

        assert product_name == product_name_added_to_basket, \
            'Наименование добавляемого товара не совпадает с товаром, который был добавлен'
        assert product_price == basket_sum, \
            'Цена за товар не соответствует стоимости корзины с этим товаром'
