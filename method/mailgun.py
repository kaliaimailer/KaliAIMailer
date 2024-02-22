from mailgun import Mailgun

mg = Mailgun('your_mailgun_domain', 'your_mailgun_api_key')
mg.send_message(from_email='from@example.com', to_emails=['to@example.com'],
                subject='Hello', text='Sending with Mailgun is easy!')

