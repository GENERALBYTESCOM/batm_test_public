class FlowHelper:
    def __init__(self, screens):
        self.screens = screens

    def clickBuy(self):
        self.screens.dashboardScreen.clickBuyButton()
        self.screens.walletScreen.confirmWalletOwnership()
        self.screens.privacyScreen.acceptPrivacyAndDisclaimer()

    def clickSell(self):
        self.screens.dashboardScreen.clickSellButton()
        self.screens.privacyScreen.acceptPrivacy()

    def chooseTier(self, tier):
        if tier == "anonymous":
            self.screens.chooseLimitScreen.chooseAnonymousTierAndContinue()
        elif tier == "unregistered":
            self.screens.chooseLimitScreen.chooseUnregisteredTier()
        elif tier == "registered":
            self.screens.chooseLimitScreen.chooseRegisteredTier()
        else:
            raise ValueError("Unknown tier: %s" % tier)

    def finishSellTransaction(
        self, requireMarketingDecline=False, requireSmsDismiss=False
    ):
        self.screens.walletScreen.add100CzkButton()
        self.screens.dashboardScreen.completeSellTransaction()

        if requireSmsDismiss:
            self.screens.dashboardScreen.dismissSmsNotificationModal()

        if requireMarketingDecline:
            self.screens.marketingAgreementScreen.declineMarketingAgreement()

        self.screens.dashboardScreen.completeTransaction()

    def completeSellFlow(
        self, useDiscount=False, requireMarketingDecline=False, requireSmsDismiss=False
    ):
        if useDiscount:
            self.completeDiscountFlow()

        self.finishSellTransaction(requireMarketingDecline, requireSmsDismiss)

    def completeDiscountFlow(self):
        self.screens.discountScreen.submitAndCloseDiscountDialog()
        self.screens.discountScreen.verifyDiscountToast()

    # def completeSellDiscountFlow(self):
    #     self.completeDiscountFlow()
    #     self.finishSellTransaction(requireSmsDismiss=True)
    #
    # def completeUnregisteredSellFlow(self):
    #     self.completeDiscountFlow()
    #     self.finishSellTransaction(requireMarketingDecline=True)

    # def performBuyFlow2(self, tier):
    #     self.clickBuy()
    #     self.chooseTier(tier)
    #     self.screens.privacyScreen.acceptPrivacyNotice()
    #     self.verifyPhoneNumberAndOTP()
    #     self.screens.requiredDisclosuresScreen.acceptRequiredDisclosures()
    #     self.screens.walletScreen.clickCryptoWallet()
    #
    # def performSellFlow2(self, tier):
    #     self.clickSell()
    #     self.chooseTier(tier)
    #     self.screens.requiredDisclosuresScreen.acceptRequiredDisclosures()
    #     self.screens.privacyScreen.acceptPrivacyNotice()
    #     self.verifyPhoneNumberAndOTP()
    #     self.screens.discountScreen.prepareDiscountDialog()

    # def performAnonymBuyFlow(self, tier):
    #     self.clickBuy()
    #     self.chooseTier(tier)
    #     self.screens.walletScreen.clickCryptoWallet()
    #
    # def performAnonymSellFlow(self, tier):
    #     self.clickSell()
    #     self.chooseTier(tier)
    #     self.screens.discountScreen.prepareDiscountDialog()

    def performBuyLBTCFlow(self):
        self.clickBuy()
        self.screens.walletScreen.clickIHaveAWalletButton()

    def verifyPhoneNumberAndOTP(self):
        self.screens.numberScreen.assertPhoneNumberTextIsDisplayed()
        self.screens.numberScreen.enterNumber()
        self.screens.numberScreen.assertOTPTextIsDisplayed()
        self.screens.numberScreen.enterNumber()

    def performBuyFlow(self, tier):
        self.clickBuy()
        self.chooseTier(tier)
        if tier != "anonymous":
            self.screens.privacyScreen.acceptPrivacyNotice()
            self.verifyPhoneNumberAndOTP()
            self.screens.requiredDisclosuresScreen.acceptRequiredDisclosures()
        self.screens.walletScreen.clickCryptoWallet()

    def performSellFlow(self, tier):
        self.clickSell()
        self.chooseTier(tier)
        if tier != "anonymous":
            self.screens.requiredDisclosuresScreen.acceptRequiredDisclosures()
            self.screens.privacyScreen.acceptPrivacyNotice()
            self.verifyPhoneNumberAndOTP()
        self.screens.discountScreen.prepareDiscountDialog()
