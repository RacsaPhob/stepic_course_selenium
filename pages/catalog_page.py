from .base_page import BasePage
from .locators import CatalogPageLocators


class CatalogPage(BasePage):
    def should_be_basket_but(self):
        assert self.is_element_present(*CatalogPageLocators.ADD_2_BASKET_BUT), 'basket button is not represented'

    def add_2_basket_but_click(self):
        self.browser.find_element(*CatalogPageLocators.ADD_2_BASKET_BUT).click()
        self.solve_quiz_and_get_code()

    def get_current_item_name(self):
        current_item = self.browser.find_element(*CatalogPageLocators.CURRENT_ITEM_NAME)
        return current_item.text

    def get_current_item_price(self):
        current_item = self.browser.find_element(*CatalogPageLocators.CURRENT_ITEM_PRICE)
        return current_item.text

    def item_name_in_message(self):
        alert = self.browser.find_element(*CatalogPageLocators.NEW_BASKET_ITEM_ALERT)
        print(self.get_current_item_name() + ' has been added to your basket', alert.text)
        assert self.get_current_item_name() + ' has been added to your basket.' == alert.text

    def item_price_in_message(self):
        alert = self.browser.find_element(*CatalogPageLocators.BASKET_TOTAL_ALERT)
        assert self.get_current_item_price() == alert.text
