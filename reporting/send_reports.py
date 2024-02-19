from cryptography.fernet import Fernet
import smtplib
from email.message import EmailMessage
import os
from collect_all_reports import collect_reports

# Function to decrypt data
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()

# Decrypt credentials and prepare for email sending
def prepare_and_send_email():
    # Read encrypted data and keys from the file
    with open('credentials.enc', 'rb') as f:
        lines = f.readlines()
        encrypted_email, email_key = lines[0].strip(), lines[1].strip()
        encrypted_password, password_key = lines[2].strip(), lines[3].strip()
        encrypted_recipient_email, recipient_key = lines[4].strip(), lines[5].strip()

    # Decrypt the credentials
    sender_email = decrypt_data(email_key, encrypted_email)
    sender_password = decrypt_data(password_key, encrypted_password)
    recipient_email = decrypt_data(recipient_key, encrypted_recipient_email)

    # Call send_email with the decrypted credentials
    send_email(
        "Daily Report with Multiple Files",
        "Please find the attached daily report, including screenshots and logs.",
        collect_reports(),  # This needs to collect and return a list of file paths
        recipient_email,
        sender_email,
        sender_password
    )

    # Cleanup: Remove the report files if no longer needed
    for file in collect_reports():
        os.remove(file)

def send_email(subject, body, attachment_filenames, recipient_email, sender_email, sender_password):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(body)

    # Attach specified files
    for filename in attachment_filenames:
        with open(filename, 'rb') as f:
            file_data = f.read()
            filename = os.path.basename(filename)
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=filename)

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    print("Email sent successfully.")

# Assuming collect_reports is defined in collect_all_reports.py and correctly imports take_screenshot from ScreenshotModule.py
if __name__ == "__main__":
    prepare_and_send_email()
