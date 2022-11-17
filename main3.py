import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLCDNumber
from PyQt5.QtWidgets import QLabel, QLineEdit, QCheckBox, QPlainTextEdit
from random import randrange


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Ним наносит ответный удар')

        self.btn = QPushButton('+' + str(randrange(100)), self)
        self.btn.move(50, 70)
        self.btn.resize(150, 30)
        self.btn.clicked.connect(self.clicked)

        self.btn1 = QPushButton(str(-randrange(100)), self)
        self.btn1.move(210, 70)
        self.btn1.resize(150, 30)
        self.btn1.clicked.connect(self.clicked)

        self.label = QLabel('Осталось ходов', self)
        self.label1 = QLabel('Текущее число', self)
        self.label3 = QLabel(self)
        self.monic = QLCDNumber(self)
        self.monic1 = QLCDNumber(self)




        self.label.move(20, 110)
        self.label.resize(100, 30)

        self.label1.move(20, 150)
        self.label1.resize(100, 30)

        self.label3.move(20, 10)
        self.label3.resize(300, 30)

        self.monic.display(10)
        self.monic.move(250, 110)
        self.monic.resize(100, 30)

        self.monic1.display(randrange(100))
        self.monic1.move(250, 150)
        self.monic1.resize(100, 30)

    def clicked(self):
        self.label3.setText('')
        self.monic.display(self.monic.value() - 1)
        self.monic1.display(self.monic1.value() + int(self.sender().text()))
        if self.monic1.value() == 0:
            self.label3.setText('Вы победили, начинаем новую игру')
            self.btn.setText(('+' + str(randrange(100))))
            self.btn1.setText((str(-randrange(100))))
            self.monic1.display(randrange(100))
            self.monic.display(10)
        if self.monic.value() == 0:
            if self.monic1.value() != 0:
                self.label3.setText('Вы проиграли, начинаем новую игру')
                self.btn.setText(('+' + str(randrange(100))))
                self.btn1.setText((str(-randrange(100))))
                self.monic1.display(randrange(100))
                self.monic.display(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstForm()
    ex.show()
    sys.exit(app.exec())