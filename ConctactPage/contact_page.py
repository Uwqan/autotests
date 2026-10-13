from selenium.webdriver.common.by import By
from base_page import BasePage


class ContactPage(BasePage):
    NAME_INPUT      = (By.ID, "name")
    EMAIL_INPUT     = (By.ID, "email")
    SUBJECT_INPUT   = (By.ID, "subject")
    MESSAGE_INPUT   = (By.ID, "message")
    SUBMIT_BUTTON   = (By.ID, "submit-btn")

    NAME_ERROR      = (By.ID, "name-error")
    EMAIL_ERROR     = (By.ID, "email-error")
    SUBJECT_ERROR   = (By.ID, "subject-error")
    MESSAGE_ERROR   = (By.ID, "message-error")
    SUCCESS_MESSAGE = (By.ID, "success")

    def open_page(self):
        self.open("/")
        return self

    def fill_name(self, name):
        return self.type(*self.NAME_INPUT, name)

    def fill_email(self, email):
        return self.type(*self.EMAIL_INPUT, email)

    def fill_subject(self, subject):
        return self.type(*self.SUBJECT_INPUT, subject)

    def fill_message(self, message):
        return self.type(*self.MESSAGE_INPUT, message)

    def fill_form(self, name, email, subject, message):
        self.fill_name(name)
        self.fill_email(email)
        self.fill_subject(subject)
        self.fill_message(message)
        return self

    def submit(self):
        self.click(*self.SUBMIT_BUTTON)
        return self

    def get_success_text(self):
        return self.get_text(*self.SUCCESS_MESSAGE)

    def get_name_error(self):
        return self.get_text(*self.NAME_ERROR)

    def is_success_visible(self):
        return self.is_visible(*self.SUCCESS_MESSAGE)