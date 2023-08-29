from PyQt6.QtWidgets import QApplication

import task1_1

if __name__ == '__main__':
    app = QApplication([])
    test = task1_1.Helper()
    print(test.countWords("я люблю   орехи, но больше   всего я    люблю киви  "))
    test.showGuiWindow()
    app.exec()