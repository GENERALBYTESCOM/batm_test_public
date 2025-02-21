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
    prepareDiscountDialog,
    completeTransaction,
    submitAndCloseDiscountDialog,
    verifyDiscountToast,
)

from sikuli import type, wait

BTC_DESTINATION_ADDRESS = "bc1qcwjpenc7vyrun0ttzsm72xwdu8rklgjwdma5vg"
DISCOUNT_TEXT = "ATTT"

checkMainScreenAndClickLogo()
assertExists("BTC_button.png", "BTC LOGO")
assertClick("BTC_button.png", "BTC LOGO")
clickBuyButton()
processPurchaseSteps()
clickCryptoWallet()
type(BTC_DESTINATION_ADDRESS)
clickScanQrButton()
wait("questionnaire_radio_text.png", WAIT_TIMEOUT)
assertExists("questionnaire_radio_text.png", "QUESTIONNAIRE SCREEN RADIO")
assertExists("DONE_button.png", "DONE BUTTON")
assertClick("DONE_button.png", "DONE BUTTON")
insertBanknoteAndVerify("100 CZK")
assertExists("BUY_BTC_button.png", "BUY OK BUTTON")
prepareDiscountDialog()
type(DISCOUNT_TEXT)
submitAndCloseDiscountDialog()
verifyDiscountToast()
assertExists("BUY_BTC_button.png", "BUY OK BUTTON")
assertClick("BUY_BTC_button.png", "BUY OK BUTTON")
completeTransaction()
