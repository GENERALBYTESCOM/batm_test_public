from Screens.BasePage import BasePage


class InsertMoneyScreen(BasePage):
    def buyBTC(self):
        self.assertExists("BUY_BTC_button.png", "BUY BTC BUTTON")
        self.clickElement("BUY_BTC_button.png", "BUY BTC BUTTON")

    def buyLTC(self):
        self.assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
        self.clickElement("BUY_LTC_button.png", "BUY LTC BUTTON")

    def buyETH(self):
        self.assertExists("BUY_ETH_button.png", "BUY ETH BUTTON")
        self.clickElement("BUY_ETH_button.png", "BUY ETH BUTTON")
