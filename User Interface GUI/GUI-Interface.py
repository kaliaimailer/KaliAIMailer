import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

def create_window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(1200, 600)
    window.setWindowTitle('Kali AI Mailer')

    # Set the window icon
    icon = QIcon("C:/KaliAIMailer/User Interface GUI/kaliaimailer.ico")  
    window.setWindowIcon(icon)

    # Logo dimensions
    logo_width = 800  # Adjust the width as needed
    logo_height = 400  # Adjust the height as needed

    # Logo at the top
    logo_pixmap = QPixmap("C:/KaliAIMailer/User Interface GUI/Kaliaimailer-logo.jpg")  # Replace with the path to your logo image
    logo_pixmap = logo_pixmap.scaled(logo_width, logo_height, Qt.KeepAspectRatio)  # Scale the logo
    logo_label = QLabel(window)
    logo_label.setPixmap(logo_pixmap)
    logo_label.setAlignment(Qt.AlignCenter)
    logo_label.setGeometry(200, 20, logo_width, logo_height)  # Adjust the position and size of the logo

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    create_window()
