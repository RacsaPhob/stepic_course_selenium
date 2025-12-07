from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')

class CatalogPageLocators():
    ADD_2_BASKET_BUT = (By.CLASS_NAME, 'btn-add-to-basket')
    CURRENT_ITEM_NAME = (By.TAG_NAME, 'h1')
    CURRENT_ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    NEW_BASKET_ITEM_ALERT = (By.CLASS_NAME, 'alertinner')
    BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, '.alert-info strong')
