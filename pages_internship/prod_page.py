from selenium.webdriver.common.by import By
from pages_internship.base_page import Page_Internship
from selenium.webdriver import ActionChains


class Product_Internship(Page_Internship):
    print(f'in Product_Internship(Page_Internship)')
    SEARCH_INPUT = (
        By.CSS_SELECTOR, "li.header-search.header-search-dropdown.has-icon.has-dropdown.menu-item-has-children")
    SEARCH_TOOLTIP = (By.ID, 'woocommerce-product-search-field-0')
    SEARCH_SUBMIT = (By.XPATH, "//*[contains(@class, 'ux-search-submit')]")

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
