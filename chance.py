import sys
import random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.coords = [40, 40]
        self.btn_size = [120, 40]
        self.d = 15
        self.w = 500
        self.h = 400
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, self.w, self.h)
        self.setWindowTitle('Убегающая кнопка')

        self.btn = QPushButton(self)
        self.btn.setText("Нажми меня")
        self.btn.resize(*self.btn_size)
        self.btn.move(*self.coords)
        self.show()

    def mouseMoveEvent(self, event):
        self.coords[0] = random.randint(0, self.w - self.btn_size[0])
        self.coords[1] = random.randint(0, self.h - self.btn_size[1])
        self.btn.move(*self.coords)
        self.coor


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())