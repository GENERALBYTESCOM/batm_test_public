from Utils import (
    assertClick,
    assertExists,
    clickBtcButton,
    checkMainScreenAndClickLogo,
    clickBuyButton,
    insertBanknoteAndVerify,
    processPurchaseSteps,
    clickScanQrButton,
    clickCryptoWallet,
    prepareDiscountDialog,
    completeTransaction,
    submitAndCloseDiscountDialog,
    verifyDiscountToast,
    questionnaireRadio,
)

from sikuli import type

BTC_DESTINATION_ADDRESS = "bc1qcwjpenc7vyrun0ttzsm72xwdu8rklgjwdma5vg"
DISCOUNT_TEXT = "ATTT"

checkMainScreenAndClickLogo()
clickBtcButton()
clickBuyButton()
processPurchaseSteps()
clickCryptoWallet()
type(BTC_DESTINATION_ADDRESS)
clickScanQrButton()
questionnaireRadio()
insertBanknoteAndVerify("100 CZK")
assertExists("BUY_BTC_button.png", "BUY OK BUTTON")
prepareDiscountDialog()
type(DISCOUNT_TEXT)
submitAndCloseDiscountDialog()
verifyDiscountToast()
assertExists("BUY_BTC_button.png", "BUY OK BUTTON")
assertClick("BUY_BTC_button.png", "BUY OK BUTTON")
completeTransaction()
