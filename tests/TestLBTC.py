import logging
import unittest

from sikuli import wait

from BaseTest import BaseTest
from Config.Constants import LBTC_DISCOUNT_TEXT, WAIT_TIMEOUT
from Helpers.FlowHelper import FlowHelper
from Screens.ScreenManager import ScreenManager


class TestLBTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        logging.info(
            "setUp: Initializing screens for TestLBTC: %s", self._testMethodName
        )
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)
        self.screens.dashboardScreen.clickCoinButton("lbtc")

    def tearDown(self):
        logging.info("Test '%s' cleaned up.", self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyLBTC(self):
        logging.info("=== Started test: Anonym Buy LBTC ===")
        self.flow.performBuyFlow()
        self.screens.chooseLimitScreen.chooseAnonymousTierAndContinue()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        wait("BUY_LBTC_button.png", WAIT_TIMEOUT)
        self.screens.discountScreen.prepareDiscountDialog()
        type(LBTC_DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyLBTC()
        self.screens.dashboardScreen.waitAndCompleteNotDoneYetTransaction()
        logging.info("=== Completed test: Anonym Buy LBTC ===")

    def testAnonymSellLBTC(self):
        logging.info("=== Started test: Anonym Sell LBTC ===")
        self.flow.performAnonymSellFlow()
        type(LBTC_DISCOUNT_TEXT)
        self.flow.completeSellDiscountFlow()
        logging.info("=== Completed test: Anonym Sell LBTC ===")

    def testUnregisteredSellLBTC(self):
        logging.info("=== Started test: Unregistered Sell LBTC ===")
        self.flow.performUnregisteredSellFlow()
        type(LBTC_DISCOUNT_TEXT)
        self.flow.completeUnregisteredSellFlow()
        logging.info("=== Completed test: Unregistered Sell LBTC ===")

    def testUnregisteredBuyLBTC(self):
        logging.info("=== Started test: Unregistered Buy LBTC ===")
        self.flow.performBuyFlow()
        self.screens.chooseLimitScreen.chooseUnregisteredTier()
        self.flow.verifyPhoneNumberAndOTP()
        self.screens.requiredDisclosuresScreen.acceptRequiredDisclosures()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        wait("BUY_LBTC_button.png", WAIT_TIMEOUT)
        self.screens.discountScreen.prepareDiscountDialog()
        type(LBTC_DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyLBTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.waitAndCompleteNotDoneYetTransaction()
        logging.info("=== Completed test: Unregistered Buy LBTC ===")


if __name__ == "__main__":
    unittest.main(exit=False)
