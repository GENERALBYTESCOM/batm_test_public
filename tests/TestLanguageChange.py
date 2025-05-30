import logging
import unittest

from BaseTest import BaseTest
from Helpers.ScreenshotManager import safeTearDown
from Screens.DashboardScreen import DashboardScreen
from Screens.LanguageScreen import LanguageScreen


class TestLanguageChange(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        self.screens = self.baseTest.screens
        self.languageScreen = LanguageScreen()
        self.dashboardScreen = DashboardScreen()

    def tearDown(self):
        safeTearDown(self)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testLanguageChange(self):
        logging.info("Started test: Language Change.")
        self.languageScreen.verifyWelcomeLogo("EN")
        self.dashboardScreen.chooseLanguageButton()
        self.languageScreen.switchArrow("right")
        self.languageScreen.switchArrow("left")
        self.languageScreen.selectLanguage("CZ")
        self.languageScreen.selectLanguage("DE")
        self.dashboardScreen.chooseLanguageButton()
        self.languageScreen.selectLanguage("EN")
        self.dashboardScreen.chooseLanguageButton()
        self.languageScreen.cancelAndVerify()


if __name__ == "__main__":
    unittest.main(exit=False)
