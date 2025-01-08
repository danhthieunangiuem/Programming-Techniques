from PyQt6.QtWidgets import QMessageBox

from Mainwindow import Ui_MainWindow
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
        m_text = self.lineEdit_m.text().strip()
        d_text = self.lineEdit_d.text().strip()

        # Kiểm tra nếu ô nhập liệu bị bỏ trống
        if not n_text or not m_text or not d_text:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không được để trống ô nhập liệu.")
            return
        try:
            n = int(n_text)
            m = int(m_text)
            d = int(d_text)
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi", "N,K phải là số nguyên.")
            return

        if m > n or d > n:
            QMessageBox.warning(self.MainWindow, "Lỗi", "N phải lớn hớn M,D")
            return
        P = (math.comb(d, 1) * math.comb(n - d, m - 1) / math.comb(n, m))
        self.lineEdit_p.setText(str(P))

    def show(self):
        self.MainWindow.show()