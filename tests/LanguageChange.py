from Utils import WAIT_TIMEOUT, assertClick, assertExists, checkMainScreenAndClickLogo

from sikuli import wait, Pattern


def chooseLanguageButton():
    assertExists("choose_language_button.png", "CHOOSE LANGUAGE SCREEN")
    assertClick("choose_language_button.png", "CHOOSE LANGUAGE BUTTON")


def selectLanguage(bannerImage, bannerLabel, welcomeLogo, similarity=0.90):
    wait(bannerImage, WAIT_TIMEOUT)
    pattern = Pattern(bannerImage).similar(similarity)
    assertExists(pattern, bannerLabel)
    assertClick(pattern, bannerLabel)
    assertExists(welcomeLogo, "%s WELCOME LOGO" % bannerLabel)


def clickArrowRight():
    assertExists("arrow_to_the_right_button.png", "ARROW TO THE RIGHT")
    assertClick("arrow_to_the_right_button.png", "ARROW TO THE RIGHT")


def clickArrowLeft():
    assertExists("arrow_to_the_left_button.png", "ARROW TO THE LEFT")
    assertClick("arrow_to_the_left_button.png", "ARROW TO THE LEFT")


def cancelAndVerify():
    assertExists("CANCEL_button.png", "CANCEL BUTTON")
    assertClick("CANCEL_button.png", "CANCEL BUTTON")
    assertExists("EN_welcome_logo_text.png", "EN WELCOME LOGO")


checkMainScreenAndClickLogo()
assertExists("EN_welcome_logo_text.png", "EN WELCOME LOGO")
chooseLanguageButton()
clickArrowRight()
wait("arrow_to_the_left_button.png", WAIT_TIMEOUT)
clickArrowLeft()
selectLanguage("CZ_banner.png", "CZ BUTTON", "CZ_welcome_logo_text.png", 0.90)
chooseLanguageButton()
selectLanguage("ES_banner.png", "ES BUTTON", "ES_welcome_logo_text.png", 0.90)
selectLanguage("DE_banner.png", "DE BUTTON", "DE_welcome_logo_text.png", 0.90)
chooseLanguageButton()
selectLanguage("EN_banner.png", "EN BUTTON", "EN_welcome_logo_text.png", 0.90)
chooseLanguageButton()
cancelAndVerify()
