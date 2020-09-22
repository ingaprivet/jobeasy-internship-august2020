from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages_internship.base_page import Page_Internship
import time


class TopNavMenu_Internship(Page_Internship):
    LOGO_SUBMIT = (By.XPATH, "//a[@rel='home']")
    CURRENT_PAGE = (By.XPATH, "//a[@title='gettop.us - Just another WordPress site']")
    SELECT_TOP_NAV_ITEM = (By.CSS_SELECTOR, "ul.header-nav.header-nav-main.nav.nav-left.nav-uppercase a.nav-top-link")
    PAGE_TEXT_CURRENT = (By.CSS_SELECTOR, "div.is-large")
    TOOLTIP_DROPDOWN = (By.CSS_SELECTOR, "a:hover")
    ICON_USER = (By.CSS_SELECTOR, "i.icon-user")
    LOGIN_FORM = (By.ID, "login-form-popup")

    def logo_present(self):
        self.wait_for_element_appear(*self.LOGO_SUBMIT)

    def go_to_page(self):
        self.click(*self.LOGO_SUBMIT)

    def verify_page_displayed(self):
        self.find_elements(*self.CURRENT_PAGE)

    # @when 'Select a Mac product from header-nav-main and open correct product page'
    def select_product_opens_page(self):
        # finds all elements from header-nav-main
        hover_ul = self.find_elements(*self.SELECT_TOP_NAV_ITEM)
        time.sleep(2)

        windows_before = self.driver.current_window_handle  # Store the parent_window_handle for future use
        array_of_links = []
        array_of_text = []

        index = 0

        for link in hover_ul:
            link_info = link.get_attribute("href")
            array_of_links.append(link_info)
            text_info = link.get_attribute("innerText")
            array_of_text.append(text_info)

        for link in hover_ul:
            url_link = array_of_links[index]  # url fr om the saved array
            text_info_default = array_of_text[index]

            self.driver.execute_script(
                "window.open('" + url_link + "');")  # Open the hrefs one by one through execute_script method in a new tab
            WebDriverWait(self.driver, 10).until(
                EC.number_of_windows_to_be(2))  # Induce  WebDriverWait for the number_of_windows_to_be 2

            assert url_link == array_of_links[
                index], f'Expected {array_of_links[index]} url address, but got {url_link} url address'

            windows_after = self.driver.window_handles

            for x in windows_after:
                if x != windows_before[0]:
                    self.driver.switch_to.window(x)  # switch_to the new window
                    time.sleep(3)

            print("Perform your verification on page {}".format(self.driver.title))
            page_text_current = self.find_element(*self.PAGE_TEXT_CURRENT).text

            self.driver.close()  # close the window
            self.driver.switch_to.window(windows_before)  # switch_to the parent_window_handl
            #time.sleep(2)

            index += 1
            assert text_info_default in page_text_current, f'Expected {text_info_default} to be in {page_text_current}'
            print(f'Expected text: ' + text_info_default + f' is in the actual text: ' + page_text_current)
            #self.verify_text(text_info_default, *self.PAGE_TEXT_CURRENT) !!! do not have available selector":"div.is-large to execute base page method

    # @when 'Hoover over header-nav-main item and display correct menu options'
    def hover_and_display(self):
        # self.driver.implicitly_wait(15)
        hover_ul = self.find_elements(*self.SELECT_TOP_NAV_ITEM)

        for i in hover_ul:
            # hover over all items one by one
            ActionChains(self.driver).move_to_element(i).perform()
            text_to_verify_tooltip = i.get_attribute("text")
            #time.sleep(2)

            try:
                tooltip = self.find_element(*self.TOOLTIP_DROPDOWN)
                print("Perform your verification on page {}".format(self.driver.title))
                self.verify_text(text_to_verify_tooltip.upper(), *self.TOOLTIP_DROPDOWN)
                time.sleep(2)
            except NoSuchElementException:
                break

    # @when 'Clicking on Account icon'
    def go_to_login_form(self):
        self.click(*self.ICON_USER)
        #time.sleep(2)

    # @then('Login form opens')
    def verify_login_form(self):
        self.wait_for_element_appear(*self.LOGIN_FORM)
        #time.sleep(2)






