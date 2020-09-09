from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from app_internship.application_internship import Application_Internship
from features.logger import logger
import datetime

now = datetime.datetime.now()
# print(f'Current date and time : ' + now.strftime("%Y-%m-%d %H:%M:%S"))
bs_user = 'ingabukhvalova1'
bs_pw = 'T6ChdbMGku9CL7mMzxp5'


# def browser_init(context, name):
#:param context: Behave context

def browser_init(context, name):
    context.driver = webdriver.Chrome(
        executable_path='/Users/ingabukhvalova/PycharmProjects/jobeasy-internship-august2020/drivers/chromedriver')

    # context.driver = webdriver.Firefox(
    #  executable_path='/Users/ingabukhvalova/PycharmProjects/python-selenium-automation/drivers/geckodriver')

    # context.driver = webdriver.Safari()

    ### Code for HEADLESS
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(
    #    executable_path='/Users/ingabukhvalova/PycharmProjects/python-selenium-automation/drivers/chromedriver',
    #    chrome_options=options)
    ### End HEADLESS

    ###Code for EventFiringWebDriver
    # from features.logger import MyListener
    # context.driver = EventFiringWebDriver(context.driver, MyListener())
    ###End for EventFiringWebDriver

    ###Code for Browser Stack for Chrome
    '''desired_cap = {

        'os': 'OS X',
        'os_version': 'Sierra',
        'browser': 'Chrome',
        'browser_version': '81',
        'project': 'Selenium Automation',
        'build': "1.1.01",
        'name': name

    }'''
    ###End for Browser Stack for Chrome

    ### Code for Browser Stack for Appium
    '''desired_cap = {
        'automationName': 'Appium',
        'browserstack.appium_version': '1.11.1',
        'project': 'Selenium Automation',
        'build': "1.1.01",
        'name': name,
        'device': 'Google Nexus 6',
        'real_mobile': 'true',
        'os': 'android',
        'browserstack.debug': 'true',
        'os_version': '6.0',
        'autoGrantPermissions': 'true'
    }'''
    ###End for Appium!!! '''
    #  'app_internship' => 'my-app_internship-name'

    ### Code for Browser Stack URL
    # BROWSERSTACK_URL = 'https://ingabukhvalova1:T6ChdbMGku9CL7mMzxp5@hub-cloud.browserstack.com/wd/hub'
    '''BROWSERSTACK_URL = f'https://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'

    context.driver = webdriver.Remote(

        command_executor=BROWSERSTACK_URL,
        desired_capabilities=desired_cap
    )
    '''
    ###End for Browser Stack URL

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app_internship = Application_Internship(context.driver)
    context.driver.wait = WebDriverWait(context.driver, 10)


# my code
def open_new_tab(context, link):
    window_count = len(context.driver.window_handles)
    context.driver.execute_script('''window.open("''' + link + '''","_blank");''')

    while len(context.driver.window_handles) != window_count + 1:
        # sleep(0.5)
        context.driver.wait(0, 5)
    context.driver.switch_to.window(context.driver.window_handles[-1])


# my code

def before_scenario(context, scenario):
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'\nStarted step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.info(f'\nStarted failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
