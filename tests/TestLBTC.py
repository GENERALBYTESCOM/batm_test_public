import logging
import unittest

from AbstractTestCase import AbstractTestCase
from Screens.BasePage import WAIT_TIMEOUT
from Utils.Config import LBTC_DISCOUNT_TEXT
from sikuli import wait, type


class TestLBTC(AbstractTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestLBTC, cls).setUpClass()

    def setUp(self):
        super(TestLBTC, self).setUp()
        logging.info("=== setUp: Initializing screens for TestLBTC ===")

        self.mainScreen.checkMainScreenAndClickLogo()
        self.mainScreen.clickLbtcButton()

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")

    def testAnonymBuyLBTC(self):
        logging.info("Started test: Anonym Buy LBTC.")

        self.mainScreen.clickBuyButton()
        self.walletScreen.confirmWalletOwnership()
        self.privacyScreen.acceptPrivacyAndDisclaimer()

        self.basePage.clickElement("I_have_a_wallet.png", "YES, I HAVE A WALLET BUTTON")
        self.tierSelectScreen.chooseAnonymousTierAndContinue()
        self.walletScreen.insertBanknoteAndVerify("100 CZK")
        wait("BUY_LBTC_button.png", WAIT_TIMEOUT)

        self.discountScreen.prepareDiscountDialog()
        type(LBTC_DISCOUNT_TEXT)
        self.discountScreen.submitAndCloseDiscountDialog()
        self.discountScreen.verifyDiscountToast()
        self.basePage.clickElement("BUY_LBTC_button.png", "BUY LBTC BUTTON")
        wait("DONE_completed_button.png", WAIT_TIMEOUT)
        self.basePage.clickElement("DONE_completed_button.png", "BUY DONE BUTTON")
        logging.info("Completed test: Anonym Buy LBTC.")

    def testAnonymSellLBTC(self):
        logging.info("Started test: Anonym Sell LBTC.")
        self.performAnonymSellFlow()
        type(LBTC_DISCOUNT_TEXT)
        self.completeSellDiscountFlow()
        logging.info("Completed test: Anonym Sell LBTC.")


if __name__ == "__main__":
    unittest.main()
