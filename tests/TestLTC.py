import logging
import unittest

from AbstractTestCase import AbstractTestCase
from Utils.Config import LTC_DESTINATION_ADDRESS, LTC_DISCOUNT_TEXT


class TestLTC(AbstractTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestLTC, cls).setUpClass()

    def setUp(self):
        super(TestLTC, self).setUp()
        logging.info("=== setUp: Initializing screens for TestLTC ===")

        self.mainScreen.checkMainScreenAndClickLogo()
        self.mainScreen.clickLtcButton()

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")

    def testAnonymBuyLTC(self):
        logging.info("Started test: Anonym Buy LTC.")

        self.performAnonymBuyFlow()
        type(LTC_DESTINATION_ADDRESS)
        self.walletScreen.clickScanQrButton()
        self.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")

        self.discountScreen.prepareDiscountDialog()
        type(LTC_DISCOUNT_TEXT)
        self.completeBuyDiscountFlow()
        self.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.basePage.clickElement("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.mainScreen.completeTransaction()
        logging.info("Completed test: Anonym Buy LTC.")

    def testAnonymSellLTC(self):
        logging.info("Started test: Anonym Sell LTC.")
        self.performAnonymSellFlow()
        type(LTC_DISCOUNT_TEXT)
        self.completeSellDiscountFlow()
        logging.info("Completed test: Anonym Sell LTC.")


if __name__ == "__main__":
    unittest.main()
