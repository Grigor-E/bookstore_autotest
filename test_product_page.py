import pytest
import time
import faker
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        f = faker.Faker()
        email = f.email()                                                 # генерация email
        password = str(time.time())                                       # генерация password
        page.register_new_user(email=email, password=password)            # регистрация пользователя
        page.should_be_authorized_user()                                  # проверка того, что пользователь залогинен

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
        page.open()                          # открытие страницы
        page.should_not_be_success_message() # ожидаем, что там нет сообщения об успешном добавлении товара в корзину

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
        page.open()                          # открытие страницы
        page.click_add_product_to_basket()   # добавление товара в корзину

@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()                          # открытие страницы
    page.select_add_product()            # добавление товара в корзину, проверка наименования и цены товара

@pytest.mark.xfail(reason="there is no need to fix this error")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()                          # открытие страницы
    page.click_add_product_to_basket()   # добавление товара в корзину
    page.should_not_be_success_message() # ожидаем, что там нет сообщения об успешном добавлении товара в корзину

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()                          # открытие страницы
    page.should_not_be_success_message() # ожидаем, что там нет сообщения об успешном добавлении товара в корзину

@pytest.mark.xfail(reason="there is no need to fix this error")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()                          # открытие страницы
    page.click_add_product_to_basket()   # добавление товара в корзину
    page.should_dissapear_of_success_message()  # элемент присутствует на странице и должен исчезнуть

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()                          # открытие страницы
    page.go_to_login_page()              # переход по ссылке на формы логина и регистрации

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()                          # открытие страницы
    page.should_be_login_link()          # проверка ссылки на формы логина и регистрации

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)    # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()                          # открытие страницы
    page.go_to_basket_page()             # переход в корзину
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.sould_be_empty_basket()  # проверка наличия элемента с сообщением о том, что корзина пуста
    # отрицательная проверка
    # basket_page.sould_be_empty_basket_message()
    # проверка отсутствия элемента с сообщением о том, что корзина пуста





