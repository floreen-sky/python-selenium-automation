# 7.1 Rewrite these scenarios with Page Object pattern:
#
# Scenario: Logged out user sees Sign in page when clicking Orders
#  Given Open Amazon page
#  When Click Amazon Orders link
#  Then Verify Sign In page is opened

# Scenario: 'Your Shopping Cart is empty' shown if no product added
#  Given Open Amazon page
#  When Click on cart icon
#  Then Verify 'Your Shopping Cart is empty.' text present


#7.2 Rewrite “Add a product to cart” scenario using Page Object pattern.


#Feature file

"""
Feature: Amazon Log Out

  Scenario: Logged out user sees Sign In page when clicking Orders
    Given Open Amazon Page
    When Click on Orders Button
    Then Verify if Sign In appears in the opened Page


Feature: Amazon Cart

  # Home Work 7.1 - second scenario (with Page Object)

  Scenario: Verify that Amazon Cart is empty

    Given Open Amazon Page
    When Click on Cart Icon
    Then Verify that Your Shopping Cart is empty


  # Home Work 7.2 (with Page Object)

  Scenario: Add an Item to Cart and verify if is there

    Given Open Amazon Page
    When Input World Map in the search field
    Then Click on search Button
    Then Click on Amazon's Choice Product
    When Add Item to Cart
    Then Verify if Item is added to Cart
"""

#Steps file

"""
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Home Work 7.1 (with Page Object)


@given('Open Amazon Page')
def open_amazon(context):
    context.app.amazon_page.open_amazon()


@when('Click on Orders Button')
def click_orders(context):
    context.app.amazon_page.click_orders()


@then('Verify if Sign In appears in the opened Page')
def verify_sign_in(context):
    context.app.amazon_page.verify_sign_in()


@when('Click on Cart Icon')
def click_cart(context):
    context.app.amazon_page.click_cart()


@then('Verify that Your Shopping Cart is empty')
def verify_empty_cart(context):
    context.app.amazon_page.verify_empty_cart()


# Home Work 7.2 (with Page Object)


@when('Input {search_query} in the search field')
def input_item(context, search_query):
    context.app.amazon_page.input_item(search_query)


@then('Click on Search Button')
def click_search_button(context):
    context.app.amazon_page.click_search_button()


@then("Click on Amazon's Choice Product")
def click_amazon_choice(context):
    context.app.amazon_page.click_amazon_choice()


@when('Add Item to Cart')
def add_item_to_cart(context):
    context.app.amazon_page.add_item_to_cart()
    sleep(3)


@then('Verify if Item is added to Cart')
def verify_item_in_cart(context):
    context.app.amazon_page.verify_item_in_cart('1')

"""

#Base Page file

"""
class Page:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def verify_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text} instead got {actual_text}'

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)
"""

#Amazon Page file

"""
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class AmazonUserCart(Page):
    ORDERS_BUTTON = (By.XPATH, "//a[contains(@href, 'nav_orders_first')]")
    SIGN_IN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")
    CART_ICON = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')
    CART_TEXT = (By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty h2')
    SEARCH_ITEM = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#nav-search-submit-button')
    AMAZON_CHOICE = (By.XPATH, "//span[@id='B016X2TQZ8-amazons-choice-label']")
    ADD_ITEM = (By.CSS_SELECTOR, '#add-to-cart-button')
    ITEMS_IN_CART = (By.CSS_SELECTOR, '#nav-cart-count')

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
"""

#Application file

"""
from pages.amazon_page import AmazonUserCart


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.amazon_page = AmazonUserCart(self.driver)
"""

#environment file

"""
from app.application import Application

from selenium import webdriver


def browser_init(context):

    #:param context: Behave context

    context.driver = webdriver.Chrome()
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

"""