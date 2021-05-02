from pages.amazon_page import AmazonUserCart


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.amazon_page = AmazonUserCart(self.driver)