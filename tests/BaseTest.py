import logging
import os
import sys

from sikuli import ImagePath, getBundlePath

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

        self.failedScreenshotsDir = os.path.join(
            projectRoot, "tests", "FailedScreenshots"
        )
        ensureScreenshotsDir(self.failedScreenshotsDir)

        logging.basicConfig(
            format="[%(levelname)s] %(asctime)s - %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )
        self.screens = ScreenManager()
        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        logging.info("SikuliX environment configured successfully.")

    def teardownEnv(self):
        logging.info("SikuliX environment cleanup completed.")

    def handleFailureScreenshot(self, testInstance):
        if sys.exc_info()[0] is not None:
            testId = getTestClassAndMethod(testInstance)
            screenshotPath = captureScreenshot(self.failedScreenshotsDir, testId)
            print("Screenshot saved to: {}".format(screenshotPath))
            logging.info("Failure in test: %s", testId)
