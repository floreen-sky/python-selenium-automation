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


# Home Work 4
# 4.1

LINKS = (By.CSS_SELECTOR, 'div#zg_tabs a')


@given('Open Amazon BestSellers Page')
def open_bestsellers_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify if there are {expected_links} links displayed')
def verify_5_links(context, expected_links):
    actual_links = context.driver.find_elements(*LINKS)
    assert len(actual_links) == int(expected_links), f'Expected 5 links, but we see {len(actual_links)}'


# 4.2
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


# Home Work 5


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
    # selected_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected {expected_colors} but got {selected_color}'
    # print(selected_colors)


# Home Work 6.2


TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')
TITLE = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')


@when('Verify each Link')
def verify_links(context):
    links = context.driver.find_elements(*TOP_LINKS)

    for i in range(len(links)):
        one_link = context.driver.find_elements(*TOP_LINKS)[i]
        one_link_text = one_link.text
        one_link.click()
        one_title_text = context.driver.find_element(*TITLE).text

        assert one_title_text in one_title_text, f'Expected {one_link_text} not in {one_title_text}'


# Home Work 9.1


@when('Select {department} Department')
def select_dept(context, department):
    context.app.amazon_page.select_dept(department)


@then('Input {search_item} in the search Box and click search')
def input_search_item(context, search_item):
    context.app.amazon_page.input_search_item(search_item)


@then('Verify if {department} Department is selected')
def verify_department(context, department):
    context.app.amazon_page.verify_department(department)


# Home Work 9.2


@when('Hover over New Arrival button')
def hover_new_arrivals(context):
    context.app.amazon_page.hover_new_arrivals()


@then('Verify if {deal} Deal is visible')
def verify_deals(context, deal):
    context.app.amazon_page.verify_deals(deal)