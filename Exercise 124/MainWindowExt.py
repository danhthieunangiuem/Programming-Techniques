import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from MainWindow import Ui_MainWindow

class EmployeeManager(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối các nút với chức năng
        self.ui.pushButtoExportAll.clicked.connect(self.export_all)
        self.ui.pushButton_Filter.clicked.connect(self.filter_data)
        self.ui.pushButtonExportTop3.clicked.connect(self.export_top3_oldest)
        self.ui.pushButton_Count.clicked.connect(self.count_by_role)
        self.ui.pushButton_Add.clicked.connect(self.add_employee)

        self.df = pd.DataFrame()  # Khởi tạo DataFrame rỗng
        self.load_data()

    def load_data(self):
        """Tải dữ liệu từ file CSV"""
        file_path = "../Exercise 124/employee.csv"
        try:
            self.df = pd.read_csv(file_path)
            self.update_table(self.df)
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi tải dữ liệu: {e}")

    def update_table(self, data):
        """Cập nhật bảng hiển thị từ DataFrame"""
        self.ui.tableWidget_employee.setRowCount(len(data))
        self.ui.tableWidget_employee.setColumnCount(len(data.columns))
        self.ui.tableWidget_employee.setHorizontalHeaderLabels(data.columns)

        for i, row in data.iterrows():
            for j, value in enumerate(row):
                self.ui.tableWidget_employee.setItem(i, j, QTableWidgetItem(str(value)))

    def add_employee(self):
        """Thêm nhân viên mới vào danh sách"""
        new_employee = {
            "EmployeeID": len(self.df) + 1,
            "Name": f"Employee {len(self.df) + 1}",
            "Dob": "1995-07-15",
            "Role": "Developer"
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_employee])], ignore_index=True)
        self.update_table(self.df)

    def filter_data(self):
        """Lọc nhân viên theo năm sinh hoặc Tester"""
        year_text = self.ui.lineEdit.text().strip()

        if not year_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập năm sinh hoặc 'Tester'")
            return

        if year_text.isdigit():
            year = int(year_text)
            if "Dob" in self.df.columns:
                self.df["Dob"] = pd.to_datetime(self.df["Dob"], errors="coerce")
                filtered_df = self.df[self.df["Dob"].dt.year == year]
            else:
                QMessageBox.critical(self, "Lỗi", "Không tìm thấy cột 'DateOfBirth' trong dữ liệu")
                return
        elif year_text.lower() == "tester":
            filtered_df = self.df[self.df["Role"].str.lower() == "tester"]
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập năm hợp lệ hoặc 'Tester'")
            return

        self.update_table(filtered_df)

    def export_top3_oldest(self):
        """Xuất 3 nhân viên lớn tuổi nhất"""
        self.df["DateOfBirth"] = pd.to_datetime(self.df["DateOfBirth"])
        oldest_df = self.df.sort_values(by="DateOfBirth").head(3)
        self.update_table(oldest_df)

    def count_by_role(self):
        """Đếm số nhân viên theo vai trò"""
        role_counts = self.df["Role"].value_counts().reset_index()
        role_counts.columns = ["Role", "Count"]

        self.ui.tableWidget_count.setRowCount(len(role_counts))
        self.ui.tableWidget_count.setColumnCount(2)
        self.ui.tableWidget_count.setHorizontalHeaderLabels(["Role", "Count"])

        for i, row in role_counts.iterrows():
            self.ui.tableWidget_count.setItem(i, 0, QTableWidgetItem(row["Role"]))
            self.ui.tableWidget_count.setItem(i, 1, QTableWidgetItem(str(row["Count"])))

    def export_all(self):
        """Xuất tất cả nhân viên ra file CSV"""
        file_path, _ = QFileDialog.getSaveFileName(self, "Lưu File CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.df.to_csv(file_path, index=False)
            QMessageBox.information(self, "Xuất dữ liệu", "Dữ liệu đã được lưu thành công!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeManager()
    window.show()
    sys.exit(app.exec())
