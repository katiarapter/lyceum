import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('first.ui', self)
        self.pushButton.clicked.connect(self.menager)
        self.pushButton_2.clicked.connect(self.assistant)
        self.pushButton_3.clicked.connect(self.visitor)

    def menager(self):
        pass

    def assistant(self):
        pass

    def visitor(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
