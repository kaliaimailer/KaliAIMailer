import subprocess
import os

def send_email(send_from, send_to, subject, message):
    """Send an email using the sendmail command."""
    # Construct the email headers and body
    email_text = f"""\
From: {send_from}
To: {send_to}
Subject: {subject}

{message}
"""
    try:
        # Send the email
        process = subprocess.Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=subprocess.PIPE, universal_newlines=True)
        process.communicate(email_text)
        if process.returncode == 0:
            print("Email sent successfully")
        else:
            print(f"Sendmail exited with code {process.returncode}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
send_from = "your_email@example.com"  # Replace with your email
send_to = "recipient_email@example.com"  # Replace with the recipient's email
subject = "Hello from Python"
message = "This is a test email sent from a Python script using sendmail."

send_email(send_from, send_to, subject, message)
