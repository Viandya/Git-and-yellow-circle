import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.setWindowTitle('Circle Generator')

        self.button_generate.clicked.connect(self.generate_circle)

    def generate_circle(self):
        diameter = random.randint(50, 200)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        color = QColor(Qt.yellow)
        painter.setBrush(color)
        painter.setPen(QPen(color, 2))

        painter.drawEllipse(x, y, diameter, diameter)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
