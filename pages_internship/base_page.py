from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page_Internship:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://gettop.us/'
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text: str, *locator):
        #print(f'in verify_text of base_page')
        actual_text = self.driver.find_element(*locator).text
        #print(f'actual_text = ', actual_text)
        assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'
        print(f'Expected text: ' + expected_text + f' is in the actual text: ' + actual_text)


