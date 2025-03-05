from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    clickBtcButton,
    clickSellButton,
    acceptPrivacy,
    questionnaireRadio,
    verifyDiscountToast,
    completeTransaction,
    checkMainScreenAndClickLogo,
    chooseAnonymousTierAndContinue,
    waitAndClickDiscountInputField,
    submitAndCloseDiscountDialog,
)

from sikuli import type, wait

DISCOUNT_TEXT = "ATTT"

checkMainScreenAndClickLogo()
clickBtcButton()
clickSellButton()
acceptPrivacy()
chooseAnonymousTierAndContinue()
questionnaireRadio()
assertExists("discount_code_button.png", "DISCOUNT BUTTON")
assertClick("discount_code_button.png", "DISCOUNT BUTTON")
wait("enter_discount_code_text.png", WAIT_TIMEOUT)
assertExists("enter_discount_code_text.png", "ENTER DISCOUNT CODE DIALOGUE")
waitAndClickDiscountInputField()
type(DISCOUNT_TEXT)
submitAndCloseDiscountDialog()
verifyDiscountToast()
assertExists("+100_CZK_button.png", "+100 CZK BUTTON")
assertClick("+100_CZK_button.png", "+100 CZK BUTTON")
assertExists("SELL_complete_button.png", "SELL BUTTON")
assertClick("SELL_complete_button.png", "SELL BUTTON")
assertExists(
    "sms_transaction_notification_in_modal.png", "SMS TRANSACTION NOTIFICATION"
)
assertClick("NO_button_in_modal.png", "NO BUTTON IN MODAL")
completeTransaction()
