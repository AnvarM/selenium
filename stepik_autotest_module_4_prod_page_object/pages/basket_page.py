from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def no_goods_in_basket(self):
        self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "This element shouldnt'be presented"

    def check_basket_is_empty(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        template = "Your basket is empty. Continue shopping"
        assert text == template, "Should be message: '{}', but got '{}'".format(template, text)