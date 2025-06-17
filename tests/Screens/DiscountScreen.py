from Config.Constants import WAIT_TIMEOUT
from Screens.BasePage import BasePage
from sikuli import waitVanish, wait, sleep


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
        btn = self.osFile("send_text_input_text.png")
        self.clickElement(btn, "TEXT INPUT FIELD")

    def prepareDiscountDialog(self):
        self.openDiscountDialog()
        self.waitAndClickDiscountInputField()

    def submitAndCloseDiscountDialog(self):
        btn = self.osFile("send_text_input_button.png")
        self.clickElement(btn, "SEND TEXT INPUT BUTTON")
        sleep(3)
        self.clickElement("OK_button.png", "OK BUTTON")
        waitVanish("enter_discount_code_text_in_modal.png")

    def verifyDiscountToast(self):
        self.assertExists("discount_code_accepted_toast.png", "DISCOUNT ACCEPTED TOAST")
        waitVanish("discount_code_accepted_toast.png")
