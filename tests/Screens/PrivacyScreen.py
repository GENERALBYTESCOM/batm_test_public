from Screens.BasePage import BasePage


class PrivacyScreen(BasePage):
    def acceptPrivacy(self):
        self.assertExists("pep_question_text.png", "PEP QUESTION TEXT")
        self.clickElement("NO_button.png", "NO BUTTON")
        self.assertExists("privacy_policy_text.png", "PRIVACY POLICY TEXT")
        self.clickElement("I_agree_button.png", "I AGREE BUTTON")

    def acceptPrivacyAndDisclaimer(self):
        self.acceptPrivacy()
        self.assertExists("scam_disclaimer_text.png", "SCAM DISCLAIMER TEXT EXIST")
        self.clickElement("OK_button.png", "OK BUTTON")

    def acceptPrivacyNotice(self):
        self.assertExists("privacy_notice_text.png", "PRIVACY NOTICE TEXT EXIST")
        self.clickElement("I_agree_button.png", "I AGREE BUTTON")
