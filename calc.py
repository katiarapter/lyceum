import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QStatusBar
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QRadioButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        answer = ''
        if self.radioButton.isChecked() is True:
            answer = self.radioButton.text() + ', '
        if self.radioButton_2.isChecked() is True:
            answer += self.radioButton_2.text() + ', '
        if self.radioButton_3.isChecked() is True:
            answer += self.radioButton_3.text() + ', '
        if self.radioButton_6.isChecked() is True:
            answer += self.radioButton_6.text() + ' и '
        if self.radioButton_5.isChecked() is True:
            answer += self.radioButton_5.text() + ' и '
        if self.radioButton_4.isChecked() is True:
            answer += self.radioButton_4.text() + ' и '
        if self.radioButton_7.isChecked() is True:
            answer += self.radioButton_7.text() + '  '
        if self.radioButton_8.isChecked() is True:
            answer += self.radioButton_8.text() + '  '
        if self.radioButton_9.isChecked() is True:
            answer += self.radioButton_9.text() + '  '
        self.label_4.setText(f"Цвета: {answer[:-2]}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
