import logging
import unittest

from BaseTest import BaseTest
from FlowHelper import FlowHelper
from Screens.ScreenManager import ScreenManager
from Utils.Config import BTC_DESTINATION_ADDRESS, DISCOUNT_TEXT


class TestBTCDiscount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        logging.info(
            "setUp: Initializing screens for {}.{}".format(
                self.__class__.__name__, self._testMethodName
            )
        )
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)

        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        self.screens.dashboardScreen.clickCoinButton("btc")

    def tearDown(self):
        logging.info("Test '%s' cleaned up.", self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyDiscount(self):
        logging.info("=== Started test: Anonym Buy Discount ===")
        self.flow.performAnonymBuyFlow()
        type(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Anonym Buy Discount ===")

    def testAnonymSellDiscount(self):
        logging.info("=== Started test: Anonym Sell Discount ===")
        self.flow.performAnonymSellFlow()
        type(DISCOUNT_TEXT)
        self.flow.completeSellDiscountFlow()
        logging.info("=== Completed test: Anonym Sell Discount ===")

    def testUnregisteredBuyDiscount(self):
        logging.info("=== Started test: Unregistered Buy Discount ===")
        self.flow.performUnregisteredBuyFlow()
        type(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Unregistered Buy Discount ===")

    def testUnregisteredSellDiscount(self):
        logging.info("=== Started test: Unregistered Sell Discount ===")
        self.flow.performUnregisteredSellFlow()
        type(DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.walletScreen.add100CzkButton()
        self.screens.dashboardScreen.completeSellTransaction()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Unregistered Sell Discount ===")


if __name__ == "__main__":
    unittest.main(exit=False)
