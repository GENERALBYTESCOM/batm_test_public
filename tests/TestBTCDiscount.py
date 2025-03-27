import logging
import unittest

from BaseTest import BaseTest
from FlowHelper import FlowHelper
from Screens.BasePage import WAIT_TIMEOUT
from Screens.ScreenManager import ScreenManager
from Utils.Config import BTC_DESTINATION_ADDRESS, DISCOUNT_TEXT
from sikuli import wait, type


class TestBTCDiscount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        logging.info("=== setUp: Initializing screens for TestBTCDiscount ===")
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)

        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        self.screens.dashboardScreen.clickBtcButton()

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyDiscount(self):
        logging.info("Started test: Anonym Buy Discount.")
        self.flow.performAnonymBuyFlow()
        type(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")

        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()

        self.screens.insertMoneyScreen.buyBTC()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("Completed test: Anonym Buy Discount.")

    def testAnonymSellDiscount(self):
        logging.info("Started test: Anonym Sell Discount.")
        self.flow.performAnonymSellFlow()
        type(DISCOUNT_TEXT)
        self.flow.completeSellDiscountFlow()
        logging.info("Completed test: Anonym Sell Discount.")

    def testUnregisteredBuyDiscount(self):
        logging.info("Started test: Unregistered Buy Discount.")

        self.screens.dashboardScreen.clickBuyButton()
        self.screens.walletScreen.confirmWalletOwnership()
        self.screens.privacyScreen.acceptPrivacyAndDisclaimer()
        self.screens.chooseLimitScreen.chooseUnregisteredTier()
        self.screens.privacyScreen.acceptPrivacyNotice()

        wait("phone_number_text.png", WAIT_TIMEOUT)
        self.screens.basePage.assertExists(
            "phone_number_text.png", "PHONE NUMBER TEXT EXIST"
        )
        self.screens.numberScreen.enterNumber()

        self.screens.basePage.assertExists(
            "one_time_password_text.png", "ONE TIME PASSWORD TEXT EXIST"
        )
        self.screens.numberScreen.enterNumber()

        self.screens.basePage.assertExists(
            "required_disclosures_text.png", "REQUIRED DISCLOSURES TEXT EXIST"
        )
        wait("CONTINUE_button.png", WAIT_TIMEOUT)
        self.screens.basePage.clickElement("CONTINUE_button.png", "CONTINUE BUTTON")

        self.screens.walletScreen.clickCryptoWallet()
        type(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")

        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.basePage.assertExists(
            "marketing_agreement_text.png", "MARKETING AGREEMENT TEXT EXIST"
        )
        self.screens.basePage.clickElement("NO_THANKS_button.png", "NO THANKS BUTTON")

        self.screens.dashboardScreen.completeTransaction()
        logging.info("Completed test: Unregistered Buy Discount.")


if __name__ == "__main__":
    unittest.main(exit=False)
