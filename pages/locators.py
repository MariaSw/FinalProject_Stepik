from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    SUBSTRING_LOGIN_URL = "/login/"

class ProductPageLocators():
    ADD_TO_BUSKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADDED_TO_BUSKET_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1)")
    BUSKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info:nth-child(3)")

    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, "article.product_page .product_main > .price_color")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info:nth-child(3) strong")

    PRODUCT_NAME_ON_PAGE = (By.CSS_SELECTOR, "article.product_page .product_main > h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success:nth-child(1) strong")
#myoption
