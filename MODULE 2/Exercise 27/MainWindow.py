# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\KTLT\Exercise 59 27\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(80, 150, 651, 51))
        self.lineEdit1.setObjectName("lineEdit1")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 280, 231, 51))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(80, 360, 651, 51))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 90, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(300, 220, 131, 16))
        self.label_1.setObjectName("label_1")
        self.lineEdit_number1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_number1.setGeometry(QtCore.QRect(440, 220, 71, 21))
        self.lineEdit_number1.setObjectName("lineEdit_number1")
        self.lineEdit_number2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_number2.setGeometry(QtCore.QRect(440, 430, 71, 21))
        self.lineEdit_number2.setObjectName("lineEdit_number2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 430, 131, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Optimize"))
        self.label.setText(_translate("MainWindow", "Input String"))
        self.label_1.setText(_translate("MainWindow", "Number of characters:"))
        self.label_2.setText(_translate("MainWindow", "Number of characters:"))
