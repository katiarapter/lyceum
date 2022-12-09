import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QComboBox, QTableWidget
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


password = False
password_a = False


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('first.ui', self)
        self.setWindowTitle('Кинотеатр')
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

        self.password_form_m = PasswordFormM()
        self.password_form_m.setUpdatesEnabled(True)
        self.password_form_m.hide()

        self.password_form_a = PasswordFormA()
        self.password_form_a.setUpdatesEnabled(True)
        self.password_form_a.hide()

    def menager(self):
        global password
        self.password_form_m.show()
        if password is True:
            self.password_form_m.hide()
            password = False
            self.menager_form.show()

    def assistant(self):
        global password_a
        self.password_form_a.show()
        if password_a is True:
            self.password_form_a.hide()
            password_a = False
            self.assistant_form.show()

    def visitor(self):
        if self.visitor_form.isHidden():
            self.visitor_form.show()
        else:
            self.visitor_form.hide()


class MenagerForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menager.ui', self)
        self.setWindowTitle('Менеджер')
        self.comboBox.activated[str].connect(self.genre)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton.clicked.connect(self.add)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('films')
        self.model.select()
        self.tableView.setModel(self.model)

    def genre(self, text):
        self.model.setFilter('genre=(SELECT id FROM genres WHERE title = "{}")'.format(text))
        self.model.select()
        self.tableView.setModel(self.model)

    def delete(self):
        name = self.lineEdit_2.text()
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        # res = cur.execute("""DELETE FROM films WHERE title = ? """, (name, )).fetchall()
        cur.close()
        # con.commit()
        # здесь появляется ошибка loked db
        con.close()

    def add(self):
        name = self.lineEdit_2.text()
        amount = self.lineEdit.text()
        genre = self.lineEdit_3.text()
        duration = self.lineEdit_4.text()
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        # res = cur.execute("""INSERT INTO films VALUES (?, ?, ?, ?, ?) """,
        # (0, name, amount, genre, duration)).fetchall()
        cur.close()
        # con.commit()
        # здесь появляется ошибка loked db
        con.close()


class AssistantForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('assistant.ui', self)
        self.setWindowTitle('Кассир')
        self.label_9.hide()
        self.pushButton.clicked.connect(self.sell)

        self.comboBox.activated[str].connect(self.genre)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('films')
        self.model.select()
        self.tableView.setModel(self.model)

    def genre(self, text):
        self.model.setFilter('genre=(SELECT id FROM genres WHERE title = "{}")'.format(text))
        self.model.select()
        self.tableView.setModel(self.model)

    def sell(self):
        valid = QMessageBox.question(
            self, '', "Действительно продать билеты?",
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            amount = self.lineEdit.text()
            name = self.lineEdit_2.text()
            con = sqlite3.connect('films_db.sqlite')
            cur = con.cursor()
            # res = cur.execute("""UPDATE films SET tickets=? WHERE title = ? """, (amount, name)).fetchall()
            count = cur.execute("""SELECT tickets FROM films WHERE title = ? """, (name, )).fetchall()
            cur.close()
            # con.commit()
            # здесь появляется ошибка loked db
            con.close()
            print(f'prodano {amount} from {name}')
            print(f'ostalos {int(count[0][0]) - int(amount)} byletov')
            print(f'Измените пожауйста в таблице значение на {int(count[0][0]) - int(amount)}')
            self.label_9.show()


class VisitorForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('visitor.ui', self)
        self.setWindowTitle('Покупатель')
        self.comboBox.activated[str].connect(self.genre)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('films_db.sqlite')
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('films')
        self.model.select()
        self.tableView.setModel(self.model)

    def genre(self, text):
        self.model.setFilter('genre=(SELECT id FROM genres WHERE title = "{}")'.format(text))
        self.model.select()
        self.tableView.setModel(self.model)


class PasswordFormM(QWidget):
    def __init__(self):
        super().__init__()
        self.label_2 = None
        self.name_input = None
        self.name_label = None
        self.label = None
        self.btn = None
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 400, 250)
        self.setWindowTitle('Пароль')
        self.setStyleSheet('background-color: turquoise;')

        self.btn = QPushButton('Ввести', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText('Пожалуйста, введите пароль')
        self.label.move(40, 30)

        self.label_2 = QLabel(self)
        self.label_2.setText('                                               ')
        self.label_2.move(40, 200)

        self.name_label = QLabel(self)
        self.name_label.setText('Пароль: ')
        self.name_label.move(40, 90)

        self.name_input = QLineEdit(self)
        self.name_input.move(150, 90)

    def hello(self):
        global password
        name = self.name_input.text()
        if name == '':
            password = True
            self.label_2.setText('Нажмите на кнопку еще раз')
        else:
            password = False
            self.label_2.setText('Вы ввели не тот пароль!!!')


class PasswordFormA(QWidget):
    def __init__(self):
        super().__init__()
        self.label_2 = None
        self.name_input = None
        self.name_label = None
        self.label = None
        self.btn = None
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 400, 250)
        self.setWindowTitle('Пароль')
        self.setStyleSheet('background-color: turquoise;')

        self.btn = QPushButton('Ввести', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText('Пожалуйста, введите пароль')
        self.label.move(40, 30)

        self.label_2 = QLabel(self)
        self.label_2.setText('                                               ')
        self.label_2.move(40, 200)

        self.name_label = QLabel(self)
        self.name_label.setText('Пароль: ')
        self.name_label.move(40, 90)

        self.name_input = QLineEdit(self)
        self.name_input.move(150, 90)

    def hello(self):
        global password_a
        name = self.name_input.text()
        if name == '':
            password_a = True
            self.label_2.setText('Нажмите на кнопку еще раз')
        else:
            password_a = False
            self.label_2.setText('Вы ввели не тот пароль!!!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
