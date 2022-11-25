import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('first.ui', self)
        self.pushButton.clicked.connect(self.menager)
        self.pushButton_2.clicked.connect(self.assistant)
        self.pushButton_3.clicked.connect(self.visitor)

        self.menager_form = MenagerForm(self, "Данные для второй формы")
        self.menager_form.setUpdatesEnabled(True)
        self.menager_form.hide()

        self.assistant_form = AssistantForm(self, "Данные для второй формы")
        self.assistant_form.setUpdatesEnabled(True)
        self.assistant_form.hide()

        self.visitor_form = VisitorForm(self, "Данные для второй формы")
        self.visitor_form.setUpdatesEnabled(True)
        self.visitor_form.hide()

    def menager(self):
        if self.menager_form.isHidden():
            self.menager_form.show()
        else:
            self.menager_form.hide()

    def assistant(self):
        if self.assistant_form.isHidden():
            self.assistant_form.show()
        else:
            self.assistant_form.hide()

    def visitor(self):
        if self.visitor_form.isHidden():
            self.visitor_form.show()
        else:
            self.visitor_form.hide()


class MenagerForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 300, 300)
        self.setWindowTitle('Вторая форма менаджера')


class AssistantForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 300, 300)
        self.setWindowTitle('Вторая форма кассира')


class VisitorForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(600, 300, 300, 300)
        self.setWindowTitle('Вторая форма посетителя')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
