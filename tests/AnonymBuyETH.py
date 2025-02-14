from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    checkMainScreenAndClickLogo,
    insertBanknoteAndVerify,
    processPurchaseSteps,
    clickScanQrButton,
    clickCryptoWallet,
    applyDiscountCode,
    completeTransaction,
)

from sikuli import type, wait

ETH_DESTINATION_ADDRESS = "0xCa5B0c8c0Cce45f2054FbB47505D8d7f831f9394"
ETH_DISCOUNT_TEXT = "ETH"


checkMainScreenAndClickLogo()
assertExists("tests/screenshots/ETH_button.png", "ETH LOGO")
assertClick("tests/screenshots/ETH_button.png", "ETH LOGO")
processPurchaseSteps()
clickCryptoWallet()
type(ETH_DESTINATION_ADDRESS)
clickScanQrButton()
insertBanknoteAndVerify("100 CZK")
wait("tests/screenshots/BUY_ETH_button.png", WAIT_TIMEOUT)
applyDiscountCode(ETH_DISCOUNT_TEXT)
assertExists("BUY_ETH_button.png", "BUY OK BUTTON")
assertClick("BUY_ETH_button.png", "BUY OK BUTTON")
completeTransaction()
