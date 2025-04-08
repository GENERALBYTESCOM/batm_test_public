from Config.Constants import WAIT_TIMEOUT
from Screens.BasePage import BasePage
from sikuli import wait


class NumberScreen(BasePage):
    def enterNumber(self):
        self.clickElement("1_button.png", "1 BUTTON")
        wait("1_appear.png", WAIT_TIMEOUT)
        self.clickElement("2_button.png", "2 BUTTON")
        wait("12_appear.png", WAIT_TIMEOUT)
        self.clickElement("3_button.png", "3 BUTTON")
        wait("123_appear.png", WAIT_TIMEOUT)
        self.clickElement("4_button.png", "4 BUTTON")
        wait("1234_appear.png", WAIT_TIMEOUT)
        self.clickElement("5_button.png", "5 BUTTON")
        wait("12345_appear.png", WAIT_TIMEOUT)
        self.clickElement("OK_button.png", "OK BUTTON")

    def assertPhoneNumberTextIsDisplayed(self):
        wait("phone_number_text.png", WAIT_TIMEOUT)
        self.assertExists("phone_number_text.png", "PHONE NUMBER TEXT EXIST")

    def assertOTPTextIsDisplayed(self):
        wait("one_time_password_text.png", WAIT_TIMEOUT)
        self.assertExists("one_time_password_text.png", "ONE TIME PASSWORD TEXT EXIST")
