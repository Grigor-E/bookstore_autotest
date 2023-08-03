from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    # Getters

    def get_add_product_to_basket(self):
        return self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)

    def get_name_product(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)

    def get_price_product(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)

    def get_name_product_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET)

    def get_price_product_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET)

    # Actions

    def click_add_product_to_basket(self):
        self.get_add_product_to_basket().click()

    # Methods

    def select_add_product(self):
        self.click_add_product_to_basket()     # выполнение метода добавления товара в корзину
        self.solve_quiz_and_get_code()         # выполнение метода вычисления математического выражения
        self.assert_word(self.get_name_product(), self.get_name_product_in_basket()) # выполнение метода сравнения названия товара добавленного в корзину
        self.assert_word(self.get_price_product(), self.get_price_product_in_basket()) # выполнение метода сравнения цены товара добавленного в корзину

    def should_not_be_success_message(self):
        # выполнение метода проверки отсутсвия сообщения об успехе
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        # выполнение метода проверки исчезновения сообщения об успехе
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message didn't disappear"






