from Config.Constants import WAIT_TIMEOUT
from Screens.BasePage import BasePage
from sikuli import wait, Pattern


class LanguageScreen(BasePage):
    def selectLanguage(self, bannerImage, bannerLabel, welcomeLogo, similarity=0.90):
        wait(bannerImage, WAIT_TIMEOUT)
        pattern = Pattern(bannerImage).similar(similarity)
        self.assertExists(pattern, bannerLabel)
        self.clickElement(pattern, bannerLabel)
        self.assertExists(welcomeLogo, "%s WELCOME LOGO" % bannerLabel)

    def clickArrowRight(self):
        self.assertExists("arrow_to_the_right_button.png", "ARROW TO THE RIGHT")
        self.clickElement("arrow_to_the_right_button.png", "ARROW TO THE RIGHT")

    def clickArrowLeft(self):
        self.assertExists("arrow_to_the_left_button.png", "ARROW TO THE LEFT")
        self.clickElement("arrow_to_the_left_button.png", "ARROW TO THE LEFT")

    def cancelAndVerify(self):
        self.clickElement("CANCEL_button.png", "CANCEL BUTTON")
        self.assertExists("EN_welcome_logo_text.png", "EN WELCOME LOGO")
