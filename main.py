from PyQt6.QtWidgets import QApplication

import task1_2

if __name__ == '__main__':
    app = QApplication([])
    window = task1_2.MainWindow()
    window.show()
    app.exec()

