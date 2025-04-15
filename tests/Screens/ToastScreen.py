from Screens.BasePage import BasePage
from sikuli import waitVanish


class ToastScreen(BasePage):
    def errorBTCWallet(self):
        self.assertExists("error_wallet.png", "ERROR BTC WALLET TOAST")
        waitVanish("error_wallet.png")

    def errorLimitTransaction(self):
        self.assertExists(
            "cash_limit_exceeded_for_transaction.png",
            "CASH LIMIT EXCEEDED FOR THIS TRANSACTION TEXT",
        )
        waitVanish("cash_limit_exceeded_for_transaction.png")
