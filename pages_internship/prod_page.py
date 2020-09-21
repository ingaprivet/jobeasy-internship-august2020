from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages_internship.base_page import Page_Internship
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time


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
    REVIEW_SUBMIT = (By.CSS_SELECTOR, "input#submit.submit")
    ZOOM_ICON = (By.CSS_SELECTOR, "a.zoom-button")
    CLOSE_ICON = (By.CSS_SELECTOR, "button.pswp__button.pswp__button--close")
    ICON_HEART = (By.CSS_SELECTOR, "button.wishlist-button.button.is-outline.circle.icon")
    POPUP_TEXT = (By.XPATH, "//div[contains(text(),'Product added!')]")
    SCROLL_ARROW = (By.CSS_SELECTOR, "button.pswp__button--arrow--left")
    WISHLIST_PRODUCT = (By.CSS_SELECTOR, "td.product-name")

    HOME_LINK = (By.XPATH, "//a[contains(text(),'Home')]")
    CATEGORY_LINK = (By.XPATH, "//*[contains(@class,'posted_in')]//*[text()='Accessories']")

    PAGE_TEXT_CURRENT = (By.CSS_SELECTOR, "nav.woocommerce-breadcrumb.breadcrumbs.uppercase")
    NETWORKS_BLOCK = (By.CSS_SELECTOR, "div.social-icons.share-icons.share-row.relative")

    NETWORKS_ICONS = (By.CSS_SELECTOR, "div.social-icons a.icon.button.circle.is-outline.tooltip")

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

    def verify_product_attributes_shown(self):
        print("Perform your verification on page {}".format(self.driver.title))

        assert self.find_element(
            *self.PRODUCT_IMAGE), f'Expected to find {self.find_element(*self.PRODUCT_IMAGE).get_attribute("title")} product image on a page'
        print(f'Expected image for product ' + self.find_element(*self.PRODUCT_IMAGE).get_attribute("title") +
              f' is shown on this page ')

        assert self.find_element(
            *self.PRODUCT_NAME), f'Expected to find {self.find_element(*self.PRODUCT_NAME).text} product name on a page'
        print(f'Expected name for product ' + self.find_element(*self.PRODUCT_NAME).text +
              f' is shown on this page ')

        assert self.find_element(
            *self.PRODUCT_PRICE), f'Expected to find {self.find_element(*self.PRODUCT_PRICE).text} product price on a page'
        print(f'Expected price for product ' + self.find_element(*self.PRODUCT_PRICE).text +
              f' is shown on this page ')

        assert self.find_element(
            *self.PRODUCT_DESCRIPTION), f'Expected to find {self.find_element(*self.PRODUCT_DESCRIPTION).text} product price on a page'
        print(f'Expected description for product ' + self.find_element(*self.PRODUCT_DESCRIPTION).text +
              f' is shown on this page ')

    def verify_zoomin_product_image(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.ZOOM_ICON)).click().perform()
        time.sleep(5)
        print("Perform your verification on page {}".format(self.driver.title))

        assert self.find_element(
            *self.ZOOM_ICON), f'Expected to find {self.find_element(*self.ZOOM_ICON).get_attribute("href")} product zoom on a page'
        print(f'Expected zoom icon for product ' + self.find_element(*self.PRODUCT_NAME).text +
              f' is shown on this page ')

    def verify_scroll_product_images(self):
        ActionChains(self.driver).move_to_element(self.find_element(*self.SCROLL_ARROW)).click().perform()
        time.sleep(5)

        print("Perform your verification on page {}".format(self.driver.title))
        assert self.find_element(
            *self.SCROLL_ARROW), f'Expected to find {self.find_element(*self.SCROLL_ARROW)} product scroll arrow on a page'
        print(f'Expected scroll arrow for product ' + self.find_element(*self.PRODUCT_NAME).text +
              f' is shown on this page ')

    def verify_close_product_images(self):
        close_icon = self.find_element(*self.CLOSE_ICON)
        # ActionChains(self.driver).move_to_element(self.find_element(*self.CLOSE_ICON)).click().perform()

        self.click(*self.CLOSE_ICON)
        time.sleep(5)

        print("Perform your verification on page {}".format(self.driver.title))
        assert self.find_element(
            *self.CLOSE_ICON), f'Expected to find {self.find_element(*self.CLOSE_ICON)} product close icon on a page'
        print(f'Expected close icon for product ' + self.find_element(*self.PRODUCT_NAME).text +
              f' is shown on this page ')

    def hover_click_heart_icon(self):
        heart_icon = self.find_element(*self.ICON_HEART)
        ActionChains(self.driver).move_to_element(heart_icon).click().perform()
        time.sleep(5)

        # take screenshot
        self.driver.save_screenshot("pageImage.png")

    def verify_product_added_wishlist(self):
        print("Perform your verification on page {}".format(self.driver.title))
        assert self.find_element(
            *self.POPUP_TEXT), f'Expected to find {self.find_element(*self.POPUP_TEXT)} product added popup on a page'
        print(f'Expected product added popup ' + self.find_element(*self.POPUP_TEXT).text +
              f' is shown on this page ')

    def click_home_link(self):
        self.click(*self.HOME_LINK)

    def click_product_category_link(self):
        self.click(*self.CATEGORY_LINK)

    def product_category_shown(self, product_category):
        print("Perform your verification on page {}".format(self.driver.title))
        assert self.find_element(
            *self.PAGE_TEXT_CURRENT), f'Expected to find {product_category} product category on a page'
        print(f'Expected text: ' + product_category +
              f' is in the actual page title: ' + self.find_element(
            *self.PAGE_TEXT_CURRENT).text)

    def social_network_logos_shown(self):
        print("Perform your verification on page {}".format(self.driver.title))

        hover_networks_block = self.find_element(*self.NETWORKS_BLOCK)
        ActionChains(self.driver).move_to_element(hover_networks_block).perform()
        time.sleep(5)
        assert self.find_element(
            *self.NETWORKS_BLOCK), f'Expected to find {self.find_element(*self.NETWORKS_BLOCK)} element on a page'
        print(f'Expected social networks block ' + self.find_element(*self.NETWORKS_BLOCK).text +
              f' is shown on this page ')

    def hover_click_social_networks(self):
        hover_networks_icons = self.find_elements(*self.NETWORKS_ICONS)
        time.sleep(2)

        windows_before = self.driver.current_window_handle  # Store the parent_window_handle for future use

        array_of_links = []

        index = 0

        for link in hover_networks_icons:

            link_info = link.get_attribute("href")

            if not link_info.startswith('whatsapp') and not link_info.startswith('https://tumblr.com/') and not link_info.startswith('mailto') and not link_info.startswith('https://pinterest') :
                array_of_links.append(link_info)

        for link in array_of_links:
            url_link = array_of_links[index]  # url from the saved array

            self.driver.execute_script(
                "window.open('" + url_link + "');")  # Open the hrefs one by one through execute_script method in a new tab
            WebDriverWait(self.driver, 10).until(
                EC.number_of_windows_to_be(2))  # Induce  WebDriverWait for the number_of_windows_to_be 2

            windows_after = self.driver.window_handles  # list

            for x in windows_after:
                if x != windows_before:
                    self.driver.switch_to.window(x)  # switch_to the new window
                    windows_new = self.driver.current_url
                    assert url_link[:25].find(
                        windows_new[:25]) != -1, f'Expected {url_link[:25]} to be in {windows_new[:25]}'

                    print(f'Expected url: ' + url_link[:25] + f' is in the actual url: ' + windows_new[:25])
                    time.sleep(3)

            self.driver.close()  # close the window
            self.driver.switch_to.window(windows_before)  # switch_to the parent_window_handle
            time.sleep(2)

            index += 1
