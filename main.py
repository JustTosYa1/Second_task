import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("UI.ui", self)
        self.button = self.findChild(QPushButton, "generateButton")
        self.button.clicked.connect(self.add_circle)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter) in self.circles:
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(QRect(x, y, diameter, diameter))

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
