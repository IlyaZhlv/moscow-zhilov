import sys
from random import randrange

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor

from UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.flag = False

        self.setupUi(self)
        self.setup_program()

    def setup_program(self):
        self.pushButton.clicked.connect(self.create_circle)

    def paintEvent(self, event):
        if self.flag:
            size = randrange(20, 150)

            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(randrange(256), randrange(256), randrange(256)))
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
