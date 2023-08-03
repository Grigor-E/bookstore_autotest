from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def sould_be_empty_basket(self):
        # реализация проверки наличия элемента с сообщением о том, что корзина пуста
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented"

    def sould_be_empty_basket_message(self):
        # реализация проверки отсутствия элемента с сообщением о том, что корзина пуста
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is presented, but should not be"


