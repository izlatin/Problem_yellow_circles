import sys
from random import choice

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(290, 10, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setObjectName("button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "GENERATE"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
            clr = [choice(range(256)), choice(range(256)), choice(range(256))]
            color = QColor(*clr)
            print(clr)
            qp.setBrush(color)
            size = choice(range(50, 250))
            qp.drawEllipse(choice(range(0, 550)), choice(range(100, 350)), size, size)
        self.flag += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
