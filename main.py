import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.uic import loadUi
from PyQt5 import QtCore

class LoginUi(QMainWindow):
    def __init__(self):
        super(LoginUi, self).__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "LoginForm.ui")
        loadUi(ui_path, self)  # Use absolute path to ensure the UI file is found

        # Make the window frameless and transparent
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Connect the Exit button to the close function
        self.ExitButton.clicked.connect(self.close)

        # Enable dragging
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = LoginUi()
    ui.show()
    app.exec_()
