from selenium.webdriver.common.by import By
from pages_internship.base_page import Page_Internship
import time


class SearchResultsInternship(Page_Internship):
    print(f'in SearchResultsInternship(Page_Internship)')

    RESULTS_FOUND_MESSAGE = (By.XPATH, "//input[contains(@value, 'Watch Series 5')]")
    RESULTS_NOT_FOUND_MESSAGE = (By.XPATH, "//p[contains(text(),'No products were found matching your selection.')]")

    def verify_found_results_text(self, search_world):
        search_result = self.find_element(*self.RESULTS_FOUND_MESSAGE)
        search_result_header = search_result.get_attribute("value")
        # time.sleep(2)
        assert search_world in search_result_header, f'Incorrect header: {search_result_header}'

    def verify_no_results_text(self, empty_result):
        search_result_empty = self.find_element(*self.RESULTS_NOT_FOUND_MESSAGE).text
        # time.sleep(2)
        assert empty_result in search_result_empty, f'Incorrect header: {search_result_empty}'


