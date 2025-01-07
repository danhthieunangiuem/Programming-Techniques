from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow
import re


def is_prime(num):
    """Kiểm tra số nguyên tố"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

class MainWindowEx(Ui_MainWindow):

    def __init__(self):
        self.MainWindow = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        # Kết nối nút bấm với hàm xử lý
        self.pushButton.clicked.connect(self.calculate_statistics)

    def calculate_statistics(self):
        input_string = self.lineEditstring.text().strip()

        # Kiểm tra chuỗi trống
        if not input_string:
            QMessageBox.warning(self, "Warning", "Please enter a string.")
            return
        # Kiểm tra định dạng hợp lệ
        if not re.fullmatch(r'[-\d; ]+', input_string):
            QMessageBox.warning(self, "Warning", "Invalid format. Please use digits, '-', and ';'.")
            self.clear_results()
            return
        numbers = [int(num) for num in re.findall(r'-?\d+', input_string)]

        # Negative Numbers
        negative_numbers = [num for num in numbers if num < 0]
        self.lineEditresult.setText(', '.join(map(str, negative_numbers)) if negative_numbers else "None")

        # Prime Numbers
        prime_numbers = [num for num in numbers if is_prime(num)]
        self.lineEditresult_2.setText(', '.join(map(str, prime_numbers)) if prime_numbers else "None")

        # Even Numbers
        even_numbers = [num for num in numbers if num % 2 == 0]
        self.lineEditresult_3.setText(', '.join(map(str, even_numbers)) if even_numbers else "None")

        # Average Value
        avg_value = sum(numbers) / len(numbers) if numbers else 0
        self.lineEditresult_4.setText(f"{avg_value:.2f}")

    def show(self):
        self.MainWindow.show()
