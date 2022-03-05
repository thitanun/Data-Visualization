from PyQt5 import QtCore, QtGui, QtWidgets
import rangeSlide
import tableManage
import mainpage


class Ui_FilterMark(object):

    def setupUi(self, FilterMark):
        FilterMark.setObjectName("FilterMark")
        FilterMark.resize(403, 151)
        self.conf_bttn = QtWidgets.QPushButton(FilterMark)
        self.conf_bttn.setGeometry(QtCore.QRect(170, 110, 75, 23))
        self.conf_bttn.setObjectName("conf_bttn")
        self.canc_bttn = QtWidgets.QPushButton(FilterMark)
        self.canc_bttn.setGeometry(QtCore.QRect(250, 110, 75, 23))
        self.canc_bttn.setObjectName("canc_bttn")
        self.canc_bttn.clicked.connect(FilterMark.close)

        self.hz_slider = rangeSlide.DataRange(QtCore.Qt.Horizontal, FilterMark)
        self.hz_slider.setGeometry(QtCore.QRect(30, 50, 351, 16))
        self.hz_slider.setMinimumHeight(30)
        # self.hz_slider.setMinimum(0)
        # self.hz_slider.setMaximum(100)
        self.hz_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)

        self.min_label = QtWidgets.QLabel(FilterMark)
        self.min_label.setGeometry(QtCore.QRect(20, 80, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.min_label.setFont(font)
        self.min_label.setObjectName("min_label")
        self.max_label = QtWidgets.QLabel(FilterMark)
        self.max_label.setGeometry(QtCore.QRect(330, 80, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.max_label.setFont(font)
        self.max_label.setObjectName("max_label")
        self.num_min = QtWidgets.QLineEdit(FilterMark)
        self.num_min.setGeometry(QtCore.QRect(30, 20, 121, 21))
        self.num_min.setObjectName("num_min")
        self.num_max = QtWidgets.QLineEdit(FilterMark)
        self.num_max.setGeometry(QtCore.QRect(270, 20, 111, 21))
        self.num_max.setObjectName("num_max")
        self.ap_bttn = QtWidgets.QPushButton(FilterMark)
        self.ap_bttn.setGeometry(QtCore.QRect(90, 110, 75, 23))
        self.ap_bttn.setObjectName("ap_bttn")


        self.retranslateUi(FilterMark)
        QtCore.QMetaObject.connectSlotsByName(FilterMark)


        self.hz_slider.min_change.connect(self.min_ch)
        self.hz_slider.max_change.connect(self.max_ch)


    def retranslateUi(self, FilterMark):
        _translate = QtCore.QCoreApplication.translate
        FilterMark.setWindowTitle(_translate("FilterMark", "Filter Window"))
        self.conf_bttn.setText(_translate("FilterMark", "Confirm"))
        self.canc_bttn.setText(_translate("FilterMark", "Cancel"))
        # self.min_label.setText(_translate("FilterMark", "MIN"))
        # self.max_label.setText(_translate("FilterMark", "MAX"))
        self.ap_bttn.setText(_translate("FilterMark", "Apply"))


    def range_data(self, value): #trans
        self.val_min = int(self.min_label.text())
        # print('vm', self.val_min.type)
        # print(self.val_min)
        self.val_max = int(self.max_label.text())
        # self.val_max = int(self.num_max.text())
        # new_val = self.val_min - self.val_max
        new_val = self.val_max - self.val_min
        return ((value * new_val) / 100) + self.val_min

    def min_ch(self): #update min
        # print(self.hz_slider.low()) -> 0
        self.val_min = self.hz_slider.low()
        # print(self.val_min) -> 0 after mute max min setting
        # print(self.val_min) -> 0 before mute max min setting
        min_data = self.range_data(self.val_min)
        # print('min', min_data)
        self.num_min.setText(str(int(min_data)))
        # self.num_min.setText(int(min_data))


    def max_ch(self): #update max
        self.val_max = self.hz_slider.high()
        # print(self.val_max)
        max_data = self.range_data(self.val_max)
        # print('max', max_data)
        self.num_max.setText(str(int(max_data)))
        # self.num_max.setText(int(max_data))


    def fin_mark(self):
        data = mainpage.mt.data_box.selectedItems()
        file_read = tableManage.TableView.read_data(data)
        row_list,column_list = tableManage.TableView.row_column_list()
        
        # print("row_list",row_list)
        # print("column_list",column_list)
        list_dim,list_meas,list_mark,list_filter = tableManage.TableView.dim_meas_rc(file_read,row_list,column_list)
        if len(list_dim) == 0 and len(list_meas) == 0 and len(list_mark) == 0:
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)  
            mainpage.mt.table_box.setColumnCount(0)
        elif  len(list_dim) == 0 and len(list_meas) != 0 and len(list_mark) != 0:
                    mainpage.mt.table_box.clear()
                    mainpage.mt.table_box.setRowCount(0)   
                    mainpage.mt.table_box.setColumnCount(0)  
        else:
            # print(list_dim)
            # print(list_meas)
            # print(list_mark)
            if len(list_mark) == 0:
                if len(list_meas) == 0:
                    frame_merge = tableManage.TableView.show_dim_meas(file_read,list_dim,list_meas,list_filter)
            else:
                    frame_merge = tableManage.TableView.check_mark(file_read,list_dim,list_meas,list_mark,list_filter)
            # self.filter_add(frame_merge)
            frame_data = tableManage.TableView.filter_add(frame_merge)

        return frame_data


    def meas_col(self):
        #marks selected
        data = self.fin_mark()
        # data = self.fin_mark()
        head = list(data.head(0))
        # head = mainpage.mt.col_box.selectedItems()
        # print(head)
        # print(head[1])
        # print('0', head[0])
        # try:
        #     print(len(data))
        #     if len(data) > 1:
        #         self.num_min.setText(str(data[head[1]].min()))
        #         print(self.num_min.text())
        #         self.num_max.setText(str(data[head[1]].max()))
        #         # print(self.num_max.text())
        #         self.min_label.setText(str(int(data[head[1]].min())))
        #         # print(self.min_label.text())
        #         self.max_label.setText(str(int(data[head[1]].max())))
        #         # print(self.max_label.text())
                    
        #     self.hz_slider.setLow((int(data[head[1]].min())))
        #     self.hz_slider.setHigh((int(data[head[1]].max())))
        # except:
        #     print("error")
        try:
            for i in head:
                if i in tableManage.TableView.measList:
                    # print(i)
                    if len(data) > 1:
                        print(i)
                        self.num_min.setText(str(data[i].min()))
                        # print(self.num_min.text())
                        self.num_max.setText(str(data[i].max()))
                        # print(self.num_max.text())
                        self.min_label.setText(str(int(data[i].min())))
                        # print(self.min_label.text())
                        self.max_label.setText(str(int(data[i].max())))
                        # print(self.max_label.text())
                    
                    self.hz_slider.setLow((int(data[i].min())))
                    self.hz_slider.setHigh((int(data[i].max())))
        except:
            print("error")

     

    def meas_row(self):
        #marks selected
        data = self.fin_mark()
        # data = self.fin_mark()
        head = list(data.head(0))
        print(head)
        try:
            for i in head:
                # print('1', i)
                if i in tableManage.TableView.measList:
                    # print('2', i)
                    if len(data) > 1:
                        # print('hey', i)
                        self.num_min.setText(str(data[i].min()))
                        # print(self.num_min.text())
                        self.num_max.setText(str(data[i].max()))
                        # print(self.num_max.text())
                        self.min_label.setText(str(int(data[i].min())))
                        # print(self.min_label.text())
                        self.max_label.setText(str(int(data[i].max())))
                        # print(self.max_label.text())
                    
                    self.hz_slider.setLow((int(data[i].min())))
                    self.hz_slider.setHigh((int(data[i].max())))
        except:
            print("error")