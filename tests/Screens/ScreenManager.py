import logging

from Screens.BasePage import BasePage
from Screens.ChooseLimitScreen import ChooseLimitScreen
from Screens.DashboardScreen import DashboardScreen
from Screens.DiscountScreen import DiscountScreen
from Screens.InsertMoneyScreen import InsertMoneyScreen
from Screens.NumberScreen import NumberScreen
from Screens.PrivacyScreen import PrivacyScreen
from Screens.WalletScreen import WalletScreen


class ScreenManager:
    def __init__(self):
        self.basePage = BasePage()
        self.screens = {
            "wallet": WalletScreen(),
            "number": NumberScreen(),
            "privacy": PrivacyScreen(),
            "discount": DiscountScreen(),
            "dashboard": DashboardScreen(),
            "chooseLimit": ChooseLimitScreen(),
            "insertMoney": InsertMoneyScreen(),
        }
        logging.info("Screen Manager: All screens initialized.")

    @property
    def walletScreen(self):
        return self.screens["wallet"]

    @property
    def numberScreen(self):
        return self.screens["number"]

    @property
    def privacyScreen(self):
        return self.screens["privacy"]

    @property
    def discountScreen(self):
        return self.screens["discount"]

    @property
    def dashboardScreen(self):
        return self.screens["dashboard"]

    @property
    def chooseLimitScreen(self):
        return self.screens["chooseLimit"]

    @property
    def insertMoneyScreen(self):
        return self.screens["insertMoney"]
