import logging
import unittest

from AbstractTestCase import AbstractTestCase
from Utils.Config import ETH_DESTINATION_ADDRESS, ETH_DISCOUNT_TEXT
from sikuli import type


class TestETH(AbstractTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestETH, cls).setUpClass()

    def setUp(self):
        super(TestETH, self).setUp()
        logging.info("=== setUp: Initializing screens for TestLTC ===")

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")

    def testAnonymBuyETH(self):
        logging.info("Started test: Test Anonym Buy ETH.")

        self.mainScreen.checkMainScreenAndClickLogo()
        self.mainScreen.clickEthButton()
        self.performAnonymBuyFlow()
        type(ETH_DESTINATION_ADDRESS)
        self.walletScreen.clickScanQrButton()
        self.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.basePage.assertExists("BUY_ETH_button.png", "BUY ETH BUTTON")

        self.discountScreen.prepareDiscountDialog()
        type(ETH_DISCOUNT_TEXT)
        self.completeBuyDiscountFlow()
        self.basePage.assertExists("BUY_ETH_button.png", "BUY ETH BUTTON")
        self.basePage.clickElement("BUY_ETH_button.png", "BUY ETH BUTTON")
        self.mainScreen.completeTransaction()
        logging.info("Completed test: Test Anonym Buy ETH.")


if __name__ == "__main__":
    unittest.main()
