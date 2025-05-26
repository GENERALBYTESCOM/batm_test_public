import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import ETH_DESTINATION_ADDRESS, DISCOUNT_TEXT, AMOUNT
from Helpers.FlowHelper import FlowHelper
from Helpers.ScreenshotManager import safeSetUp, safeTearDown


class TestETH(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        self.screens = self.baseTest.screens
        self.flow = FlowHelper(self.screens)
        safeSetUp(self, coin="eth")

    def tearDown(self):
        safeTearDown(self)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyETH(self):
        logging.info("=== Started test: Test Anonym Buy ETH ===")
        self.flow.performBuyFlow(tier="anonymous")
        self.screens.basePage.typeText(ETH_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_ETH_button.png", "BUY ETH BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyETH()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Test Anonym Buy ETH ===")

    def testUnregisteredBuyETH(self):
        logging.info("=== Started test: Test Unregistered Buy ETH ===")
        self.flow.performBuyFlow(tier="unregistered")
        self.screens.basePage.typeText(ETH_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_ETH_button.png", "BUY ETH BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyETH()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Test Unregistered Buy ETH ===")

    def testRegisteredBuyETH(self):
        logging.info("=== Started test: Test Registered Buy ETH ===")
        self.flow.performBuyFlow(tier="registered")
        self.screens.basePage.typeText(ETH_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_ETH_button.png", "BUY ETH BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyETH()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Registered Buy ETH ===")


if __name__ == "__main__":
    unittest.main(exit=False)
