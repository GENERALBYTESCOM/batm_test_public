import sys
from sikuli import wait, click, find, type, Pattern, has, waitVanish

WAIT_TIMEOUT = 7
BTC_DESTINATION_ADDRESS = "1GBjMVQputwgRkCJ9zK2u9KJVkcEnFXi7z"


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


def openBanknoteDropdown():
    if has(Pattern("1722425469678.png").similar(0.71)):
        assertClick(
            Pattern("1722425469678.png").similar(0.95), "OPEN BANKNOTES DROPDOWN 100"
        )
    elif has(Pattern("1722427265172.png").similar(0.95)):
        assertClick(
            Pattern("1722427265172.png").similar(0.95), "OPEN BANKNOTES DROPDOWN 200"
        )
    elif has(Pattern("1722427299365.png").similar(0.95)):
        assertClick(
            Pattern("1722427299365.png").similar(0.95), "OPEN BANKNOTES DROPDOWN 500"
        )
    elif has(Pattern("1722427411838.png").similar(0.95)):
        assertClick(
            Pattern("1722427411838.png").similar(0.95), "OPEN BANKNOTES DROPDOWN 1000"
        )
    elif has(Pattern("1722427462571.png").similar(0.95)):
        assertClick(
            Pattern("1722427462571.png").similar(0.95), "OPEN BANKNOTES DROPDOWN 2000"
        )
    elif has(Pattern("1722427510166.png").similar(0.95)):
        assertClick(
            Pattern("1722427510166.png").similar(0.95), "OPEN BANKNOTES DROPDOWN 5000"
        )
    else:
        sys.stdout.write("CANNOT OPEN DROPDOWN")
        sys.exit()
    sys.stdout.flush()


if has("tests/screenshots/1724847707672.png"):
    assertClick("tests/screenshots/1727773516372.png", "SCREENSAVER")
assertExists("1728304602566.png", "LTC LOGO")
assertClick("1728304616977.png", "LTC LOGO")
assertExists("1727773811641.png", "BUY BUTTON EXIST")
assertClick("1727774023585.png", "BUY BUTTON")
wait("1727774440040.png", WAIT_TIMEOUT)
assertExists(
    "1727774440040.png",
    "WHERE DO YOU WANT TO SEND PURCHASED CRYPTO CURRENCY? TEXT EXIST",
)
assertClick("1727774055016.png", "SEND COINS TO MY WALLET BUTTON")
assertExists("1728054995323.png", "PEP QUESTION TEXT EXIST")
assertClick("1727774141922.png", "NO BUTTON")
assertExists("1728045451719.png", "PRIVACY POLICY TEXT EXIST")
assertClick("1727774206671.png", "I AGREE BUTTON")
assertExists("1727774640062.png", "SCAM DISCLAMER TEXT EXIST")
assertClick("1727774656743.png", "OK BUTTON")
assertExists("1727774734990.png", "CHOOSE CASH LIMIT TEXT EXIST")
assertClick("1727774745878.png", "UP TO 300 CZK BUTTON")
assertExists("1727774810178.png", "REQUIRED DISCLOSURES TEXT EXIST")
wait("1727774823267.png", WAIT_TIMEOUT)
assertClick("1727774823267.png", "CONTINUE BUTTON")
assertExists("1728038970895.png", "DON'T HAVE WALLET? TEXT EXIST")
assertClick("1728038995960.png", "DON'T HAVE WALLET BUTTON")
assertExists("1728039017399.png", "DON'T HAVE A WALLET? TEXT EXIST")
assertClick("1728039029519.png", "SEND BITCOIN BY EMAIL BUTTON")
wait("1728039295591.png", WAIT_TIMEOUT)
assertClick("1728039306920.png", "INPUT LINE")
find("1727954109388.png")
assertClick("1727955584803.png", "CLICK INPUT LINE")
type("aa@gg.com")
assertClick("1727954348111.png", "SEND TEXT INPUT BUTTON")
wait("1728045640206.png", WAIT_TIMEOUT)
assertClick("1728039389040.png", "DONE BUTTON")
assertExists("1728039518831.png", "ONE TIME PASSWORD TEXT EXIST")
assertClick("1728039530360.png", "OK BUTTON")
wait("1727791976270.png", WAIT_TIMEOUT)
assertExists("1727783995345.png", "DISCOUNT INPUT TEXT EXIST")
assertClick("1727784005958.png", "ENTER DISCOUNT CODE BUTTON")
wait("1727955164721.png", WAIT_TIMEOUT)
find("1727954109388.png")
assertClick("1727955584803.png", "CLICK INPUT")
type("123")
assertClick("1727954348111.png", "SEND TEXT INPUT BUTTON")
wait("1727954667429.png", WAIT_TIMEOUT)
assertExists("1727954277029.png", "ENTER DISCOUNT CODE LOGO")
assertClick("1727954257108.png", "OK BUTTON")
waitVanish("1727955164721.png", WAIT_TIMEOUT)
assertExists("1727954323733.png", "UNKNOWN DISCOUNT CODE TEXT EXIST")
waitVanish("1727954323733.png", WAIT_TIMEOUT)
find("1727790898506.png")
assertClick("1727791300173.png", "CLICK DROPDOWN")
assertExists("1727784530186.png", "INSERTED VALUE = 100 CZK")
assertClick("1727791315299.png", "INSERT BANKNOTE 100 CZK")


def openBanknoteDropdown():
    if has("1727792164614.png"):
        assertClick("1727792215829.png", "SELECT 100 CZK")


assertClick("1727784547352.png", "INSERT BANKNOTE 100 CZK")
assertExists("1727784268519.png", "INSERT CASH LOGO")
wait("1728307044742.png", WAIT_TIMEOUT)
assertClick("1728307056118.png", "BUY LTC BUTTON")
assertExists("1728305846284.png", "PROCESSING TRANSACTION COMPLETED TEXT EXIST")
assertClick("1728056816610.png", "DONE BUTTON")
