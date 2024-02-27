import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to read SMTP settings
def read_smtp_settings(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row  # Assuming only one row

# Function to read contact details
def read_contacts(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Function to send email
def send_email(smtp_info, contacts, subject, html_content):
    server = smtplib.SMTP(smtp_info['smtp_server'], smtp_info['smtp_port'])
    server.starttls()
    server.login(smtp_info['email'], smtp_info['password'])
    
    for contact in contacts:
        msg = MIMEMultipart()
        msg['From'] = smtp_info['email']
        msg['To'] = contact['email']
        msg['Subject'] = subject
        
        msg.attach(MIMEText(html_content, 'html'))
        
        server.send_message(msg)
    
    server.quit()
    print("Emails sent successfully.")

# HTML content of your email
html_content = """
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.google.com">Visit our website</a>.
    </p>
  </body>
</html>
"""

smtp_info = read_smtp_settings('C:/KaliAIMailer/data/smtp.csv')
contacts = read_contacts('C:/KaliAIMailer/data/contact.csv')
subject = "Hello from Python"

send_email(smtp_info, contacts, subject, html_content)
