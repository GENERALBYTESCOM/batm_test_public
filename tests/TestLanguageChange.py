import logging
import unittest

from sikuli import wait

from BaseTest import BaseTest
from Config.Constants import WAIT_TIMEOUT
from Screens.LanguageScreen import LanguageScreen
from Screens.ScreenManager import ScreenManager


class TestLanguageChange(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        logging.info(
            "setUp: Initializing screens for TestLanguageChange: %s",
            self._testMethodName,
        )
        self.screens = ScreenManager()
        self.languageScreen = LanguageScreen()

    def tearDown(self):
        logging.info("Test '%s' cleaned up.", self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testLanguageChange(self):
        logging.info("Started test: Language Change.")
        self.screens.basePage.assertExists(
            "EN_welcome_logo_text.png", "EN WELCOME LOGO"
        )
        self.screens.dashboardScreen.chooseLanguageButton()
        self.languageScreen.clickArrowRight()
        wait("arrow_to_the_left_button.png", WAIT_TIMEOUT)
        self.languageScreen.clickArrowLeft()
        self.languageScreen.selectLanguage(
            "CZ_banner.png", "CZ BUTTON", "CZ_welcome_logo_text.png", 0.90
        )
        self.screens.dashboardScreen.chooseLanguageButton()
        self.languageScreen.selectLanguage(
            "ES_banner.png", "ES BUTTON", "ES_welcome_logo_text.png", 0.90
        )
        self.languageScreen.selectLanguage(
            "DE_banner.png", "DE BUTTON", "DE_welcome_logo_text.png", 0.90
        )
        self.screens.dashboardScreen.chooseLanguageButton()
        self.languageScreen.selectLanguage(
            "EN_banner.png", "EN BUTTON", "EN_welcome_logo_text.png", 0.90
        )
        self.screens.dashboardScreen.chooseLanguageButton()
        self.languageScreen.cancelAndVerify()


if __name__ == "__main__":
    unittest.main()
