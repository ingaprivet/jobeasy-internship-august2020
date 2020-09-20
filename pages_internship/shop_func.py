from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_internship.base_page import Page_Internship
import time


class ShopServices(Page_Internship):
    print(f'in ShopServices(Page_Internship)')

    RECENTLY_VIEWD_BLOCK = (By.CSS_SELECTOR, "aside.widget.woocommerce.widget_recently_viewed_products")
    RECENTLY_VIEWD_ITEMS = (By.CSS_SELECTOR, "aside ul.product_list_widget a")

    BROWSE_CATEGORIES = (By.CSS_SELECTOR, "li.cat-item a")
    NEXT_PAGE_ICON = (By.CSS_SELECTOR, "a.page-number")
    NEXT_PAGE_ARROW = (By.CSS_SELECTOR, "a.next.page-number")

    PAGE_TEXT_CURRENT = (By.XPATH, "//*[contains(text(),'Page 2')]")
    GO_HOME_LINK = (By.XPATH, "//a[contains(text(),'Home')]")

    SLIDER_HANDLE = (By.CSS_SELECTOR, "span.ui-slider-handle")

    FILTER_BUTTON = (By.CSS_SELECTOR, "div.price_slider_amount button")

    ACTIVE_FILTERS = (By.CSS_SELECTOR, "h2.widgettitle")

    MIN_PRICE = (By.CSS_SELECTOR, "span.from")
    MAX_PRICE = (By.CSS_SELECTOR, "div.price_label span.to")

    MIX_PRICE_FILTERED = (By.XPATH, "//li[contains(@class, 'chosen')]//a[contains(text(),'Min')]")
    MAX_PRICE_FILTERED = (By.XPATH, "//li[contains(@class, 'chosen')]//a[contains(text(),'Max')]")
    # CLEAR_FILTERS = (By.XPATH, "//div[contains(@class, 'inline-block')]//a[contains(@aria-label, 'Remove filter')]")
    # CLEAR_FILTERS = (By.CSS_SELECTOR, "a.tooltipstered span.woocommerce-Price-amount.amount")

    # CLEAR_FILTERS = (By.CSS_SELECTOR, "a.tooltipstered::before")
    CLEAR_FILTERS = (By.CSS_SELECTOR, "li.chosen")
    NO_MATCH_BY_PRICE_MESSAGE = (By.CSS_SELECTOR, "p.woocommerce-info")

    def open_shop_page(self):
        self.open_page(f'dp/shop/ ')

    def recently_viewed_items_shown(self):
        print("Perform your verification on page {}".format(self.driver.title))

        assert self.find_element(
            *self.RECENTLY_VIEWD_BLOCK), f'Expected to find {self.find_element(*self.RECENTLY_VIEWD_BLOCK).get_attribute("title")} recently viewed items on a page'
        print(
            f'Expected recently viewed items ' + self.find_element(*self.RECENTLY_VIEWD_BLOCK).get_attribute("title") +
            f' shown on this page ')

    def item_page_shown(self):
        recently_viewed_items = self.find_elements(*self.RECENTLY_VIEWD_ITEMS)

        windows_before = self.driver.current_window_handle  # Store the parent_window_handle for future use

        for e in recently_viewed_items:
            url_link = e.get_attribute("href")
            self.driver.execute_script(
                "window.open('" + url_link + "');")  # Open the hrefs one by one through execute_script method in a new tab
            WebDriverWait(self.driver, 10).until(
                EC.number_of_windows_to_be(2))  # Induce  WebDriverWait for the number_of_windows_to_be 2

            windows_after = self.driver.window_handles  # list

            for x in windows_after:
                if x != windows_before:
                    self.driver.switch_to.window(x)  # switch_to the new window
                    windows_new = self.driver.current_url
                    assert url_link.find(
                        windows_new) != -1, f'Expected {url_link} to be in {windows_new}'

                    print(f'Expected url: ' + url_link + f' is in the actual url: ' + windows_new)

            self.driver.close()  # close the window
            self.driver.switch_to.window(windows_before)  # switch_to the parent_window_handle

    def verify_categories_block(self, cat_01, cat_02, cat_03, cat_04):
        '''def verify_footer_section(self, footer_cat01, footer_cat02, footer_cat03):
            print("Perform your verification on page {}".format(self.driver.title))
            self.verify_text(footer_cat01.upper(), *self.BEST_SELLING_FOOTER)
            self.verify_text(footer_cat02.upper(), *self.LATEST_FOOTER)
            self.verify_text(footer_cat03.upper(), *self.TOP_RATED_FOOTER)'''
        pass

    def click_open_category_page(self):

        browse_categories = self.find_elements(*self.BROWSE_CATEGORIES)
        windows_before = self.driver.current_window_handle  # Store the parent_window_handle for future use

        for e in browse_categories:
            url_link = e.get_attribute("href")
            category_title = e.get_attribute("text")
            print("Perform your verification on page {}".format(self.driver.title))

            print(f'text = ', category_title)

            self.driver.execute_script(
                "window.open('" + url_link + "');")  # Open the hrefs one by one through execute_script method in a new tab
            WebDriverWait(self.driver, 10).until(
                EC.number_of_windows_to_be(2))  # Induce  WebDriverWait for the number_of_windows_to_be 2

            windows_after = self.driver.window_handles  # list

            for x in windows_after:
                if x != windows_before:
                    self.driver.switch_to.window(x)  # switch_to the new window
                    windows_new = self.driver.current_url
                    assert url_link.find(
                        windows_new) != -1, f'Expected {url_link} to be in {windows_new}'

                    print(f'Expected url: ' + url_link + f' is in the actual url: ' + windows_new)

            self.driver.close()  # close the window
            self.driver.switch_to.window(windows_before)  # switch_to the parent_window_handle

    def open_next_page_number(self):
        next_page_icon = self.find_element(*self.NEXT_PAGE_ICON)
        ActionChains(self.driver).move_to_element(next_page_icon).click().perform()
        # time.sleep(5)

    def open_next_page_arrow(self):
        next_page_arrow = self.find_element(*self.NEXT_PAGE_ARROW)
        ActionChains(self.driver).move_to_element(next_page_arrow).click().perform()
        # time.sleep(5)

    def verify_correct_page_number_shown(self, expected_page_text):

        print("Perform your verification on page {}".format(self.driver.title))
        # page_text = self.find_element(
        #   *self.PAGE_TEXT_CURRENT).get_attribute("innerText")

        assert self.find_element(*self.PAGE_TEXT_CURRENT).get_attribute("innerText"), \
            f'Expected to find {expected_page_text} ' \
            f'product category on a page'
        print(f'Expected text: ' + expected_page_text +
              f' is in the actual page title: ' +
              self.find_element(*self.PAGE_TEXT_CURRENT).get_attribute("innerText"))

    def go_home(self):
        print("Perform your verification on page {}".format(self.driver.title))
        go_home_link = self.find_element(*self.GO_HOME_LINK)
        ActionChains(self.driver).move_to_element(go_home_link).click(go_home_link).perform()

    def use_price_filter(self):
        slider_handle = self.find_elements(*self.SLIDER_HANDLE)[0]

        ActionChains(self.driver).click_and_hold(slider_handle).move_by_offset(100, 0).perform()
        # time.sleep(5)

        min_price = self.find_element(*self.MIN_PRICE).get_attribute("innerText")
        max_price = self.find_element(*self.MAX_PRICE).get_attribute("innerText")
        self.driver.response = min_price, max_price  # this will create a tuple to be passed to the next step

        print("Perform your verification on page {}".format(self.driver.title))

        assert self.find_element(
            *self.SLIDER_HANDLE), f'Expected to find {self.find_element(*self.SLIDER_HANDLE).text} price ' \
                                  f'filter slider on a page'
        print(f'Expected  price filter slider ' + self.find_element(*self.SLIDER_HANDLE).text +
              f' is shown on this page ')

    def click_filter_button(self):
        filter_button = self.find_element(*self.FILTER_BUTTON)
        ActionChains(self.driver).move_to_element(filter_button).click().perform()

    def filtered_price_items_shown(self):

        active_filters_text = self.find_element(*self.ACTIVE_FILTERS).text
        active_min_price_text = self.find_elements(*self.MIX_PRICE_FILTERED)[1].text
        active_max_price_text = self.find_elements(*self.MAX_PRICE_FILTERED)[1].text

        price_expected = self.driver.response
        min_price_expected = price_expected[0]
        max_price_expected = price_expected[1]

        print("Perform your verification on page {}".format(self.driver.title))
        assert min_price_expected in active_min_price_text, f'Expected text {min_price_expected}, ' \
                                                            f'but got {active_min_price_text}'
        print(f'Expected text: ' + min_price_expected +
              f' is in the actual price filter: ' + active_min_price_text)

        assert max_price_expected in active_max_price_text, f'Expected text {max_price_expected}, ' \
                                                            f'but got {active_max_price_text}'
        print(f'Expected text: ' + max_price_expected +
              f' is in the actual price filter: ' + active_max_price_text)

        assert self.find_element(
            *self.ACTIVE_FILTERS), f'Expected to find {self.find_element(*self.ACTIVE_FILTERS).text} active filters on a page'
        print(f'Expected  active filters block ' + self.find_element(*self.ACTIVE_FILTERS).text +
              f' is shown on this page ')

    def price_filter_reset(self):
        pass

        '''clear_filters_max = self.find_elements(*self.CLEAR_FILTERS)[0]
        clear_filters_min = self.find_elements(*self.CLEAR_FILTERS)[1]

        print(f'clear_filters_min = ', clear_filters_min)

        ActionChains(self.driver).move_to_element(clear_filters_max).click().perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(clear_filters_min).click().perform()
        time.sleep(2)
        print("Perform your verification on page {}".format(self.driver.title))
'''

    def verify_no_match_message(self,no_match_message):

        slider_handle = self.find_elements(*self.SLIDER_HANDLE)[0]
        ActionChains(self.driver).click_and_hold(slider_handle).move_by_offset(300, 0).perform()

        filter_button = self.find_element(*self.FILTER_BUTTON)
        ActionChains(self.driver).move_to_element(filter_button).click().perform()

        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(no_match_message, *self.NO_MATCH_BY_PRICE_MESSAGE)


