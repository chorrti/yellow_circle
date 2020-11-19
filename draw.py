import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randrange


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x = -1
        self.y = -1
        self.radius = 0
        self.f = False
        self.qp = QPainter()
        self.btn.clicked.connect(self.trigger)

    def trigger(self):
        self.f = True
        self.update()

    def paintEvent(self, event):
        if self.f:
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        self.radius = randint(1, 100)
        self.x = randrange(50, 800)
        self.y = randrange(50, 600)
        color = QColor(255, 255, 0)
        self.qp.setBrush(color)
        self.qp.drawEllipse(self.x, self.y, self.radius, self.radius)

    def initUI(self):
        uic.loadUi('file.ui', self)
        self.setWindowTitle('круги появляются. зачем..')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())