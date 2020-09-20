from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages_internship.base_page import Page_Internship
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
import time


class CheckoutServices(Page_Internship):
    print(f'in CheckoutServices(Page_Internship)')

    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, ".select2-selection__rendered")
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

    def click_country_dropdown(self, country):
        print(f'click_count_dropdown')
        # click_country_dropdown = self.find_element(*self.COUNTRY_DROPDOWN)
        # ActionChains(self.driver).move_to_element(click_country_dropdown).click().perform()

        self.input(country, *self.COUNTRY_DROPDOWN)

        # e = browser.find_element_by_xpath('//[@id="react-select-5--value"]/div[2]/input')
        # click_country_dropdown.send_keys("China")
        # click_country_dropdown.send_keys(Keys.RETURN)
        time.sleep(5)

    def go_back(self):
        cart_icon = self.find_element(*self.CART_ICON)
        ActionChains(self.driver).move_to_element(cart_icon).click().perform()

    def place_order(self):
        self.click(*self.PLACE_ORDER_BUTTON)

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
        self.input(test_wording, *self.INPUT_FIRST_NAME)

        self.input(test_wording, *self.INPUT_LAST_NAME)

        self.input(test_wording, *self.INPUT_COMPANY)

        # self.input(test_wording, *self.INPUT_COUNTRY)

        self.input(test_wording, *self.INPUT_ADDR1)

        self.input(test_wording, *self.INPUT_ADDR2)

        self.input(test_wording, *self.INPUT_CITY)

        # self.input(test_wording, *self.INPUT_STATE)

        self.input(test_wording, *self.INPUT_ZIP)

        self.input(test_wording, *self.INPUT_PHONE)

        self.input(test_wording, *self.INPUT_EMAIL)

        time.sleep(5)

        # self.click(*self.PLACE_ORDER_BUTTON)
        place_order_button = self.find_element(*self.PLACE_ORDER_BUTTON)
        ActionChains(self.driver).move_to_element(place_order_button).click().perform()
