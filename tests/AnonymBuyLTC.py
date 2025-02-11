from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    checkMainScreenAndClickLogo,
    insertBanknote,
    processPurchaseSteps,
)

from sikuli import find, type, wait, waitVanish

checkMainScreenAndClickLogo()
assertExists("tests/screenshots/LTC_logo.png", "LTC LOGO")
assertClick("tests/screenshots/LTC_logo.png", "LTC LOGO")
processPurchaseSteps()
assertExists(
    "tests/screenshots/don't_have_a_wallet_button.png", "DON'T HAVE WALLET? TEXT EXIST"
)
assertClick(
    "tests/screenshots/don't_have_a_wallet_button.png", "DON'T HAVE WALLET BUTTON"
)
wait("tests/screenshots/don't_have_a_altcoin_wallet_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/don't_have_a_altcoin_wallet_text.png",
    "DON'T HAVE A WALLET? TEXT EXIST",
)
assertClick(
    "tests/screenshots/send_altcoin_by_email_button.png", "SEND ALTCOIN BY EMAIL BUTTON"
)
wait("tests/screenshots/your_email_text.png", WAIT_TIMEOUT)
assertClick("tests/screenshots/input_line_for_email.png", "INPUT LINE")
find("tests/screenshots/send_text_input_button.png")
assertClick("tests/screenshots/send_text_input_field.png", "CLICK INPUT LINE")
type("aa@gg.com")
assertClick("tests/screenshots/send_text_input_button.png", "SEND TEXT INPUT BUTTON")
wait("tests/screenshots/DONE_button.png", WAIT_TIMEOUT)
assertClick("tests/screenshots/DONE_button.png", "DONE BUTTON")
wait("tests/screenshots/one_time_password_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/one_time_password_text.png", "ONE TIME PASSWORD TEXT EXIST"
)
assertClick("tests/screenshots/OK_button.png", "OK BUTTON")
wait("tests/screenshots/insert_cash_text.png", WAIT_TIMEOUT)
assertExists("tests/screenshots/discount_text.png", "DISCOUNT INPUT TEXT EXIST")
assertClick("tests/screenshots/discount_code_button.png", "DISCOUNT BUTTON")
wait("tests/screenshots/enter_discount_code_text.png", WAIT_TIMEOUT)
find("tests/screenshots/send_text_input_button.png")
assertClick("tests/screenshots/send_text_input_field.png", "CLICK INPUT")
type("123")
assertClick("tests/screenshots/send_text_input_button.png", "SEND TEXT INPUT BUTTON")
waitVanish("tests/screenshots/enter_discount_code_text.png", WAIT_TIMEOUT)
assertClick("tests/screenshots/OK_button.png", "OK BUTTON")
assertExists(
    "tests/screenshots/unknown_discount_code_text.png",
    "UNKNOWN DISCOUNT CODE TOAST",
)
waitVanish("tests/screenshots/unknown_discount_code_text.png", WAIT_TIMEOUT)
insertBanknote("100 CZK")
assertExists("tests/screenshots/insert_cash_text.png", "INSERT CASH TEXT")
wait("tests/screenshots/BUY_LTC_button.png", WAIT_TIMEOUT)
assertClick("tests/screenshots/BUY_LTC_button.png", "BUY LTC BUTTON")
wait("tests/screenshots/transaction_completed_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/transaction_completed_text.png",
    "TRANSACTION COMPLETED TEXT EXIST",
)
assertClick("tests/screenshots/DONE_completed_button.png", "DONE BUTTON")
