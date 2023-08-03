from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")               # локатор ссылки на формы регистрации и логина
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")   # несуществующий локатор
    SEE_BASKET = (By.CSS_SELECTOR, ".basket-mini > :nth-child(2) a.btn.btn-default") # локатор кнопки "Посмотреть корзину"

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")  # локатор сообщения о пустой корзине

class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")                # локатор формы логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")          # локатор формы регистрации

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form .btn")     # локатор кнопки "Добавить в корзину"
    NAME_PRODUCT = (By.CSS_SELECTOR, "#content_inner > .product_page :nth-child(2) h1")  # локатор наименования продукта
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")             # локатор цены продукта
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")       # локатор наименования продукта добавленного в корзину
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")      # локатор цены продукта добавленного в корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1) .alertinner")      # локатор сообщения о добавлении товара в корзину