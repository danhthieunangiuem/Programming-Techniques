from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.total_customers = 0  # Tổng số khách hàng cho thống kê
        self.student_customers = 0  # Tổng số khách hàng là sinh viên
        self.total_payment = 0  # Tổng giá trị thanh toán
        self.customer_count = 0  # Đếm số khách hàng mới

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_calc.clicked.connect(self.Calculate)
        self.pushButton_exit.clicked.connect(self.MainWindow.close)
        self.pushButton_stat.clicked.connect(self.Stat)  # Kết nối nút "Thống Kê" với hàm ThongKe
        self.pushButton_new.clicked.connect(self.NewCustomer)  # Kết nối nút "New" với hàm NewCustomer

    def NewCustomer(self):
        # Tăng số đếm khách hàng lên mỗi khi nhấn "New"
        self.customer_count += 1
        # Xóa nội dung các ô nhập liệu và đặt focus về ô tên khách hàng
        self.lineEdit_customer.clear()
        self.lineEdit_quantity.clear()
        self.lineEdit_payment.clear()
        self.checkBox.setChecked(False)  # Bỏ chọn checkbox nếu đã chọn trước đó
        self.lineEdit_customer.setFocus()

    def Calculate(self):
        c_text = self.lineEdit_customer.text().strip()
        q_text = self.lineEdit_quantity.text().strip()

        # Kiểm tra nếu ô nhập liệu bị bỏ trống
        if not c_text or not q_text:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Không được để trống ô nhập liệu.")
            return

        try:
            q = int(q_text)  # Số lượng sách
        except ValueError:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Số lượng sách phải là nguyên dương.")
            return

        # Tính toán giá sách và áp dụng giảm giá nếu có
        if self.checkBox.isChecked():  # Sử dụng isChecked để kiểm tra trạng thái của checkBox
            p = (q * 20000) - (q * 20000) * (5 / 100)
            self.student_customers += 1  # Tăng số khách hàng là sinh viên nếu checkBox được chọn
        else:
            p = q * 20000

        # Cập nhật tổng giá trị thanh toán và tổng số khách hàng
        self.total_payment += p
        self.total_customers += 1

        # Hiển thị kết quả thanh toán
        self.lineEdit_payment.setText(str(p))

    def Stat(self):
        # Hiển thị kết quả thống kê vào các nhãn trong groupbox “Thông tin Thống kê”
        self.lineEdit_totalcustomer.setText(str(self.total_customers))
        self.lineEdit_totalstudent.setText(str(self.student_customers))
        self.lineEdit_totalrevenue.setText(str(self.total_payment))

    def show(self):
        self.MainWindow.show()
