import logging
import unittest

from BaseTest import BaseTest
from FlowHelper import FlowHelper
from Screens.ScreenManager import ScreenManager
from Utils.Config import LTC_DESTINATION_ADDRESS, LTC_DISCOUNT_TEXT


class TestLTC(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseTest = BaseTest()
        cls.baseTest.setupEnv()

    def setUp(self):
        logging.info("=== setUp: Initializing screens for TestLTC ===")
        self.screens = ScreenManager()
        self.flow = FlowHelper(self.screens)

        self.screens.dashboardScreen.checkMainScreenAndClickLogo()
        self.screens.dashboardScreen.clickLtcButton()

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")

    @classmethod
    def tearDownClass(cls):
        cls.baseTest.teardownEnv()

    def testAnonymBuyLTC(self):
        logging.info("Started test: Anonym Buy LTC.")
        self.flow.performAnonymBuyFlow()
        type(LTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")

        self.screens.discountScreen.prepareDiscountDialog()
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeBuyDiscountFlow()
        self.screens.insertMoneyScreen.buyLTC()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("Completed test: Anonym Buy LTC.")

    def testAnonymSellLTC(self):
        logging.info("Started test: Anonym Sell LTC.")
        self.flow.performAnonymSellFlow()
        type(LTC_DISCOUNT_TEXT)
        self.flow.completeSellDiscountFlow()
        logging.info("Completed test: Anonym Sell LTC.")


if __name__ == "__main__":
    unittest.main(exit=False)
