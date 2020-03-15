from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_busket(self):
        busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET_BUTTON)
        busket_button.click()

    def should_be_present_added_to_busket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BUSKET_MESSAGE), "Added to busket message is not present"

    def should_be_correct_product_in_busket_message(self):
        assert self.elements_equal(*ProductPageLocators.PRODUCT_NAME_ON_PAGE,
                                   *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Product in the message is different from added"

    def should_be_present_busket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BUSKET_PRICE_MESSAGE), "Busket price message is not present"

    def should_be_correct_price_in_busket_message(self):
        assert self.elements_equal(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE,
                                   *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE), "Busket price is not correct"

    def should_not_be_added_to_busket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BUSKET_MESSAGE), "Added to busket message is present while it shouldn't"

    def should_disappear_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BUSKET_MESSAGE), "Added to busket message should disappear while it didn't"
