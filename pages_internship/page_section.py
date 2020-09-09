from selenium.webdriver import ActionChains

from pages_internship.base_page import Page_Internship
from selenium.webdriver.common.by import By
import time
index.lockgit

class PageSection(Page_Internship):
    BROWSE_CAT_TEXT = (By.XPATH, "//span[contains(text(),'Browse our Categories')]")
    LATEST_SALE_TEXT = (By.XPATH, "//span[contains(text(),'Latest products on sale')]")

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
