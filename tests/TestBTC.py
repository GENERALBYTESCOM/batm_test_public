import logging
import unittest

from BaseTest import BaseTest
from Config.ConfigReader import ConfigReader
from Config.Constants import (
    BTC_DESTINATION_ADDRESS,
    DISCOUNT_TEXT,
    AMOUNT,
)
from Helpers.FlowHelper import FlowHelper
from Helpers.ScreenshotManager import safeSetUp, safeTearDown

config = ConfigReader.loadProperties()
deviceType = config.get("DEVICE", "")


class TestBTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        self.screens = self.baseTest.screens
        self.flow = FlowHelper(self.screens)
        safeSetUp(self, coin="btc")

    def tearDown(self):
        safeTearDown(self)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyBTC(self):
        logging.info("=== Started test: Anonym Buy BTC ===")
        self.flow.performBuyFlow(tier="anonymous")
        self.screens.basePage.typeText(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Anonym Buy BTC ===")

    @unittest.skipIf(
        deviceType != "BATM10", "Sell tests are skipped unless DEVICE=BATM10"
    )
    def testAnonymSellBTC(self):
        logging.info("=== Started test: Anonym Sell BTC ===")
        self.flow.performSellFlow(tier="anonymous")
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            amount=AMOUNT,
            useDiscount=True,
            requireMarketingDecline=False,
            requireSmsDismiss=True,
        )
        logging.info("=== Completed test: Anonym Sell BTC ===")

    def testUnregisteredBuyBTC(self):
        logging.info("=== Started test: Unregistered Buy BTC ===")
        self.flow.performBuyFlow(tier="unregistered")
        self.screens.basePage.typeText(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Unregistered Buy BTC ===")

    @unittest.skipIf(
        deviceType != "BATM10", "Sell tests are skipped unless DEVICE=BATM10"
    )
    def testUnregisteredSellBTC(self):
        logging.info("=== Started test: Unregistered Sell BTC ===")
        self.flow.performSellFlow(tier="unregistered")
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            amount=AMOUNT,
            useDiscount=True,
            requireMarketingDecline=True,
            requireSmsDismiss=False,
        )
        logging.info("=== Completed test: Unregistered Sell BTC ===")

    def testRegisteredBuyBTC(self):
        logging.info("=== Started test: Registered Buy BTC ===")
        self.flow.performBuyFlow(tier="registered")
        self.screens.basePage.typeText(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Registered Buy BTC ===")

    @unittest.skipIf(
        deviceType != "BATM10", "Sell tests are skipped unless DEVICE=BATM10"
    )
    def testRegisteredSellBTC(self):
        logging.info("=== Started test: Registered Sell BTC ===")
        self.flow.performSellFlow(tier="registered")
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            amount=AMOUNT,
            useDiscount=True,
            requireMarketingDecline=True,
            requireSmsDismiss=False,
        )
        logging.info("=== Completed test: Registered Sell BTC ===")


if __name__ == "__main__":
    unittest.main(exit=False)
