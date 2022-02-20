import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox
from PyQt5.QtCore import QRect
import mainpage
import tableManage
import pandas as pd

class ChartView(QWidget):
    def __init__(self, parent = None):
        # self.fig = Figure(figsize=(4.5, 4.3), dpi=100)
        super().__init__(parent)

        fig = Figure(figsize=(4.5, 4.3))
        self.canvas = FigureCanvas(fig)
        self.axes = self.canvas.figure.add_subplot(111)
        # self.axes = self.fig.add_subplot(111)


        # FigureCanvas.__init__(self, self.fig)
        # self.setParent(parent)

        self.gr_combo = QComboBox(self)
        self.gr_combo.setGeometry(300,0,220,22)
        self.gr_combo.setEditable(False)
        self.gr_combo.addItem('NONE')
        self.gr_combo.addItem('BAR chart')
        self.gr_combo.addItem('PIE chart')
        self.gr_combo.addItem('LINE chart')


        self.button_showdata = QPushButton('Plot',self)
        self.button_showdata.move(550,0)
        self.button_showdata.clicked.connect(self.show_graph)
        self.button_showdata.setToolTip("Show graph from selected data")
        self.button_showdata.show()

        grlay = QVBoxLayout(self)
        grlay.addWidget(self.canvas)
        grlay.addWidget(self.gr_combo)
        grlay.addWidget(self.button_showdata)

    def show_graph(self):
        if self.gr_combo.currentText() == 'NONE' :
            pass

        elif self.gr_combo.currentText() == 'BAR chart' :
            data = {"Production":[10000, 12000, 14000],"Sales":[9000, 10500, 12000]}
            index = ["2017", "2018", "2019"]
            dataFrame = pd.DataFrame(data=data, index=index)
            self.barPlot(dataFrame, "barh")
            print("data in graph done")

        elif self.gr_combo.currentText() == 'PIE chart' :
            self.piePlot()
            # pass

        elif self.gr_combo.currentText() == 'LINE chart' :
            self.linePlot()


    # def barPlot(self):
    #     self.axes.cla()
    #     # bartest = self.canvas
    #     # test2 = plt.bartest()
    #     data_s_mark = tableManage.TableView.marks_set()
    #     frame_data = pd.DataFrame.from_dict(data_s_mark)
    #     # test = tableManage.TableView.get_dim()
    #     # print("BELOW")
    #     # print(test)
    #     print("bar chart!")
    #     print("clear!")
    #     data = mainpage.mt.meas_box.selectedItems()
    #     # data = tableManage.TableView.get_rowlist()
    #     select_toppic = []
    #     for i in range(len(data)):#measure select
    #         select_toppic.append(str(mainpage.mt.meas_box.selectedItems()[i].text()))
    #     labels = []
    #     u = []
    #     row_file_read = len(frame_data)
    #     for m in range(row_file_read):#data plot
    #         k = ""      
    #         for n, key in enumerate(frame_data.keys()):
                
    #             if key in select_toppic:
    #                 u.append(frame_data[key][m])
    #             else:    
    #                 k += (frame_data[key][m])
    #         labels.append(k)
    #     # self.axes.bar(labels, u)
    #     self.canvas.figure.tight_layout()
    #     self.canvas.bar(labels, u)
    #     # self.canvas.draw()
    #     # self.canvas.figure.bar(labels, u)


    def piePlot(self):
        pass


    def linePlot(self):
        pass


    def barPlot(self, _dataframe, typebar):
        print("bar plot here")
        self.axes.cla()
        print("aaaaa")
        _dataframe.plot(kind=typebar, ax=self.canvas.figure.gca())
        print("MOMMY LOVE YAE")
        if typebar == "barh":
            self.canvas.figure.gca().invert_yaxis()
            print("hey")

        else:
            self.canvas.figure.gca()
            print("hi")

        self.axes.legend()
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        print("FINISH!")
