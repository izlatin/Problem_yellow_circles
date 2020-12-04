import sys
from random import choice

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow_circle.ui', self)

        self.button.clicked.connect(self.draw)
        self.really = False
        self.flag = 0

    def draw(self):
        self.really = True
        self.repaint()
        self.really = False

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_figure(qp)
        qp.end()

    def draw_figure(self, qp):
        if self.flag > 1:
            color = QColor('yellow')
            qp.setBrush(color)
            size = choice(range(50, 250))
            qp.drawEllipse(choice(range(0, 550)), choice(range(100, 350)), size, size)
        self.flag += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
