import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import (
    LTC_DESTINATION_ADDRESS,
    DISCOUNT_TEXT,
    AMOUNT,
)
from Helpers.FlowHelper import FlowHelper
from Helpers.ScreenshotManager import safeSetUp, safeTearDown


class TestLTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        self.screens = self.baseTest.screens
        self.flow = FlowHelper(self.screens)
        safeSetUp(self, coin="ltc")

    def tearDown(self):
        safeTearDown(self)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyLTC(self):
        logging.info("=== Started test: Anonym Buy LTC ===")
        self.flow.performBuyFlow(tier="anonymous")
        self.screens.basePage.typeText(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Anonym Buy LTC ===")

    def testUnregisteredBuyLTC(self):
        logging.info("=== Started test: Unregistered Buy LTC ===")
        self.flow.performBuyFlow(tier="unregistered")
        self.screens.basePage.typeText(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Unregistered Buy LTC ===")

    def testRegisteredBuyLTC(self):
        logging.info("=== Started test: Registered Buy LTC ===")
        self.flow.performBuyFlow(tier="registered")
        self.screens.basePage.typeText(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Registered Buy LTC ===")


if __name__ == "__main__":
    unittest.main(exit=False)
