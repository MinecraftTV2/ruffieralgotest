# write a code for the second app
from calendar import c
import instr
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

class MainWin:
    def __init__(self, app):
        self.app = app

        self.main_win = QWidget()
        self.main_win.setWindowTitle('Ruffier Test')
        self.main_win.resize(1000, 600)
        self.main_win.move(200, 100)

        self.layout = QVBoxLayout()
        
        self.textname = QLabel(instr.txt_name)
        self.layout.addWidget(self.textname, alignment=Qt.AlignCenter)
        self.editline1 = QLineEdit('Full name') #name
        self.layout.addWidget(self.editline1, alignment=Qt.AlignCenter)
        self.textage = QLabel('age')
        self.layout.addWidget(self.textage, alignment=Qt.AlignCenter)
        self.editline2 = QLineEdit('0') #age
        self.layout.addWidget(self.editline2, alignment=Qt.AlignCenter)
        self.text1 = QLabel(instr.txt_test1)
        self.layout.addWidget(self.text1, alignment=Qt.AlignCenter)
        self.button1 = QPushButton(instr.txt_starttest1)
        self.layout.addWidget(self.button1, alignment=Qt.AlignCenter)
        self.editline3 = QLineEdit('0') #1st reading
        self.layout.addWidget(self.editline3, alignment=Qt.AlignCenter)
        self.text2 = QLabel(instr.txt_test2)
        self.layout.addWidget(self.text2, alignment=Qt.AlignCenter)
        self.button2 = QPushButton(instr.txt_starttest2)
        self.layout.addWidget(self.button2, alignment=Qt.AlignCenter)
        self.editline4 = QLineEdit('0') #2nd reading
        self.layout.addWidget(self.editline4, alignment=Qt.AlignCenter)
        self.text3 = QLabel(instr.txt_test3)
        self.layout.addWidget(self.text3, alignment=Qt.AlignCenter)
        self.button3 = QPushButton(instr.txt_starttest3)
        self.layout.addWidget(self.button3, alignment=Qt.AlignCenter)
        self.editline5 = QLineEdit('0') # 3rd reading
        self.layout.addWidget(self.editline5, alignment=Qt.AlignCenter)
        self.button4 = QPushButton(instr.txt_sendresults)
        self.layout.addWidget(self.button4, alignment=Qt.AlignCenter)

        def controlres():
            self.app.control_results(self.editline1.text(), self.editline2.text(), self.editline3.text(), self.editline4.text(), self.editline5.text())
            self.main_win.hide()

        self.button4.clicked.connect(controlres)

        self.main_win.hide()
        self.main_win.setLayout(self.layout)

    def show(self):
        self.main_win.show()