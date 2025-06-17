from Config.Constants import WAIT_TIMEOUT
from Screens.BasePage import BasePage
from sikuli import wait, exists


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
        if exists("crypto_wallet_field_win.png", WAIT_TIMEOUT):
            self.clickElement("crypto_wallet_field_win.png", "CRYPTO WALLET FIELD")
        elif exists("crypto_wallet_field.png", WAIT_TIMEOUT):
            self.clickElement("crypto_wallet_field.png", "CRYPTO WALLET FIELD")

    def clickScanQrButton(self):
        if exists("scan_qr_code_button_win.png", WAIT_TIMEOUT):
            self.clickElement("scan_qr_code_button_win.png", "SCAN QR CODE BUTTON")
        elif exists("scan_qr_code_button.png", WAIT_TIMEOUT):
            self.clickElement("scan_qr_code_button.png", "SCAN QR CODE BUTTON")

    def insertBanknoteAndVerify(self, amount):
        self.waitForInsertCash()
        self.selectBanknoteFromDdAndInsert(amount)
        self.verifyInsertedAmount(amount)

    def waitForInsertCash(self):
        wait("insert_cash_text.png", WAIT_TIMEOUT)
        self.assertExists(
            "cash_amount_inserted_text.png", "CASH AMOUNT INSERTED TEXT EXIST"
        )
        self.assertExists("cash_amount_inserted_value_0.png", "INSERTED VALUE = 0.00")

    def selectBanknoteFromDdAndInsert(self, amount):
        self.clickElement("banknote_dropdown_button.png", "CLICK ON DROPDOWN")
        banknoteDropdownValue = "%s_banknote_value.png" % int(float(amount))
        self.assertExists(banknoteDropdownValue, "INSERTED VALUE = %s" % amount)
        self.clickElement(banknoteDropdownValue, "INSERT BANKNOTE %s" % amount)
        if exists("insert_banknote_button_win.png", WAIT_TIMEOUT):
            self.clickElement(
                "insert_banknote_button_win.png", "INSERT BANKNOTE BUTTON"
            )
        elif exists("insert_banknote_button.png", WAIT_TIMEOUT):
            self.clickElement("insert_banknote_button.png", "INSERT BANKNOTE BUTTON")

    def verifyInsertedAmount(self, amount):
        if "." not in str(amount):
            amountDisplay = "%s.00" % amount
        else:
            amountDisplay = str(amount)
        img = "cash_amount_inserted_value_%s.png" % amountDisplay
        wait(img, WAIT_TIMEOUT)
        self.assertExists(img, "INSERTED AMOUNT %s IS DISPLAYED" % amountDisplay)

    def clickAddAmountButton(self, amount):
        buttonImg = "+%s_sell_button.png" % amount
        comment = "+%s SELL BUTTON" % amount
        self.assertExists(buttonImg, comment)
        self.clickElement(buttonImg, comment)

    def clickIHaveAWalletButton(self):
        self.assertExists(
            "you_must_have_a_wallet_text.png", "YOU MUST HAVE A WALLET TEXT EXIST"
        )
        self.clickElement("I_have_a_wallet.png", "YES, I HAVE A WALLET BUTTON")

    def clickCancelButton(self):
        self.clickElement("CANCEL_button.png", "CANCEL BUTTON")
