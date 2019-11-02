from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_LINK)
        button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        product_name = str(self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text).split("\n")[0]
        return product_name

    def get_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price

    def get_price_basket(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        return price_basket

    def get_product_name_added_to_basket(self):
        product_name_added_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_TO_BASKET).text
        return product_name_added_to_basket

    def is_added_to_basket_item_correct(self):
        template = self.get_product_name()
        result = self.get_product_name_added_to_basket()
        assert template == result, "Should be {}, but got {}".format(template, result)

    def is_price_correct(self):
        template = self.get_price()
        result = self.get_price_basket()
        assert template == result, "Should be {}, but got {}".format(template, result)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disapeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"