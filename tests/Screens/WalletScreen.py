from Config.Constants import WAIT_TIMEOUT
from Screens.BasePage import BasePage
from sikuli import wait


class WalletScreen(BasePage):
    def confirmWalletOwnership(self):
        wait("wallet_ownership_screen_text.png", WAIT_TIMEOUT)
        self.assertExists(
            "send_coins_to_my_wallet_button.png",
            "WALLET OWNERSHIP SCREEN TEXT EXIST",
        )
        self.clickElement(
            "send_coins_to_my_wallet_button.png",
            "WALLET OWNERSHIP AGREEMENT BUTTON",
        )

    def clickCryptoWallet(self):
        self.assertExists(
            "scan_your_wallet's_QR_text.png",
            "SCAN YOUR WALLET'S QR TEXT EXIST",
        )
        self.assertExists("crypto_wallet_field.png", "CRYPTO WALLET FIELD")
        self.clickElement("crypto_wallet_field.png", "CRYPTO WALLET FIELD")

    def clickScanQrButton(self):
        self.assertExists("scan_qr_code_button.png", "SCAN QR CODE BUTTON")
        self.clickElement("scan_qr_code_button.png", "SCAN QR CODE BUTTON")

    def insertBanknoteAndVerify(self, amount="100 CZK"):
        wait("insert_cash_text.png", WAIT_TIMEOUT)
        self.assertExists(
            "cash_amount_inserted_value_0_CZK.png", "INSERTED VALUE = 0 CZK"
        )
        self.clickElement("CZK_banknote_dropdown_button.png", "DROPDOWN")
        self.assertExists(
            "%s_banknote_value.png" % amount.split()[0], "INSERTED VALUE = %s" % amount
        )
        self.clickElement(
            "%s_banknote_value.png" % amount.split()[0], "INSERT BANKNOTE %s" % amount
        )
        self.clickElement("insert_banknote_button.png", "INSERT BANKNOTE BUTTON")
        insertedAmountPattern = "cash_amount_inserted_value_%s.png" % amount.replace(
            " ", "_"
        )
        wait(insertedAmountPattern, WAIT_TIMEOUT)

    def add100CzkButton(self):
        self.assertExists("+100_CZK_button.png", "+100 CZK BUTTON")
        self.clickElement("+100_CZK_button.png", "+100 CZK BUTTON")

    def clickIHaveAWalletButton(self):
        self.assertExists(
            "you_must_have_a_wallet_text.png", "YOU MUST HAVE A WALLET TEXT EXIST"
        )
        self.clickElement("I_have_a_wallet.png", "YES, I HAVE A WALLET BUTTON")

    def clickCancelButton(self):
        self.clickElement("CANCEL_button.png", "CANCEL BUTTON")

    def insertBanknoteAndExpectError(self, amount):
        wait("insert_cash_text.png", WAIT_TIMEOUT)
        self.assertExists(
            "cash_amount_inserted_value_0_CZK.png", "INSERTED VALUE = 0 CZK"
        )
        self.clickElement("CZK_banknote_dropdown_button.png", "DROPDOWN")
        self.assertExists(
            "%s_banknote_value.png" % amount.split()[0], "INSERTED VALUE = %s" % amount
        )
        self.clickElement(
            "%s_banknote_value.png" % amount.split()[0], "INSERT BANKNOTE %s" % amount
        )
        self.clickElement("insert_banknote_button.png", "INSERT BANKNOTE BUTTON")
