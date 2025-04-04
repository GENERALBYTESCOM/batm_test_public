from Screens.BasePage import BasePage


class MarketingAgreementScreen(BasePage):
    def declineMarketingAgreement(self):
        self.assertExists(
            "marketing_agreement_text.png", "MARKETING AGREEMENT TEXT EXIST"
        )
        self.clickElement("NO_THANKS_button.png", "NO THANKS BUTTON")
