# reporting/reporting_to_admin.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    sender_email = "your_email@example.com"
    receiver_email = "admin_email@example.com"
    password = "your_password"  # Use a secure method for handling passwords

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email successfully sent to admin.")
    except Exception as e:
        print(f"Failed to send email: {e}")
