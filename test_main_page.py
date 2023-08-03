import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
        page.open()                      # открытие страницы
        page.go_to_login_page()          # выполнение метода страницы — переход на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page() # проверка на корректный url адрес, наличие форм логина и регистрации

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link() # проверка на корректный url адрес, наличие форм логина и регистрации

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()  # открытие страницы
    page.go_to_basket_page()  # переход в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.sould_be_empty_basket()  # проверка наличия элемента с сообщением о том, что корзина пуста
    basket_page.sould_be_empty_basket_message()  # проверка отсутствия элемента с сообщением о том, что корзина пуста
