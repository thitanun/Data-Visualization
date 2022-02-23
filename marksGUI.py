from PyQt5 import QtCore, QtGui, QtWidgets
import mainpage
import rangeSlide


class Ui_MarkWindow(object):
    def setupUi(self, MarkWindow):
        MarkWindow.setObjectName("MarkWindow")
        MarkWindow.resize(403, 179)
        self.mark_menu = QtWidgets.QComboBox(MarkWindow)
        self.mark_menu.setGeometry(QtCore.QRect(130, 20, 151, 31))
        self.mark_menu.setObjectName("mark_menu")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.mark_menu.addItem("")
        self.con_bttn = QtWidgets.QPushButton(MarkWindow)
        self.con_bttn.setGeometry(QtCore.QRect(240, 140, 75, 23))
        self.con_bttn.setObjectName("con_bttn")
        self.con_bttn.clicked.connect(mainpage.mt.set_marks)
        self.con_bttn.clicked.connect(MarkWindow.close)
        self.can_bttn = QtWidgets.QPushButton(MarkWindow)
        self.can_bttn.setGeometry(QtCore.QRect(320, 140, 75, 23))
        self.can_bttn.setObjectName("can_bttn")
        self.can_bttn.clicked.connect(MarkWindow.close)


        # self.hz_slider = QtWidgets.QSlider(MarkWindow)
        # self.hz_slider.setGeometry(QtCore.QRect(30, 110, 351, 16))
        # self.hz_slider.setOrientation(QtCore.Qt.Horizontal)
        # self.hz_slider.setObjectName("hz_slider")
        self.hz_slider = rangeSlide.DataRange(QtCore.Qt.Horizontal, MarkWindow)
        self.hz_slider.setGeometry(QtCore.QRect(30, 90, 351, 16))

        # self.hz_slider.min_change.connect(self.num_min.setText)
        # self.hz_slider.max_change.connect(self.num_max.setText)
        # self.hz_slider.setObjectName("hz_slider")
        self.hz_slider.setMinimumHeight(30)
        self.hz_slider.setMinimum(0)
        self.hz_slider.setMaximum(100)
        self.hz_slider.setTickPosition(QtWidgets.QSlider.TicksBelow) 


        self.min_label = QtWidgets.QLabel(MarkWindow)
        self.min_label.setGeometry(QtCore.QRect(20, 120, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.min_label.setFont(font)
        self.min_label.setObjectName("min_label")
        self.max_label = QtWidgets.QLabel(MarkWindow)
        self.max_label.setGeometry(QtCore.QRect(370, 120, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.max_label.setFont(font)
        self.max_label.setObjectName("max_label")
        self.fil_check = QtWidgets.QCheckBox(MarkWindow)
        self.fil_check.setGeometry(QtCore.QRect(30, 140, 51, 17))
        self.fil_check.setObjectName("fil_check")
        self.num_min = QtWidgets.QLineEdit(MarkWindow)
        self.num_min.setGeometry(QtCore.QRect(30, 60, 51, 21))
        self.num_min.setObjectName("num_min")
        self.num_max = QtWidgets.QLineEdit(MarkWindow)
        self.num_max.setGeometry(QtCore.QRect(330, 60, 51, 21))
        self.num_max.setObjectName("num_max")

        self.retranslateUi(MarkWindow)
        QtCore.QMetaObject.connectSlotsByName(MarkWindow)

        self.hz_slider.min_change.connect(self.num_min.setText)
        self.hz_slider.max_change.connect(self.num_max.setText)

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
        self.min_label.setText(_translate("MarkWindow", "MIN"))
        self.max_label.setText(_translate("MarkWindow", "MAX"))
        self.fil_check.setText(_translate("MarkWindow", "Filter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MarkWindow = QtWidgets.QWidget()
    ui = Ui_MarkWindow()
    ui.setupUi(MarkWindow)
    MarkWindow.show()
    sys.exit(app.exec_())
