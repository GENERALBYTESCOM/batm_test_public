from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    enterNumber,
    performCommonBuySetup,
    confirmWalletOwnership,
    acceptPrivacyAndDisclaimer,
    clickScanQrButton,
    clickCryptoWallet,
    completeTransaction,
    performDiscountFlow,
)

from Config import DISCOUNT_TEXT, BTC_DESTINATION_ADDRESS
from sikuli import type, wait

performCommonBuySetup()
confirmWalletOwnership()
acceptPrivacyAndDisclaimer()
assertExists("unregistered_tier_button.png", "UNREGISTERED TIER BUTTON")
assertClick("unregistered_tier_button.png", "UNREGISTERED TIER BUTTON")
assertExists("privacy_notice_text.png", "PRIVACY NOTICE TEXT EXIST")
assertClick("I_agree_button.png", "I AGREE BUTTON")
wait("phone_number_text.png", WAIT_TIMEOUT)
assertExists("phone_number_text.png", "PHONE NUMBER TEXT EXIST")
enterNumber()
assertExists("one_time_password_text.png", "ONE TIME PASSWORD TEXT EXIST")
enterNumber()
assertExists("required_disclosures_text.png", "REQUIRED DISCLOSURES TEXT EXIST")
wait("CONTINUE_button.png", WAIT_TIMEOUT)
assertExists("CONTINUE_button.png", "REQUIRED DISCLOSURES TEXT EXIST")
assertClick("CONTINUE_button.png", "CONTINUE BUTTON")
clickCryptoWallet()
type(BTC_DESTINATION_ADDRESS)
clickScanQrButton()
performDiscountFlow(DISCOUNT_TEXT)
assertExists("marketing_agreement_text.png", "MARKETING AGREEMENT TEXT EXIST")
assertClick("NO_THANKS_button.png", "NO THANKS BUTTON")
completeTransaction()
