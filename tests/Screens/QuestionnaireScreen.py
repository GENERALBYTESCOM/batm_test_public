from Screens.BasePage import BasePage, WAIT_TIMEOUT

from sikuli import wait


class QuestionnaireScreen(BasePage):
    def questionnaireRadio(self):
        wait("questionnaire_radio_text.png", WAIT_TIMEOUT)
        self.assertExists("questionnaire_radio_text.png", "QUESTIONNAIRE SCREEN RADIO")
        self.assertExists("DONE_button.png", "DONE BUTTON")
        self.clickElement("DONE_button.png", "DONE BUTTON")
