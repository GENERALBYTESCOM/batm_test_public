from Utils import (
    clickLtcButton,
    checkMainScreenAndClickLogo,
    initiateAnonymousSellDiscountFlow,
    completeSellDiscountFlow,
)

from sikuli import type

LTC_DISCOUNT_TEXT = "LTC"

checkMainScreenAndClickLogo()
clickLtcButton()
initiateAnonymousSellDiscountFlow()
type(LTC_DISCOUNT_TEXT)
completeSellDiscountFlow()
