import logging
import unittest

from sikuli import wait

from BaseTest import BaseTest
from Screens.BasePage import WAIT_TIMEOUT
from Screens.ScreenManager import ScreenManager
from Utils.Config import LBTC_DISCOUNT_TEXT
from FlowHelper import FlowHelper


class TestLBTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        logging.info("=== setUp: Initializing screens for TestLBTC ===")
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)

        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        self.screens.dashboardScreen.clickCoinButton("lbtc")

    def tearDown(self):
        logging.info("Test '%s' cleaned up.", self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyLBTC(self):
        logging.info("=== Started test: Anonym Buy LBTC ===")
        self.screens.dashboardScreen.clickBuyButton()
        self.screens.walletScreen.confirmWalletOwnership()
        self.screens.privacyScreen.acceptPrivacyAndDisclaimer()

        self.screens.basePage.clickElement(
            "I_have_a_wallet.png", "YES, I HAVE A WALLET BUTTON"
        )
        self.screens.chooseLimitScreen.chooseAnonymousTierAndContinue()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        wait("BUY_LBTC_button.png", WAIT_TIMEOUT)

        self.screens.discountScreen.prepareDiscountDialog()
        type(LBTC_DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.basePage.clickElement("BUY_LBTC_button.png", "BUY LBTC BUTTON")
        self.screens.dashboardScreen.waitAndCompleteNotDoneYetTransaction()
        logging.info("=== Completed test: Anonym Buy LBTC ===")

    def testAnonymSellLBTC(self):
        logging.info("=== Started test: Anonym Sell LBTC ===")
        self.flow.performAnonymSellFlow()
        type(LBTC_DISCOUNT_TEXT)
        self.flow.completeSellDiscountFlow()
        logging.info("=== Completed test: Anonym Sell LBTC ===")


if __name__ == "__main__":
    unittest.main(exit=False)
