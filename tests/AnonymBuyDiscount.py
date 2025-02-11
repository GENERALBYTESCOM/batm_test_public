
from Utils import (WAIT_TIMEOUT, assertClick, assertExists,
                   checkMainScreenAndClickLogo, insertBanknote,
                   processPurchaseSteps)

from sikuli import Pattern, find, type, wait, waitVanish

BTC_DESTINATION_ADDRESS = "bc1qcwjpenc7vyrun0ttzsm72xwdu8rklgjwdma5vg"
DISCOUNT_TEXT = "ATTT"


checkMainScreenAndClickLogo()
assertExists("tests/screenshots/BTC_button.png", "BTC LOGO")
assertClick("tests/screenshots/BTC_button.png", "BTC LOGO")
processPurchaseSteps()
assertExists(
    "tests/screenshots/enter_wallet_screen_text.png", "ENTER WALLET TEXT EXIST"
)
assertExists("tests/screenshots/crypto_wallet_field.png", "CRYPTO WALLET FIELD")
assertClick("tests/screenshots/crypto_wallet_field.png", "CRYPTO WALLET FIELD")
type(BTC_DESTINATION_ADDRESS)
assertExists("tests/screenshots/scan_qr_code_button.png", "SCAN QR CODE BUTTON")
assertClick("tests/screenshots/scan_qr_code_button.png", "SCAN QR CODE BUTTON")
wait("tests/screenshots/questionnaire_radio_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/questionnaire_radio_text.png", "QUESTIONNAIRE SCREEN RADIO"
)
assertExists("tests/screenshots/DONE_button.png", "DONE BUTTON")
assertClick("tests/screenshots/DONE_button.png", "DONE BUTTON")
assertExists("tests/screenshots/insert_cash_text.png", "INSERT MONEY TEXT EXIST")
assertExists(
    "tests/screenshots/cash_amount_inserted_value_0_CZK.png", "INSERTED VALUE = 0 CZK"
)
insertBanknote("100 CZK")
wait("tests/screenshots/cash_amount_inserted_value_100_CZK.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/cash_amount_inserted_value_100_CZK.png",
    "INSERTED VALUE = 100 CZK",
)
assertExists("tests/screenshots/tests/screenshots/BUY_BTC_button.png", "BUY OK BUTTON")
assertExists("tests/screenshots/discount_text.png", "DISCOUNT INPUT TEXT EXIST")
assertClick("tests/screenshots/discount_code_button.png", "DISCOUNT BUTTON")
wait("tests/screenshots/enter_discount_code_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/enter_discount_code_text.png", "ENTER DISCOUNT CODE DIALOGUE"
)
find("tests/screenshots/send_text_input_button.png")
assertClick("tests/screenshots/send_text_input_field.png", "TEXT INPUT BUTTON")
type(DISCOUNT_TEXT)
assertClick("tests/screenshots/send_text_input_button.png", "SEND TEXT INPUT BUTTON")
assertExists("tests/screenshots/OK_button.png", "OK BUTTON")
assertClick("tests/screenshots/OK_button.png", "OK BUTTON")
assertExists(
    "tests/screenshots/discount_code_accepted_toast.png", "DISCOUNT ACCEPTED TOAST"
)
waitVanish("tests/screenshots/discount_code_accepted_toast.png", 5)
assertExists(
    Pattern("tests/screenshots/discount_20_CZK_exist.png").exact(), "DISCOUNT 20 CZK"
)
assertExists("tests/screenshots/BUY_BTC_button.png", "BUY OK BUTTON")
assertClick("tests/screenshots/BUY_BTC_button.png", "BUY OK BUTTON")
wait("tests/screenshots/transaction_completed_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/transaction_completed_text.png",
    "TRANSACTION COMPLETED TEXT EXIST",
)
assertExists("tests/screenshots/DONE_completed_button.png", "BUY DONE BUTTON")
assertClick("tests/screenshots/DONE_completed_button.png", "BUY DONE BUTTON")
