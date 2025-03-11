from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def show(self):
        self.MainWindow.show()
