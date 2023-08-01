from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализация Page Object, передача в конструктор экземпляр драйвера и url адрес
    page.open()  # открытие страницы
    page.select_add_product() # добавление продукта в корзину
