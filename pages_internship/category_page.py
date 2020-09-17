from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages_internship.base_page import Page_Internship
from selenium.webdriver import ActionChains


class CategoryInternship(Page_Internship):
    print(f'in CategoryInternship(Page_Internship)')

    RESULTS_MESSAGE = (By.CSS_SELECTOR, "p.woocommerce-result-count.hide-for-medium")
    RESULT_ITEMS_ICONS = (By.CSS_SELECTOR, "div.product-small.col")
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, "p.category.uppercase")
    PRODUCT_NAME = (By.CSS_SELECTOR, "p.name.product-title")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.price-wrapper")

    QUICK_VIEW = (By.CSS_SELECTOR, "a.quick-view.quick-view-added")
    # QUICK_VIEW_CLOSE = (By.CSS_SELECTOR, ".pswp__button--close")
    QUICK_VIEW_CLOSE = (By.CSS_SELECTOR, "button.mfp-close")
    QUICK_VIEW_ADD_BUTTON = (By.CSS_SELECTOR, "form button.single_add_to_cart_button.button.alt")

    ITEMS_AMOUNT_ON_PAGE = (By.XPATH, "//*[@title='Qty']")
    ITEMS_AMOUNT_IN_CART = (By.CSS_SELECTOR, "span.cart-icon.image-icon strong")

    def open_category_page(self, category_name):
        # self.open_page(f'dp/product-category/{category_name}')
        self.driver.get('https://gettop.us/product-category/iphone')

    def results_message_present(self):
        print("Perform your verification on page {}".format(self.driver.title))

        assert self.find_element(
            *self.RESULTS_MESSAGE).text, f'Expected to find {self.find_element(*self.RESULTS_MESSAGE).text} results message on a page'
        print(f'Expected results message ' + self.find_element(*self.RESULTS_MESSAGE).text +
              f' is presented on this page ')

    def verify_items_presented(self, items_expected):
        print("Perform your verification on page {}".format(self.driver.title))

        result_items_icons = self.find_elements(*self.RESULT_ITEMS_ICONS)

        counter = 0

        for link in result_items_icons:
            counter += 1
        assert items_expected in str(counter), f'Expected {items_expected} to be in {str(counter)}'
        print(f'Expected items quantity: ' + items_expected + f' is in the actual items quantity: ' + str(counter))

    def verify_item_attributes_shown(self):
        print("Perform your verification on page {}".format(self.driver.title))

        result_items_icons = self.find_elements(*self.RESULT_ITEMS_ICONS)

        for link in result_items_icons:
            assert self.find_element(
                *self.PRODUCT_CATEGORY), f'Expected to see {self.find_element(*self.PRODUCT_CATEGORY).text} a product category on a page'
            print(f'Expected category for product ' + self.find_element(*self.PRODUCT_CATEGORY).text +
                  f' is shown on this page ')

            assert self.find_element(
                *self.PRODUCT_NAME), f'Expected to see {self.find_element(*self.PRODUCT_NAME).text} a product name on a page'
            print(f'Expected name for product ' + self.find_element(*self.PRODUCT_NAME).text +
                  f' is shown on this page ')

            assert self.find_element(
                *self.PRODUCT_PRICE), f'Expected to find {self.find_element(*self.PRODUCT_PRICE).text} product price on a page'
            print(f'Expected price for product ' + self.find_element(*self.PRODUCT_PRICE).text +
                  f' is shown on this page ')

    def open_close_quick_view(self):

        quick_view_icon = self.find_element(*self.QUICK_VIEW)
        ActionChains(self.driver).move_to_element(quick_view_icon).click().perform()

        # take screenshot
        self.driver.save_screenshot("pageImage.png")

        quick_view_icon_esc = self.find_element(*self.QUICK_VIEW_CLOSE)

        ActionChains(self.driver).move_to_element(quick_view_icon_esc).click().perform()

    def open_quick_view_add_cart(self):

        quick_view_icon = self.find_element(*self.QUICK_VIEW)
        ActionChains(self.driver).move_to_element(quick_view_icon).click().perform()

        items_amount_quick_view = (self.find_element(*self.ITEMS_AMOUNT_ON_PAGE)).get_attribute("value")

        self.driver.response = items_amount_quick_view  # pass value to the next step for varification

        self.click(*self.QUICK_VIEW_ADD_BUTTON)
        # self.driver.execute_script("arguments[0].click();", quick_view_add_button)

    def verify_correct_items_amount_displayed(self):
        print("Perform your verification on page {}".format(self.driver.title))

        items_amount_quick_view = self.driver.response

        items_amount_in_cart = (self.find_element(*self.ITEMS_AMOUNT_IN_CART)).text

        assert items_amount_quick_view in items_amount_in_cart, f'Expected text {items_amount_quick_view}, ' \
                                                                f'but got {items_amount_in_cart}'
        print(
            f'Expected amount: ' + items_amount_quick_view + f' is in the actual cart items amount: ' + items_amount_in_cart)
