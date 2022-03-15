from tabnanny import check
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
# from soupsieve import select
import tableManage
import graphManage
import graphEngine
from filterGUI import Ui_FilterWindow
from marksGUI import Ui_MarkWindow
from FilterMarks import Ui_FilterMark
import sys
import json
import hashlib

class mainTableau(QtWidgets.QMainWindow):
    dictpathfile = {}
    unionpathfile = {}
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1325, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.data_label = QtWidgets.QLabel(self.centralwidget)
        self.data_label.setGeometry(QtCore.QRect(10, 10, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_label.setFont(font)
        self.data_label.setObjectName("data_label")

        self.data_box = QtWidgets.QListWidget(self.centralwidget)
        self.data_box.setGeometry(QtCore.QRect(10, 30, 471, 91))
        self.data_box.setObjectName("data_box")
        self.data_box.clicked.connect(tableManage.TableView.reset_data)
        self.data_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.data_box.installEventFilter(self)

        self.dim_label = QtWidgets.QLabel(self.centralwidget)
        self.dim_label.setGeometry(QtCore.QRect(10, 130, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dim_label.setFont(font)
        self.dim_label.setObjectName("dim_label")

        self.dim_box = QtWidgets.QListWidget(self.centralwidget)
        self.dim_box.setGeometry(QtCore.QRect(10, 160, 211, 211))
        self.dim_box.setObjectName("dim_box")
        self.dim_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.dim_box.setDragEnabled(True)
        # self.dim_box.setAcceptDrops(False)
        self.dim_box.setAcceptDrops(False)
        self.dim_box.installEventFilter(self)
        # self.dim_box.clicked.connect(tableManage.TableView.dim_select)
        # self.dim_box.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.meas_label = QtWidgets.QLabel(self.centralwidget)
        self.meas_label.setGeometry(QtCore.QRect(10, 380, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.meas_label.setFont(font)
        self.meas_label.setObjectName("meas_label")

        self.meas_box = QtWidgets.QListWidget(self.centralwidget)
        self.meas_box.setGeometry(QtCore.QRect(10, 410, 211, 211))
        self.meas_box.setObjectName("meas_box")
        # self.meas_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # self.meas_box.clicked.connect(tableManage.TableView.measure_select)
        self.meas_box.setDragEnabled(True)
        self.meas_box.setAcceptDrops(False)
        # self.meas_box.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.uni_label = QtWidgets.QLabel(self.centralwidget)
        self.uni_label.setGeometry(QtCore.QRect(250, 135, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uni_label.setFont(font)
        self.uni_label.setObjectName("uni_label")

        self.uni_box = QtWidgets.QListWidget(self.centralwidget)
        self.uni_box.setGeometry(QtCore.QRect(250, 160, 231, 111))
        self.uni_box.setObjectName("uni_box")

        self.uni_button = QtWidgets.QPushButton(self.centralwidget)
        self.uni_button.setGeometry(QtCore.QRect(320, 280, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.uni_button.setFont(font)
        self.uni_button.setObjectName("uni_button")
        # self.uni_button.clicked.connect(tableManage.TableView.marks_set)

        self.col_label = QtWidgets.QLabel(self.centralwidget)
        self.col_label.setGeometry(QtCore.QRect(510, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.col_label.setFont(font)
        self.col_label.setObjectName("col_label")

        self.row_label = QtWidgets.QLabel(self.centralwidget)
        self.row_label.setGeometry(QtCore.QRect(510, 90, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.row_label.setFont(font)
        self.row_label.setObjectName("row_label")

        self.col_box = QtWidgets.QListWidget(self.centralwidget)
        self.col_box.setGeometry(QtCore.QRect(590, 30, 621, 21))
        self.col_box.setObjectName("col_box")
        self.col_box.setDragEnabled(True)
        self.col_box.setAcceptDrops(True)
        self.col_box.installEventFilter(self)
        self.col_box.itemDoubleClicked.connect(self.col_box.clearSelection)
        self.col_box.setViewMode(QtWidgets.QListWidget.IconMode)
        self.col_box.setDefaultDropAction(QtCore.Qt.MoveAction)
        # self.col_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        self.row_box = QtWidgets.QListWidget(self.centralwidget)
        self.row_box.setGeometry(QtCore.QRect(590, 90, 621, 21))
        self.row_box.setObjectName("row_box")
        self.row_box.setDragEnabled(True)
        self.row_box.setAcceptDrops(True)
        self.row_box.installEventFilter(self)
        self.row_box.itemDoubleClicked.connect(self.row_box.clearSelection)
        self.row_box.setViewMode(QtWidgets.QListWidget.IconMode)  
        self.row_box.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.col_box.clicked.connect(self.row_box.clearSelection)
        self.row_box.clicked.connect(self.col_box.clearSelection)

        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(500, 140, 791, 471))
        self.tabs.setObjectName("tabs")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")

        self.table_box = QtWidgets.QTableWidget(self.tab1)
        self.table_box.setGeometry(QtCore.QRect(0, 0, 781, 441))
        self.table_box.setObjectName("table_box")
        self.table_box.setColumnCount(0)
        self.table_box.setRowCount(0)

        self.tabs.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.widget_graph = QtWidgets.QWidget(self.tab2)
        self.widget_graph.setGeometry(QtCore.QRect(0, 10, 781, 361))
        self.widget_graph.setObjectName("widget_graph")


        self.show_chart = graphEngine.WebEngineView()
        self.plot_box = QtWidgets.QVBoxLayout() #set box for plot graph
        self.plot_box.addWidget(self.show_chart)
        self.widget_graph.setLayout(self.plot_box)


        self.button_showdata = QtWidgets.QPushButton(self.tab2)
        self.button_showdata.setGeometry(QtCore.QRect(690, 410, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button_showdata.setFont(font)
        self.button_showdata.setObjectName("button_showdata")
        self.gr_combo = QtWidgets.QComboBox(self.tab2)
        self.gr_combo.setGeometry(QtCore.QRect(690, 380, 91, 21))
        self.gr_combo.setObjectName("gr_combo")
        self.gr_combo.addItem("")
        self.gr_combo.addItem("")
        self.gr_combo.addItem("")
        self.gr_combo.addItem("")
        self.tabs.addTab(self.tab2, "")

        self.del_col = QtWidgets.QPushButton(self.centralwidget)
        self.del_col.setGeometry(QtCore.QRect(1220, 30, 61, 28))
        self.del_col.setObjectName("del_col")
        self.del_col.clicked.connect(self.delete_column)

        self.del_row = QtWidgets.QPushButton(self.centralwidget)
        self.del_row.setGeometry(QtCore.QRect(1220, 90, 61, 28))
        self.del_row.setObjectName("del_row")
        self.del_row.clicked.connect(self.delete_row)

        self.fil_label = QtWidgets.QLabel(self.centralwidget)
        self.fil_label.setGeometry(QtCore.QRect(250, 310, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fil_label.setFont(font)
        self.fil_label.setObjectName("fil_label")

        self.fil_box = QtWidgets.QListWidget(self.centralwidget)
        self.fil_box.setGeometry(QtCore.QRect(250, 330, 231, 101))
        self.fil_box.setObjectName("fil_box")
        self.fil_box.setDragEnabled(True)
        self.fil_box.setAcceptDrops(False)
        self.fil_box.itemDoubleClicked.connect(self.fil_box.clearSelection)
        # self.fil_box.setViewMode(QtWidgets.QListWidget.IconMode)
        # self.fil_box.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.drill_label = QtWidgets.QLabel(self.centralwidget)
        self.drill_label.setGeometry(QtCore.QRect(250, 440, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.drill_label.setFont(font)
        self.drill_label.setObjectName("drill_label")

        self.drill_box = QtWidgets.QListWidget(self.centralwidget)
        self.drill_box.setGeometry(QtCore.QRect(250, 470, 231, 101))
        self.drill_box.setObjectName("drill_box")
        self.drill_box.setDragEnabled(True)
        self.drill_box.setAcceptDrops(False)
        self.drill_box.installEventFilter(self)


        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(320, 590, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.button.clicked.connect(tableManage.TableView.show_data)

        MainWindow.setCentralWidget(self.centralwidget)
        self.mainMenu = QtWidgets.QMenuBar(MainWindow)
        self.mainMenu.setGeometry(QtCore.QRect(0, 0, 1325, 21))
        self.mainMenu.setObjectName("mainMenu")
        self.fileMenu = QtWidgets.QMenu(self.mainMenu)
        self.fileMenu.setObjectName("fileMenu")
        MainWindow.setMenuBar(self.mainMenu)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.impMenu = QtWidgets.QAction(MainWindow)
        self.impMenu.setObjectName("impMenu")
        self.impMenu.triggered.connect(tableManage.TableView.importFile)
        self.expMenu = QtWidgets.QAction(MainWindow)
        self.expMenu.setObjectName("expMenu")
        self.fileMenu.addAction(self.impMenu)
        self.fileMenu.addAction(self.expMenu)
        self.mainMenu.addAction(self.fileMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.button_showdata.clicked.connect(graphManage.GraphView)
        self.button_showdata.clicked.connect(graphManage.GraphView.fill_data)

        self.FilterPage = QtWidgets.QMainWindow()
        self.ui = Ui_FilterWindow()
        self.ui.setupUi(self.FilterPage)


        self.MarkPage = QtWidgets.QMainWindow()
        self.ui2 = Ui_MarkWindow()
        self.ui2.setupUi(self.MarkPage)
        self.ui2.mark_menu.currentTextChanged.connect(self.get_marks)


        self.FilterMark = QtWidgets.QMainWindow()
        self.ui3 = Ui_FilterMark()
        self.ui3.setupUi(self.FilterMark)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tableau"))
        self.data_label.setText(_translate("MainWindow", "Data"))
        self.dim_label.setText(_translate("MainWindow", "Dimensions"))
        self.meas_label.setText(_translate("MainWindow", "Measures"))
        self.uni_label.setText(_translate("MainWindow", "Union File"))
        self.uni_button.setText(_translate("MainWindow", "Union File"))
        self.col_label.setText(_translate("MainWindow", "Colunms"))
        self.row_label.setText(_translate("MainWindow", "Rows"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab1), _translate("MainWindow", "Data table viewer"))
        self.button_showdata.setText(_translate("MainWindow", "Plot"))
        self.gr_combo.setItemText(0, _translate("MainWindow", "NONE"))
        self.gr_combo.setItemText(1, _translate("MainWindow", "BAR chart"))
        self.gr_combo.setItemText(2, _translate("MainWindow", "PIE chart"))
        self.gr_combo.setItemText(3, _translate("MainWindow", "LINE chart"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab2), _translate("MainWindow", "Data graph viewer"))
        self.del_col.setText(_translate("MainWindow", "Del"))
        self.del_row.setText(_translate("MainWindow", "Del"))
        self.fil_label.setText(_translate("MainWindow", "Filters"))
        self.drill_label.setText(_translate("MainWindow", "Drill Down"))
        self.button.setText(_translate("MainWindow", "Data List"))
        self.fileMenu.setTitle(_translate("MainWindow", "File"))
        self.impMenu.setText(_translate("MainWindow", "Import"))
        self.expMenu.setText(_translate("MainWindow", "Export"))


    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.col_box):
            self.index = source.currentIndex().row()
            item_col = self.col_box.item(self.index).text()
            if item_col.find(".") >= 1:
                new_item_col = item_col.split(".")
                print(new_item_col)
                if new_item_col[1] in tableManage.TableView.measList:
                    self.menuCol = QtWidgets.QMenu()
                    self.menuCol.addAction('Marks')
                    self.menuCol.addAction('Filter')
                    self.menuCol.addAction('Delete')
                    self.menuCol.triggered.connect(self.actionCol)

            else:
                if item_col in tableManage.TableView.dimList:
                    self.menuCol = QtWidgets.QMenu()
                    self.menuCol.addAction('Filters')
                    self.menuCol.addAction('Delete')
                    if "DATE" in item_col.upper():
                        self.menuCol.addAction('Year')
                        # self.menuCol.triggered.connect(self.check_ok)
                        self.menuCol.addAction('Month')
                        self.menuCol.addAction('Date')
                    self.menuCol.triggered.connect(self.actionCol)
                elif item_col in tableManage.TableView.measList:
                    self.menuCol = QtWidgets.QMenu()
                    self.menuCol.addAction('Marks')
                    self.menuCol.addAction('Filter')
                    self.menuCol.addAction('Delete')
                    self.menuCol.triggered.connect(self.actionCol)

                elif item_col.find("+") >= 1:
                    print('here')
                    new_item_col = item_col.split("+")
                    self.menuCol = QtWidgets.QMenu()
                    self.menuCol.addAction('Drill down')
                    self.menuCol.addAction('Filters')
                    if "DATE" in new_item_col[0].upper():
                        self.menuCol.addAction('Year')
                        self.menuCol.addAction('Month')
                        self.menuCol.addAction('Date')
                    self.menuCol.addAction('Delete')
                    self.menuCol.triggered.connect(self.actionCol)

            if self.menuCol.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
            return True


        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.row_box):
            self.index = source.currentIndex().row()
            item_rox = self.row_box.item(self.index).text()

            if item_rox.find(".") >= 1:
                new_item_row = item_rox.split(".")
                if new_item_row[1] in tableManage.TableView.measList:
                    self.menuRow = QtWidgets.QMenu()
                    self.menuRow.addAction('Marks')
                    self.menuRow.addAction('Filter')
                    self.menuRow.addAction('Delete')
                    self.menuRow.triggered.connect(self.actionRow)

            else:
                if item_rox in tableManage.TableView.dimList:
                    self.menuRow = QtWidgets.QMenu()
                    self.menuRow.addAction('Filters')
                    self.menuRow.addAction('Delete')
                    if "DATE" in item_rox.upper():
                        self.menuRow.addAction('Year')
                        # self.menuCol.triggered.connect(self.check_ok)
                        self.menuRow.addAction('Month')
                        self.menuRow.addAction('Date')
                    self.menuRow.triggered.connect(self.actionRow)
                elif item_rox in tableManage.TableView.measList:
                    self.menuRow = QtWidgets.QMenu()
                    self.menuRow.addAction('Marks')
                    self.menuRow.addAction('Filter')
                    self.menuRow.addAction('Delete')
                    self.menuRow.triggered.connect(self.actionRow)

                elif item_rox.find("+") >= 1:
                    print('here')
                    new_item_row = item_rox.split("+")
                    self.menuRow = QtWidgets.QMenu()
                    self.menuRow.addAction('Drill down')
                    self.menuRow.addAction('Filters')
                    if "DATE" in new_item_row[0].upper():
                        self.menuRow.addAction('Year')
                        self.menuRow.addAction('Month')
                        self.menuRow.addAction('Date')
                    self.menuRow.addAction('Delete')
                    self.menuRow.triggered.connect(self.actionRow)

            if self.menuRow.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
            return True
        
        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.dim_box):
            self.index = source.currentIndex().row()
            item_dim = self.dim_box.item(self.index).text()
            if len(self.dim_box.selectedItems()) == 1:
                if self.dim_box.item(self.index).text().find("+") >= 1:
                    self.menuDim = QtWidgets.QMenu()
                    self.menuDim.addAction('Delete')
                    self.menuDim.triggered.connect(self.actionDim)
                else:
                    self.menuDim = QtWidgets.QMenu()
            elif len(self.dim_box.selectedItems()) >= 2:
                self.menuDim = QtWidgets.QMenu()
                self.menuDim.addAction('Add')
                # self.menuDim.addAction('Delete')
                self.menuDim.triggered.connect(self.actionDim)

            if self.menuDim.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
            return True

        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.drill_box):
            self.index = source.currentIndex().row()
            item_dim = self.drill_box.item(self.index).text()
            self.menudrill_box = QtWidgets.QMenu()           
            self.menudrill_box.addAction('Delete')
            self.menudrill_box.triggered.connect(self.actionDrill)

            if self.menudrill_box.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                
            return True
        
        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.data_box):
            self.index = source.currentIndex().row()
            item_dim = self.data_box.item(self.index).text()
            self.menudata_box = QtWidgets.QMenu()           
            self.menudata_box.addAction('Delete')
            self.menudata_box.triggered.connect(self.actionDatabox)

            if self.menudata_box.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                
            return True

        return super(mainTableau, self).eventFilter(source, event)

    # def check_ok(self):
    #     print("Ok")
    
    def actionCol(self, action):
        if action.text() == "Filters":
            self.FilterPage.show()
            col_select = str(self.col_box.selectedItems()[0].text())
            fil_list_data = tableManage.TableView.fil_select_dim(col_select)
            print("fil_list_data",fil_list_data)
            file_filter_check = tableManage.TableView.list_filter_dim(fil_list_data,col_select)
            print("file_filter_check",file_filter_check)
            self.insert_filter(fil_list_data,file_filter_check)
            # print(col_select)
            # print(fil_list_data)

        elif action.text() == "Marks":
            self.MarkPage.show()

        elif action.text() == "Filter":
            self.ui3.meas_col()
            self.FilterMark.show()

        elif action.text() == "Delete":
            self.col_box.takeItem(self.index)

        elif action.text() == "Drill down":
            new_gr_dim = ""
            self.gr_dim_select = self.col_box.item(self.index).text()
            print(self.gr_dim_select)
            self.group_data = self.gr_dim_select.split("+")
            print('group', self.group_data)
            if len(self.group_data) > 2:
                _group = self.group_data[1:]
                for i in _group:
                    new_gr_dim += i + "+"
                new_gr_dim = new_gr_dim[:-1]
                # self.col_box.addItem(new_gr_dim)
                self.col_box.insertItem(self.index + 1, new_gr_dim)
            elif len(self.group_data) == 2:
                # self.col_box.addItem(self.group_data[1])
                self.col_box.insertItem(self.index + 1, self.group_data[1])


        elif action.text() == "Year":
            # print("OK! year")
            self.data_status = "Year"
            self.check_gr_data()
        
        elif action.text() == "Month":
            # print("OK! month")
            self.data_status = "Month"
            self.check_gr_data()

        elif action.text() == "Date":
            # print("OK! date")
            self.data_status = "Date"
            self.check_gr_data()

            
    def actionRow(self, action):
        if action.text() == "Filters":
            self.FilterPage.show()
            row_select = str(self.row_box.selectedItems()[0].text())            
            fil_list_data = tableManage.TableView.fil_select_dim(row_select)
            file_filter_check = tableManage.TableView.list_filter_dim(fil_list_data,row_select)
            self.insert_filter(fil_list_data,file_filter_check)
            # print(fil_list_data)
            # print(row_select)

        elif action.text() == "Marks":
            self.MarkPage.show()

        elif action.text() == "Filter":
            self.ui3.meas_row()
            self.FilterMark.show()

        elif action.text() == "Delete":
            self.row_box.takeItem(self.index)

        elif action.text() == "Drill down":
            new_gr_dim = ""
            self.gr_dim_select = self.row_box.item(self.index).text()
            print(self.gr_dim_select)
            self.group_data = self.gr_dim_select.split("+")
            print('group', self.group_data)
            if len(self.group_data) > 2:
                _group = self.group_data[1:]
                for i in _group:
                    new_gr_dim += i + "+"
                new_gr_dim = new_gr_dim[:-1]
                self.row_box.insertItem(self.index + 1, new_gr_dim)
            elif len(self.group_data) == 2:
                self.row_box.insertItem(self.index + 1, self.group_data[1])
        
        # elif action.text() == "Year" or "Month" or "Date":
        #     print("OK! year month date")
        #     self.get_datetime()

        elif action.text() == "Year":
            print("OK! year")
            self.data_status = "Year"
            self.check_gr_data()
        
        elif action.text() == "Month":
            print("OK! month")
            self.data_status = "Month"
            self.check_gr_data()

        elif action.text() == "Date":
            print("OK! date")
            self.data_status = "Date"
            self.check_gr_data()

    def actionDrill(self, action):
        if action.text() == "Delete":
            item = self.drill_box.item(self.index).text()
            tableManage.TableView.del_list_drilldown(item)
            self.drill_box.takeItem(self.index)
    
    def actionDatabox(self, action):
        if action.text() == "Delete":
            item = self.data_box.item(self.index).text()
            self.data_box.takeItem(self.index)
            self.table_box.clear()
            self.table_box.setRowCount(0)
            self.dim_box.clear()
            self.meas_box.clear()
            self.row_box.clear()
            self.col_box.clear()
            self.fil_box.clear()
            self.drill_box.clear()

    def actionDim(self, action):
        if action.text() == "Delete":
            self.dim_box.takeItem(self.index)
            self.drill_box.takeItem(self.index)

        elif action.text() == "Add":
            self.dim_item = ""
            self.gr_dim = []
            for i in self.dim_box.selectedItems():
                # print('dim se', i)
                self.dim_item += i.text() + "+"
                # print('dim item', self.dim_item)
            self.dim_item = self.dim_item[:-1]
            # print('dim item2', self.dim_item)
            i = QtWidgets.QListWidgetItem(self.dim_item)
            self.dim_box.addItem(i)
            self.dim_box.clearSelection()



    def get_marks(self):
        self.status = self.ui2.mark_menu.currentText()
        # print('status', self.status)


    def set_marks(self):
        # if self.col_box.selectedItems() and self.data_c in tableManage.TableView.measList:
        if self.col_box.selectedItems():
            # print('col box se', str(self.col_box.selectedItems()) )
            # self.row_box.clearSelection()
            for i in self.col_box.selectedItems():
                self.old_data = i.text()
                # print('self.old_data', self.old_data)
            bef_list = []
            bef_list.append(self.col_box.item(self.index).text())
            # print('bef_list', bef_list)
            now_list = []
            for k in range(len(bef_list)):
                if self.old_data == bef_list[k]:
                    if self.status == 'NONE':
                        data_sp = self.old_data.split('.')
                        # print('data_sp', data_sp)
                        if len(data_sp) == 1:
                            now_list.append(data_sp[0])
                        else:
                            now_list.append(data_sp[1])
                    else:
                        data_sp = self.old_data.split('.')
                        # print('data_sp', data_sp)
                        if len(data_sp) == 1:
                            now_list.append(self.status + '.' + data_sp[0])
                        else:
                            now_list.append(self.status + '.' + data_sp[1])
                else:
                    now_list.append(bef_list[k])
            # self.col_box.clear()
            for m in range(len(now_list)):
                self.col_box.takeItem(self.index)
                self.col_box.insertItem(self.index, str(now_list[m]))
                self.col_box.clearSelection()

        elif self.row_box.selectedItems():
            # print('row box se', str(self.row_box.selectedItems()))
            # self.col_box.clearSelection()
            for i in self.row_box.selectedItems():
                self.old_data = i.text()
                # print('self.old_data', self.old_data)
            bef_list = []
            bef_list.append(self.row_box.item(self.index).text())
            # print('bef_list', bef_list)
            now_list = []
            for k in range(len(bef_list)):
                if self.old_data == bef_list[k]:
                    if self.status == 'NONE':
                        data_sp = self.old_data.split('.')
                        # print('data_sp none', data_sp)
                        if len(data_sp) == 1:
                            now_list.append(data_sp[0])
                        else:
                            now_list.append(data_sp[1])
                    else:
                        data_sp = self.old_data.split('.')
                        # print('data_sp', data_sp)
                        if len(data_sp) == 1:
                            now_list.append(self.status + '.' + data_sp[0])
                            # print('0', now_list)
                        else:
                            now_list.append(self.status + '.' + data_sp[1])
                            # print('1', now_list)
                else:
                    now_list.append(bef_list[k])
                    # print('not k', now_list)
            # print('row', self.row_box)        
            # self.row_box.clear()
            for m in range(len(now_list)):
                self.row_box.takeItem(self.index)
                self.row_box.insertItem(self.index, str(now_list[m]))
                self.row_box.clearSelection()
                # print('fin row', self.row_box)
    
    def check_gr_data(self):
        self.found_plus = False
        if self.col_box.selectedItems():
            # print('ok get', self.col_box.selectedItems())
            if self.col_box.item(self.index).text().find("+") >= 1:
                self.found_plus = True
                print("found +")
                self.set_datetime()
            else:
                print("not found +")
                self.set_datetime()

        elif self.row_box.selectedItems():
            # print('ok get', self.col_box.selectedItems())
            if self.row_box.item(self.index).text().find("+") >= 1:
                self.found_plus = True
                print("found +")
                self.set_datetime()
            else:
                print("not found +")
                self.set_datetime()

    def set_datetime(self):
        if self.col_box.selectedItems():
            if self.found_plus == False:
                for i in self.col_box.selectedItems():
                    self.old_data = i.text()
                print('old', self.old_data)
                bef_list = []
                bef_list.append(self.col_box.item(self.index).text())
                # print(bef_list)
                now_list = []
                for k in range(len(bef_list)):
                    if self.old_data == bef_list[k]:
                        data_ymd_sp = self.old_data.split('.')
                        print('hey', data_ymd_sp)
                        if len(data_ymd_sp) == 1:
                            now_list.append(self.data_status + '.' + data_ymd_sp[0])
                            print(now_list)
                        else:
                            now_list.append(self.data_status + '.' + data_ymd_sp[1])
                            # print('2', now_list)
                for m in range(len(now_list)):
                    self.col_box.takeItem(self.index)
                    self.col_box.insertItem(self.index, str(now_list[m]))
                    self.col_box.clearSelection()

            elif self.found_plus == True:
                self.gr_data_set = ""
                self.data_set = self.col_box.item(self.index).text()
                self.gr_data_set = self.data_set.split("+")
                bef_list = []
                bef_list.append(self.gr_data_set[0])
                now_list = []
                for k in range(len(bef_list)):
                    if self.gr_data_set[0] == bef_list[k]:
                        data_ymd_sp = self.gr_data_set[0].split('.')
                        if len(data_ymd_sp) == 1:
                            now_list.append(self.data_status + '.' + self.data_set)
                        else:
                            data_ymd_sp = self.data_set.split('.')
                            now_list.append(self.data_status + '.' + data_ymd_sp[1])
                for m in range(len(now_list)):
                    self.col_box.takeItem(self.index)
                    self.col_box.insertItem(self.index, str(now_list[m]))
                    self.col_box.clearSelection()


        elif self.row_box.selectedItems():
            if self.found_plus == False:
                for i in self.row_box.selectedItems():
                    self.old_data = i.text()
                bef_list = []
                bef_list.append(self.row_box.item(self.index).text())
                now_list = []
                for k in range(len(bef_list)):
                    if self.old_data == bef_list[k]:
                        print(bef_list[k])
                        data_ymd_sp = self.old_data.split('.')
                        # print('data_sp', data_ymd_sp)
                        # print('len', len(data_ymd_sp))
                        if len(data_ymd_sp) == 1:
                            print(data_ymd_sp[0])
                            now_list.append(self.data_status + '.' + data_ymd_sp[0])
                        else:
                            print(data_ymd_sp[1])
                            now_list.append(self.data_status + '.' + data_ymd_sp[1])
                    else:
                        # print("last")
                        now_list.append(bef_list[k])
                for m in range(len(now_list)):
                    self.row_box.takeItem(self.index)
                    self.row_box.insertItem(self.index, str(now_list[m]))
                    self.row_box.clearSelection()

            elif self.found_plus == True:
                self.gr_data_set = ""
                self.data_set = self.row_box.item(self.index).text()
                self.gr_data_set = self.data_set.split("+")
                bef_list = []
                bef_list.append(self.gr_data_set[0])
                now_list = []
                for k in range(len(bef_list)):
                    if self.gr_data_set[0] == bef_list[k]:
                        data_ymd_sp = self.gr_data_set[0].split('.')
                        if len(data_ymd_sp) == 1:
                            now_list.append(self.data_status + '.' + self.data_set)
                        else:
                            data_ymd_sp = self.data_set.split('.')
                            now_list.append(self.data_status + '.' + data_ymd_sp[1])
                for m in range(len(now_list)):
                    self.row_box.takeItem(self.index)
                    self.row_box.insertItem(self.index, str(now_list[m]))
                    self.row_box.clearSelection()
    

    def delete_row(self):
        self.row_box.clear()
    
    def delete_column(self):
        self.col_box.clear()

    def insert_filter(self,fil_list_data,file_filter_check):
        # print("insert_filter ",fil_list_data)
        # print("insert_filter check",file_filter_check)
        self.ui.fil_data.clear()
        for a,name_data in enumerate(fil_list_data):
            toppic_ml = QtWidgets.QListWidgetItem(name_data)
            if name_data in file_filter_check:
                toppic_ml.setCheckState(QtCore.Qt.Checked)
                self.ui.fil_data.insertItem(a,toppic_ml)
            else:
                toppic_ml.setCheckState(QtCore.Qt.Unchecked)
                self.ui.fil_data.insertItem(a,toppic_ml)
    

    def confirm_filter(self):
        read_data,select_topic = tableManage.TableView.list_checkpath_filter()
        fil_list = []
        dimension,measure = tableManage.TableView.dim_meas_list()

        if self.col_box.selectedItems():
            data_select = str(self.col_box.selectedItems()[0].text())

        elif self.row_box.selectedItems():
            data_select = str(self.row_box.selectedItems()[0].text())

        if data_select in dimension:
            fil_list_data = tableManage.TableView.fil_select_dim(data_select)
            for i in range(self.ui.fil_data.count()):
                check_i = self.ui.fil_data.item(i)
                if check_i.checkState():
                    item_i = self.ui.fil_data.item(i).text()
                    fil_list.append(item_i)
            for path in select_topic:
                md5_hash = hashlib.md5()
                file_md5 = open(path, "rb")
                file_md5_read = file_md5.read()
                md5_hash.update(file_md5_read)
                code_md5 = md5_hash.hexdigest()
                if fil_list_data == fil_list:
                    if data_select in read_data[code_md5]["filter"]:
                        del read_data[code_md5]["filter"][data_select]
                else:
                    read_data[code_md5]["filter"][data_select] = fil_list
                with open('filterdata.json', 'w') as file_json:
                    json.dump(read_data, file_json)
            tableManage.TableView.filter_boxadd()


app = QtWidgets.QApplication(sys.argv)
# mt = QtWidgets.QMainWindow()
mainApp = QtWidgets.QMainWindow()
mt = mainTableau()
mt.setupUi(mainApp)
mainApp.show()
sys.exit(app.exec_())
