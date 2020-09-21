from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages_internship.base_page import Page_Internship
import time


class WishlistServices(Page_Internship):
    print(f'in WishlistServices(Page_Internship)')

    WISHLIST_ICON = (By.CSS_SELECTOR, "div.wishlist-icon")
    CURRENT_PAGE = (By.CSS_SELECTOR, "h2")
    EMPTY_WISHLIST = (By.CSS_SELECTOR, "td.wishlist-empty")
    PRODUCT_ON_WISHLIST = (By.CSS_SELECTOR, "td.product-name a")
    REMOVE_WISHLIST_ICON = (By.CSS_SELECTOR, "a.remove.remove_from_wishlist")
    REMOVE_WISHLIST_MESSAGE = (By.CSS_SELECTOR, "div.message-container.container.success-color.medium-text-center")
    WISHLIST_IMAGE = (By.CSS_SELECTOR, "td.product-thumbnail")
    WISHLIST_ITEM = (By.CSS_SELECTOR, "h1.product-title.product_title.entry-title")

    NETWORKS_BLOCK = (By.CSS_SELECTOR, "div.yith-wcwl-share.social-icons.share-icons.share-row.relative")

    def open_wishlist_page(self):
        self.open_page(f'dp/my-account/wishlist/ ')

    def hover_click_wishlist_icon(self):
        wishlist_icon = self.find_element(*self.WISHLIST_ICON)
        ActionChains(self.driver).move_to_element(wishlist_icon).click().perform()
        time.sleep(5)

    def verify_wishlist_page_opened(self):
        wishlist_page_text = self.find_element(*self.CURRENT_PAGE).text
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(wishlist_page_text, *self.CURRENT_PAGE)
        time.sleep(2)

    def veify_wishlist_empty_message(self, empty_message):
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(empty_message, *self.EMPTY_WISHLIST)
        time.sleep(2)

    def verify_product_added_wishlist(self, product_added):
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(product_added, *self.PRODUCT_ON_WISHLIST)
        time.sleep(2)

    def click_remove_wishlist(self):
        remove_wishlist_icon = self.find_element(*self.REMOVE_WISHLIST_ICON)
        ActionChains(self.driver).move_to_element(remove_wishlist_icon).click().perform()
        time.sleep(5)

    def verify_product_removed_wishlist(self, product_removed_message):
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(product_removed_message, *self.REMOVE_WISHLIST_MESSAGE)
        time.sleep(2)

    def click_wishlist_item(self):
        wishlist_image = self.find_element(*self.WISHLIST_IMAGE)
        ActionChains(self.driver).move_to_element(wishlist_image).click().perform()
        time.sleep(5)

    def open_product_page(self, wishlist_item):
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(wishlist_item, *self.WISHLIST_ITEM)
        time.sleep(2)
