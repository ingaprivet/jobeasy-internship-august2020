from selenium.webdriver.common.by import By
from pages_internship.base_page import Page_Internship
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Product_Internship(Page_Internship):
    print(f'in Product_Internship(Page_Internship)')

    PRODUCT_IMAGE = (By.CSS_SELECTOR, "img.wp-post-image.skip-lazy")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1.product-title")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price.product-page-price")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "div.product-short-description")

    SEARCH_INPUT = (
        By.CSS_SELECTOR, "li.header-search.header-search-dropdown.has-icon.has-dropdown.menu-item-has-children")
    SEARCH_TOOLTIP = (By.ID, 'woocommerce-product-search-field-0')
    SEARCH_SUBMIT = (By.XPATH, "//*[contains(@class, 'ux-search-submit')]")

    MINUS_BUTTON = (By.CSS_SELECTOR, "input.minus.button.is-form")
    PLUS_BUTTON = (By.CSS_SELECTOR, "input.plus.button.is-form")
    ADD_BUTTON = (By.NAME, "add-to-cart")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.button.checkout.wc-forward")

    ITEMS_AMOUNT_ON_PAGE = (By.XPATH, "//*[@title='Qty']")
    ITEMS_AMOUNT_IN_CART = (By.CSS_SELECTOR, "span.cart-icon.image-icon strong")
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.message-container.container.success-color.medium-text-center")
    OUT_OF_STOCK_MESSAGE = (By.CSS_SELECTOR, "p.stock.out-of-stock")
    UMAYLIKE_WIDGET = (By.CSS_SELECTOR, "h3.widget-title.shop-sidebar")

    SUGGESTED_PRODUCT_AVAILABLE = (By.CSS_SELECTOR, "aside span.product-title")

    REVIEW_COMMENT = (By.ID, "comment")
    # REVIEW_COMMENT = (By.CSS_SELECTOR, "textarea")
    # REVIEW_COMMENT = (By.CSS_SELECTOR, "p.comment-form-comment")
    # REVIEW_COMMENT = (By.CSS_SELECTOR, "textarea#comment")
    REVIEW_SUBMIT = (By.CSS_SELECTOR, "input#submit.submit")

    def open_prod_page(self, product_id):
        self.open_page(f'dp/product/{product_id}')

    def click_plus_button(self):
        self.click(*self.PLUS_BUTTON)

    def click_minus_button(self):
        self.click(*self.MINUS_BUTTON)

    # @When Hoover over magni icon
    def hover_magni_icon(self):
        magni_icon = self.find_element(*self.SEARCH_INPUT)
        ActionChains(self.driver).move_to_element(magni_icon).perform()

        # take screenshot
        location = magni_icon.location
        size = magni_icon.size
        self.driver.save_screenshot("pageImage.png")

    # @And Verify search tooltip is displayed
    def verify_search_tooltip(self):
        self.wait_for_element_appear(*self.SEARCH_TOOLTIP)

    # @Then Search for Watch Series 5
    def search_word_func(self, search_word):
        self.input(search_word, *self.SEARCH_TOOLTIP)
        self.click(*self.SEARCH_SUBMIT)

    # @Product results for Watch Series 5 are shown
    # will grab from class SearchResultsInternship(Page_Internship)

    def verify_item_added_message_shown(self, item_added_message_passed):
        item_added_message_shown = (self.find_element(*self.ITEM_ADDED_MESSAGE)).get_attribute("innerText")
        print("Perform your verification on page {}".format(self.driver.title))
        assert item_added_message_passed in item_added_message_shown, f'Expected text {item_added_message_passed}, ' \
                                                                      f'but got {item_added_message_shown} '

        print(f'Expected text: ' + item_added_message_passed +
              f' is in the actual cart product title: ' + item_added_message_shown)

    def hover_back_forwar_arrows(self):
        arrow_icon = self.find_element(*self.SEARCH_INPUT)
        ActionChains(self.driver).move_to_element(arrow_icon).perform()

    def verify_outofstock_message_shown(self, out_of_stock_message_passed):
        out_of_stock_message_shown = (self.find_element(*self.OUT_OF_STOCK_MESSAGE)).get_attribute("innerText")

        print("Perform your verification on page {}".format(self.driver.title))
        assert out_of_stock_message_passed in out_of_stock_message_shown, f'Expected text {out_of_stock_message_passed}, ' \
                                                                          f'but got {out_of_stock_message_shown} '

        print(f'Expected text: ' + out_of_stock_message_passed +
              f' is in the actual cart product title: ' + out_of_stock_message_shown)

    def verify_add_button_available(self):
        print("Perform your verification on page {}".format(self.driver.title))
        try:
            self.find_element(*self.ADD_BUTTON).text

        except NoSuchElementException:
            print(f'Will handle NoSuchElementException')
            print(f'Add to Cart button is not shown to the user')

    def verify_checkout_button_available(self):
        print("Perform your verification on page {}".format(self.driver.title))
        try:
            self.find_element(*self.CHECKOUT_BUTTON)

        except NoSuchElementException:
            print(f'Will handle NoSuchElementException')
            print(f'Checkout button is not shown to the user')

    def verify_umaylike_widget_text(self, umaylike_widget_text_passed):
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(umaylike_widget_text_passed, *self.UMAYLIKE_WIDGET)

    def verify_suggested_products_shown(self):
        print("Perform your verification on page {}".format(self.driver.title))
        self.click(*self.SUGGESTED_PRODUCT_AVAILABLE)

    def verify_correct_page_shown(self):
        page_expected = (self.find_element(*self.UMAYLIKE_WIDGET)).text
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(page_expected, *self.UMAYLIKE_WIDGET)

    #  then Verify Product review text can be submitted
    def verify_product_review_submission(self, product_review_text):
        print(f'product_review_text = ', product_review_text)
        # e = self.driver.find_element(*self.REVIEW_COMMENT)
        # e.send_keys(product_review_text)
        # self.input(product_review_text, *self.REVIEW_COMMENT)
        # self.click(*self.REVIEW_SUBMIT)

    def verify_product_attributes_shown(self, product_image, product_name, product_price, product_description):
        print("Perform your verification on page {}".format(self.driver.title))

        assert self.find_element(*self.PRODUCT_IMAGE), f'Expected to find {self.find_element(*self.PRODUCT_IMAGE).get_attribute("title")} product image on a page'
        print(f'Expected image for product: ' + self.find_element(*self.PRODUCT_IMAGE).get_attribute("title") +
              f' is shown on this page ')

        assert self.find_element(*self.PRODUCT_NAME), f'Expected to find {self.find_element(*self.PRODUCT_NAME).text} product name on a page'
        print(f'Expected name for product: ' + self.find_element(*self.PRODUCT_NAME).text +
              f' is shown on this page ')

        assert self.find_element(*self.PRODUCT_PRICE), f'Expected to find {self.find_element(*self.PRODUCT_PRICE).text} product price on a page'
        print(f'Expected price for product: ' + self.find_element(*self.PRODUCT_PRICE).text +
              f' is shown on this page ')

        assert self.find_element(*self.PRODUCT_DESCRIPTION), f'Expected to find {self.find_element(*self.PRODUCT_DESCRIPTION).text} product price on a page'
        print(f'Expected description for product: ' + self.find_element(*self.PRODUCT_DESCRIPTION).text +
             f' is shown on this page ')

