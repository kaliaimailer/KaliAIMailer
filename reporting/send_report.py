from cryptography.fernet import Fernet
import smtplib
from email.message import EmailMessage
import os

# Function to decrypt data
def decrypt_data(key, encrypted_data):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()

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
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=os.path.basename(filename))

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

    print("Email sent successfully.")

# Example usage
if __name__ == "__main__":

    from collect_all_reports import collect_reports
    report_files = collect_reports()  # This now includes multiple reports
    subject = "Daily Report with Multiple Files"
    body = "Please find the attached daily report, including screenshots and logs."

    send_email(subject, body, report_files, recipient_email, sender_email, sender_password)

    # Cleanup: Remove the report files if no longer needed
    for file in report_files:
        os.remove(file)

