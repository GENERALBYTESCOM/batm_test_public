from Config.Constants import WAIT_TIMEOUT
from Screens.BasePage import BasePage
from sikuli import waitVanish, wait, sleep, exists


class DiscountScreen(BasePage):
    def openDiscountDialog(self):
        self.assertExists("discount_code_button.png", "DISCOUNT BUTTON EXIST")
        self.clickElement("discount_code_button.png", "DISCOUNT BUTTON")
        wait("enter_discount_code_text_in_modal.png", WAIT_TIMEOUT)
        self.assertExists(
            "enter_discount_code_text_in_modal.png", "ENTER DISCOUNT CODE DIALOGUE"
        )

    def waitAndClickDiscountInputField(self):
        wait("enter_discount_code_text_in_modal.png", WAIT_TIMEOUT)
        if exists("send_text_input_text_win.png", WAIT_TIMEOUT):
            self.clickElement("send_text_input_text_win.png", "TEXT INPUT FIELD")
        elif exists("send_text_input_text.png", WAIT_TIMEOUT):
            self.clickElement("send_text_input_text.png", "TEXT INPUT FIELD")

    def prepareDiscountDialog(self):
        self.openDiscountDialog()
        self.waitAndClickDiscountInputField()

    def submitAndCloseDiscountDialog(self):
        if exists("send_text_input_button_win.png", WAIT_TIMEOUT):
            self.clickElement("send_text_input_button_win.png", "SEND TEXT INPUT BUTTON")
        elif exists("send_text_input_button.png", WAIT_TIMEOUT):
            self.clickElement("send_text_input_button.png", "SEND TEXT INPUT BUTTON")
        sleep(3)
        self.clickElement("OK_button.png", "OK BUTTON")
        waitVanish("enter_discount_code_text_in_modal.png")

    def verifyDiscountToast(self):
        self.assertExists("discount_code_accepted_toast.png", "DISCOUNT ACCEPTED TOAST")
        waitVanish("discount_code_accepted_toast.png")
