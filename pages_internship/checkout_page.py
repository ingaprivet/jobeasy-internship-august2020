from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages_internship.base_page import PageServices
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time


class CheckoutServices(PageServices):
    # print(f'in CheckoutServices(PageServices)')

    CART_ICON = (By.CSS_SELECTOR, ".cart-icon.image-icon")
    PLACE_ORDER_BUTTON = (By.ID, "place_order")
    INFO_MISSING_MESSAGE = (By.XPATH, "//li[contains(@data-id, 'billing_first_name')]")
    FORM_ELEMENTS = (By.CSS_SELECTOR, "span.woocommerce-input-wrapper")
    INPUT_FIRST_NAME = (By.ID, "billing_first_name")
    INPUT_LAST_NAME = (By.ID, "billing_last_name")
    INPUT_COMPANY = (By.ID, "billing_company")
    INPUT_COUNTRY = (By.ID, "billing_country")
    INPUT_ADDR1 = (By.ID, "billing_address_1")
    INPUT_ADDR2 = (By.ID, "billing_address_2")
    INPUT_CITY = (By.ID, "billing_city")
    INPUT_STATE = (By.ID, "billing_state")
    INPUT_ZIP = (By.ID, "billing_postcode")
    INPUT_PHONE = (By.ID, "billing_phone")
    INPUT_EMAIL = (By.ID, "billing_email")

    COUNTRY_DROPDOWN = (By.ID, "billing_country")

    def click_country_dropdown(self, alias):
        country_dropdown = self.find_element(*self.COUNTRY_DROPDOWN)
        select = Select(country_dropdown)
        select.select_by_value(alias)

    def go_back(self):
        cart_icon = self.find_element(*self.CART_ICON)
        ActionChains(self.driver).move_to_element(cart_icon).click().perform()

    def place_order(self):
        order_button = self.find_element(*self.PLACE_ORDER_BUTTON)
        ActionChains(self.driver).move_to_element(order_button).click().perform()

    def verify_info_missing_message(self, info_missing_expected):
        info_missing_expected_page = self.find_element(*self.INFO_MISSING_MESSAGE).text
        print("Perform your verification on page {}".format(self.driver.title))
        self.verify_text(info_missing_expected[0:18], *self.INFO_MISSING_MESSAGE)

    def fill_out_form(self):
        # finds all form elements
        # form_elements = self.find_elements(*self.FORM_ELEMENTS)
        # form_element.clear()
        # form_element.send_keys(test_wording)

        test_wording = 'Internship 2020 JobEasy'
        # self.input(test_wording, *self.INPUT_FIRST_NAME)

        self.input(test_wording, *self.INPUT_LAST_NAME)

        self.input(test_wording, *self.INPUT_COMPANY)

        # self.input(test_wording, *self.INPUT_COUNTRY)

        self.input(test_wording, *self.INPUT_ADDR1)

        self.input(test_wording, *self.INPUT_ADDR2)

        self.input(test_wording, *self.INPUT_CITY)

        self.input(test_wording, *self.INPUT_STATE)

        self.input(test_wording, *self.INPUT_ZIP)

        self.input('646 2223333', *self.INPUT_PHONE)

        self.input('gettop@gmail.com', *self.INPUT_EMAIL)
        time.sleep(2)
