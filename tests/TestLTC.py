import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import LTC_DESTINATION_ADDRESS, LTC_DISCOUNT_TEXT
from Helpers.FlowHelper import FlowHelper
from Helpers.ScreenshotManager import safeSetUp, safeTearDown
from Screens.ScreenManager import ScreenManager


class TestLTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        self.screens = ScreenManager()
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
        type(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Anonym Buy LTC ===")

    def testAnonymSellLTC(self):
        logging.info("=== Started test: Anonym Sell LTC ===")
        self.flow.performSellFlow(tier="anonymous")
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            useDiscount=True, requireMarketingDecline=False, requireSmsDismiss=True
        )
        logging.info("=== Completed test: Anonym Sell LTC ===")

    def testUnregisteredBuyLTC(self):
        logging.info("=== Started test: Unregistered Buy LTC ===")
        self.flow.performBuyFlow(tier="unregistered")
        type(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Unregistered Buy LTC ===")

    def testUnregisteredSellLTC(self):
        logging.info("=== Started test: Unregistered Sell LTC ===")
        self.flow.performSellFlow(tier="unregistered")
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            useDiscount=True, requireMarketingDecline=True, requireSmsDismiss=False
        )
        logging.info("=== Completed test: Unregistered Sell LTC ===")

    def testRegisteredBuyLTC(self):
        logging.info("=== Started test: Registered Buy LTC ===")
        self.flow.performBuyFlow(tier="registered")
        type(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Registered Buy LTC ===")

    def testRegisteredSellLTC(self):
        logging.info("=== Started test: Registered Sell LTC ===")
        self.flow.performSellFlow(tier="registered")
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            useDiscount=True, requireMarketingDecline=True, requireSmsDismiss=False
        )
        logging.info("=== Completed test: Registered Sell LTC ===")


if __name__ == "__main__":
    unittest.main(exit=False)
