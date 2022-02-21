from PyQt5 import QtCore, QtGui, QtWidgets
import mainpage


class Ui_MarkWindow(object):
    def setupUi(self, MarkWindow):
        MarkWindow.setObjectName("MarkWindow")
        MarkWindow.resize(403, 440)
        self.mark_menu = QtWidgets.QComboBox(MarkWindow)
        self.mark_menu.setGeometry(QtCore.QRect(130, 100, 151, 31))
        self.mark_menu.setObjectName("mark_menu")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.con_bttn = QtWidgets.QPushButton(MarkWindow)
        self.con_bttn.setGeometry(QtCore.QRect(240, 400, 75, 23))
        self.con_bttn.setObjectName("con_bttn")
        self.con_bttn.clicked.connect(mainpage.mt.set_marks)
        self.con_bttn.clicked.connect(MarkWindow.close)
        self.can_bttn = QtWidgets.QPushButton(MarkWindow)
        self.can_bttn.setGeometry(QtCore.QRect(320, 400, 75, 23))
        self.can_bttn.setObjectName("can_bttn")
        self.can_bttn.clicked.connect(MarkWindow.close)

        self.retranslateUi(MarkWindow)
        QtCore.QMetaObject.connectSlotsByName(MarkWindow)

    def retranslateUi(self, MarkWindow):
        _translate = QtCore.QCoreApplication.translate
        MarkWindow.setWindowTitle(_translate("MarkWindow", "MarkWindow"))
        self.mark_menu.setItemText(0, _translate("MarkWindow", "NONE"))
        self.mark_menu.setItemText(1, _translate("MarkWindow", "MEAN"))
        self.mark_menu.setItemText(2, _translate("MarkWindow", "MEDIAN"))
        self.mark_menu.setItemText(3, _translate("MarkWindow", "MAX"))
        self.mark_menu.setItemText(4, _translate("MarkWindow", "MIN"))
        self.mark_menu.setItemText(5, _translate("MarkWindow", "SUM"))
        self.mark_menu.setItemText(6, _translate("MarkWindow", "COUNT"))
        self.con_bttn.setText(_translate("MarkWindow", "Confirm"))
        self.can_bttn.setText(_translate("MarkWindow", "Cancle"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MarkWindow = QtWidgets.QWidget()
#     ui = Ui_MarkWindow()
#     ui.setupUi(MarkWindow)
#     MarkWindow.show()
#     sys.exit(app.exec_())
