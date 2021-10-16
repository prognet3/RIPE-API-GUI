from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton, QHBoxLayout
import sys
from PyQt5.QtGui import *
from RPKI import ResultForGUI


class Automation(QWidget):
    def __init__(self):
        super().__init__()
        self.api_result = ResultForGUI()

        self.setWindowTitle("Automation")
        # self.resize(700, 700)
        self.setStyleSheet("background-color: #808b96 ")
        self.setGeometry(450, 100, 400, 600)
        self.setWindowIcon(QIcon("automation.jpg"))

        self.btn1 = QPushButton("Announced Prefixes")
        self.btn1.setStyleSheet("background-color :   #58D68D ")
        self.btn1.setFont(QFont('Times', 12))
        self.btn2 = QPushButton("RPKI")
        self.btn2.setStyleSheet("background-color :   #FFC300 ")
        self.btn2.setFont(QFont('Times', 12))
        self.btn3 = QPushButton("Clear")
        self.btn3.setStyleSheet("background-color :   #F1948A ")
        self.btn3.setFont(QFont('Times', 12))
        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet("background: #f4f6f7")
        layout = QHBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout1 = QVBoxLayout()
        layout1.addLayout(layout)
        layout1.addWidget(self.textEdit)
        self.setLayout(layout1)
        self.btn1.clicked.connect(self.announced_prefixes_ripe)
        self.btn2.clicked.connect(self.rpki_ripe)
        self.btn3.clicked.connect(self.clear)

    def announced_prefixes_ripe(self):
        finalll = self.api_result.announced()
        for i in finalll:
            self.textEdit.append(i)

    def rpki_ripe(self):
        finalllttt = self.api_result.rpki()
        for i in finalllttt:
            self.textEdit.append(i)

    def clear(self):
        self.textEdit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Automation()
    win.show()
    sys.exit(app.exec_())
