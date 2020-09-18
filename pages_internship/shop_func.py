from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages_internship.base_page import Page_Internship
import time


class ShopServices(Page_Internship):
    RECENTLY_VIEWD_BLOCK = (By.CSS_SELECTOR, "aside.widget.woocommerce.widget_recently_viewed_products")
    RECENTLY_VIEWD_ITEMS = (By.CSS_SELECTOR, "aside ul.product_list_widget a")

    def open_shop_page(self):
        self.open_page(f'dp/shop/ ')
        time.sleep(5)

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
                    time.sleep(3)

            self.driver.close()  # close the window
            self.driver.switch_to.window(windows_before)  # switch_to the parent_window_handle
            time.sleep(2)
