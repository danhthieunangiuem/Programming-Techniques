from PyQt6.QtWidgets import  QWidget, QPushButton, QVBoxLayout
from MainWindow import Ui_MainWindow
import random

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.containerWidget = QWidget()
        self.verticalLayoutButton = QVBoxLayout(self.containerWidget)
        self.scrollArea.setWidget(self.containerWidget)
        self.scrollArea.setWidgetResizable(True)
        self.MainWindow = MainWindow
        self.pushButton_create.clicked.connect(self.create)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_update.clicked.connect(self.update)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_asc.clicked.connect(self.sort_asc)
        self.pushButton_des.clicked.connect(self.sort_des)
        self.pushButton_remove.clicked.connect(self.remove)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def create(self):
        try:
            # Validate input
            n_text = self.lineEdit.text().strip()
            if not n_text:
                raise ValueError("Input cannot be empty.")

            n = int(n_text)
            if n <= 0:
                raise ValueError("Number must be a positive integer.")

            # Clear existing buttons
            self.clearLayout(self.verticalLayoutButton)

            # Create random buttons
            for i in range(n):
                x = random.randint(-100, 100)
                print(x)
                btn = QPushButton(text=str(x))
                self.verticalLayoutButton.addWidget(btn)

        except ValueError as e:
            from PyQt6.QtWidgets import QMessageBox
            QMessageBox.warning(self.MainWindow, "Input Error", str(e))

    def add(self):
        x = random.randint(0, 10)
        btn = QPushButton(text=str(x))
        self.verticalLayoutButton.addWidget(btn)

    def delete(self):
        for i in reversed(range(self.verticalLayoutButton.count())):
            button = self.verticalLayoutButton.itemAt(i).widget()
            value = int(button.text())
            if value < 0:
                self.verticalLayoutButton.removeWidget(button)
                button.deleteLater()

    def sort_asc(self):
        buttons = []
        for i in range(self.verticalLayoutButton.count()):
            button = self.verticalLayoutButton.itemAt(i).widget()
            value = int(button.text())
            buttons.append((value, button))
        buttons.sort(key=lambda x: x[0])
        for _, button in buttons:
            self.verticalLayoutButton.removeWidget(button)
        for _, button in buttons:
            self.verticalLayoutButton.addWidget(button)

    def sort_des(self):
        buttons = []
        for i in range(self.verticalLayoutButton.count()):
            button = self.verticalLayoutButton.itemAt(i).widget()
            value = int(button.text())
            buttons.append((value, button))
        buttons.sort(key=lambda x: x[0], reverse=True)
        for _, button in buttons:
            self.verticalLayoutButton.removeWidget(button)
        for _, button in buttons:
            self.verticalLayoutButton.addWidget(button)

    def remove(self):
        self.clearLayout(self.verticalLayoutButton)

    def update(self):
        for i in range(self.verticalLayoutButton.count()):
            button = self.verticalLayoutButton.itemAt(i).widget()
            current_value = int(button.text())
            new_value = current_value // 10
            button.setText(f"{new_value}")

    def show(self):
        self.MainWindow.show()