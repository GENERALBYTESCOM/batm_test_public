import logging
import unittest

from AbstractTestCase import AbstractTestCase
from Screens.BasePage import WAIT_TIMEOUT
from Screens.NumberScreen import NumberScreen
from Utils.Config import BTC_DESTINATION_ADDRESS, DISCOUNT_TEXT
from sikuli import wait, type


class TestBTCDiscount(AbstractTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestBTCDiscount, cls).setUpClass()

    def setUp(self):
        super(TestBTCDiscount, self).setUp()
        logging.info("=== setUp: Initializing screens for TestBTCDiscount ===")
        self.numberScreen = NumberScreen()

        self.mainScreen.checkMainScreenAndClickLogo()
        self.mainScreen.clickBtcButton()

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")

    def testAnonymBuyDiscount(self):
        logging.info("Started test: Anonym Buy Discount.")
        self.performAnonymBuyFlow()
        type(BTC_DESTINATION_ADDRESS)
        self.walletScreen.clickScanQrButton()
        self.walletScreen.insertBanknoteAndVerify("100 CZK")

        self.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.completeBuyDiscountFlow()

        self.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.basePage.clickElement("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.mainScreen.completeTransaction()
        logging.info("Completed test: Anonym Buy Discount.")

    def testAnonymSellDiscount(self):
        logging.info("Started test: Anonym Sell Discount.")
        self.performAnonymSellFlow()
        type(DISCOUNT_TEXT)
        self.completeSellDiscountFlow()
        logging.info("Completed test: Anonym Sell Discount.")

    def testUnregisteredBuyDiscount(self):
        logging.info("Started test: Unregistered Buy Discount.")

        self.mainScreen.clickBuyButton()
        self.walletScreen.confirmWalletOwnership()
        self.privacyScreen.acceptPrivacyAndDisclaimer()
        self.tierSelectScreen.chooseUnregisteredTier()
        self.privacyScreen.acceptPrivacyNotice()

        wait("phone_number_text.png", WAIT_TIMEOUT)
        self.basePage.assertExists("phone_number_text.png", "PHONE NUMBER TEXT EXIST")
        self.numberScreen.enterNumber()

        self.basePage.assertExists(
            "one_time_password_text.png", "ONE TIME PASSWORD TEXT EXIST"
        )
        self.numberScreen.enterNumber()

        self.basePage.assertExists(
            "required_disclosures_text.png", "REQUIRED DISCLOSURES TEXT EXIST"
        )
        wait("CONTINUE_button.png", WAIT_TIMEOUT)
        self.basePage.clickElement("CONTINUE_button.png", "CONTINUE BUTTON")

        self.walletScreen.clickCryptoWallet()
        type(BTC_DESTINATION_ADDRESS)
        self.walletScreen.clickScanQrButton()
        self.walletScreen.insertBanknoteAndVerify("100 CZK")

        self.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.discountScreen.submitAndCloseDiscountDialog()
        self.discountScreen.verifyDiscountToast()

        self.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.basePage.clickElement("BUY_BTC_button.png", "BUY BTC BUTTON")

        self.basePage.assertExists(
            "marketing_agreement_text.png", "MARKETING AGREEMENT TEXT EXIST"
        )
        self.basePage.clickElement("NO_THANKS_button.png", "NO THANKS BUTTON")

        self.mainScreen.completeTransaction()
        logging.info("Completed test: Unregistered Buy Discount.")


if __name__ == "__main__":
    unittest.main()
