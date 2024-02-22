import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, password):
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Create server object with SSL option
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print("Successfully sent email")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example usage
send_email(
    subject="Hello from Python",
    message="This is a test email sent from a Python script.",
    from_addr="your_email@gmail.com",
    to_addr="recipient_email@gmail.com",
    password="your_password"
)
