import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import ETH_DESTINATION_ADDRESS, BTC_DESTINATION_ADDRESS


class TestNegativeScenarios(BaseTest):
    def setUp(self):
        super().setUp()
        self.screens.dashboardScreen.clickCoinButton("btc")

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
