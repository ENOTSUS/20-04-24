# Form implementation generated from reading ui file 'C:\Users\Valera\Desktop\qt_lab\ui\create.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 762)
        MainWindow.setStyleSheet("background: black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(210, 50, 321, 391))
        self.listWidget.setStyleSheet("background: white;")
        self.listWidget.setObjectName("listWidget")
        self.toolButton = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(490, 20, 25, 19))
        self.toolButton.setStyleSheet("background: red;")
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(230, 460, 271, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_stop = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.button_stop.setStyleSheet("background: red;")
        self.button_stop.setObjectName("button_stop")
        self.horizontalLayout.addWidget(self.button_stop)
        self.button_play = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.button_play.setStyleSheet("background: green;")
        self.button_play.setObjectName("button_play")
        self.horizontalLayout.addWidget(self.button_play)
        self.button_rand = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.button_rand.setStyleSheet("background: orange;")
        self.button_rand.setObjectName("button_rand")
        self.horizontalLayout.addWidget(self.button_rand)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.toolButton.setText(_translate("MainWindow", "On"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.button_play.setText(_translate("MainWindow", "Play"))
        self.button_rand.setText(_translate("MainWindow", "Rand"))





# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
