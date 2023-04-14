from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from split_button import SplitButton  # Assuming the SplitButton class is defined in a separate file


class SplitButtonApp(QMainWindow):
    def __init__(self):
        super(SplitButtonApp, self).__init__()

        # Set up the main window
        self.setWindowTitle("Split Button App")
        self.setGeometry(100, 100, 400, 400)

        # Create the split button
        self.split_button = SplitButton()
        self.split_button.clicked.connect(self.split)

        # Set the split button as the central widget of the main window
        central_widget = QWidget()
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().addWidget(self.split_button)
        self.setCentralWidget(central_widget)

        # Set window properties
        # self.setWindowFlags(Qt.FramelessWindowHint)  # Remove window frame
        # self.setAttribute(Qt.WA_TranslucentBackground)  # Make window background transparent
        # self.setStyleSheet("background-color: rgba(0,0,0,255);")  # Set window background color to black

        self.show()

    def split(self):
        print("Split button clicked!")


if __name__ == "__main__":
    app = QApplication([])
    window = SplitButtonApp()
    app.exec_()
