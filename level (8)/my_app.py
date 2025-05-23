# write here a code for the main app and the first screen
from second_win import MainWin
from final_win import EndWin
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
import instr 

class App:
    def __init__(self) -> None:        
        self.app = QApplication([])
        self.first_win = QWidget()
        self.second_win = MainWin(self)
        self.third_win = EndWin(self)

        self.first_win.setWindowTitle('Ruffier Test')
        self.first_win.resize(1000, 600)
        self.first_win.move(200, 100)
        self.first_win.show()

        self.result = ''

        layout = QVBoxLayout(self.first_win)
        text = QLabel(instr.txt_hello)
        layout.addWidget(text, alignment=Qt.AlignCenter)
        button_next = QPushButton(instr.txt_next)        
        layout.addWidget(button_next, alignment=Qt.AlignCenter) 
        self.first_win.setLayout(layout)


        def hide_first_win():
            self.first_win.hide()
            self.second_win.show()

        button_next.clicked.connect(hide_first_win)
           
        self.app.exec_()

    def control_results(self, name, age, test1, test2, test3):
        if age != '0' and test1 != '0' and test2 != '0' and test3 != '0':
           #kalkulacie
            ri = ((4*(int(test1) + int(test2) + int(test3)))-200)/10

            if int(age) >= 15:
                if ri >= 15: self.result = 'hrozna srdcova funkcia'
                elif ri >= 11: self.result = 'ne gut srdcova funkcia'
                elif ri >= 6: self.result = 'gut srdcova funkcia'
                elif ri >= 0.5: self.result = 'velmi gut srdcova funkcia'
                elif ri == 0: self.result = 'super srdcova funkcia'
                else: 'bad input woodhead'
                self.third_win.show(self.result)

            else:
                print('too zoung')  
                self.first_win.show()          
        else:
            print('not good')
            self.second_win.show()
            self.third_win.hide()
            
        

if __name__ == '__main__':
    app = App()
    app.run()