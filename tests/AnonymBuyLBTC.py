from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    prepareDiscountDialog,
    insertBanknoteAndVerify,
    confirmWalletOwnership,
    checkMainScreenAndClickLogo,
    acceptPrivacyAndDisclaimer,
    submitAndCloseDiscountDialog,
    chooseAnonymousTierAndContinue,
)

from sikuli import wait, type, waitVanish

LBTC_DISCOUNT_TEXT = "LBTC"

checkMainScreenAndClickLogo()
assertExists("LBTC_button.png", "LBTC LOGO")
assertClick("LBTC_button.png", "LBTC LOGO")
confirmWalletOwnership()
acceptPrivacyAndDisclaimer()
wait("you_must_have_a_wallet_text.png", WAIT_TIMEOUT)
assertClick("I_have_a_wallet.png", "YES, I HAVE A WALLET BUTTON")
chooseAnonymousTierAndContinue()
insertBanknoteAndVerify("100 CZK")
wait("BUY_LBTC_button.png", WAIT_TIMEOUT)
prepareDiscountDialog()
type(LBTC_DISCOUNT_TEXT)
submitAndCloseDiscountDialog()
assertExists("discount_code_accepted_toast.png", "DISCOUNT ACCEPTED TOAST")
waitVanish("discount_code_accepted_toast.png", WAIT_TIMEOUT)
assertExists("BUY_LBTC_button.png", "BUY LBTC BUTTON")
assertClick("BUY_LBTC_button.png", "BUY LBTC BUTTON")
assertExists(
    "wait_we_are_not_done_yet_text.png",
    "WAIT, WE ARE NOT DONE YET! TEXT EXIST",
)
assertExists("DONE_completed_button.png", "BUY DONE BUTTON")
assertClick("DONE_completed_button.png", "BUY DONE BUTTON")
