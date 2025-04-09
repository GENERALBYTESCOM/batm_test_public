import logging
import os
import sys

from sikuli import ImagePath, getBundlePath

from Screens.ScreenManager import ScreenManager


class BaseTest:
    def __init__(self):
        self.screens = None

    def setupEnv(self):
        bundleDir = os.path.dirname(getBundlePath())
        projectRoot = os.path.abspath(bundleDir)

        testsDir = os.path.join(projectRoot, "tests")
        if testsDir not in sys.path:
            sys.path.append(testsDir)

        screenshotsDir = os.path.join(projectRoot, "tests", "Screenshots")
        if screenshotsDir not in list(ImagePath.getPaths()):
            ImagePath.add(screenshotsDir)

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
