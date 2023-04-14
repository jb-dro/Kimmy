from PyQt5.QtWidgets import QPushButton, QSizePolicy


class SplitButton(QPushButton):
    text = 'Click me!'

    def __init__(self):
        super(SplitButton, self).__init__()

        # fill height and width
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
