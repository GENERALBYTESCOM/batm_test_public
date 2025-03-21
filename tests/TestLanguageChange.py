import logging
import unittest

from AbstractTestCase import AbstractTestCase
from Screens.BasePage import WAIT_TIMEOUT
from Screens.LanguageScreen import LanguageScreen
from sikuli import wait


class TestLanguageChange(AbstractTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestLanguageChange, cls).setUpClass()

    def setUp(self):
        super(TestLanguageChange, self).setUp()
        logging.info("=== setUp: Initializing screens for TestLanguageChange ===")
        self.languageScreen = LanguageScreen()

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")

    def testLanguageChange(self):
        logging.info("Started test: Language Change.")

        self.mainScreen.checkMainScreenAndClickLogo()
        self.basePage.assertExists("EN_welcome_logo_text.png", "EN WELCOME LOGO")
        self.mainScreen.chooseLanguageButton()
        self.languageScreen.clickArrowRight()
        wait("arrow_to_the_left_button.png", WAIT_TIMEOUT)
        self.languageScreen.clickArrowLeft()
        self.languageScreen.selectLanguage(
            "CZ_banner.png", "CZ BUTTON", "CZ_welcome_logo_text.png", 0.90
        )
        self.mainScreen.chooseLanguageButton()
        self.languageScreen.selectLanguage(
            "ES_banner.png", "ES BUTTON", "ES_welcome_logo_text.png", 0.90
        )
        self.languageScreen.selectLanguage(
            "DE_banner.png", "DE BUTTON", "DE_welcome_logo_text.png", 0.90
        )
        self.mainScreen.chooseLanguageButton()
        self.languageScreen.selectLanguage(
            "EN_banner.png", "EN BUTTON", "EN_welcome_logo_text.png", 0.90
        )
        self.mainScreen.chooseLanguageButton()
        self.languageScreen.cancelAndVerify()


if __name__ == "__main__":
    unittest.main()
