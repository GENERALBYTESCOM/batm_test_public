from Utils import (
    clickLbtcButton,
    clickSellButton,
    acceptPrivacy,
    openDiscountDialog,
    checkMainScreenAndClickLogo,
    chooseAnonymousTierAndContinue,
    waitAndClickDiscountInputField,
    completeSellDiscountFlow,
)

from sikuli import type

LBTC_DISCOUNT_TEXT = "LBTC"

checkMainScreenAndClickLogo()
clickLbtcButton()
clickSellButton()
acceptPrivacy()
chooseAnonymousTierAndContinue()
openDiscountDialog()
waitAndClickDiscountInputField()
type(LBTC_DISCOUNT_TEXT)
completeSellDiscountFlow()
