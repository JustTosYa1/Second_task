import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(500, 300)
        self.setMaximumSize(500, 300)
        self.setWindowTitle("Рисователь кружков")

        self.button = QPushButton("Создать окружности", self)
        self.button.clicked.connect(self.add_circle)
        self.button.setGeometry(150, 120, 200, 40)
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, diameter, color) in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(QRect(x, y, diameter, diameter))

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
