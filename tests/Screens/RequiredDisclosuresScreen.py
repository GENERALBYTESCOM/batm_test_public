from Screens.BasePage import BasePage, WAIT_TIMEOUT

from sikuli import wait


class RequiredDisclosuresScreen(BasePage):
    def acceptRequiredDisclosures(self):
        self.assertExists(
            "required_disclosures_text.png", "REQUIRED DISCLOSURES TEXT EXIST"
        )
        wait("CONTINUE_button.png", WAIT_TIMEOUT)
        self.clickElement("CONTINUE_button.png", "CONTINUE BUTTON")
