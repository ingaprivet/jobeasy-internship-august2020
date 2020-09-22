from selenium.webdriver import ActionChains

from pages_internship.base_page import PageServices
from selenium.webdriver.common.by import By
import time


class TopBannerServices(PageServices):
    CLICK_ARROW = (By.CSS_SELECTOR, "svg.flickity-button-icon")
    CLICK_DOTS = (By.CSS_SELECTOR, "li.dot")

    PRODUCT_LINK_01 = (By.XPATH, "//*[contains(@class, 'fill')]//*[contains(@href, '/product-category/ipad/')]")
    PRODUCT_LINK_02 = (By.XPATH, "//*[contains(@class, 'fill')]//*[contains(@href, '/product-category/macbook/')]")

    BANNER_SUBMIT_01 = (By.XPATH, "//*[contains(@href, 'product-category/macbook')]")
    BANNER_SUBMIT_02 = (By.XPATH, "//*[contains(@href, 'product-category/ipad')]")

    # @when('Click on right and left arrows')
    def click_arrows(self):
        self.click(*self.CLICK_ARROW)
        #time.sleep(5)

    # @when('Click bottom dots')
    def click_bottom_dots(self):
        self.click(*self.CLICK_DOTS)

    def verify_page(self):
        print("Perform your verification on page {}".format(self.driver.title))
        current_page_text = (self.find_element(*self.BANNER_SUBMIT_01)).text
        current_page_text_01 = (self.find_element(*self.BANNER_SUBMIT_02)).text

        if current_page_text is not None and current_page_text_01 is not None:
            self.verify_text(current_page_text, *self.BANNER_SUBMIT_01)
            self.verify_text(current_page_text_01, *self.BANNER_SUBMIT_02)
        elif current_page_text is None:
            self.verify_text(current_page_text_01, *self.BANNER_SUBMIT_02)
        elif current_page_text_01 is None:
            self.verify_text(current_page_text, *self.BANNER_SUBMIT_01)

    # @when('Click on Product01 banner')
    def click_banner_product01(self):
        self.wait_for_element_click(*self.PRODUCT_LINK_01)
        # time.sleep(5)

    # @when('Click on Product02 banner')
    def click_banner_product02(self):
        self.wait_for_element_click(*self.PRODUCT_LINK_02)
        # time.sleep(5)
