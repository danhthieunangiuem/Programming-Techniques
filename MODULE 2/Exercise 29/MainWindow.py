# Form implementation generated from reading ui file 'C:\Users\ACER\PycharmProjects\KTLT\Exercise 59 29\MainWindow.ui'
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
        self.labeltitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.labeltitle.setGeometry(QtCore.QRect(290, 60, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labeltitle.setFont(font)
        self.labeltitle.setObjectName("labeltitle")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 360, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.labelstring = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelstring.setGeometry(QtCore.QRect(210, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelstring.setFont(font)
        self.labelstring.setObjectName("labelstring")
        self.labelresult = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelresult.setGeometry(QtCore.QRect(210, 260, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelresult.setFont(font)
        self.labelresult.setObjectName("labelresult")
        self.lineEditstring = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditstring.setGeometry(QtCore.QRect(310, 160, 281, 31))
        self.lineEditstring.setObjectName("lineEditstring")
        self.lineEditresult = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditresult.setGeometry(QtCore.QRect(310, 260, 281, 31))
        self.lineEditresult.setObjectName("lineEditresult")
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
        self.labeltitle.setText(_translate("MainWindow", "Find Negative String"))
        self.pushButton.setText(_translate("MainWindow", "Find"))
        self.labelstring.setText(_translate("MainWindow", "String"))
        self.labelresult.setText(_translate("MainWindow", "Result"))
