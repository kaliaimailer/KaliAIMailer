# In your connector.py
from data_module import DataModule
from mailer_module import MailerModule
from feedback_module import FeedbackModule

class Connector:
    def __init__(self):
        self.data_module = DataModule()
        self.mailer_module = MailerModule()
        self.feedback_module = FeedbackModule()

    def get_data(self, data_type):
        if data_type == 'email':
            return self.data_module.get_emails()
        elif data_type == 'address':
            return self.data_module.get_addresses()

    def send_email(self, email_content):
        self.mailer_module.send_email(email_content)

    def collect_feedback(self):
        return self.feedback_module.collect_feedback()
