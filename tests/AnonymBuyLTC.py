import sys
from sikuli import wait, click, find, type, has, waitVanish

WAIT_TIMEOUT = 7


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


if has("tests/screenshots/main_screen.png"):
    assertClick("tests/screenshots/BTC_logo.png", "SCREENSAVER")
assertExists("tests/screenshots/LTC_logo.png", "LTC LOGO")
assertClick("tests/screenshots/LTC_logo.png", "LTC LOGO")
assertExists("tests/screenshots/BUY_button.png", "BUY BUTTON EXIST")
assertClick("tests/screenshots/BUY_button.png", "BUY BUTTON")
wait("tests/screenshots/where_do_you_want_to_send_crypto_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/where_do_you_want_to_send_crypto_text.png",
    "WHERE DO YOU WANT TO SEND PURCHASED CRYPTO CURRENCY? TEXT EXIST",
)
assertClick(
    "tests/screenshots/send_coins_to_my_wallet_button.png",
    "SEND COINS TO MY WALLET BUTTON",
)
assertExists(
    "tests/screenshots/are_you_politically_exposed_person_text.png",
    "ARE YOU A POLITICALLY EXPOSED PERSon TEXT EXIST",
)
assertClick("tests/screenshots/NO_button.png", "NO BUTTON")
assertExists("tests/screenshots/privacy_policy_button.png", "PRIVACY POLICY TEXT EXIST")
assertClick("tests/screenshots/i_agree_button.png", "I AGREE BUTTON")
assertExists(
    "tests/screenshots/choose_cash_limit_text.png", "CHOOSE CASH LIMIT TEXT EXIST"
)
assertClick("tests/screenshots/up_to_300_CZK.png", "UP TO 300 CZK BUTTON")
assertExists(
    "tests/screenshots/don't_have_a_wallet_button.png", "DON'T HAVE WALLET? TEXT EXIST"
)
assertClick(
    "tests/screenshots/don't_have_a_wallet_button.png", "DON'T HAVE WALLET BUTTON"
)
assertExists(
    "tests/screenshots/don't_have_a_wallet_text.png", "DON'T HAVE A WALLET? TEXT EXIST"
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
assertClick(
    "tests/screenshots/enter_discount_code_button.png", "ENTER DISCOUNT CODE BUTTON"
)
wait("tests/screenshots/enter_discount_code_text.png", WAIT_TIMEOUT)
find("tests/screenshots/send_text_input_button.png")
assertClick("tests/screenshots/send_text_input_field.png", "CLICK INPUT")
type("123")
assertClick("tests/screenshots/send_text_input_button.png", "SEND TEXT INPUT BUTTON")
waitVanish("tests/screenshots/enter_discount_code_text.png", WAIT_TIMEOUT)
assertClick("tests/screenshots/OK_button.png", "OK BUTTON")
assertExists(
    "tests/screenshots/unknown_discount_code_text.png",
    "UNKNOWN DISCOUNT CODE TEXT EXIST",
)
waitVanish("tests/screenshots/unknown_discount_code_text.png", WAIT_TIMEOUT)
find("tests/screenshots/CZK_banknote_dropdown.png")
assertClick("tests/screenshots/CZK_banknote_dropdown_button.png", "CLICK DROPDOWN")
assertExists("tests/screenshots/100_banknote_value.png", "INSERTED VALUE = 100 CZK")
assertClick("tests/screenshots/100_banknote_value.png", "INSERT BANKNOTE 100 CZK")


def openBanknoteDropdown():
    if has("tests/screenshots/toggle_button.png"):
        assertClick("tests/screenshots/100_banknote_value.png", "SELECT 100 CZK")


assertClick("tests/screenshots/insert_banknote_button.png", "INSERT BANKNOTE 100 CZK")
assertExists("tests/screenshots/insert_cash_text.png", "INSERT CASH TEXT")
wait("tests/screenshots/BUY_LTC_button.png", WAIT_TIMEOUT)
assertClick("tests/screenshots/BUY_LTC_button.png", "BUY LTC BUTTON")
wait("tests/screenshots/processing_transaction_completed_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/processing_transaction_completed_text.png",
    "PROCESSING TRANSACTION COMPLETED TEXT EXIST",
)
assertClick("tests/screenshots/DONE_completed_button.png", "DONE BUTTON")
