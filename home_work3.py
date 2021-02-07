"""
1. Find the most optimal locators for Create Account (Registration) page elements:

Amazon logo
$$('i.a-icon.a-icon-logo')

Create account title
$$('h1.a-spacing-small')

Your name field
$$('input#ap_customer_name')

Email field
$$('input#ap_email')

Password field
$$('input#ap_password')

Together the 'i' icon and the text under the password field
$$('div.a-box.a-alert-inline.a-alert-inline-info.auth-inlined-information-message.a-spacing-top-mini')

The 'i' icon under the password field
$$('i.a-icon.a-icon-alert')

Text under the password field
$$('div.a-alert-content')

Re-enter password field
$$('input#ap_password_check')

Create your Amazon account button
$$('span#a-autoid-0-announce')

Conditions of Use link under Create your Amazon account button
$$("a[href*='ap_register_notification_condition_of_use']")

Privacy Notice link under Create your Amazon account button
$$("a[href*='ap_register_notification_privacy_notice']")

Sign-In link
$$("a[href*='/ap/signin']")

"""

##########

"""

2. Update a test case for support search using BDD
User can search for Cancelling an order on Amazon (test case from Ex 2 of HW2)

# Feature file

Feature: Test Scenarios for Search functionality

  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon Help Page
    When Search Cancel order in the Search the help library field
    Then Verify Cancel Items or Orders
    
    
# Steps file

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon Help Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html ')


@when('Search Cancel order in the Search the help library field')
def input_cancel_order(context):
    context.driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)


@then('Verify Cancel Items or Orders')
def verify_word(context):
    expected_text = 'Cancel Items or Orders'
    assert expected_text in context.driver.page_source, f'Cancel Items or Orders text not found on the page'

"""

###########

"""

3. Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Shopping Cart is empty.

# Feature file

Feature: Amazon Cart

  Scenario: Verify that Amazon Cart is empty

    Given Open Amazon Page
    When Click on Cart Icon
    Then Verify that Your Shopping Cart is empty



# Steps file

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Cart Icon')
def click_cart(context):
    cart = context.driver.find_element_by_css_selector("span.nav-cart-icon.nav-sprite")
    cart.click()


@then('Verify that Your Shopping Cart is empty')
def verify_empty_cart(context):
    actual_text3 = context.driver.find_element_by_css_selector("div.a-row.sc-your-amazon-cart-is-empty h2").text
    expected_text3 = 'Your Amazon Cart is empty'
    assert expected_text3 == actual_text3
    print('Your Shopping Cart is empty')


"""