from PyQt6.QtWidgets import QMessageBox

from MainWindow import Ui_MainWindow
import math

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton.clicked.connect(self.Calculate)
    def Calculate(self):
        n_text = self.lineEdit_n.text().strip()
        k_text = self.lineEdit_k.text().strip()

        # Kiểm tra nếu ô nhập liệu bị bỏ trống
        if not n_text or not k_text:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không được để trống ô nhập liệu.")
            return
        try:
            n = int(n_text)
            k = int(k_text)
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi", "N,K phải là số nguyên.")
            return

        if k<=n:
            a=math.factorial(n) // math.factorial(n - k)
            b = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        else: a=0;b=0
        self.lineEdit_a.setText(str(a))
        self.lineEdit_b.setText(str(b))
    def show(self):
        self.MainWindow.show()