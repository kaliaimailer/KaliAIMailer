import pandas as pd
import imaplib
import email
from email.header import decode_header

# Load email and password from CSV
credentials = pd.read_csv('C:/KaliAIMailer/Self_Checker/credentials.csv')
email_user = credentials['email'][0]
email_pass = credentials['your_password'][0]

# Connect to the email server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_user, email_pass)

# Select the inbox
mail.select('inbox')

# Search for all emails
result, data = mail.search(None, 'ALL')
mail_ids = data[0]

id_list = mail_ids.split()

# Get the latest 10 emails
latest_ten_emails = id_list[-10:]

for i in latest_ten_emails:
    result, data = mail.fetch(i, '(RFC822)')
    
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            # Decode email subject
            subject, encoding = decode_header(msg['Subject'])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or 'utf-8')
            print(f'Subject: {subject}')

mail.logout()
