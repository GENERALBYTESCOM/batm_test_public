import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import ETH_DESTINATION_ADDRESS, BTC_DESTINATION_ADDRESS
from Helpers.FlowHelper import FlowHelper
from Helpers.ScreenshotManager import safeSetUp, safeTearDown


class TestNegativeScenarios(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        self.initScreensAndFlow("btc")

    def initScreensAndFlow(self, coin):
        self.screens = self.baseTest.screens
        self.flow = FlowHelper(self.screens)
        safeSetUp(self, coin)

    def tearDown(self):
        safeTearDown(self)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testBannedAddress(self):
        logging.info("=== Started test: Anonymous Buy BTC Banned Address ===")
        self.flow.performBuyFlow(tier="anonymous")
        self.screens.basePage.typeText(ETH_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.toastScreen.errorBTCWallet()
        self.screens.walletScreen.clickCancelButton()
        logging.info("=== Completed test: Anonymous Buy BTC Banned Address ===")

    def testOverTheLimit(self):
        logging.info("=== Started test: Anonymous Buy BTC Over the limit ===")
        self.flow.performBuyFlow(tier="anonymous")
        self.screens.basePage.typeText(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        total = 0
        for _ in range(5):
            self.screens.walletScreen.insertBanknoteAndVerify("100")
            total += 100
            self.screens.walletScreen.verifyInsertedAmount(str(total))
        self.screens.walletScreen.insertBanknoteAndVerify("100")
        self.screens.toastScreen.errorLimitTransaction()
        self.screens.walletScreen.clickCancelButton()
        self.screens.dashboardScreen.abortTransaction()
        logging.info("=== Completed test: Anonymous Buy BTC Over the limit ===")


if __name__ == "__main__":
    unittest.main(exit=False)
