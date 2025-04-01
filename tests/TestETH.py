import logging
import unittest

from Utils.Config import ETH_DESTINATION_ADDRESS, ETH_DISCOUNT_TEXT
from Utils.TestEnvironmentHelper import TestEnvironmentHelper
from sikuli import type


class TestETH(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestEnvironmentHelper.setUpTestClass(cls)

    def setUp(self):
        TestEnvironmentHelper.setUpTestMethod(self)
        self.screens.dashboardScreen.clickCoinButton("eth")

    def tearDown(self):
        logging.info("Test '%s' cleaned up.", self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        cls.env.teardownClassEnv()

    def testAnonymBuyETH(self):
        logging.info("=== Started test: Test Anonym Buy ETH ===")
        self.flow.performAnonymBuyFlow()
        type(ETH_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_ETH_button.png", "BUY ETH BUTTON")

        self.screens.discountScreen.prepareDiscountDialog()
        type(ETH_DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyETH()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Test Anonym Buy ETH ===")


if __name__ == "__main__":
    unittest.main(exit=False)
