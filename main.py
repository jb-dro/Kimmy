# Simple PyQt5 text editor application

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Text Editor")
        # get the screen geometry
        screen = QApplication.desktop().screenGeometry()
        # get the screen size
        width, height = screen.width(), screen.height()
        # set to full screen
        self.setGeometry(0, 0, width, height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()