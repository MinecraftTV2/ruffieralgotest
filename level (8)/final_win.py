from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

class EndWin: 
    def __init__(self, app):
        self.app = app

        self.win = QWidget()
        self.win.setWindowTitle('Ruffier Test')
        self.win.resize(1000, 600)
        self.win.move(200, 100)

        self.layout = QVBoxLayout()
        self.text = QLabel('')
        self.layout.addWidget(self.text, alignment=Qt.AlignCenter)

        self.win.hide()
        self.win.setLayout(self.layout)

    def show(self, result):
        result = 'congrats: ' + result
        self.text.setText(result)
        self.win.show()