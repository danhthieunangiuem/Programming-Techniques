from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
import re
from MainWindow import Ui_MainWindow  # Giả sử file giao diện được lưu là MainWindow.py


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        # Kết nối nút bấm với hàm xử lý
        self.pushButton.clicked.connect(self.find_negative_numbers)

    def find_negative_numbers(self):
        """
        Tìm và hiển thị các số nguyên âm trong chuỗi nhập vào.
        """
        input_string = self.lineEditstring.text()

        # Kiểm tra nếu chuỗi trống
        if not input_string:
            QMessageBox.warning(self, "Warning", "Please enter a string.")
            return

        # Sử dụng regex để tìm các số nguyên âm
        negative_numbers = re.findall(r'-(\d+)', input_string)
        if negative_numbers:
            result = ' '.join(f"-{num}" for num in negative_numbers)
            self.lineEditresult.setText(result)
        else:
            self.lineEditresult.setText("No negative numbers found.")

    def show(self):
        self.MainWindow.show()