from Screens.BasePage import BasePage
from Screens.RequiredDisclosuresScreen import RequiredDisclosuresScreen


class ChooseLimitScreen(BasePage):
    def chooseAnonymousTierAndContinue(self):
        self.assertExists("choose_cash_limit_text.png", "CHOOSE CASH LIMIT")
        self.clickElement("anonymous_tier_button.png", "ANONYMOUS TIER")
        RequiredDisclosuresScreen(self.device).acceptRequiredDisclosures()

    def chooseUnregisteredTier(self):
        self.assertExists("choose_cash_limit_text.png", "CHOOSE CASH LIMIT")
        self.assertExists("unregistered_tier_button.png", "UNREGISTERED TIER BUTTON")
        self.clickElement("unregistered_tier_button.png", "UNREGISTERED TIER BUTTON")

    def chooseRegisteredTier(self):
        self.assertExists("choose_cash_limit_text.png", "CHOOSE CASH LIMIT")
        self.assertExists("registered_tier_button.png", "REGISTERED TIER BUTTON")
        self.clickElement("registered_tier_button.png", "REGISTERED TIER BUTTON")
