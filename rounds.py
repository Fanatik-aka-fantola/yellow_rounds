from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
import sys
import random


class YellowRounds(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setFixedSize(800, 600)
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.size = random.randint(10, 100)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))
            x, y = random.randint(100, 800 - 100), random.randint(100, 600 - 100)
            qp.drawEllipse(x, y, self.size, self.size)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowRounds()
    ex.show()
    sys.exit(app.exec())
