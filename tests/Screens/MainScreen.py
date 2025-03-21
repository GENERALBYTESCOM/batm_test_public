from Screens.BasePage import BasePage, WAIT_TIMEOUT

from sikuli import has, wait


class MainScreen(BasePage):
    def checkMainScreenAndClickLogo(self):
        if has("main_screen.png", WAIT_TIMEOUT):
            self.clickElement("BTC_logo.png", "SCREENSAVER")

    def clickBtcButton(self):
        self.assertExists("BTC_button.png", "BTC LOGO")
        self.clickElement("BTC_button.png", "BTC LOGO")

    def clickLbtcButton(self):
        self.assertExists("LBTC_button.png", "LBTC LOGO")
        self.clickElement("LBTC_button.png", "LBTC LOGO")

    def clickLtcButton(self):
        self.assertExists("LTC_button.png", "LTC LOGO")
        self.clickElement("LTC_button.png", "LTC LOGO")

    def clickEthButton(self):
        self.assertExists("ETH_button.png", "ETH LOGO")
        self.clickElement("ETH_button.png", "ETH LOGO")

    def chooseLanguageButton(self):
        self.assertExists("choose_language_button.png", "CHOOSE LANGUAGE SCREEN")
        self.clickElement("choose_language_button.png", "CHOOSE LANGUAGE BUTTON")

    def clickBuyButton(self):
        self.assertExists("BUY_button.png", "BUY BUTTON")
        self.clickElement("BUY_button.png", "BUY BUTTON")

    def clickSellButton(self):
        self.assertExists("SELL_button.png", "SELL BUTTON")
        self.clickElement("SELL_button.png", "SELL BUTTON")

    def completeSellTransaction(self):
        self.assertExists("SELL_complete_button.png", "SELL BUTTON")
        self.clickElement("SELL_complete_button.png", "SELL BUTTON")

    def completeTransaction(self):
        wait("transaction_completed_text.png", WAIT_TIMEOUT)
        self.clickElement("DONE_completed_button.png", "BUY DONE BUTTON")

    def dismissSmsNotificationModal(self):
        self.assertExists(
            "sms_transaction_notification_in_modal.png", "SMS TRANSACTION NOTIFICATION"
        )
        self.clickElement("NO_button_in_modal.png", "NO BUTTON IN MODAL")
