# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\KTLT\Exercise 127\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 548)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 80, 671, 421))
        self.tableWidget.setStyleSheet("background-color: rgb(221, 255, 247);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 440, 55, 21))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 80, 93, 28))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 140, 101, 28))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 200, 111, 28))
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 170, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(820, 260, 93, 28))
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 320, 93, 28))
        self.pushButton_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 85, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(820, 380, 93, 28))
        self.pushButton_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(170, 255, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(820, 440, 93, 28))
        self.pushButton_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Refresh "))
        self.pushButton_2.setText(_translate("MainWindow", "Sort By Price"))
        self.pushButton_3.setText(_translate("MainWindow", "Reduce by Symbol"))
        self.pushButton_4.setText(_translate("MainWindow", "USD Column"))
        self.pushButton_5.setText(_translate("MainWindow", "Add New Row"))
        self.pushButton_6.setText(_translate("MainWindow", "Statistics"))
        self.pushButton_7.setText(_translate("MainWindow", "Delete"))
        self.label_2.setText(_translate("MainWindow", "EXERCISE 127"))
