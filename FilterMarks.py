from PyQt5 import QtCore, QtGui, QtWidgets
import tableManage
import mainpage


class Ui_FilterMark(object):

    def setupUi(self, FilterMark):
        FilterMark.setObjectName("FilterMark")
        FilterMark.resize(403, 151)
        self.conf_bttn = QtWidgets.QPushButton(FilterMark)
        self.conf_bttn.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.conf_bttn.setObjectName("conf_bttn")

        self.canc_bttn = QtWidgets.QPushButton(FilterMark)
        self.canc_bttn.setGeometry(QtCore.QRect(200, 100, 75, 23))
        self.canc_bttn.setObjectName("canc_bttn")
        self.canc_bttn.clicked.connect(FilterMark.close)
        
        self.min_label = QtWidgets.QLabel(FilterMark)
        self.min_label.setGeometry(QtCore.QRect(20, 70, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.min_label.setFont(font)
        self.min_label.setObjectName("min_label")

        self.max_label = QtWidgets.QLabel(FilterMark)
        self.max_label.setGeometry(QtCore.QRect(270, 70, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.max_label.setFont(font)
        self.max_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.max_label.setObjectName("max_label")

        self.num_min = QtWidgets.QLineEdit(FilterMark)
        self.num_min.setGeometry(QtCore.QRect(20, 30, 151, 21))
        self.num_min.setObjectName("num_min")

        self.num_max = QtWidgets.QLineEdit(FilterMark)
        self.num_max.setGeometry(QtCore.QRect(230, 30, 151, 21))
        self.num_max.setObjectName("num_max")

        self.retranslateUi(FilterMark)
        QtCore.QMetaObject.connectSlotsByName(FilterMark)

    def retranslateUi(self, FilterMark):
        _translate = QtCore.QCoreApplication.translate
        FilterMark.setWindowTitle(_translate("FilterMark", "Filter Window"))
        self.conf_bttn.setText(_translate("FilterMark", "Confirm"))
        self.canc_bttn.setText(_translate("FilterMark", "Cancle"))



    def fin_mark(self):
        data_file = mainpage.mt.data_box.selectedItems()
        file_read = tableManage.TableView.read_data(data_file)
        row_list,column_list = tableManage.TableView.row_column_list()
        # print('row list', row_list)
        # print('col_list', column_list)

        list_dim,list_meas,self.list_mark,list_filter = tableManage.TableView.dim_meas_rc(row_list,column_list)
        print(list_dim,list_meas,self.list_mark,list_filter)

        if len(self.list_mark) == 0 and len(list_meas) == 0:
                frame_merge = tableManage.TableView.show_dim_meas(file_read,list_dim,list_meas,list_filter)
        else:
                frame_merge = tableManage.TableView.check_mark(file_read,list_dim,list_meas,self.list_mark,list_filter)
            
        frame_data = tableManage.TableView.filter_add(frame_merge)
        # print('frame', frame_data)
        return frame_data


    def meas_col(self):
        data = self.fin_mark()
        print('col', data)
        head = list(data.head(0))
        # print('head', head)

        for sele_col in mainpage.mt.col_box.selectedItems():
            col_sele_data = sele_col.text()
            # print('sele', col_sele_data)

        if col_sele_data.find('.') >= 1:
            print('found . ')
            new_col_sp = col_sele_data.split('.')
            # print('new sp', new_col_sp)

            sele_data_new = ""
            # print('list', self.list_mark)
            for a in self.list_mark:
                if a == new_col_sp[0]:
                    sele_data_new = a + '.' + new_col_sp[1]
                    # print('data new', sele_data_new)

            for j in head:
                # print('j',j)
                if j == sele_data_new:
                    if len(data) > 1:
                        # print('j again',j)
                        self.num_min.setText(str(data[j].min()))
                        self.num_max.setText(str(data[j].max()))
                        self.min_label.setText(str(int(data[j].min())))
                        self.max_label.setText(str(int(data[j].max())))

        else:
            print('else')
            list_sele_col = []
            list_sele_col.append(col_sele_data)
            # print(list_sele_col)

            sele_data_new = ""
            sele_data_new = 'SUM' + '.' + list_sele_col[0]
            # print('data new', sele_data_new)

            for j in head:
                # print('j',j)
                if j == sele_data_new:
                    if len(data) > 1:
                        # print('j again',j)
                        self.num_min.setText(str(data[j].min()))
                        self.num_max.setText(str(data[j].max()))
                        self.min_label.setText(str(int(data[j].min())))
                        self.max_label.setText(str(int(data[j].max())))


     

    def meas_row(self):
        data = self.fin_mark()
        print('row', data)
        head = list(data.head(0))

        for sele_row in mainpage.mt.row_box.selectedItems():
            row_sele_data = sele_row.text()

        if row_sele_data.find('.') >= 1:
            print('found . ')
            new_row_sp = row_sele_data.split('.')

            sele_data_new = ""
            for a in self.list_mark:
                if a == new_row_sp[0]:
                    sele_data_new = a + '.' + new_row_sp[1]

            for j in head:
                if j == sele_data_new:
                    if len(data) > 1:
                        self.num_min.setText(str(data[j].min()))
                        self.num_max.setText(str(data[j].max()))
                        self.min_label.setText(str(data[j].min()))
                        self.max_label.setText(str(data[j].max()))

        else:
            print('else')
            list_sele_row = []
            list_sele_row.append(row_sele_data)

            sele_data_new = ""
            sele_data_new = 'SUM' + '.' + list_sele_row[0]

            for j in head:
                if j == sele_data_new:
                    if len(data) > 1:
                        self.num_min.setText(str(data[j].min()))
                        self.num_max.setText(str(data[j].max()))
                        self.min_label.setText(str(data[j].min()))
                        self.max_label.setText(str(data[j].max()))