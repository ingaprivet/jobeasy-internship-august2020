from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
CLICK_ARROW = (By.CSS_SELECTOR, "svg.flickity-button-icon")
# $x("//div[@id='slider-771962463']//*[contains(@class, 'arrow')]")
# CLICK_ARROW = (By.XPATH, "//div[@id='slider-771962463']//*[contains(@class, 'arrow')]")


CLICK_DOTS = (By.CSS_SELECTOR, "li.dot")
# $x("//li[contains(@class, 'dot')]")
# CLICK_DOTS = (By.XPATH, "//li[contains(@class, 'dot')]")


@given('Open Home page')
def open_google(context):
    context.driver.get('https://gettop.us//')


'''

 When Click on right and left arrors
    And Click bottom dots
    Then Top banners are shown

@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)
'''


@when('Click bottom dots')
def click_dots(context):
    print(f'in Click bottom dots')
    context.driver.find_element(*CLICK_DOTS).click()
    sleep(5)


@when('Click on right and left arrows')
def click_arror(context):
    print(f'Click on right and left arrowrs')
    context.driver.find_element(*CLICK_ARROW).click()
    sleep(5)


'''
@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)


@then('First result contains {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)
'''
