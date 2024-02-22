import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(smtp_host, smtp_port, username, password, from_addr, to_addr, subject, body):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Setup the SMTP server connection
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()  # Upgrade the connection to secure
        server.login(username, password)
        
        # Send the email
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Example usage
if __name__ == "__main__":
    smtp_host = 'your.smtp.server.com'  # Specify your SMTP server
    smtp_port = 587  # Specify your SMTP server's port (commonly 587 for TLS)
    username = 'your_username'
    password = 'your_password'
    from_addr = 'your_email@example.com'
    to_addr = 'recipient_email@example.com'
    subject = 'Test Email from Python'
    body = 'Hello, this is a test email sent from a Python script in VS Code.'

    send_email(smtp_host, smtp_port, username, password, from_addr, to_addr, subject, body)
