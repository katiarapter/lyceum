import sys

from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.fl = 0
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Генерация флага')
        self.btn = QPushButton('Выбирите количество цветов', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.run)

    def run(self):
        age, ok_pressed = QInputDialog.getInt(
            self, "Цвет", "Сколько цветов?",
            8, 1, 10, 1)
        self.age = age
        self.fl = 1

    def paintEvent(self, event):
        if self.fl == 1:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        for i in range(1, self.age + 1):
            qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
            qp.drawRect(70, 40 + 30 * i, 120, 30)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())