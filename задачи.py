import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QPushButton, QTableWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Genres(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('films_db.sqlite')
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Фильтрация по жанрам')

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(180, 10, 400, 350)

        self.pushButton = QPushButton('Пуск', self)
        self.pushButton.setGeometry(50, 100, 80, 30)
        self.pushButton.clicked.connect(self.run)

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(10, 10, 160, 30)
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

    def run(self):
        cur = self.con.cursor()
        print(str(self.comboBox.currentText()))
        result = cur.execute("""SELECT title, genre, year FROM Films WHERE genre=(SELECT id 
                FROM genres WHERE title = ?)""", (str(self.comboBox.currentText()),)).fetchall()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Genres()
    ex.show()
    sys.exit(app.exec())
