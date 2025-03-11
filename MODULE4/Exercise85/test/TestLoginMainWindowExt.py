from PyQt6.QtWidgets import QApplication, QMainWindow

from MODULE4.Exercise85.ui.LoginMainWindowExt import LoginMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()