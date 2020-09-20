from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages_internship.base_page import Page_Internship
import time


class CartServices(Page_Internship):
    CART_ICON = (By.CSS_SELECTOR, "span.cart-icon.image-icon")
    CART_TOOLTIP = (By.CSS_SELECTOR, "li.html.widget_shopping_cart")
    SUBTOTAL_CART = (By.CSS_SELECTOR, "span.woocommerce-Price-amount.amount")

    CURRENT_PAGE = (By.CSS_SELECTOR, "a.current")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, ".cart-empty")
    NO_PROD_CART_TEXT = (By.CSS_SELECTOR, "p.woocommerce-mini-cart__empty-message")

    ADD_BUTTON = (By.NAME, "add-to-cart")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "a.remove.remove.remove_from_cart_button")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "a.button.wc-forward")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.button.checkout.wc-forward")

    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, "p.price.product-page-price")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, "span.cart-price")
    PRODUCT_TITLE_ON_PAGE = (By.CSS_SELECTOR, "h1.product-title.product_title.entry-title")
    # PRODUCT_TITLE_IN_CART =  (By.CSS_SELECTOR, "a[href*='gettop.us/product/airpods/']")
    PRODUCT_TITLE_IN_CART = (By.XPATH, "//a[contains(text(),'AirPods with Wireless Charging Case')]")

    ITEMS_AMOUNT_ON_PAGE = (By.XPATH, "//*[@title='Qty']")
    ITEMS_AMOUNT_IN_CART = (By.CSS_SELECTOR, "span.cart-icon.image-icon strong")

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def verify_found_results_text(self, search_text):
        self.verify_text(search_text, *self.EMPTY_CART_TEXT)

    def click_add_button(self):
        self.wait_for_element_click(*self.ADD_BUTTON)

    def verify_correct_prod_price_displayed(self):
        print("Perform your verification on page {}".format(self.driver.title))
        prod_price_on_page = (self.find_element(*self.PRODUCT_PRICE_ON_PAGE)).get_attribute("innerText")
        self.verify_text(prod_price_on_page, *self.PRODUCT_PRICE_IN_CART)

    def verify_correct_items_amount_displayed(self):
        print("Perform your verification on page {}".format(self.driver.title))

        items_amount_in_cart = (self.find_element(*self.ITEMS_AMOUNT_IN_CART)).text
        items_amount_page = (self.find_element(*self.ITEMS_AMOUNT_ON_PAGE)).get_attribute("value")

        assert items_amount_page in items_amount_in_cart, f'Expected text {items_amount_page}, ' \
                                                          f'but got {items_amount_in_cart}'
        print(
            f'Expected amount: ' + items_amount_page + f' is in the actual cart items amount: ' + items_amount_in_cart)

        # self.verify_text(items_amount_page, self.ITEMS_AMOUNT_IN_CART)

    def hover_cart_icon(self):
        cart_icon = self.find_element(*self.CART_ICON)
        ActionChains(self.driver).move_to_element(cart_icon).perform()
        cart_tooltip = self.find_element(*self.CART_TOOLTIP)
        # self.driver.implicitly_wait(20)

    def click_remove_from_cart(self):
        self.click(*self.REMOVE_BUTTON)

    def verify_product_removed(self, no_prod_cart):
        self.find_element(*self.NO_PROD_CART_TEXT)
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(no_prod_cart, *self.NO_PROD_CART_TEXT)

    def click_view_cart_button(self):
        self.click(*self.VIEW_CART_BUTTON)

    def verify_page(self):
        print("in verify_page of CART_FUNC")
        print("Perform your verification on page {}".format(self.driver.title))
        current_page_text = (self.find_element(*self.CURRENT_PAGE)).text
        self.verify_text(current_page_text, *self.CURRENT_PAGE)
        time.sleep(5)

    def click_checkout_button(self):
        self.click(*self.CHECKOUT_BUTTON)

    def verify_cart_correct_products(self):
        print("Perform your verification on page {}".format(self.driver.title))
        product_title_text_page = self.find_element(*self.PRODUCT_TITLE_ON_PAGE).text
        product_title_text_cart = self.find_element(*self.PRODUCT_TITLE_IN_CART).get_attribute("innerText")
        assert product_title_text_page in product_title_text_cart, f'Expected text {product_title_text_page}, ' \
                                                                   f'but got {product_title_text_cart} '

        print(f'Expected text: ' + product_title_text_page +
              f' is in the actual cart product title: ' + product_title_text_cart)

    def verify_cart_correct_subtotal(self):
        print("Perform your verification on page {}".format(self.driver.title))
        subtotal_cart = (self.find_element(*self.SUBTOTAL_CART)).text[1:-3]
        prod_price_on_page = (self.find_element(*self.PRODUCT_PRICE_ON_PAGE)).text[1:-3]
        items_amount_cart = (self.find_element(*self.ITEMS_AMOUNT_IN_CART)).text

        int_calculated_subtotal = int(float(prod_price_on_page)) * int(float(items_amount_cart))
        calculated_subtotal = str(int_calculated_subtotal)
        int_subtotal_cart = int(subtotal_cart)

        assert int_calculated_subtotal == int_subtotal_cart, f'Expected text {calculated_subtotal}, ' \
                                                             f'but got {subtotal_cart}'
        print(f'Expected subtotal: ' + subtotal_cart + f' is in the actual cart subtotal: ' + calculated_subtotal)

    def input_quantity(self, input_quantity):
        self.input(input_quantity, *self.ITEMS_AMOUNT_ON_PAGE)
