# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MarksGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.con_bttn = QtWidgets.QPushButton(MarkWindow)
        self.con_bttn.setGeometry(QtCore.QRect(320, 400, 75, 23))
        self.con_bttn.setObjectName("con_bttn")

        self.retranslateUi(MarkWindow)
        QtCore.QMetaObject.connectSlotsByName(MarkWindow)

    def retranslateUi(self, MarkWindow):
        _translate = QtCore.QCoreApplication.translate
        MarkWindow.setWindowTitle(_translate("MarkWindow", "MarkWindow"))
        self.mark_menu.setItemText(0, _translate("MarkWindow", "MEAN"))
        self.mark_menu.setItemText(1, _translate("MarkWindow", "MEDIAN"))
        self.mark_menu.setItemText(2, _translate("MarkWindow", "MAX"))
        self.mark_menu.setItemText(3, _translate("MarkWindow", "MIN"))
        self.mark_menu.setItemText(4, _translate("MarkWindow", "SUM"))
        self.mark_menu.setItemText(5, _translate("MarkWindow", "COUNT"))
        self.con_bttn.setText(_translate("MarkWindow", "Confirm"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MarkWindow = QtWidgets.QWidget()
#     ui = Ui_MarkWindow()
#     ui.setupUi(MarkWindow)
#     MarkWindow.show()
#     sys.exit(app.exec_())