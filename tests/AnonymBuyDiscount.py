import sys
from sikuli import wait, click, find, type, has, waitVanish, Pattern

WAIT_TIMEOUT = 10
BTC_DESTINATION_ADDRESS = "bc1qcwjpenc7vyrun0ttzsm72xwdu8rklgjwdma5vg"
DISCOUNT_TEXT = "ATTT"


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
assertExists("tests/screenshots/BTC_button.png", "BTC LOGO")
assertClick("tests/screenshots/BTC_button.png", "BTC LOGO")
assertExists("tests/screenshots/BUY_button.png", "BUY BUTTON")
assertClick("tests/screenshots/BUY_button.png", "BUY BUTTON")
wait("tests/screenshots/where_do_you_want_to_send_crypto_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/where_do_you_want_to_send_crypto_text.png",
    "WALLET OWNERSHIP SCREEN TEXT EXIST",
)
assertClick(
    "tests/screenshots/send_coins_to_my_wallet_button.png",
    "WALLET OWNERSHIP AGREEMENT BUTTON",
)
assertExists("tests/screenshots/pep_question_text.png", "PEP QUESTION TEXT EXIST")
assertClick("tests/screenshots/NO_button.png", "NO BUTTON")
assertExists("tests/screenshots/privacy_policy_text.png", "PRIVACY POLICY TEXT EXIST")
assertClick("tests/screenshots/i_agree_button.png", "I AGREE BUTTON")
assertExists("tests/screenshots/scam_disclaimer_text.png", "SCAM DISCLAIMER TEXT EXIST")
assertClick("tests/screenshots/tests/screenshots/OK_button.png", "OK BUTTON")
assertExists(
    "tests/screenshots/choose_cash_limit_text.png", "CHOOSE CASH LIMIT TEXT EXIST"
)
assertExists("tests/screenshots/anonymous_tier_button.png", "ANONYMOUS TIER BUTTON")
assertClick("tests/screenshots/anonymous_tier_button.png", "ANONYMOUS TIER BUTTON")
assertExists("tests/screenshots/CONTINUE_button.png", "REQUIRED DISCLOSURES TEXT EXIST")
wait("tests/screenshots/CONTINUE_button.png", WAIT_TIMEOUT)
assertClick("tests/screenshots/CONTINUE_button.png", "DISCLOSURE CONTINUE BUTTON")
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
find("tests/screenshots/CZK_banknote_dropdown.png")
assertClick(
    "tests/screenshots/CZK_banknote_dropdown_button.png", "OPEN BANKNOTES DROPDOWN"
)
assertExists("tests/screenshots/100_banknote_value.png", "INSERTED VALUE = 100 CZK")
assertClick("tests/screenshots/100_banknote_value.png", "INSERT BANKNOTE 100 CZK")
assertExists("tests/screenshots/insert_banknote_button.png", "INSERT BANKNOTE BUTTON")
assertClick("tests/screenshots/insert_banknote_button.png", "INSERT BANKNOTE BUTTON")
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
