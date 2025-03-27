import logging
import unittest

from BaseTest import BaseTest
from FlowHelper import FlowHelper
from Screens.ScreenManager import ScreenManager
from Utils.Config import ETH_DESTINATION_ADDRESS, ETH_DISCOUNT_TEXT
from sikuli import type


class TestETH(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        logging.info("=== setUp: Initializing screens for TestETH ===")
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)

        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        self.screens.dashboardScreen.clickEthButton()

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyETH(self):
        logging.info("Started test: Test Anonym Buy ETH.")
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
        logging.info("Completed test: Test Anonym Buy ETH.")


if __name__ == "__main__":
    unittest.main(exit=False)
