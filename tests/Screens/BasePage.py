import logging
import os
import sys

from Config.Constants import WAIT_TIMEOUT
from sikuli import click, exists, type, FindFailed, Pattern

currentDir = os.path.dirname(os.path.abspath(__file__))
projectRoot = os.path.abspath(os.path.join(currentDir, "..", ".."))
if projectRoot not in sys.path:
    sys.path.insert(0, projectRoot)


class BasePage:
    def __init__(self, device):
        self.device = device

    def clickElement(self, image, name, similarity=0.7):
        pattern = Pattern(image).similar(similarity)
        if exists(pattern, WAIT_TIMEOUT):
            click(pattern)
            logging.info(
                "Clicked on %s",
                name,
            )
        else:
            raise FindFailed("%s not found!" % name)

    def assertExists(self, image, name, similarity=0.7):
        pattern = Pattern(image).similar(similarity)
        if exists(pattern, WAIT_TIMEOUT):
            logging.info("%s exists", name)
        else:
            raise FindFailed("%s not found!" % name)

    def typeText(self, text):
        type(text)
        logging.info("Typed text: %s", text)
