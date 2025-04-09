import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import ETH_DESTINATION_ADDRESS, ETH_DISCOUNT_TEXT
from Helpers.FlowHelper import FlowHelper
from Screens.ScreenManager import ScreenManager


class TestETH(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        logging.info(
            "setUp: Initializing screens for TestETH: %s",
            self._testMethodName,
        )
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)
        self.screens.dashboardScreen.clickCoinButton("eth")

    def tearDown(self):
        logging.info("Test '%s' cleaned up.", self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

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

    def testUnregisteredBuyETH(self):
        logging.info("=== Started test: Test Unregistered Buy ETH ===")
        self.flow.performUnregisteredBuyFlow()
        type(ETH_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_ETH_button.png", "BUY ETH BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(ETH_DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyETH()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()


if __name__ == "__main__":
    unittest.main(exit=False)
