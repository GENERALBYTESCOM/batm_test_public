from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    clickLtcButton,
    checkMainScreenAndClickLogo,
    insertBanknoteAndVerify,
    processPurchaseSteps,
    clickCryptoWallet,
    clickScanQrButton,
    clickBuyButton,
    prepareDiscountDialog,
    completeTransaction,
    submitAndCloseDiscountDialog,
    verifyDiscountToast,
)

from sikuli import type, wait

LTC_DESTINATION_ADDRESS = "LgbEoMr5eJWKEyzXs4ZYBiEjCaUTxbsDm8"
LTC_DISCOUNT_TEXT = "LTC"

checkMainScreenAndClickLogo()
clickLtcButton()
clickBuyButton()
processPurchaseSteps()
clickCryptoWallet()
type(LTC_DESTINATION_ADDRESS)
clickScanQrButton()
insertBanknoteAndVerify("100 CZK")
wait("BUY_LTC_button.png", WAIT_TIMEOUT)
prepareDiscountDialog()
type(LTC_DISCOUNT_TEXT)
submitAndCloseDiscountDialog()
verifyDiscountToast()
assertExists("BUY_LTC_button.png", "BUY LTC BUTTON")
assertClick("BUY_LTC_button.png", "BUY LTC BUTTON")
completeTransaction()
