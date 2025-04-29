import logging

from Config.Constants import WAIT_TIMEOUT
from sikuli import click, exists, type, FindFailed, Pattern


class BasePage:
    def __init__(self):
        pass

    def clickElement(self, image, name, similarity=0.8):
        pattern = Pattern(image).similar(similarity)
        if exists(pattern, WAIT_TIMEOUT):
            click(pattern)
            logging.info(
                "Clicked on %s",
                name,
            )
        else:
            raise FindFailed("%s not found!" % name)

    def assertExists(self, image, name, similarity=0.8):
        pattern = Pattern(image).similar(similarity)
        if exists(pattern, WAIT_TIMEOUT):
            logging.info("%s exists", name)
        else:
            raise FindFailed("%s not found!" % name)

    def typeText(self, text):
        type(text)
        logging.info("Typed text: %s", text)
