from PyQt5 import QtCore, QtGui, QtWidgets
import mainpage
import tableManage
import json

class Ui_FilterWindow(object):
    def setupUi(self, FilterWindow):
        FilterWindow.setObjectName("FilterWindow")
        FilterWindow.resize(400, 411)
        self.seall_bttn = QtWidgets.QPushButton(FilterWindow)
        self.seall_bttn.setGeometry(QtCore.QRect(20, 370, 75, 23))
        self.seall_bttn.setObjectName("seall_bttn")
        self.seall_bttn.clicked.connect(self.check_all)
        self.deall_bttn = QtWidgets.QPushButton(FilterWindow)
        self.deall_bttn.setGeometry(QtCore.QRect(100, 370, 75, 23))
        self.deall_bttn.setObjectName("deall_bttn")
        self.deall_bttn.clicked.connect(self.uncheck_all)
        # self.fil_data = QtWidgets.QListView(FilterWindow)
        self.fil_data = QtWidgets.QListWidget(FilterWindow)
        self.fil_data.setGeometry(QtCore.QRect(20, 21, 361, 341))
        self.fil_data.setObjectName("fil_data")
        self.confirm_bttn = QtWidgets.QPushButton(FilterWindow)
        self.confirm_bttn.setGeometry(QtCore.QRect(250, 370, 61, 23))
        self.confirm_bttn.setObjectName("confirm_bttn")
        self.confirm_bttn.clicked.connect(mainpage.mt.confirm_filter)
        self.confirm_bttn.clicked.connect(FilterWindow.close) 
        self.cancle_bttn = QtWidgets.QPushButton(FilterWindow)
        self.cancle_bttn.setGeometry(QtCore.QRect(320, 370, 61, 23))
        self.cancle_bttn.setObjectName("cancle_bttn")
        self.cancle_bttn.clicked.connect(FilterWindow.close) 

        self.retranslateUi(FilterWindow)
        QtCore.QMetaObject.connectSlotsByName(FilterWindow)

    def retranslateUi(self, FilterWindow):
        _translate = QtCore.QCoreApplication.translate
        FilterWindow.setWindowTitle(_translate("FilterWindow", "FilterWindow"))
        self.seall_bttn.setText(_translate("FilterWindow", "Select All"))
        self.deall_bttn.setText(_translate("FilterWindow", "Deselect All"))
        self.confirm_bttn.setText(_translate("FilterWindow", "Confirm"))
        self.cancle_bttn.setText(_translate("FilterWindow", "Cancle"))


    def check_all(self):
        for i in range(self.fil_data.count()):
            item = self.fil_data.item(i)
            item.setCheckState(QtCore.Qt.Checked)
    
    def uncheck_all(self):
        for i in range(self.fil_data.count()):
            item = self.fil_data.item(i)
            item.setCheckState(QtCore.Qt.Unchecked)
