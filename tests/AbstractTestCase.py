import logging
import unittest

from BaseTest import BaseTest
from Screens.BasePage import BasePage
from Screens.DiscountScreen import DiscountScreen
from Screens.MainScreen import MainScreen
from Screens.PrivacyScreen import PrivacyScreen
from Screens.TierSelectScreen import TierSelectScreen
from Screens.WalletScreen import WalletScreen


class AbstractTestCase(BaseTest, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(AbstractTestCase, cls).setupEnv()

    def setUp(self):
        super(AbstractTestCase, self).setUp()
        logging.info("=== setUp: Initializing common screens ===")
        self._initScreens()

    def tearDown(self):
        logging.info("=== tearDown: Cleaning up after test ===")
        super(AbstractTestCase, self).tearDown()

    def _initScreens(self):
        self.basePage = BasePage()
        self.mainScreen = MainScreen()
        self.walletScreen = WalletScreen()
        self.privacyScreen = PrivacyScreen()
        self.discountScreen = DiscountScreen()
        self.tierSelectScreen = TierSelectScreen()

    def performAnonymBuyFlow(self):
        self.mainScreen.clickBuyButton()
        self.walletScreen.confirmWalletOwnership()
        self.privacyScreen.acceptPrivacyAndDisclaimer()
        self.tierSelectScreen.chooseAnonymousTierAndContinue()
        self.walletScreen.clickCryptoWallet()

    def performAnonymSellFlow(self):
        self.mainScreen.clickSellButton()
        self.privacyScreen.acceptPrivacy()
        self.tierSelectScreen.chooseAnonymousTierAndContinue()
        self.discountScreen.openDiscountDialog()
        self.discountScreen.waitAndClickDiscountInputField()

    def completeBuyDiscountFlow(self):
        self.discountScreen.submitAndCloseDiscountDialog()
        self.discountScreen.verifyDiscountToast()

    def completeSellDiscountFlow(self):
        self.discountScreen.submitAndCloseDiscountDialog()
        self.discountScreen.verifyDiscountToast()
        self.walletScreen.add100CzkButton()
        self.mainScreen.completeSellTransaction()
        self.mainScreen.dismissSmsNotificationModal()
        self.mainScreen.completeTransaction()
