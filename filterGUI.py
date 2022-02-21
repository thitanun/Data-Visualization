from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilterWindow(object):
    def setupUi(self, FilterWindow):
        FilterWindow.setObjectName("FilterWindow")
        FilterWindow.resize(400, 411)
        self.seall_bttn = QtWidgets.QPushButton(FilterWindow)
        self.seall_bttn.setGeometry(QtCore.QRect(20, 370, 75, 23))
        self.seall_bttn.setObjectName("seall_bttn")
        self.deall_bttn = QtWidgets.QPushButton(FilterWindow)
        self.deall_bttn.setGeometry(QtCore.QRect(100, 370, 75, 23))
        self.deall_bttn.setObjectName("deall_bttn")
        self.fil_data = QtWidgets.QListView(FilterWindow)
        self.fil_data.setGeometry(QtCore.QRect(20, 21, 361, 341))
        self.fil_data.setObjectName("fil_data")
        self.confirm_bttn = QtWidgets.QPushButton(FilterWindow)
        self.confirm_bttn.setGeometry(QtCore.QRect(250, 370, 61, 23))
        self.confirm_bttn.setObjectName("confirm_bttn")
        self.cancle_bttn = QtWidgets.QPushButton(FilterWindow)
        self.cancle_bttn.setGeometry(QtCore.QRect(320, 370, 61, 23))
        self.cancle_bttn.setObjectName("cancle_bttn")

        self.retranslateUi(FilterWindow)
        QtCore.QMetaObject.connectSlotsByName(FilterWindow)

    def retranslateUi(self, FilterWindow):
        _translate = QtCore.QCoreApplication.translate
        FilterWindow.setWindowTitle(_translate("FilterWindow", "FilterWindow"))
        self.seall_bttn.setText(_translate("FilterWindow", "Select All"))
        self.deall_bttn.setText(_translate("FilterWindow", "Deselect All"))
        self.confirm_bttn.setText(_translate("FilterWindow", "Confirm"))
        self.cancle_bttn.setText(_translate("FilterWindow", "Cancle"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     FilterWindow = QtWidgets.QWidget()
#     ui = Ui_FilterWindow()
#     ui.setupUi(FilterWindow)
#     FilterWindow.show()
#     sys.exit(app.exec_())
