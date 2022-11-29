import sys

from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QApplication, QComboBox, QPushButton, QTableWidget

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


class MenagerForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Менеджер')
        self.setStyleSheet("background-color: plum;")


class AssistantForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Кассир')
        self.setStyleSheet("background-color: plum;")


class VisitorForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: plum;")
        self.con = sqlite3.connect("films_db.sqlite")
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Посетитель')

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(10, 10, 150, 40)
        self.comboBox.addItem('комедия')
        self.comboBox.addItem('драма')
        self.comboBox.addItem('мелодрама')
        self.comboBox.addItem('детектив')
        self.comboBox.addItem('документальный')
        self.comboBox.addItem('ужасы')
        self.comboBox.addItem('музыка')
        self.comboBox.addItem('фантастика')
        self.comboBox.addItem('анимация')
        self.comboBox.addItem('биография')
        self.comboBox.addItem('боевик')
        self.comboBox.addItem('приключения')
        self.comboBox.addItem('война')
        self.comboBox.addItem('семейный')
        self.comboBox.addItem('триллер')
        self.comboBox.addItem('фэнтези')
        self.comboBox.addItem('вестерн')
        self.comboBox.addItem('мистика')
        self.comboBox.addItem('короткометражный')
        self.comboBox.addItem('мюзикл')
        self.comboBox.addItem('исторический')
        self.comboBox.addItem('нуар')

        self.pushButton = QPushButton('Показать', self)
        self.pushButton.setGeometry(80, 100, 80, 40)
        self.pushButton.clicked.connect(self.run)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(180, 10, 400, 400)

    def run(self):
        cur = self.con.cursor()
        result = cur.execute('''SELECT * FROM films WHERE genre=(SELECT id FROM genres WHERE title = {})''', (
            str(self.comboBox.currentText()))).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


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
