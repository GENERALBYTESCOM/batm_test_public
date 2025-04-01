import logging
import os
import sys

from Screens.ScreenManager import ScreenManager
from Utils.FlowHelper import FlowHelper
from sikuli import ImagePath, getBundlePath


class BaseTest:
    def __init__(self):
        self.screens = None
        self.flow = None

    def setupEnv(self):
        bundleDir = os.path.dirname(getBundlePath())
        projectRoot = os.path.abspath(bundleDir)
        if projectRoot not in sys.path:
            sys.path.append(projectRoot)

        pagesDir = os.path.join(projectRoot, "tests", "Screens")
        screenshotsDir = os.path.join(projectRoot, "tests", "Screenshots")
        if pagesDir not in sys.path:
            sys.path.append(pagesDir)

        if screenshotsDir not in list(ImagePath.getPaths()):
            ImagePath.add(screenshotsDir)

        logging.basicConfig(
            format="[%(levelname)s] %(asctime)s - %(message)s",
            datefmt="%H:%M:%S",
            level=logging.INFO,
        )
        logging.info("SikuliX environment configured successfully.")

    def setupTestObjects(self):
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)
        self.screens.dashboardScreen.checkMainScreenAndClickLogo()

    def teardownEnv(self):
        logging.info("SikuliX environment cleanup completed.")
