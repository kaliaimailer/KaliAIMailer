import sendgrid
from sendgrid.helpers.mail import Mail

sg = sendgrid.SendGridAPIClient('your_sendgrid_api_key')
email = Mail(from_email='from@example.com', to_emails='to@example.com',
             subject='Sending with SendGrid is Fun',
             plain_text_content='and easy to do anywhere, even with Python')

response = sg.send(email)
print(response.status_code)
