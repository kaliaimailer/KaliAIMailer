# In your brain.py
from connector import Connector

class Brain:
    def __init__(self):
        self.connector = Connector()

    def process(self):
        # Use the connector to interact with modules
        emails = self.connector.get_data('email')
        for email in emails:
            self.connector.send_email(email)
        feedback = self.connector.collect_feedback()
        # Process feedback