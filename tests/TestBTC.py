import logging
import unittest

from BaseTest import BaseTest
from Config.Constants import BTC_DESTINATION_ADDRESS, DISCOUNT_TEXT


class TestBTC(BaseTest):
    def setUp(self):
        super().setUp()
        self.screens.dashboardScreen.clickCoinButton("btc")

    def testAnonymBuyBTC(self):
        logging.info("=== Started test: Anonym Buy BTC ===")
        self.flow.performBuyFlow(tier="anonymous")
        type(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Anonym Buy BTC ===")

    def testAnonymSellBTC(self):
        logging.info("=== Started test: Anonym Sell BTC ===")
        self.flow.performSellFlow(tier="anonymous")
        type(DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            useDiscount=True, requireMarketingDecline=False, requireSmsDismiss=True
        )
        logging.info("=== Completed test: Anonym Sell BTC ===")

    def testUnregisteredBuyBTC(self):
        logging.info("=== Started test: Unregistered Buy BTC ===")
        self.flow.performBuyFlow(tier="unregistered")
        type(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Unregistered Buy BTC ===")

    def testUnregisteredSellBTC(self):
        logging.info("=== Started test: Unregistered Sell BTC ===")
        self.flow.performSellFlow(tier="unregistered")
        type(DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            useDiscount=True, requireMarketingDecline=True, requireSmsDismiss=False
        )
        logging.info("=== Completed test: Unregistered Sell BTC ===")

    def testRegisteredBuyBTC(self):
        logging.info("=== Started test: Registered Buy BTC ===")
        self.flow.performBuyFlow(tier="registered")
        type(BTC_DESTINATION_ADDRESS)
        self.screens.walletScreen.clickScanQrButton()
        self.screens.walletScreen.insertBanknoteAndVerify("100 CZK")
        self.screens.basePage.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.screens.discountScreen.prepareDiscountDialog()
        type(DISCOUNT_TEXT)
        self.flow.completeDiscountFlow()
        self.screens.insertMoneyScreen.buyBTC()
        self.screens.marketingAgreementScreen.declineMarketingAgreement()
        self.screens.dashboardScreen.completeTransaction()
        logging.info("=== Completed test: Registered Buy BTC ===")

    def testRegisteredSellBTC(self):
        logging.info("=== Started test: Registered Sell BTC ===")
        self.flow.performSellFlow(tier="registered")
        type(DISCOUNT_TEXT)
        self.flow.completeSellFlow(
            useDiscount=True, requireMarketingDecline=True, requireSmsDismiss=False
        )
        logging.info("=== Completed test: Registered Sell BTC ===")


if __name__ == "__main__":
    unittest.main(exit=False)
