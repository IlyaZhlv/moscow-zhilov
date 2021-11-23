import sys
from random import randint

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor

from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('UI.ui', self)
        self.flag = False

        self.setup_program()

    def setup_program(self):
        self.pushButton.clicked.connect(self.create_circle)

    def paintEvent(self, event):
        if self.flag:
            size = randint(20, 150)

            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(140, 170, size, size)
            qp.end()

            self.flag = False

    def create_circle(self):
        self.flag = True

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
