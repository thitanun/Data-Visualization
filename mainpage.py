from PyQt5 import QtCore, QtGui, QtWidgets
import tableManage
import graphManage
from filterGUI import Ui_FilterWindow
from marksGUI import Ui_MarkWindow
import sys

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
        self.data_box.setGeometry(QtCore.QRect(10, 30, 211, 121))
        self.data_box.setObjectName("data_box")
        self.data_box.clicked.connect(tableManage.TableView.reset_data)
        self.data_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        self.dim_label = QtWidgets.QLabel(self.centralwidget)
        self.dim_label.setGeometry(QtCore.QRect(10, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dim_label.setFont(font)
        self.dim_label.setObjectName("dim_label")

        self.dim_box = QtWidgets.QListWidget(self.centralwidget)
        self.dim_box.setGeometry(QtCore.QRect(10, 190, 211, 211))
        self.dim_box.setObjectName("dim_box")
        self.dim_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.dim_box.setDragEnabled(True)
        # self.dim_box.setAcceptDrops(False)
        self.dim_box.setAcceptDrops(True)
        self.dim_box.clicked.connect(tableManage.TableView.dim_select)
        # self.dim_box.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.meas_label = QtWidgets.QLabel(self.centralwidget)
        self.meas_label.setGeometry(QtCore.QRect(10, 410, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.meas_label.setFont(font)
        self.meas_label.setObjectName("meas_label")

        self.meas_box = QtWidgets.QListWidget(self.centralwidget)
        self.meas_box.setGeometry(QtCore.QRect(10, 440, 211, 181))
        self.meas_box.setObjectName("meas_box")
        self.meas_box.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.meas_box.clicked.connect(tableManage.TableView.measure_select)
        self.meas_box.setDragEnabled(True)
        self.meas_box.setAcceptDrops(True)
        # self.meas_box.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.uni_label = QtWidgets.QLabel(self.centralwidget)
        self.uni_label.setGeometry(QtCore.QRect(250, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uni_label.setFont(font)
        self.uni_label.setObjectName("uni_label")

        self.uni_box = QtWidgets.QListWidget(self.centralwidget)
        self.uni_box.setGeometry(QtCore.QRect(250, 30, 231, 111))
        self.uni_box.setObjectName("uni_box")

        self.uni_button = QtWidgets.QPushButton(self.centralwidget)
        self.uni_button.setGeometry(QtCore.QRect(320, 150, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.uni_button.setFont(font)
        self.uni_button.setObjectName("uni_button")
        self.uni_button.clicked.connect(tableManage.TableView.marks_set)

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
        self.col_box.setViewMode(QtWidgets.QListWidget.IconMode)
        self.col_box.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.row_box = QtWidgets.QListWidget(self.centralwidget)
        self.row_box.setGeometry(QtCore.QRect(590, 90, 621, 21))
        self.row_box.setObjectName("row_box")
        self.row_box.setDragEnabled(True)
        self.row_box.setAcceptDrops(True)
        self.row_box.installEventFilter(self)
        self.row_box.setViewMode(QtWidgets.QListWidget.IconMode)  
        self.row_box.setDefaultDropAction(QtCore.Qt.MoveAction)

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
        self.del_row = QtWidgets.QPushButton(self.centralwidget)
        self.del_row.setGeometry(QtCore.QRect(1220, 90, 61, 28))
        self.del_row.setObjectName("del_row")

        self.fil_label = QtWidgets.QLabel(self.centralwidget)
        self.fil_label.setGeometry(QtCore.QRect(250, 190, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fil_label.setFont(font)
        self.fil_label.setObjectName("fil_label")

        self.fil_box = QtWidgets.QListWidget(self.centralwidget)
        self.fil_box.setGeometry(QtCore.QRect(250, 220, 231, 101))
        self.fil_box.setObjectName("fil_box")
        self.fil_box.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.cat_label = QtWidgets.QLabel(self.centralwidget)
        self.cat_label.setGeometry(QtCore.QRect(250, 330, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cat_label.setFont(font)
        self.cat_label.setObjectName("cat_label")

        self.cat_box = QtWidgets.QListWidget(self.centralwidget)
        self.cat_box.setGeometry(QtCore.QRect(250, 360, 231, 101))
        self.cat_box.setObjectName("cat_box")
        self.cat_box.clicked.connect(tableManage.TableView.marks_set)

        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(320, 480, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.button.clicked.connect(tableManage.TableView.show_data)

        MainWindow.setCentralWidget(self.centralwidget)
        self.mainMenu = QtWidgets.QMenuBar(MainWindow)
        self.mainMenu.setGeometry(QtCore.QRect(0, 0, 1325, 26))
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

        self.FilterPage = QtWidgets.QMainWindow()
        self.ui2 = Ui_FilterWindow()
        self.ui2.setupUi(self.FilterPage)

        self.MarkPage = QtWidgets.QMainWindow()
        self.ui3 = Ui_MarkWindow()
        self.ui3.setupUi(self.MarkPage)

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
        self.cat_label.setText(_translate("MainWindow", "Marked"))
        self.button.setText(_translate("MainWindow", "Data List"))
        self.fileMenu.setTitle(_translate("MainWindow", "File"))
        self.impMenu.setText(_translate("MainWindow", "Import"))
        self.expMenu.setText(_translate("MainWindow", "Export"))


    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.col_box):
            menuCol = QtWidgets.QMenu()
            # self.fil_act = QtWidgets.QAction("Filter")
            # self.mrk_act = QtWidgets.QAction("Marks")
            menuCol.addAction("Filter")
            menuCol.addAction("Marks")
            menuCol.triggered.connect(self.show_page)
            if menuCol.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                # print(item.text())

        if (event.type() == QtCore.QEvent.ContextMenu and
            source is self.row_box):
            menuRow = QtWidgets.QMenu()
            menuRow.addAction('Filter')
            menuRow.addAction('Marks')
            if menuRow.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                # print(item.text())
        return super(mainTableau, self).eventFilter(source, event)

    
    def show_page(self, action):
        if action.text() == "Filter":
            self.FilterPage.show()
        elif action.text() == "Marks":
            self.MarkPage.show()



app = QtWidgets.QApplication(sys.argv)
# mt = QtWidgets.QMainWindow()
mainApp = QtWidgets.QMainWindow()
mt = mainTableau()
mt.setupUi(mainApp)
mainApp.show()
sys.exit(app.exec_())
