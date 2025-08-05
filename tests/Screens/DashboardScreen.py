from Config.Constants import WAIT_TIMEOUT
from Screens.BasePage import BasePage
from sikuli import exists, wait


class DashboardScreen(BasePage):
    coinButtons = {
        "btc": {"image": "BTC_button.png", "desc": "BTC LOGO"},
        "lbtc": {"image": "LBTC_button.png", "desc": "LBTC LOGO"},
        "ltc": {"image": "LTC_button.png", "desc": "LTC LOGO"},
        "eth": {"image": "ETH_button.png", "desc": "ETH LOGO"},
    }

    def clickCoinButton(self, coin):
        coin = coin.lower()
        if coin not in self.coinButtons:
            raise ValueError("Unsupported coin: {}".format(coin))
        btn = self.coinButtons[coin]
        self.assertExists(btn["image"], btn["desc"])
        self.clickElement(btn["image"], btn["desc"])

    def checkMainScreenAndClickLogo(self):
        if exists("main_screen.png", 5):
            self.clickElement("main_screen.png", "SCREENSAVER")

    def chooseLanguageButton(self):
        self.assertExists("choose_language_button.png", "CHOOSE LANGUAGE SCREEN")
        self.clickElement("choose_language_button.png", "CHOOSE LANGUAGE BUTTON")

    def clickBuyButton(self):
        self.clickElement("BUY_button.png", "BUY BUTTON")

    def clickSellButton(self):
        self.assertExists("SELL_button.png", "SELL BUTTON")
        self.clickElement("SELL_button.png", "SELL BUTTON")

    def completeSellTransaction(self):
        self.assertExists("SELL_complete_button.png", "SELL COMPLETE BUTTON")
        self.clickElement("SELL_complete_button.png", "SELL COMPLETE BUTTON")

    def completeTransaction(self):
        wait("transaction_completed_text.png", 60)
        self.assertExists(
            "transaction_completed_text.png", "TRANSACTION COMPLETED TEXT EXIST"
        )
        wait("DONE_completed_button.png", WAIT_TIMEOUT)
        self.clickElement("DONE_completed_button.png", "BUY DONE BUTTON")

    def dismissSmsNotificationModal(self):
        self.assertExists(
            "sms_transaction_notification_in_modal.png", "SMS TRANSACTION NOTIFICATION"
        )
        self.clickElement("NO_button_in_modal.png", "NO BUTTON IN MODAL")

    def waitAndCompleteNotDoneYetTransaction(self):
        wait("wait_we_are_not_done_yet_text.png", WAIT_TIMEOUT)
        self.assertExists("wait_we_are_not_done_yet_text.png", "NOT DONE YET TEXT")
        wait("DONE_completed_button.png", 40)
        self.clickElement("DONE_completed_button.png", "BUY DONE BUTTON")

    def abortTransaction(self):
        self.assertExists(
            "abort_this_transaction_text_in_modal.png",
            "ABORT TRANSACTION TEXT EXIST IN MODAL",
        )
        self.clickElement("abort_transaction_button.png", "ABORT TRANSACTION BUTTON")
        wait("transaction_canceled_text.png", WAIT_TIMEOUT)
        self.assertExists(
            "transaction_canceled_text.png", "TRANSACTION CANCELED TEXT EXIST"
        )
        self.clickElement(
            "DONE_completed_button.png", "DONE BUTTON AFTER CANCELED TRANSACTION"
        )
