# 6.1 Create a window handling test case from the class
# and verify that user can open amazon applications from Terms of Conditions

"""
# Feature file

Feature: Window Handling on Amazon

  Scenario: User can open and close Amazon Applications

    Given Open Amazon T&C page
    When Store original windows
    And Click on Amazon applications link
    And Switch to the newly opened window
    Then Verify if Amazon app page is opened
    And User can close new window and switch back to original


# Steps file

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


LINK = (By.CSS_SELECTOR, "a[href*='1000625601']")
APP_TITLE = (By.CSS_SELECTOR, "#mgt-email-sms-download-header")

@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)


@when('Click on Amazon applications link')
def click_link(context):
    context.driver.find_element(*LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    # context.driver.wait.until(EC.new_window_is_opened) # I get an error at this line << 'WebDriver' object has no attribute 'wait' >>
    print(context.driver.window_handles)
    context.driver.switch_to.window(context.driver.window_handles[1])


@then('Verify if Amazon app page is opened')
def verify_new_page(context):
    actual_result = context.driver.find_element(*APP_TITLE).text
    assert actual_result == 'Download the app today!', f'Expected Amazon App Page'


@then('User can close new window and switch back to original')
def close_new_switch_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
"""

# 6.2 [Loops] Make a test case which:
# - Clicks on Best Sellers link on the top menu
# - Clicks on each top link and verify that new page opens

"""
# Feature file

Feature: Amazon BestSellers

  Scenario: Best Seller Links verified with Loop

    Given Open Amazon Page
    Then Click on Best Seller Section
    When Verify each Link


# Steps file

from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_SELLER = (By.CSS_SELECTOR, '#nav-xshop a[href*="bestsellers"]')
TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')
TITLE = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    
    
@then('Click on Best Seller Section')
def click_best_seller(context):
    context.driver.find_element(*BEST_SELLER).click()


@when('Verify each Link')
def verify_links(context):
    links = context.driver.find_elements(*TOP_LINKS)

    for i in range(len(links)):
        one_link = context.driver.find_elements(*TOP_LINKS)[i]
        one_link_text = one_link.text
        one_link.click()
        one_title_text = context.driver.find_element(*TITLE).text

        assert one_title_text in one_title_text, f'Expected {one_link_text} not in {one_title_text}'
        
"""
