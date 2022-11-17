import sys

from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QLabel, QLineEdit, QPlainTextEdit
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle('Перемешивание')
        self.btn = QPushButton('Загрузить строки', self)
        self.btn.move(20, 10)
        self.btn.clicked.connect(self.run)
        self.name_input = QLineEdit(self)
        self.name_input.move(20, 60)
        self.name_input.resize(360, 400)


    def run(self):
        self.name_input.setPlainText('')
        answer = []
        result
        with open('lines.txt') as file:
            for elem in file:
                answer.append(elem)
            for i in range(1, len(answer) + 1, 2):
                result.append(answer[i] + "\n")
            for i in range(0, len(answer), 2):
                result.append(answer[i] + "\n")
            self.name_input.setText(*result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())