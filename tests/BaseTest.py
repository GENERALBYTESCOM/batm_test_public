import logging
import os
import sys

from sikuli import ImagePath, getBundlePath

from Helpers.LoggingHelper import configureLogging, cleanLogsDir
from Helpers.ScreenshotManager import (
    ensureScreenshotsDir,
    captureScreenshot,
    getTestClassAndMethod,
)
from Screens.ScreenManager import ScreenManager


class BaseTest:
    def __init__(self):
        self.screens = None
        self.failedScreenshotsDir = None

    def setupEnv(self):
        bundleDir = os.path.dirname(getBundlePath())
        projectRoot = os.path.abspath(bundleDir)

        testsDir = os.path.join(projectRoot, "tests")
        if testsDir not in sys.path:
            sys.path.append(testsDir)

        screenshotsDir = os.path.join(projectRoot, "tests", "Screenshots")
        if screenshotsDir not in list(ImagePath.getPaths()):
            ImagePath.add(screenshotsDir)

        self.failedScreenshotsDir = os.path.join(testsDir, "FailedScreenshots")
        ensureScreenshotsDir(self.failedScreenshotsDir)

        logDir = os.path.join(testsDir, "Logs")
        cleanLogsDir(logDir)
        configureLogging(logDir)

        self.screens = ScreenManager()
        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        logging.info("SikuliX environment configured successfully.")

    def teardownEnv(self):
        logging.info("SikuliX environment cleanup completed.")

    def handleFailureScreenshot(self, testInstance):
        testId = getTestClassAndMethod(testInstance)
        screenshotPath = captureScreenshot(self.failedScreenshotsDir, testId)
        logging.info("Screenshot saved to: %s", screenshotPath)
