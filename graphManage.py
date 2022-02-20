import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QComboBox
import PyQt5.QtCore as qtc
import mainpage
import tableManage
import pandas as pd

class GraphView(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        # fig = Figure(figsize=(4.5, 4.3))
        # fig = Figure(figsize=(6, 3))
        fig = Figure(figsize=(8, 3.8))
        self.canvas = FigureCanvas(fig)
        self.ax = self.canvas.figure.add_subplot(111)


        self.gr_combo = QComboBox(self)
        self.gr_combo.setGeometry(300,475,220,22)
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

        self.toolbar = NavigationToolbar(self.canvas, self)

        grlay = QVBoxLayout(self)
        grlay.addWidget(self.toolbar)
        grlay.addWidget(self.canvas)
        grlay.addWidget(self.gr_combo, alignment = qtc.Qt.AlignRight)
        grlay.addWidget(self.button_showdata, alignment = qtc.Qt.AlignRight)


    def show_graph(self):
        if self.gr_combo.currentText() == 'NONE' :
            print("You didn't select data")


        elif self.gr_combo.currentText() == 'BAR chart' :
            data_s_mark = tableManage.TableView.marks_set()
            frame_data = pd.DataFrame.from_dict(data_s_mark)
            print("bar chart!")
            print("clear!")
            data = mainpage.mt.meas_box.selectedItems()
            select_toppic = []
            for i in range(len(data)):#measure select
                select_toppic.append(str(mainpage.mt.meas_box.selectedItems()[i].text()))
            labels = []
            u = []
            row_file_read = len(frame_data)
            for m in range(row_file_read):#data plot
                k = ""      
                for n, key in enumerate(frame_data.keys()):
                    
                    if key in select_toppic:
                        u.append(frame_data[key][m])
                    else:    
                        k += (frame_data[key][m])
                labels.append(k)
            dataFrame = pd.DataFrame(data=u, index=labels)
            self.barPlot(dataFrame, "barh")
            print("data in graph done")


        elif self.gr_combo.currentText() == 'PIE chart' :
            data_s_mark = tableManage.TableView.marks_set()
            frame_data = pd.DataFrame.from_dict(data_s_mark)
            print("pie chart!")
            print("clear!")
            data = mainpage.mt.meas_box.selectedItems()
            select_toppic = []
            print("pass sele")
            for i in range(len(data)):#measure select
                select_toppic.append(str(mainpage.mt.meas_box.selectedItems()[i].text()))
            labels = []
            u = []
            row_file_read = len(frame_data)
            print("pass first for")
            for m in range(row_file_read):#data plot
                k = []      
                for n, key in enumerate(frame_data.keys()):                
                    if key in select_toppic:
                        u.append(frame_data[key][m])
                    else:    
                        k.append(frame_data[key][m])
                labels.append(k)
            x = np.array(u)
            # dataFrame = pd.DataFrame(data=u, index=labels)
            self.piePlot(x, labels)
            print("DONE")


        elif self.gr_combo.currentText() == 'LINE chart' :
            print("line chart!")
            print("clear!")
            data_s_mark = tableManage.TableView.marks_set()
            frame_data = pd.DataFrame.from_dict(data_s_mark)
            data = mainpage.mt.meas_box.selectedItems()
            select_toppic = []
            for i in range(len(data)):#measure select
                select_toppic.append(str(mainpage.mt.meas_box.selectedItems()[i].text()))
            labels = []
            u = []
            row_file_read = len(frame_data)
            for m in range(row_file_read):#data plot
                k = ""      
                for n, key in enumerate(frame_data.keys()):
                    
                    if key in select_toppic:
                        u.append(frame_data[key][m])
                    else:    
                        k += (frame_data[key][m])
                labels.append(k)
            # dataFrame = pd.DataFrame(data=u, index=labels)
            self.linePlot(u, labels)
            print("data in graph done")


    def barPlot(self, _dataframe, typebar):
        print("bar plot here")
        self.ax.cla()
        _dataframe.plot(kind=typebar, ax=self.canvas.figure.gca()) #gca mean get current axis
        if typebar == "barh":
            self.canvas.figure.gca().invert_yaxis()
            
        else:
            self.canvas.figure.gca()
            print("hi")

        self.ax.legend()
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        print("FINISH!")


    def piePlot(self, datapie, index):
        print("pie plot here")
        self.ax.cla()

        self.ax.pie(datapie, labels=index, autopct = '%1.1f%%')
        self.ax.legend()
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        print("FINISH!")




    def linePlot(self, dataline, index):
        print("line plot here")
        self.ax.cla()

        self.ax.plot(dataline, index)
        self.ax.legend()
        self.canvas.figure.tight_layout()
        self.canvas.draw()
        print("FINISH!")

