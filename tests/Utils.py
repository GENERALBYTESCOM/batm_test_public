import sys
import os
from time import sleep
from sikuli import addImagePath, click, find, has, wait, waitVanish

WAIT_TIMEOUT = 15

base_dir = os.path.dirname(__file__)
screenshots_dir = os.path.join(base_dir, "screenshots")
addImagePath(screenshots_dir)


def assertExists(pattern, name):
    sys.stdout.write("Assert '" + name + "' exists...")
    if has(pattern, WAIT_TIMEOUT):
        sys.stdout.write("OK")
    else:
        sys.stdout.write("FAIL")
        sys.exit()
    sys.stdout.flush()


def assertClick(pattern, name):
    sys.stdout.write("Click on '" + name + "'...")
    if click(pattern):
        sys.stdout.write("OK")
    else:
        sys.stdout.write("FAIL")
        sys.exit()
    sys.stdout.flush()


def processPurchaseSteps():
    confirmWalletOwnership()
    acceptPrivacyAndDisclaimer()
    chooseAnonymousTierAndContinue()


def prepareDiscountDialog():
    openDiscountDialog()
    waitAndClickDiscountInputField()


def completeSellDiscountFlow():
    submitAndCloseDiscountDialog()
    verifyDiscountToast()
    add100CzkButton()
    completeSellTransaction()
    dismissSmsNotificationModal()
    completeTransaction()


def initiateAnonymousSellDiscountFlow():
    clickSellButton()
    acceptPrivacy()
    chooseAnonymousTierAndContinue()
    openDiscountDialog()
    waitAndClickDiscountInputField()


def checkMainScreenAndClickLogo():
    if has("main_screen.png"):
        assertClick("BTC_logo.png", "SCREENSAVER")


def clickBuyButton():
    assertExists("BUY_button.png", "BUY BUTTON")
    assertClick("BUY_button.png", "BUY BUTTON")


def clickSellButton():
    assertExists("SELL_button.png", "SELL BUTTON")
    assertClick("SELL_button.png", "SELL BUTTON")


def confirmWalletOwnership():
    wait("wallet_ownership_screen_text.png", WAIT_TIMEOUT)
    assertExists(
        "send_coins_to_my_wallet_button.png",
        "WALLET OWNERSHIP SCREEN TEXT EXIST",
    )
    assertClick(
        "send_coins_to_my_wallet_button.png",
        "WALLET OWNERSHIP AGREEMENT BUTTON",
    )


def acceptPrivacy():
    assertExists("pep_question_text.png", "PEP QUESTION TEXT EXIST")
    assertClick("NO_button.png", "NO BUTTON")
    assertExists("privacy_policy_text.png", "PRIVACY POLICY TEXT EXIST")
    assertClick("I_agree_button.png", "I AGREE BUTTON")


def acceptPrivacyAndDisclaimer():
    acceptPrivacy()
    assertExists("scam_disclaimer_text.png", "SCAM DISCLAIMER TEXT EXIST")
    assertClick("OK_button.png", "OK BUTTON")


def chooseAnonymousTierAndContinue():
    assertExists("choose_cash_limit_text.png", "CHOOSE CASH LIMIT TEXT EXIST")
    assertExists("anonymous_tier_button.png", "ANONYMOUS TIER BUTTON")
    assertClick("anonymous_tier_button.png", "ANONYMOUS TIER BUTTON")
    wait("CONTINUE_button.png", WAIT_TIMEOUT)
    assertExists("CONTINUE_button.png", "REQUIRED DISCLOSURES TEXT EXIST")
    assertClick("CONTINUE_button.png", "CONTINUE BUTTON")


