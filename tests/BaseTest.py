import logging
import os
import sys
import unittest

from sikuli import ImagePath, getBundlePath

from Helpers.FlowHelper import FlowHelper
from Screens.ScreenManager import ScreenManager


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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
        logging.info("SikuliX environment configured successfully.")

    @classmethod
    def tearDownClass(cls):
        logging.info("SikuliX environment cleanup completed.")

    def setUp(self):
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)
        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        logging.info("Test '%s' setUp done.", self._testMethodName)

    def tearDown(self):
        logging.info("Test '%s' cleaned up successfully.", self._testMethodName)

    @staticmethod
    def getSuper(targetClass, instance):
        return super(targetClass, instance)
