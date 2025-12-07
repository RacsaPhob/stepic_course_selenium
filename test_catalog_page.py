from selenium.webdriver.common.by import By
import pytest
from .pages.catalog_page import CatalogPage
from time import sleep

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('url', urls)
def test_user_can_click_busket_button(browser, url):
    print(url)
    page = CatalogPage(browser, url)
    page.open()
    page.should_be_basket_but()
    page.add_2_basket_but_click()
    page.item_name_in_message()
    page.item_price_in_message()

