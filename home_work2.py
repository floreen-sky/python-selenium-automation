"""
2. Practice with locators. Create locators + search strategy for these page elements of Amazon Sign in page:

Amazon logo
$x("//div[@class='a-icon a-icon-logo']")

Email field
$x("//input[@id='ap_email']")

Continue button
$x("//input[@id='continue']")

Need help link
$x("//span[@class='a-expander-prompt']")

Forgot your password link
$x("//a[@id='auth-fpp-link-bottom']")

Other issues with Sign-In link
$x("//a[@id='ap-other-signin-issues-link']")

Create your Amazon account button
$x("//a[@id='createAccountSubmit']")

*Conditions of use link
$x("//a[contains(@href,'ap_signin_notification_condition_of_use')]")

*Privacy Notice link
$x("//a[contains(@href,'ap_signin_notification_privacy_notice')]")

"""

# 3. Create a test case for Help search using python & selenium script
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(4)
#
# driver.get('https://www.amazon.com/gp/help/customer/display.html ')
# driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)
# expected_text = 'Cancel Items or Orders'
# assert expected_text in driver.page_source, f'Cancel Items or Orders text not found on the page'
# driver.quit()


# 4. Create a Test Case using BDD (Behave features and steps)
# Test Case: Logged out user sees Sign in page when clicking Orders

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_orders_first')]").click()
actual_text1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
expected_text1 = 'Sign-In'
assert expected_text1 == actual_text1
print('Sign-In is displayed on the page')
driver.quit()
