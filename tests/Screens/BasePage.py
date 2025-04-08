import logging

from Config.Constants import WAIT_TIMEOUT
from sikuli import click, exists, wait, sleep, FindFailed


class BasePage:
    def __init__(self):
        pass

    def clickElement(self, image, name):
        if exists(image, WAIT_TIMEOUT):
            click(image)
            logging.info("Clicked on %s", name)
        else:
            raise FindFailed("%s not found!" % name)

    def assertExists(self, image, name):
        if exists(image, WAIT_TIMEOUT):
            logging.info("%s exists", name)
        else:
            raise FindFailed("%s not found!" % name)

    def waitElement(self, pattern):
        wait(pattern, WAIT_TIMEOUT)

    def sleep(self, secs):
        sleep(secs)
