import logging.handlers
import datetime
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

now = datetime.datetime.now()
print(f'Current date and time : ' + now.strftime("%Y-%m-%d %H:%M:%S"))

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info('foo bar')

handler = logging.FileHandler('./jobeasy-internship-august2020/test_automation.log')
# handler = logging.StreamHandler() #= will print all messages to the terminal
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s (%(name)s) %(message)s')
# formatter = logging.Formatter(logging.BASIC_FORMAT)

handler.setFormatter(formatter)
logger.addHandler(handler)


class MyListener(AbstractEventListener):
    logger = logger

    def before_find(self, by, value, driver):
        message = (by, value, "searching ...")
        logger.info(message)

    def after_find(self, by, value, driver):
        message = (by, value, "found.")
        logger.info(message)

    def on_exception(self, exception, driver):
        logger.warning(Exception)
