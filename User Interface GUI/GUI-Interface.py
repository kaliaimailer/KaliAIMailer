import sys
from PyQt5.QtWidgets import QApplication, QWidget

def create_window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(1200, 600)
    window.setWindowTitle('Kali AI Mailer')
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    create_window()
