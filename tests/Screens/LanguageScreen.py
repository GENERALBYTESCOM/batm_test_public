from Config.Constants import WAIT_TIMEOUT
from Screens.BasePage import BasePage
from sikuli import wait, sleep, Pattern, FindFailed


class LanguageScreen(BasePage):
    langBanners = {
        "EN": ["GB_EN_banner.png", "US_EN_banner.png"],
        "CZ": ["CZ_banner.png"],
        "DE": ["DE_banner.png"],
    }

    welcomeLogos = {
        "EN": "EN_welcome_logo_text.png",
        "CZ": "CZ_welcome_logo_text.png",
        "DE": "DE_welcome_logo_text.png",
    }

    def selectLanguage(self, lang):
        banners = self.langBanners[lang]
        for banner in banners:
            try:
                wait(Pattern(banner).similar(0.8), WAIT_TIMEOUT)
                sleep(1)
                self.clickElement(banner, "%s BUTTON" % lang, similarity=0.8)
                break
            except FindFailed:
                continue
        wait(self.welcomeLogos[lang], WAIT_TIMEOUT)
        self.assertExists(self.welcomeLogos[lang], "%s WELCOME LOGO" % lang)

    def verifyWelcomeLogo(self, lang):
        self.assertExists(self.welcomeLogos[lang], "%s WELCOME LOGO" % lang)

    def switchArrow(self, direction):
        if direction == "right":
            self.assertExists(
                "arrow_to_the_right_button.png", "ARROW TO THE RIGHT EXIST"
            )
            self.clickElement("arrow_to_the_right_button.png", "ARROW TO THE RIGHT")
        elif direction == "left":
            self.assertExists("arrow_to_the_left_button.png", "ARROW TO THE LEFT EXIST")
            self.clickElement("arrow_to_the_left_button.png", "ARROW TO THE LEFT")

    def cancelAndVerify(self):
        self.clickElement("CANCEL_button.png", "CANCEL BUTTON CLICKED")
        self.assertExists("EN_welcome_logo_text.png", "EN WELCOME LOGO EXIST")
