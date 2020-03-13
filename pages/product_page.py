from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_busket(self):
        busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        busket_button.click()

    def should_be_added_to_busket_message(self):
        self.should_be_present_busket_message()
        self.busket_message_content_should_be_correct()

    def should_be_present_busket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BUSKET_MESSAGE), "Added to busket message is not present"

    def busket_message_content_should_be_correct(self):
        assert self.elements_equal(*ProductPageLocators.PRODUCT_NAME_ON_PAGE,
                                   *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Product in the message is different from added"

    def should_be_busket_price_message(self):
        self.should_be_present_busket_price_message()
        self.busket_price_message_content_should_be_correct()

    def should_be_present_busket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BUSKET_PRICE_MESSAGE), "Busket price message is not present"

    def busket_price_message_content_should_be_correct(self):
        assert self.elements_equal(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE,
                                   *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE), "Busket price is not correct"


#myoption
