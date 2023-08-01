from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    # Getters

    def get_add_product_to_basket(self):
        return self.browser.find_element(*ProductPageLocators.ADD_TO_BASCET)

    def get_name_product(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)

    def get_price_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)

    # Actions

    def click_add_product_to_basket(self):
        self.get_add_product_to_basket().click()

    # Methods

    def select_add_product(self):
        self.click_add_product_to_basket()     # выполнение метода добавления товара в корзину
        self.solve_quiz_and_get_code()         # выполнение метода вычисления математического выражения
        self.assert_word(self.get_name_product(), "The shellcoder's handbook") # выполнение метода сравнения названия товара добавленного в корзину
        self.assert_word(self.get_price_product(), "£9.99") # выполнение метода сравнения цены товара добавленного в корзину






