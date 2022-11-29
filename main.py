import sys

from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QApplication, QComboBox, QPushButton, QTableWidget
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow

password = None


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('first.ui', self)
        self.pushButton.clicked.connect(self.visitor)
        self.pushButton_2.clicked.connect(self.menager)
        self.pushButton_3.clicked.connect(self.assistant)

        self.menager_form = MenagerForm()
        self.menager_form.setUpdatesEnabled(True)
        self.menager_form.hide()

        self.assistant_form = AssistantForm()
        self.assistant_form.setUpdatesEnabled(True)
        self.assistant_form.hide()

        self.visitor_form = VisitorForm()
        self.visitor_form.setUpdatesEnabled(True)
        self.visitor_form.hide()

    # self.password_form = PasswordForm()
    # self.password_form.setUpdatesEnabled(True)
    # self.password_form.hide()

    def menager(self):
        global password
        # self.password_form.show()
        if self.menager_form.isHidden():
            self.menager_form.show()
        else:
            self.menager_form.hide()

    def assistant(self):
        global password
        # self.password_form.show()
        if self.assistant_form.isHidden():
            self.assistant_form.show()
        else:
            self.assistant_form.hide()

    def visitor(self):
        if self.visitor_form.isHidden():
            self.visitor_form.show()
        else:
            self.visitor_form.hide()


class MenagerForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('visitor.ui', self)
        self.setStyleSheet("background-color: plum;")
        self.comboBox.activated[str].connect(self.run)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('films')
        self.model.select()
        self.tableView.setModel(self.model)

    def run(self, text):
        self.model.setFilter('genre=(SELECT id FROM genres WHERE title = "{}")'.format(text))
        self.model.select()
        self.tableView.setModel(self.model)


class AssistantForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('visitor.ui', self)
        self.setStyleSheet("background-color: plum;")
        self.comboBox.activated[str].connect(self.run)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('films')
        self.model.select()
        self.tableView.setModel(self.model)

    def run(self, text):
        self.model.setFilter('genre=(SELECT id FROM genres WHERE title = "{}")'.format(text))
        self.model.select()
        self.tableView.setModel(self.model)

class VisitorForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('visitor.ui', self)
        self.setStyleSheet("background-color: plum;")
        self.comboBox.activated[str].connect(self.run)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('films')
        self.model.select()
        self.tableView.setModel(self.model)

    def run(self, text):
        self.model.setFilter('genre=(SELECT id FROM genres WHERE title = "{}")'.format(text))
        self.model.select()
        self.tableView.setModel(self.model)


class PasswordForm(QWidget):
    def __init__(self):
        super().__init__()
        self.name_input = None
        self.name_label = None
        self.label = None
        self.btn = None
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 400, 400)
        self.setWindowTitle('Пароль')
        self.setStyleSheet("background-color: turquoise;")

        self.btn = QPushButton('Ввести', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText("Пожалуйста, введите пароль")
        self.label.move(40, 30)

        self.name_label = QLabel(self)
        self.name_label.setText("Пароль: ")
        self.name_label.move(40, 90)

        self.name_input = QLineEdit(self)
        self.name_input.move(150, 90)

    def hello(self):
        global password
        name = self.name_input.text()
        if name == 'qwertyuiop':
            password = True
            self.password_form.hide()
        else:
            password = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
