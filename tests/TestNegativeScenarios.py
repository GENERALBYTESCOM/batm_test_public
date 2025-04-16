import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import ETH_DESTINATION_ADDRESS, BTC_DESTINATION_ADDRESS
from Helpers.FlowHelper import FlowHelper
from Screens.ScreenManager import ScreenManager


class TestNegativeScenarios(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        self.initScreensAndFlow("btc")
        logging.info("Test '%s' setUp done.", self._testMethodName)

    def initScreensAndFlow(self, coin):
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)
        self.screens.dashboardScreen.clickCoinButton(coin)

    def tearDown(self):
        logging.info("Test '%s' cleaned up successfully.", self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testBannedAddress(self):
        logging.info("=== Started test: Anonym Buy BTC Banned Address ===")
        self.flow.performBuyFlow(tier="anonymous")
        type(ETH_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.toastScreen.errorBTCWallet()
        self.screens.walletScreen.clickCancelButton()
        logging.info("=== Completed test: Anonym Buy BTC Banned Address ===")

    def testOverTheLimit(self):
        logging.info("=== Started test: Anonym Buy BTC Over the limit ===")
        self.flow.performBuyFlow(tier="anonymous")
        type(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndExpectError("1000 CZK")
        self.screens.toastScreen.errorLimitTransaction()
        self.screens.walletScreen.clickCancelButton()
        logging.info("=== Completed test: Anonym Buy BTC Over the limit ===")


if __name__ == "__main__":
    unittest.main(exit=False)
