# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\KTLT\Exercise 59 39\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 621)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 100, 113, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 110, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_create = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_create.setGeometry(QtCore.QRect(360, 100, 93, 28))
        self.pushButton_create.setObjectName("pushButton_create")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(160, 140, 311, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(parent=self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 291, 301))
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_add = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(500, 140, 93, 28))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_remove = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_remove.setGeometry(QtCore.QRect(500, 390, 93, 28))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.pushButton_update = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(500, 190, 93, 28))
        self.pushButton_update.setObjectName("pushButton_update")
        self.pushButton_delete = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(500, 240, 93, 28))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_asc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_asc.setGeometry(QtCore.QRect(500, 290, 93, 28))
        self.pushButton_asc.setObjectName("pushButton_asc")
        self.pushButton_des = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_des.setGeometry(QtCore.QRect(500, 340, 93, 28))
        self.pushButton_des.setObjectName("pushButton_des")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 26))
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
        self.label.setText(_translate("MainWindow", "List Operations"))
        self.label_2.setText(_translate("MainWindow", "N:"))
        self.pushButton_create.setText(_translate("MainWindow", "Create random"))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.pushButton_remove.setText(_translate("MainWindow", "Remove All"))
        self.pushButton_update.setText(_translate("MainWindow", "Update"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))
        self.pushButton_asc.setText(_translate("MainWindow", "Asc Sort"))
        self.pushButton_des.setText(_translate("MainWindow", "Des Sort"))
