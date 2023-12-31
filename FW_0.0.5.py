# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FW_0.0.5.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 825)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1121, 821))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_task_text = QtWidgets.QLabel(self.frame)
        self.label_task_text.setGeometry(QtCore.QRect(60, 20, 1011, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_task_text.setFont(font)
        self.label_task_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_task_text.setObjectName("label_task_text")
        self.correct_answer = QtWidgets.QLabel(self.frame)
        self.correct_answer.setGeometry(QtCore.QRect(490, 760, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.correct_answer.setFont(font)
        self.correct_answer.setStyleSheet("color: rgb(0, 0, 0);")
        self.correct_answer.setObjectName("correct_answer")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 90, 1011, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_secure_comp = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_secure_comp.setFont(font)
        self.label_secure_comp.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.label_secure_comp.setObjectName("label_secure_comp")
        self.horizontalLayout.addWidget(self.label_secure_comp)
        self.label_non_secure_comp = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_non_secure_comp.setFont(font)
        self.label_non_secure_comp.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.label_non_secure_comp.setObjectName("label_non_secure_comp")
        self.horizontalLayout.addWidget(self.label_non_secure_comp)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(60, 400, 1011, 271))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"color: rgb(85, 255, 127);")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1020, 760, 71, 28))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 71, 71);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 690, 1011, 31))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_task_text.setText(_translate("MainWindow", "Задание"))
        self.correct_answer.setText(_translate("MainWindow", "Все правильно!"))
        self.label_secure_comp.setText(_translate("MainWindow", "Защищенные компы"))
        self.label_non_secure_comp.setText(_translate("MainWindow", "Незащищенные компы"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Помощь"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
