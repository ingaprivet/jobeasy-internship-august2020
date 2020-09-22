from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_internship.base_page import PageServices
from selenium.webdriver.common.by import By
import time


class PageSectionServices(PageServices):
    BROWSE_CAT_TEXT = (By.XPATH, "//span[contains(text(),'Browse our Categories')]")
    LATEST_SALE_TEXT = (By.XPATH, "//span[contains(text(),'Latest products on sale')]")
    BEST_SELLING_FOOTER = (By.XPATH, "//span[contains(text(),'Best Selling')]")
    LATEST_FOOTER = (By.XPATH, "//span[contains(text(),'Latest')]")
    TOP_RATED_FOOTER = (By.XPATH, "//span[contains(text(),'Top Rated')]")
    COPYRIGHT_FOOTER = (By.CSS_SELECTOR, "div.copyright-footer")

    PAGE_TEXT_CURRENT = (By.CSS_SELECTOR, "nav.woocommerce-breadcrumb.breadcrumbs.uppercase")
    PRODUCT_CATEGORIES = (By.XPATH, "//*[contains(@class, 'col-inner')]//*[contains(@href, 'product-category')]")
    CALC_CATEGORIES = (By.XPATH, "div.flickity-slider div.product-category.col.is-selected")
    TOP_LINK = (By.ID, "top-link")
    # FOOTER_LINKS_BLOCK = (By.CSS_SELECTOR, "ul#menu-main-1.links.footer-nav.uppercase")

    FOOTER_LINKS_BLOCK = (By.CSS_SELECTOR,
                          "div.container.clearfix li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-has-children a")

    TAB_DESCRIPTION = (By.CSS_SELECTOR, "li.description_tab")
    TAB_REVIEW = (By.CSS_SELECTOR, "li.reviews_tab")

    def verify_current_section(self):

        print("Perform your verification on page {}".format(self.driver.title))

        current_section_text = (self.find_element(*self.BROWSE_CAT_TEXT)).text
        current_section_text01 = (self.find_element(*self.LATEST_SALE_TEXT)).text

        if current_section_text is not None and current_section_text01 is not None:
            self.verify_text(current_section_text, *self.BROWSE_CAT_TEXT)
            self.verify_text(current_section_text01, *self.LATEST_SALE_TEXT)
        elif current_section_text is None:
            self.verify_text(current_section_text01, *self.LATEST_SALE_TEXT)
        elif current_section_text01 is None:
            self.verify_text(current_section_text, *self.BROWSE_CAT_TEXT)

    def category_shown_quantity(self, cat_quantity):
        hover_ul = self.find_elements(*self.PRODUCT_CATEGORIES)
        quantity_of_product_categories = 0

        for i in hover_ul:
            # hover over all items one by one
            ActionChains(self.driver).move_to_element(i).perform()
            quantity_of_product_categories += 1

        print("Perform your verification on page {}".format(self.driver.title))
        assert str(cat_quantity) in str(
            quantity_of_product_categories), f'Expected {cat_quantity} to be in {quantity_of_product_categories}'
        print(f'Expected product category quantity: ' + str(cat_quantity) + f' is in the actual quantity: ' + str(
            quantity_of_product_categories))

    def hover_and_show(self):

        hover_cat_block = self.find_elements(*self.PRODUCT_CATEGORIES)
        #time.sleep(2)

        windows_before = self.driver.current_window_handle  # Store the parent_window_handle for future use

        array_of_links = []
        array_of_text = []

        index = 0

        for link in hover_cat_block:
            link_info = link.get_attribute("href")
            array_of_links.append(link_info)
            text_info = link.get_attribute("innerText")
            array_of_text.append(text_info)

        for link in hover_cat_block:
            url_link = array_of_links[index]  # url from the saved array
            text_info_default = array_of_text[index]

            self.driver.execute_script(
                "window.open('" + url_link + "');")  # Open the hrefs one by one through execute_script method in a new tab
            WebDriverWait(self.driver, 10).until(
                EC.number_of_windows_to_be(2))  # Induce  WebDriverWait for the number_of_windows_to_be 2

            windows_after = self.driver.window_handles  # list

            for x in windows_after:

                if x != windows_before:
                    self.driver.switch_to.window(x)  # switch_to the new window
                    windows_new = self.driver.current_url
                    print("Perform your verification on page {}".format(self.driver.title))
                    assert url_link == windows_new, f'Expected {windows_new} url address, but got {url_link} url address'
                    print(f'Expected url: ' + url_link + f' is in the actual url: ' + windows_new)
                    #time.sleep(3)

            self.driver.close()  # close the window
            self.driver.switch_to.window(windows_before)  # switch_to the parent_window_handle
            #time.sleep(2)

            index += 1

    def verify_footer_section(self, footer_cat01, footer_cat02, footer_cat03):
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(footer_cat01.upper(), *self.BEST_SELLING_FOOTER)
        self.verify_text(footer_cat02.upper(), *self.LATEST_FOOTER)
        self.verify_text(footer_cat03.upper(), *self.TOP_RATED_FOOTER)

    def verify_copy(self, footer_copy):
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(footer_copy, *self.COPYRIGHT_FOOTER)

    def hover_click_top_links(self):
        print("Perform your verification on page {}".format(self.driver.title))
        footer_links_block = self.find_elements(*self.FOOTER_LINKS_BLOCK)
        windows_before = self.driver.current_window_handle  # Store the parent_window_handle for future use
        array_of_links = []
        index = 0

        for link in footer_links_block:
            link_info = link.get_attribute("href")
            array_of_links.append(link_info)

        for link in footer_links_block:
            url_link = array_of_links[index]  # url from the saved array

            self.driver.execute_script(
                "window.open('" + url_link + "');")  # Open the hrefs one by one through execute_script method in a new tab
            WebDriverWait(self.driver, 15).until(
                EC.number_of_windows_to_be(2))  # Induce  WebDriverWait for the number_of_windows_to_be 2

            windows_after = self.driver.window_handles  # list

            for x in windows_after:

                if x != windows_before:
                    self.driver.switch_to.window(x)  # switch_to the new window
                    windows_new = self.driver.current_url
                    print("Perform your verification on page {}".format(self.driver.title))
                    assert url_link in windows_new, f'Expected text {url_link}, but got {windows_new}'

                    print(f'Expected url: ' + url_link + f' is in the actual url: ' + windows_new)

            self.driver.close()  # close the window
            self.driver.switch_to.window(windows_before)  # switch_to the parent_window_handle

            index += 1

    def hover_click_top_link(self):
        top_link = self.find_element(*self.TOP_LINK)
        ActionChains(self.driver).move_to_element(top_link).click().perform()
        #time.sleep(5)

    def verify_product_page_section(self, product_page_block):
        print("Perform your verification on page {}".format(self.driver.title))
        if product_page_block == "DESCRIPTION BLOCK":
            self.verify_text(product_page_block.upper(), *self.TAB_DESCRIPTION)
        elif product_page_block == "REVIEW BLOCK":
            self.verify_text(product_page_block.upper(), *self.TAB_REVIEW)


