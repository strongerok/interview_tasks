from PyQt6.QtWidgets import QPushButton, QMainWindow


class Helper:

    def countWords(self, string):
        arr = string.split()
        arr = list(filter(lambda x: len(x) == 4, arr))
        return str(len(arr))

    def showGuiWindow(self):
        self.window = MainWindow()
        self.window.show()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("task1_1")
        self.setGeometry(100, 60, 800, 600)

        self.button = QPushButton(self)
        self.button.setText("Закрыть")
        self.button.move(self.rect().center() - self.button.rect().center())
        self.button.setFixedWidth(200)
        self.button.clicked.connect(self.close)

    def resizeEvent(self, event):
        self.button.move(self.rect().center() - self.button.rect().center())