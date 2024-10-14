from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(960, 493)
        Help.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(Help)
        self.frame.setGeometry(QtCore.QRect(0, 0, 961, 491))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 911, 451))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "Dialog"))
        self.label.setText(_translate("Help", "КОМАНДЫ, ДОСТУПНЫЕ ДЛЯ ВВОДА В ТЕКСТОВОЕ ПОЛЕ ПОЛЬЗОВАТЕЛЕМ:\n"
"\n"
"   set ip sender 000.000.000.000 / set ip sender range 000.000.000.000 255.255.255.255      //установка ip / диапазона ip отправителя\n"
"   set ip receiver 000.000.000.000 / set ip receiver range 000.000.000.000 255.255.255.255    //установка ip / диапазона ip отправителя\n"
"   set ports AAA                                        //установка разрешенного порта\n"
"   set protocol AAA, BBB, CCC                                    //установка разрешенных протоколов\n"
"   block ip 000.000.000.000                                    //блокировка ip\n"
"   remove ports AAA, CCC                                    //убрать порт из разрешенных\n"
"   remove protocol AAA, CCC                                    //убрать протоколы из разрешенных\n"
"   clear ip                                            //очистить разрешенные ip\n"
"   clear ports                                            //очистить разрешенные порты\n"
"   clear protocol                                        //очистить разрешенные протоколы\n"
"\n"
"Задание генерируется автоматически. Условия выполнения задания:\n"
"- у обоих компьютеров есть указанный пользователем порт (только один)\n"
"- у обоих компьютеров есть указанные пользователем протоколы (1 и более)\n"
"- IP адрес отправителя совпадает с разрешенным / входит в разрешенный диапазон отправителей\n"
"- IP адрес получателя совпадает с разрешенным / входит в разрешенный диапазон получателей\n"
"\n"
"По завершении ввода команд необходимо нажать кнопку \"Проверка\".\n"
"При неправильно выполненном задании появится красная надпись \"Попробуй еще раз\". После повторного ввода либо исправления команд\n"
"при условии, что решение правильное, появится зеленая надпись \"Все правильно\"."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Help = QtWidgets.QDialog()
    ui = Ui_Help()
    ui.setupUi(Help)
    Help.show()
    sys.exit(app.exec_())
