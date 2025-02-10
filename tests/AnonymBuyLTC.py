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


if has("tests/screenshots/1724847707672.png"):
    assertClick("tests/screenshots/1727773516372.png", "SCREENSAVER")
assertExists("1738942971358.png", "LTC LOGO")
assertClick("1738942971358.png", "LTC LOGO")
assertExists("1738943148647.png", "BUY BUTTON EXIST")
assertClick("1738943148647.png", "BUY BUTTON")
wait("1738943262351.png", WAIT_TIMEOUT)
assertExists(
    "1738943262351.png",
    "WHERE DO YOU WANT TO SEND PURCHASED CRYPTO CURRENCY? TEXT EXIST",
)
assertClick("1738943373770.png", "SEND COINS TO MY WALLET BUTTON")
assertExists("1738943408415.png", "ARE YOU A POLITICALLY EXPOSED PERSon TEXT EXIST")
assertClick("1727774141922.png", "NO BUTTON")
assertExists("1738943767931.png", "PRIVACY POLICY TEXT EXIST")
assertClick("1738943780180.png", "I AGREE BUTTON")
assertExists("1738944041565.png", "CHOOSE CASH LIMIT TEXT EXIST")
assertClick("1738944025946.png", "UP TO 300 CZK BUTTON")
assertExists("1738944218917.png", "DON'T HAVE WALLET? TEXT EXIST")
assertClick("1738944218917.png", "DON'T HAVE WALLET BUTTON")
assertExists("1738944500278.png", "DON'T HAVE A WALLET? TEXT EXIST")
assertClick("1738944618727.png", "SEND ALTCOIN BY EMAIL BUTTON")
wait("1738944859476.png", WAIT_TIMEOUT)
assertClick("1738944887044.png", "INPUT LINE")
find("1738945177975.png")
assertClick("1727955584803.png", "CLICK INPUT LINE")
type("aa@gg.com")
assertClick("1738945177975.png", "SEND TEXT INPUT BUTTON")
wait("1738945655953.png", WAIT_TIMEOUT)
assertClick("1738945655953.png", "DONE BUTTON")
wait("1738946082323.png", WAIT_TIMEOUT)
assertExists("1738946082323.png", "ONE TIME PASSWORD TEXT EXIST")
assertClick("1738945878928.png", "OK BUTTON")
wait("1738946287704.png", WAIT_TIMEOUT)
assertExists("1738946502249.png", "DISCOUNT INPUT TEXT EXIST")
assertClick("1738946513153.png", "ENTER DISCOUNT CODE BUTTON")
wait("1738946538905.png", WAIT_TIMEOUT)
find("1738945177975.png")
assertClick("1727955584803.png", "CLICK INPUT")
type("123")
assertClick("1738945177975.png", "SEND TEXT INPUT BUTTON")
waitVanish("1738946538905.png", WAIT_TIMEOUT)
assertClick("1738945878928.png", "OK BUTTON")
assertExists("1738947327463.png", "UNKNOWN DISCOUNT CODE TEXT EXIST")
waitVanish("1738947327463.png", WAIT_TIMEOUT)
find("1727790898506.png")
assertClick("1727791300173.png", "CLICK DROPDOWN")
assertExists("1738947549648.png", "INSERTED VALUE = 100 CZK")
assertClick("1738947549648.png", "INSERT BANKNOTE 100 CZK")


def openBanknoteDropdown():
    if has("1727792164614.png"):
        assertClick("1738947549648.png", "SELECT 100 CZK")


assertClick("1738947729117.png", "INSERT BANKNOTE 100 CZK")
assertExists("1738946287704.png", "INSERT CASH TEXT")
wait("1738950216564.png", WAIT_TIMEOUT)
assertClick("1738950216564.png", "BUY LTC BUTTON")
wait("1738950590691.png", WAIT_TIMEOUT)
assertExists("1738950590691.png", "PROCESSING TRANSACTION COMPLETED TEXT EXIST")
assertClick("1738950606099.png", "DONE BUTTON")
