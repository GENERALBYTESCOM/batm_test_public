import logging
import unittest

from Utils.Config import LTC_DESTINATION_ADDRESS, LTC_DISCOUNT_TEXT
from Utils.TestEnvironmentHelper import TestEnvironmentHelper
from sikuli import type


class TestLTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestEnvironmentHelper.setUpTestClass(cls)

    def setUp(self):
        TestEnvironmentHelper.setUpTestMethod(self)
        self.screens.dashboardScreen.clickCoinButton("ltc")

    def tearDown(self):
        logging.info("Test '%s' cleaned up.", self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        cls.env.teardownClassEnv()

    def testAnonymBuyLTC(self):
        logging.info("=== Started test: Anonym Buy LTC ===")
        self.flow.performAnonymBuyFlow()
        type(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")

        self.screens.discountScreen.prepareDiscountDialog()
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Anonym Buy LTC ===")

    def testAnonymSellLTC(self):
        logging.info("=== Started test: Anonym Sell LTC ===")
        self.flow.performAnonymSellFlow()
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeSellDiscountFlow()
        logging.info("=== Completed test: Anonym Sell LTC ===")

    def testUnregisteredBuyLTC(self):
        logging.info("=== Started test: Unregistered Buy LTC ===")
        self.flow.performUnregisteredBuyFlow()
        type(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Unregistered Buy LTC ===")


if __name__ == "__main__":
    unittest.main(exit=False)
