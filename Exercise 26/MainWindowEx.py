from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow
import math

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.count_uppercase = 0
        self.count_words = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_exit.clicked.connect(self.MainWindow.close)
        self.pushButton_nhap.clicked.connect(self.enable_buttons)
        self.set_buttons_enabled(False)  # Vô hiệu hóa các nút khác ban đầu
        self.pushButton_demhoa.clicked.connect(self.Demsokytuhoa)
        self.pushButton_demsotu.clicked.connect(self.Demsotu)
        self.pushButton_demthuong.clicked.connect(self.Demsokytuthuong)
        self.pushButton_inNAPA.clicked.connect(self.inNAPA)
        self.pushButton_insotu.clicked.connect(self.insotutrenmoidong)
        self.pushButton_inthuong.clicked.connect(self.inthuong)
        self.pushButton_inhoa.clicked.connect(self.inhoa)

    def set_buttons_enabled(self, enabled):
        """Vô hiệu hóa hoặc kích hoạt các nút"""
        self.pushButton_demhoa.setEnabled(enabled)
        self.pushButton_inhoa.setEnabled(enabled)
        self.pushButton_insotu.setEnabled(enabled)
        self.pushButton_inthuong.setEnabled(enabled)
        self.pushButton_demsotu.setEnabled(enabled)
        self.pushButton_demthuong.setEnabled(enabled)
        self.pushButton_inNAPA.setEnabled(enabled)

    def enable_buttons(self):
        """Kiểm tra nếu có dữ liệu nhập, thì kích hoạt các nút khác"""
        # Lấy nội dung từ QTextEdit
        text = self.textEdit_nhap.toPlainText()

        if not text:
            QMessageBox.warning(self.MainWindow, "Thông báo", "Dữ liệu nhập không được để trống.")
            return

        # Kích hoạt các nút khi đã có dữ liệu nhập
        self.set_buttons_enabled(True)

    def Demsokytuhoa(self):
        # Lấy dữ liệu văn bản từ QTextEdit
        text = self.textEdit_nhap.toPlainText()

        # Đếm số ký tự in hoa
        self.count_uppercase = sum(1 for char in text if char.isupper())

        # Hiển thị kết quả vào textEdit_xuat
        self.textEdit_xuat.setText(str(self.count_uppercase))

    def Demsotu(self):
        # Lấy dữ liệu văn bản từ QTextEdit
        text = self.textEdit_nhap.toPlainText()

        # Tách chuỗi thành danh sách các từ và đếm số lượng từ
        words = text.split()

        # Đếm số lượng từ
        self.count_words = len(words)

        # Hiển thị kết quả vào textEdit_xuat
        self.textEdit_xuat.setText(str(self.count_words))

    def Demsokytuthuong(self):
        # Lấy dữ liệu văn bản từ QTextEdit
        text = self.textEdit_nhap.toPlainText()

        # Đếm số ký tự in hoa
        self.count_lowercase = sum(1 for char in text if char.islower())

        # Hiển thị kết quả vào textEdit_xuat
        self.textEdit_xuat.setText(str(self.count_lowercase))

    def inhoa(self):
        # Lấy dữ liệu văn bản từ QTextEdit
        text = self.textEdit_nhap.toPlainText()

        # Lọc các ký tự in hoa trong chuỗi
        uppercase_text = ''.join([char for char in text if char.isupper()])

        # Kiểm tra xem có ký tự in hoa nào không
        if uppercase_text:
            # Hiển thị các ký tự in hoa vào textEdit_xuat
            self.textEdit_xuat.setText(str(uppercase_text))
        else:
            # Nếu không có ký tự in hoa
            self.textEdit_xuat.setText("Không có ký tự in hoa trong chuỗi.")

    def inthuong(self):
        # Lấy dữ liệu văn bản từ QTextEdit
        text = self.textEdit_nhap.toPlainText()

        # Lọc các ký tự in hoa trong chuỗi
        lowercase_text = ''.join([char for char in text if char.islower()])

        # Kiểm tra xem có ký tự in hoa nào không
        if lowercase_text:
            # Hiển thị các ký tự in hoa vào textEdit_xuat
            self.textEdit_xuat.setText(str(lowercase_text))
        else:
            # Nếu không có ký tự in hoa
            self.textEdit_xuat.setText("Không có ký tự in hoa trong chuỗi.")

    def inNAPA(self):
        text = self.textEdit_nhap.toPlainText()

        vowels = 'aeiouAEIOU'
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

        vowels_text = ''.join([char for char in text if char in vowels])
        consonants_text = ''.join([char for char in text if char in consonants])

        # Hiển thị kết quả vào textEdit_xuat
        result = f"Nguyên âm: {vowels_text}\nPhụ âm: {consonants_text}"
        self.textEdit_xuat.setText(result)

    def insotutrenmoidong(self):
        text = self.textEdit_nhap.toPlainText()

        # Chia văn bản thành các dòng
        lines = text.split('\n')

        result = []
        for i, line in enumerate(lines):
            # Tách từ trong mỗi dòng và đếm
            words = line.split()
            word_count = len(words)
            result.append(f"Dòng {i + 1}: {word_count} từ")

        # Hiển thị kết quả vào textEdit_xuat
        self.textEdit_xuat.setText('\n'.join(result))

    def show(self):
        self.MainWindow.show()
