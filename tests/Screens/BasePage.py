import logging
import traceback

from Config.Constants import WAIT_TIMEOUT
from sikuli import click, exists, type, FindFailed


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

    def typeText(self, text):
        try:
            type(text)
            logging.info("Typed text: %s", text)
        except Exception:
            logging.error("Failed to type text '%s': %s", text, traceback.format_exc())
            raise FindFailed("Failed to type text '%s'" % text)
