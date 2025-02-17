from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    checkMainScreenAndClickLogo,
    insertBanknoteAndVerify,
    processPurchaseSteps,
    clickCryptoWallet,
    clickScanQrButton,
    applyDiscountCode,
    completeTransaction,
)

from sikuli import type, wait

LTC_DESTINATION_ADDRESS = "LgbEoMr5eJWKEyzXs4ZYBiEjCaUTxbsDm8"
LTC_DISCOUNT_TEXT = "LTC"

checkMainScreenAndClickLogo()
assertExists("tests/screenshots/LTC_button.png", "LTC LOGO")
assertClick("tests/screenshots/LTC_button.png", "LTC LOGO")
processPurchaseSteps()
clickCryptoWallet()
type(LTC_DESTINATION_ADDRESS)
clickScanQrButton()
insertBanknoteAndVerify("100 CZK")
wait("tests/screenshots/BUY_LTC_button.png", WAIT_TIMEOUT)
applyDiscountCode(LTC_DISCOUNT_TEXT)
assertExists("tests/screenshots/BUY_LTC_button.png", "BUY LTC BUTTON")
assertClick("tests/screenshots/BUY_LTC_button.png", "BUY LTC BUTTON")
completeTransaction()
