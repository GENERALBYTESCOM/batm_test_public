from Utils import (
    WAIT_TIMEOUT,
    assertClick,
    assertExists,
    checkMainScreenAndClickLogo
)

from sikuli import wait, Pattern


def choose_language_button():
    assertExists("choose_language_button.png", "CHOOSE LANGUAGE SCREEN")
    assertClick("choose_language_button.png", "CHOOSE LANGUAGE BUTTON")


def select_language(banner_image, banner_label, welcome_logo, similarity=0.90):
    wait(banner_image, WAIT_TIMEOUT)
    pattern = Pattern(banner_image).similar(similarity)
    assertExists(pattern, banner_label)
    assertClick(pattern, banner_label)
    assertExists(welcome_logo, "%s WELCOME LOGO" % banner_label)


def click_arrow_right():
    assertExists("arrow_to_the_right_button.png", "ARROW TO THE RIGHT")
    assertClick("arrow_to_the_right_button.png", "ARROW TO THE RIGHT")


def click_arrow_left():
    assertExists("arrow_to_the_left_button.png", "ARROW TO THE LEFT")
    assertClick("arrow_to_the_left_button.png", "ARROW TO THE LEFT")


def cancel_and_verify():
    assertExists("CANCEL_button.png", "CANCEL BUTTON")
    assertClick("CANCEL_button.png", "CANCEL BUTTON")
    assertExists("EN_welcome_logo_text.png", "EN WELCOME LOGO")


checkMainScreenAndClickLogo()
assertExists("EN_welcome_logo_text.png", "EN WELCOME LOGO")
choose_language_button()
click_arrow_right()
wait("arrow_to_the_left_button.png", WAIT_TIMEOUT)
click_arrow_left()
select_language("CZ_banner.png", "CZ BUTTON", "CZ_welcome_logo_text.png", 0.90)
choose_language_button()
select_language("ES_banner.png", "ES BUTTON", "ES_welcome_logo_text.png", 0.90)
select_language("DE_banner.png", "DE BUTTON", "DE_welcome_logo_text.png", 0.90)
choose_language_button()
select_language("EN_banner.png", "EN BUTTON", "EN_welcome_logo_text.png", 0.90)
choose_language_button()
cancel_and_verify()
