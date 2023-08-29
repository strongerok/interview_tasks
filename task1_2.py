from PyQt6.QtWidgets import QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QDialog, QLabel
from PyQt6.QtCore import QRegularExpression, Qt
from PyQt6.QtGui import QRegularExpressionValidator
import task1_1


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("task1_2")
        self.setGeometry(100, 60, 800, 600)
        layout = QVBoxLayout()

        self.input = QLineEdit(self)
        self.input.setFixedWidth(200)
        regex = QRegularExpression("[^0-9_{}\|*+\]\[~]*")
        validator = QRegularExpressionValidator(regex, self.input)
        self.input.setValidator(validator)

        self.btn1 = QPushButton(self)
        self.btn1.setText("Рассчитать")
        self.btn1.setFixedWidth(200)
        self.btn1.clicked.connect(self.showDialog)

        self.btn2 = QPushButton(self)
        self.btn2.setText("Открыть")
        self.btn2.setFixedWidth(200)
        self.btn2.clicked.connect(self.open)

        self.btn3 = QPushButton(self)
        self.btn3.setText("Дополнительно")
        self.btn3.setFixedWidth(200)
        self.btn3.clicked.connect(self.showOtherDialog)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        layout.addWidget(self.input)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def showDialog(self):
        obj = task1_1.Helper()

        dial = QDialog()
        dial.resize(250, 100)

        result = QLabel(dial)
        result.setText(obj.countWords(self.input.text()))

        layout = QVBoxLayout()
        layout.addWidget(result)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        dial.setLayout(layout)
        dial.setStyleSheet("QLabel{font-size: 18pt;}")
        dial.setWindowTitle("Результат")
        dial.exec()

    def open(self):
        self.obj = task1_1.Helper()
        self.obj.showGuiWindow()

    def showOtherDialog(self):
        obj = HelperChild()

        dial = QDialog()
        dial.resize(250, 100)

        result = QLabel(dial)
        result.setText(obj.countWords(self.input.text()))

        layout = QVBoxLayout()
        layout.addWidget(result)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        dial.setLayout(layout)
        dial.setStyleSheet("QLabel{font-size: 18pt;}")
        dial.setWindowTitle("Результат")
        dial.exec()


class HelperChild(task1_1.Helper):
    def countWords(self, string):
        arr = string.split()
        arr = list(filter(lambda x: len(x) == 4, arr))
        arr = [sum(1 for ch in s if ch.isupper()) for s in arr]
        arr = list(filter(lambda x: x > 1, arr))
        return str(len(arr)).ljust(4, " ")