def insertBanknoteAndVerify(amount="100 CZK"):
    wait("insert_cash_text.png", WAIT_TIMEOUT)
    assertExists("insert_cash_text.png", "INSERT MONEY TEXT EXIST")
    assertExists(
        "cash_amount_inserted_value_0_CZK.png",
        "INSERTED VALUE = 0 CZK",
    )
    find("CZK_banknote_dropdown.png")
    assertClick("CZK_banknote_dropdown_button.png", "OPEN BANKNOTES DROPDOWN")
    assertExists("100_banknote_value.png", "INSERTED VALUE = %s" % amount)
    assertClick("100_banknote_value.png", "INSERT BANKNOTE %s" % amount)
    assertExists("insert_banknote_button.png", "INSERT BANKNOTE BUTTON")
    assertClick("insert_banknote_button.png", "INSERT BANKNOTE BUTTON")
    wait("cash_amount_inserted_value_100_CZK.png", WAIT_TIMEOUT)
    assertExists(
        "cash_amount_inserted_value_100_CZK.png",
        "INSERTED VALUE = 100 CZK",
    )


def clickCryptoWallet():
    assertExists(
        "scan_your_wallet's_QR_text.png",
        "SCAN YOUR WALLET'S QR TEXT EXIST",
    )
    assertExists("crypto_wallet_field.png", "CRYPTO WALLET FIELD")
    assertClick("crypto_wallet_field.png", "CRYPTO WALLET FIELD")


def clickScanQrButton():
    assertExists("scan_qr_code_button.png", "SCAN QR CODE BUTTON")
    assertClick("scan_qr_code_button.png", "SCAN QR CODE BUTTON")


def openDiscountDialog():
    assertExists("discount_code_button.png", "DISCOUNT BUTTON EXIST")
    assertClick("discount_code_button.png", "DISCOUNT BUTTON")
    wait("enter_discount_code_text.png", WAIT_TIMEOUT)
    assertExists("enter_discount_code_text.png", "ENTER DISCOUNT CODE DIALOGUE")


def waitAndClickDiscountInputField():
    wait("enter_discount_code_text.png", WAIT_TIMEOUT)
    assertExists("send_text_input_text.png", "TEXT INPUT FIELD")
    assertClick("send_text_input_text.png", "TEXT INPUT FIELD")


def submitAndCloseDiscountDialog():
    assertExists("send_text_input_button.png", "SEND TEXT INPUT BUTTON")
    assertClick("send_text_input_button.png", "SEND TEXT INPUT BUTTON")
    sleep(3)
    assertExists("OK_button.png", "OK BUTTON")
    assertClick("OK_button.png", "OK BUTTON")
    waitVanish("enter_discount_code_text.png", WAIT_TIMEOUT)


def verifyDiscountToast():
    assertExists("discount_code_accepted_toast.png", "DISCOUNT ACCEPTED TOAST")
    waitVanish("discount_code_accepted_toast.png", WAIT_TIMEOUT)


def completeTransaction():
    wait("transaction_completed_text.png", WAIT_TIMEOUT)
    assertExists(
        "transaction_completed_text.png",
        "TRANSACTION COMPLETED TEXT EXIST",
    )
    assertExists("DONE_completed_button.png", "BUY DONE BUTTON")
    assertClick("DONE_completed_button.png", "BUY DONE BUTTON")


def questionnaireRadio():
    wait("questionnaire_radio_text.png", WAIT_TIMEOUT)
    assertExists("questionnaire_radio_text.png", "QUESTIONNAIRE SCREEN RADIO")
    assertExists("DONE_button.png", "DONE BUTTON")
    assertClick("DONE_button.png", "DONE BUTTON")


def clickBtcButton():
    assertExists("BTC_button.png", "BTC LOGO")
    assertClick("BTC_button.png", "BTC LOGO")


def clickLbtcButton():
    assertExists("LBTC_button.png", "LBTC LOGO")
    assertClick("LBTC_button.png", "LBTC LOGO")


def clickLtcButton():
    assertExists("LTC_button.png", "LTC LOGO")
    assertClick("LTC_button.png", "LTC LOGO")


def completeSellTransaction():
    assertExists("SELL_complete_button.png", "SELL BUTTON")
    assertClick("SELL_complete_button.png", "SELL BUTTON")


def add100CzkButton():
    assertExists("+100_CZK_button.png", "+100 CZK BUTTON")
    assertClick("+100_CZK_button.png", "+100 CZK BUTTON")


def dismissSmsNotificationModal():
    assertExists(
        "sms_transaction_notification_in_modal.png", "SMS TRANSACTION NOTIFICATION"
    )
    assertClick("NO_button_in_modal.png", "NO BUTTON IN MODAL")
