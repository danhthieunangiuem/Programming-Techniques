from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):

    def __init__(self):
        self.MainWindow = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton.clicked.connect(self.optimize_string)

    def optimize_string(self):
        # Get input string
        input_text = self.lineEdit1.text().strip()

        if not input_text:
            QMessageBox.warning(self.MainWindow, "Warning", "Please enter a string.")
            return

        # Process the string: Remove extra spaces, capitalize words
        optimized_text = ' '.join(word.capitalize() for word in input_text.split())

        # Display optimized text
        self.lineEdit2.setText(optimized_text)

        # Update character counts
        self.lineEdit_number1.setText(str(len(input_text)))
        self.lineEdit_number2.setText(str(len(optimized_text)))

    def show(self):
        self.MainWindow.show()
