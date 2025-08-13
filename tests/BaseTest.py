import logging
import os
import sys

from sikuli import ImagePath, exists, Pattern

from Helpers.LoggingHelper import configureLogging, cleanLogsDir
from Helpers.ScreenshotManager import (
    ensureScreenshotsDir,
    captureScreenshot,
    getTestClassAndMethod,
)
from Screens.ScreenManager import ScreenManager

currentDir = os.path.dirname(os.path.abspath(__file__))
projectRoot = os.path.abspath(os.path.join(currentDir, ".."))
if projectRoot not in sys.path:
    sys.path.insert(0, projectRoot)


class BaseTest:
    def __init__(self):
        self.screens = None
        self.failedScreenshotsDir = None
        self.device = None

    def detectDevice(self):
        screenshotsDir = os.path.join(projectRoot, "tests", "Screenshots")
        batm7Indicator = os.path.join(screenshotsDir, "BATM7", "BATM7.png")
        batm10Indicator = os.path.join(screenshotsDir, "BATM10", "BATM10.png")
        logging.info("Detecting device type...")

        if exists(Pattern(batm7Indicator).similar(0.8), 5):
            logging.info("Device detected: BATM7")
            return "BATM7"

        if exists(Pattern(batm10Indicator).similar(0.8), 5):
            logging.info("Device detected: BATM10")
            return "BATM10"

        raise RuntimeError("Unable to detect device type!")

    def setupEnv(self):
        testsDir = os.path.join(projectRoot, "tests")
        if testsDir not in sys.path:
            sys.path.append(testsDir)

        self.device = self.detectDevice()
        self.screens = ScreenManager(self.device)

        deviceImagePath = os.path.join(testsDir, "Screenshots", self.device)
        if deviceImagePath not in ImagePath.getPaths():
            ImagePath.add(deviceImagePath)
        screenshotsDir = os.path.join(projectRoot, "tests", "Screenshots")
        if screenshotsDir not in list(ImagePath.getPaths()):
            ImagePath.add(screenshotsDir)

        self.failedScreenshotsDir = os.path.join(testsDir, "FailedScreenshots")
        ensureScreenshotsDir(self.failedScreenshotsDir)

        logDir = os.path.join(testsDir, "Logs")
        cleanLogsDir(logDir)
        configureLogging(logDir)

        self.screens = ScreenManager(self.device)
        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        logging.info("SikuliX environment configured successfully.")

    def teardownEnv(self):
        logging.info("SikuliX environment cleanup completed.")

    def handleFailureScreenshot(self, testInstance):
        testId = getTestClassAndMethod(testInstance)
        screenshotPath = captureScreenshot(self.failedScreenshotsDir, testId)
        logging.info("Screenshot saved to: %s", screenshotPath)
