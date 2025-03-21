from Screens.BasePage import BasePage, WAIT_TIMEOUT

from sikuli import wait


class TierSelectScreen(BasePage):
    def chooseAnonymousTierAndContinue(self):
        self.assertExists("choose_cash_limit_text.png", "CHOOSE CASH LIMIT")
        self.assertExists("anonymous_tier_button.png", "ANONYMOUS TIER")
        self.clickElement("anonymous_tier_button.png", "ANONYMOUS TIER")
        wait("CONTINUE_button.png", WAIT_TIMEOUT)
        self.assertExists("CONTINUE_button.png", "CONTINUE BUTTON")
        self.clickElement("CONTINUE_button.png", "CONTINUE BUTTON")

    def chooseUnregisteredTier(self):
        self.assertExists("unregistered_tier_button.png", "UNREGISTERED TIER BUTTON")
        self.clickElement("unregistered_tier_button.png", "UNREGISTERED TIER BUTTON")
