class FlowHelper:
    def __init__(self, screens):
        self.screens = screens

    def performAnonymBuyFlow(self):
        self.screens.dashboardScreen.clickBuyButton()
        self.screens.walletScreen.confirmWalletOwnership()
        self.screens.privacyScreen.acceptPrivacyAndDisclaimer()
        self.screens.chooseLimitScreen.chooseAnonymousTierAndContinue()
        self.screens.walletScreen.clickCryptoWallet()

    def performAnonymSellFlow(self):
        self.screens.dashboardScreen.clickSellButton()
        self.screens.privacyScreen.acceptPrivacy()
        self.screens.chooseLimitScreen.chooseAnonymousTierAndContinue()
        self.screens.discountScreen.openDiscountDialog()
        self.screens.discountScreen.waitAndClickDiscountInputField()

    def completeBuyDiscountFlow(self):
        self.screens.discountScreen.submitAndCloseDiscountDialog()
        self.screens.discountScreen.verifyDiscountToast()

    def completeSellDiscountFlow(self):
        self.screens.discountScreen.submitAndCloseDiscountDialog()
        self.screens.discountScreen.verifyDiscountToast()
        self.screens.walletScreen.add100CzkButton()
        self.screens.dashboardScreen.completeSellTransaction()
        self.screens.dashboardScreen.dismissSmsNotificationModal()
        self.screens.dashboardScreen.completeTransaction()
