import sys

from sikuli import click, find, has, wait

WAIT_TIMEOUT = 10


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
    clickBuyButton()
    verifyWalletOwnership()
    acceptDisclaimers()
    selectCashLimit()


def checkMainScreenAndClickLogo():
    if has("tests/screenshots/main_screen.png"):
        assertClick("tests/screenshots/BTC_logo.png", "SCREENSAVER")


def clickBuyButton():
    assertExists("tests/screenshots/BUY_button.png", "BUY BUTTON")
    assertClick("tests/screenshots/BUY_button.png", "BUY BUTTON")


def verifyWalletOwnership():
    wait("tests/screenshots/where_do_you_want_to_send_crypto_text.png", WAIT_TIMEOUT)
    assertExists(
        "tests/screenshots/where_do_you_want_to_send_crypto_text.png",
        "WALLET OWNERSHIP SCREEN TEXT EXIST",
    )
    assertClick(
        "tests/screenshots/send_coins_to_my_wallet_button.png",
        "WALLET OWNERSHIP AGREEMENT BUTTON",
    )


def acceptDisclaimers():
    assertExists("tests/screenshots/pep_question_text.png", "PEP QUESTION TEXT EXIST")
    assertClick("tests/screenshots/NO_button.png", "NO BUTTON")
    assertExists(
        "tests/screenshots/privacy_policy_text.png", "PRIVACY POLICY TEXT EXIST"
    )
    assertClick("tests/screenshots/i_agree_button.png", "I AGREE BUTTON")
    assertExists(
        "tests/screenshots/scam_disclaimer_text.png", "SCAM DISCLAIMER TEXT EXIST"
    )
    assertClick("tests/screenshots/tests/screenshots/OK_button.png", "OK BUTTON")


def selectCashLimit():
    assertExists(
        "tests/screenshots/choose_cash_limit_text.png", "CHOOSE CASH LIMIT TEXT EXIST"
    )
    assertExists("tests/screenshots/anonymous_tier_button.png", "ANONYMOUS TIER BUTTON")
    assertClick("tests/screenshots/anonymous_tier_button.png", "ANONYMOUS TIER BUTTON")
    assertExists(
        "tests/screenshots/CONTINUE_button.png", "REQUIRED DISCLOSURES TEXT EXIST"
    )
    wait("tests/screenshots/CONTINUE_button.png", WAIT_TIMEOUT)
    assertClick("tests/screenshots/CONTINUE_button.png", "DISCLOSURE CONTINUE BUTTON")


def insertBanknote(amount="100 CZK"):
    find("tests/screenshots/CZK_banknote_dropdown.png")
    assertClick(
        "tests/screenshots/CZK_banknote_dropdown_button.png", "OPEN BANKNOTES DROPDOWN"
    )
    assertExists(
        "tests/screenshots/100_banknote_value.png", f"INSERTED VALUE = {amount}"
    )
    assertClick("tests/screenshots/100_banknote_value.png", f"INSERT BANKNOTE {amount}")
    assertExists(
        "tests/screenshots/insert_banknote_button.png", "INSERT BANKNOTE BUTTON"
    )
    assertClick(
        "tests/screenshots/insert_banknote_button.png", "INSERT BANKNOTE BUTTON"
    )
