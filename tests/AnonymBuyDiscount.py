from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    checkMainScreenAndClickLogo,
    clickBuyButton,
    insertBanknoteAndVerify,
    processPurchaseSteps,
    clickScanQrButton,
    clickCryptoWallet,
    applyDiscountCode,
    completeTransaction,
)

from sikuli import type, wait

BTC_DESTINATION_ADDRESS = "bc1qcwjpenc7vyrun0ttzsm72xwdu8rklgjwdma5vg"
DISCOUNT_TEXT = "ATTT"

checkMainScreenAndClickLogo()
assertExists("tests/screenshots/BTC_button.png", "BTC LOGO")
assertClick("tests/screenshots/BTC_button.png", "BTC LOGO")
clickBuyButton()
processPurchaseSteps()
clickCryptoWallet()
type(BTC_DESTINATION_ADDRESS)
clickScanQrButton()
wait("tests/screenshots/questionnaire_radio_text.png", WAIT_TIMEOUT)
assertExists(
    "tests/screenshots/questionnaire_radio_text.png", "QUESTIONNAIRE SCREEN RADIO"
)
assertExists("tests/screenshots/DONE_button.png", "DONE BUTTON")
assertClick("tests/screenshots/DONE_button.png", "DONE BUTTON")
insertBanknoteAndVerify("100 CZK")
assertExists("tests/screenshots/tests/screenshots/BUY_BTC_button.png", "BUY OK BUTTON")
applyDiscountCode(DISCOUNT_TEXT)
assertExists("tests/screenshots/BUY_BTC_button.png", "BUY OK BUTTON")
assertClick("tests/screenshots/BUY_BTC_button.png", "BUY OK BUTTON")
completeTransaction()
