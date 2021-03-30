# HW 4-1. Create a test case that will open amazon BestSellers page and and verify there are 5 links

"""

# Feature file

Feature: Amazon BestSellers

  Scenario: Verify there are 5 links
    Given Open Amazon BestSellers Page
    Then Verify if there are 5 links displayed


# Steps file

from selenium.webdriver.common.by import By
from behave import given, when, then

LINKS = (By.CSS_SELECTOR, 'div#zg_tabs a')


@given('Open Amazon BestSellers Page')
def open_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify if there are {expected_links} links displayed')
def verify_5_links(context, expected_links):
    actual_links = context.driver.find_elements(*LINKS)
    assert len(actual_links) == int(expected_links), f'Expected 5 links, but we see {len(actual_links)}'

"""


# HW 4-2. Create a test case to add any product you want into the cart, and make sure it’s there
# (check for the number of items in the cart OR open the cart and verify it’s there)

"""

# Feature file

Feature: Amazon Cart

Scenario: Add an Item to Cart and verify if is there

    Given Open Amazon Page
    When Input World Map in the search field
    Then Click on search Button
    Then Click on Best Seller Section
    Then Click on First Item
    When Add Item to Cart
    Then Verify if Item is added to Cart


# Steps file

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_ITEM = (By.CSS_SELECTOR, '#twotabsearchtextbox')
SEARCH_BUTTON = (By.CSS_SELECTOR, '#nav-search-submit-button')
BEST_SELLER = (By.CSS_SELECTOR, '#B089ZN5TQC-best-seller')
FIRST_ITEM = (By.CSS_SELECTOR, 'a[href*="/Laminated-World-Map-Poster-Set"]')
ADD_ITEM = (By.CSS_SELECTOR, '#add-to-cart-button')
ITEMS_IN_CART = (By.CSS_SELECTOR, '#nav-cart-count')


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {item} in the search field')
def input_item(context, item):
    search = context.driver.find_element(*SEARCH_ITEM)
    search.clear()
    search.send_keys(item)
    sleep(2)


@then('Click on Search Button')
def click_search_button(context):
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(1)


@then('Click on Best Seller Section')
def click_best_seller(context):
    context.driver.find_element(*BEST_SELLER).click()
    sleep(2)


@then('Click on First Item')
def click_first_item(context):
    context.driver.find_element(*FIRST_ITEM).click()


@when('Add Item to Cart')
def add_item_to_cart(context):
    context.driver.find_element(*ADD_ITEM).click()
    sleep(3)


@then('Verify if Item is added to Cart')
def verify_item_in_cart(context):
    actual_result = context.driver.find_element(*ITEMS_IN_CART).text
    assert int(actual_result) == 1, f'Expected 1 item in cart, but we see {actual_result}'

"""

