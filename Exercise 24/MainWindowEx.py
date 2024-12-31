from random import randint

from PyQt6.QtWidgets import QMessageBox
from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        # Khởi tạo số tiền ban đầu
        self.player_money = 100
        self.machine_money = 100

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_random.clicked.connect(self.Random)
        self.pushButton_exit.clicked.connect(self.MainWindow.close)
        self.pushButton_new.clicked.connect(self.NewGame)

    def Random(self):
        # Kiểm tra nếu người chơi đủ tiền để quay
        if self.player_money < 30:
            QMessageBox.warning(self.MainWindow, "Không đủ tiền", "Bạn không đủ tiền để quay!")
            return

        # Trừ tiền người chơi và cộng tiền cho máy
        self.player_money -= 30
        self.machine_money += 30

        # Quay số cho ba ô
        result1 = randint(0, 8)
        result2 = randint(0, 9)
        result3 = randint(0, 10)

        # Cập nhật các QLabel với kết quả mới
        self.label1.setText(str(result1))
        self.label2.setText(str(result2))
        self.label3.setText(str(result3))

        # Tính toán phần thưởng
        reward = 0
        if result1 == 7:
            reward += 100 + int(0.5 * self.machine_money)
        if result2 == 7:
            reward += 30 + int(0.5 * self.machine_money)
        if result3 == 7:
            reward += 10


        # Cập nhật tiền cho người chơi và máy
        if reward > 0:
            self.player_money += reward
            self.machine_money -= reward

            # Kiểm tra nếu số tiền của máy âm và xử lý chiến thắng của người chơi
            if self.machine_money < 0:
                self.machine_money = 0
                self.lineEdit_machine.setText(str(self.machine_money))
                QMessageBox.information(self.MainWindow, "Chiến thắng", "Chúc mừng! Bạn đã thắng trò chơi!")
                return

        # Cập nhật hiển thị số tiền
        self.lineEdit_player.setText(str(self.player_money))
        self.lineEdit_machine.setText(str(self.machine_money))
        # Kiểm tra nếu người chơi đủ tiền để quay
        if self.player_money < 30:
            QMessageBox.warning(self.MainWindow, "Không đủ tiền", "Bạn không đủ tiền để quay!")
            return

    def NewGame(self):
        # Khởi động lại số tiền cho người chơi và máy
        self.player_money = 100
        self.machine_money = 100
        self.lineEdit_player.setText(str(self.player_money))
        self.lineEdit_machine.setText(str(self.machine_money))

        # Đặt lại các nhãn kết quả về số 7
        self.label1.setText("7")
        self.label2.setText("7")
        self.label3.setText("7")

    def show(self):
        self.MainWindow.show()