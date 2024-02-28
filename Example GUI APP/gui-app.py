# gui.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QMessageBox
from get_ip import get_host_ip
from host_info import get_host_name, get_system_info
from send_email import send_email

class InfoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.sender_email = "your_email@gmail.com"  # Change this
        self.sender_password = "your_app_password_or_password"  # Change this
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('System Information Display and Email Sender')
        self.setGeometry(100, 100, 400, 300)  # x, y, width, height
        
        layout = QVBoxLayout()
        
        # System Info
        layout.addWidget(QLabel(f'IP Address: {get_host_ip()}'))
        layout.addWidget(QLabel(f'Hostname: {get_host_name()}'))
        layout.addWidget(QLabel(f'System Info: {get_system_info()}'))
        
        # Email Form
        layout.addWidget(QLabel('Send Email:'))
        self.recipient_email = QLineEdit()
        self.recipient_email.setPlaceholderText('Recipient Email')
        layout.addWidget(self.recipient_email)
        
        self.subject = QLineEdit()
        self.subject.setPlaceholderText('Subject')
        layout.addWidget(self.subject)
        
        self.message = QTextEdit()
        self.message.setPlaceholderText('Message')
        layout.addWidget(self.message)
        
        send_button = QPushButton('Send Email')
        send_button.clicked.connect(self.on_send_email)
        layout.addWidget(send_button)
        
        self.setLayout(layout)
        self.show()
    
    def on_send_email(self):
        if send_email(self.sender_email, self.sender_password, self.recipient_email.text(), self.subject.text(), self.message.toPlainText()):
            QMessageBox.information(self, 'Success', 'Email sent successfully!')
        else:
            QMessageBox.critical(self, 'Failure', 'Failed to send email.')

def main():
    app = QApplication(sys.argv)
    ex = InfoWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
