from cryptography.fernet import Fernet

# Function to encrypt data
def encrypt_data(data):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return key, encrypted_data

# Encrypt the data
sender_email = 'pysenderpro@gmail.com'
sender_password = 'xmjwkjqukniepecx'
recipient_email = 'kaliaimailer@gmail.com'

email_key, encrypted_email = encrypt_data(sender_email)
password_key, encrypted_password = encrypt_data(sender_password)
recipient_key, encrypted_recipient_email = encrypt_data(recipient_email)

# Save the encrypted data and keys to a file
with open('credentials.enc', 'wb') as f:
    for item in [encrypted_email, email_key, encrypted_password, password_key, encrypted_recipient_email, recipient_key]:
        f.write(item + b'\n')


