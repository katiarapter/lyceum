import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('zadacha.ui', self)
        self.comboBox.activated[str].connect(self.run)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        self.db.setDatabaseName('films_db.sqlite')
        # И откроем подключение
        self.db.open()

        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('films')
        self.model.select()
        self.tableView.setModel(self.model)

    def run(self, text):
        self.model.setFilter('genre=(SELECT id FROM genres WHERE title = "{}")'.format(text))
        self.model.select()
        self.tableView.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
