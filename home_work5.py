# 2. Create one test case that will loop through colors

"""

# Feature file

Feature: Amazon Cart

  Scenario: User can go through the various colors of the product
    Given Open Amazon product B07BJL37GD page
    Then Verify if user can click through colors


# Steps file

from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_prod_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}')


@then('Verify if user can click through colors')
def verify_can_select_color(context):
    expected_colors = ['Black', 'Blue Overdyed', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage',
                       'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage', 'Vintage Light Wash',
                       'Washed Black']
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected {expected_colors} but got {selected_color}'

"""