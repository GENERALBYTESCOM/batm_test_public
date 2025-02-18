from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    checkMainScreenAndClickLogo,
    insertBanknoteAndVerify,
    processPurchaseSteps,
    applyDiscountCode,
)

from sikuli import wait

LBTC_DISCOUNT_TEXT = "LBTC"

checkMainScreenAndClickLogo()
assertExists("tests/screenshots/LBTC_button.png", "LBTC LOGO")
assertClick("tests/screenshots/LBTC_button.png", "LBTC LOGO")
processPurchaseSteps()
insertBanknoteAndVerify("100 CZK")
wait("tests/screenshots/BUY_LBTC_button.png", WAIT_TIMEOUT)
applyDiscountCode(LBTC_DISCOUNT_TEXT)
assertExists("tests/screenshots/BUY_LBTC_button.png", "BUY LTC BUTTON")
assertClick("tests/screenshots/BUY_LBTC_button.png", "BUY LTC BUTTON")
assertExists(
    "tests/screenshots/wait_we_are_not_done_yet_text.png",
    "WAIT, WE ARE NOT DONE YET! TEXT EXIST",
)
assertExists("tests/screenshots/DONE_completed_button.png", "BUY DONE BUTTON")
assertClick("tests/screenshots/DONE_completed_button.png", "BUY DONE BUTTON")
