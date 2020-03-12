from .pages.base_page import BasePage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_to_busket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_busket_message()
    page.should_be_busket_price_message()
