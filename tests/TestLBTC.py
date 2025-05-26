import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import (
    DISCOUNT_TEXT,
    AMOUNT,
)
from Helpers.FlowHelper import FlowHelper
from Helpers.ScreenshotManager import safeSetUp, safeTearDown


class TestLBTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        self.screens = self.baseTest.screens
        self.flow = FlowHelper(self.screens)
        safeSetUp(self, coin="lbtc")

    def tearDown(self):
        safeTearDown(self)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyLBTC(self):
        logging.info("=== Started test: Anonym Buy LBTC ===")
        self.flow.performBuyLBTCFlow()
        self.screens.chooseLimitScreen.chooseAnonymousTierAndContinue()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_LBTC_button.png", "BUY LBTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLBTC()
        self.screens.dashboardScreen.waitAndCompleteNotDoneYetTransaction()
        logging.info("=== Completed test: Anonym Buy LBTC ===")

    def testUnregisteredBuyLBTC(self):
        logging.info("=== Started test: Unregistered Buy LBTC ===")
        self.flow.performBuyLBTCFlow()
        self.screens.chooseLimitScreen.chooseUnregisteredTier()
        self.flow.verifyPhoneNumberAndOTP()
        self.screens.requiredDisclosuresScreen.acceptRequiredDisclosures()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_LBTC_button.png", "BUY LBTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLBTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.waitAndCompleteNotDoneYetTransaction()
        logging.info("=== Completed test: Unregistered Buy LBTC ===")

    def testRegisteredBuyLBTC(self):
        logging.info("=== Started test: Registered Buy LBTC ===")
        self.flow.performBuyLBTCFlow()
        self.screens.chooseLimitScreen.chooseRegisteredTier()
        self.flow.verifyPhoneNumberAndOTP()
        self.screens.requiredDisclosuresScreen.acceptRequiredDisclosures()
        self.screens.walletScreen.insertBanknoteAndVerify(AMOUNT)
        self.screens.basePage.assertExists("BUY_LBTC_button.png", "BUY LBTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        self.screens.basePage.typeText(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyLBTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.waitAndCompleteNotDoneYetTransaction()
        logging.info("=== Completed test: Registered Buy LBTC ===")


if __name__ == "__main__":
    unittest.main(exit=False)
