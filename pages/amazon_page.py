from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class AmazonUserCart(Page):
    ORDERS_BUTTON = (By.XPATH, "//a[contains(@href, 'nav_orders_first')]")
    SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    CART_ICON = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')
    CART_TEXT = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2')
    SEARCH_ITEM = (By.ID, "#twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "#nav-search-submit-button")
    AMAZON_CHOICE = (By.XPATH, "//span[@id='B016X2TQZ8-amazons-choice-label']")
    ADD_ITEM = (By.CSS_SELECTOR, '#add-to-cart-button')
    ITEMS_IN_CART = (By.CSS_SELECTOR, '#nav-cart-count')
    ALL_DEPARTMENTS_DROPDOWN = (By.CSS_SELECTOR, 'select.nav-search-dropdown')
    SELECTED_DPT_CATEG = (By.CSS_SELECTOR, '#nav-subnav[data-category="{DPT_SBSTR}"]')
    NEW_ARRIVALS_BTN = (By.XPATH, "//span[contains(text(),'New Arrivals')]")
    DEALS_NEW_ARRIVALS = (By.XPATH, "//h3[contains(text(),'{Deals}')]")

    def _get_locator(self, department):
        return [self.SELECTED_DPT_CATEG[0], self.SELECTED_DPT_CATEG[1].replace('{DPT_SBSTR}', department)]

    def _get_locator_arrivals(self, deal):
        return [self.DEALS_NEW_ARRIVALS[0],self.DEALS_NEW_ARRIVALS[1].replace('{Deals}', deal)]

    def open_amazon(self):
        self.open_url('https://www.amazon.com/')

    def click_orders(self):
        self.click(*self.ORDERS_BUTTON)

    def verify_sign_in(self, result_word='Sign-In'):
        self.verify_text(result_word, *self.SIGN_IN_TEXT)
        print('Sign-In is displayed on the page')

    def click_cart(self):
        self.click(*self.CART_ICON)

    def verify_empty_cart(self, result_word='Your Amazon Cart is empty'):
        self.verify_text(result_word, *self.CART_TEXT)
        print('Your Shopping Cart is empty')

    def input_item(self, search_query):
        self.input_text(search_query, *self.SEARCH_ITEM)

    def click_search_button(self):
        self.click(*self.SEARCH_BUTTON)

    def click_amazon_choice(self):
        self.click(*self.AMAZON_CHOICE)

    def add_item_to_cart(self):
        self.click(*self.ADD_ITEM)

    def verify_item_in_cart(self, result_test):
        self.verify_text(result_test, *self.ITEMS_IN_CART)

    def select_dept(self, department: str):
        select = Select(self.find_element(*self.ALL_DEPARTMENTS_DROPDOWN))
        select.select_by_value(f'search-alias={department}')
        sleep(1)

    def input_search_item(self, search_item):
        self.input_text(search_item, *self.SEARCH_ITEM)
        self.click(*self.SEARCH_BUTTON)

    def verify_department(self, department):
        locator = self._get_locator(department)
        self.wait_for_element_appear(*locator)

    def hover_new_arrivals(self):
        self.hover_object(*self.NEW_ARRIVALS_BTN)
        sleep(3)

    def verify_deals(self, deal):
        locator = self._get_locator_arrivals(deal)
        self.wait_for_element_appear(*locator)