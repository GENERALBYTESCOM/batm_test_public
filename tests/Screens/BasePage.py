import logging
import os
import sys

from Config.ConfigReader import ConfigReader
from Config.Constants import WAIT_TIMEOUT
from sikuli import click, exists, type, FindFailed, Pattern, ImagePath

currentDir = os.path.dirname(os.path.abspath(__file__))
projectRoot = os.path.abspath(os.path.join(currentDir, "..", ".."))
if projectRoot not in sys.path:
    sys.path.insert(0, projectRoot)

config = ConfigReader.loadProperties()
device = config["DEVICE"]
deviceImageDir = os.path.abspath(
    os.path.join(projectRoot, "tests", "Screenshots", device)
)
if deviceImageDir not in ImagePath.getPaths():
    ImagePath.add(deviceImageDir)


class BasePage:
    def __init__(self):
        self.osType = ConfigReader.getOsType()

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

    def osFile(self, baseFileName):
        if self.osType == "windows":
            if baseFileName.endswith(".png"):
                return baseFileName.replace(".png", "_win.png")
            return baseFileName + "_win"
        return baseFileName
