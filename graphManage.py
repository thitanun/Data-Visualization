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
import altair as alt

class GraphView(QWidget):
    @classmethod
    def fill_data(self):
        print('starting graph...')
        data_file = mainpage.mt.data_box.selectedItems()
        select_toppic = []
        for i in range(len(data_file)): #all pathfile
            select_toppic.append(str(data_file[i].text())) #get text name file
        file_read = tableManage.TableView.read_data(select_toppic)
        dimension,measure = tableManage.TableView.dim_meas_list()
        self.row_list,self.column_list = tableManage.TableView.row_column_list()
        self.list_dim,self.list_meas,self.list_mark,self.list_filter = tableManage.TableView.dim_meas_rc(self.row_list,self.column_list)

        if len(self.list_mark) == 0 and len(self.list_meas) == 0:
            frame_merge = tableManage.TableView.show_dim_meas(file_read,self.list_dim,self.list_meas,self.list_filter)
        else:
            new_file_read,list_dimfil = tableManage.TableView.check_date_filter(file_read,self.list_dim,self.list_filter)
            frame_merge = tableManage.TableView.check_mark(new_file_read,list_dimfil,self.list_meas,self.list_mark)
            # frame_merge = tableManage.TableView.check_mark(file_read,self.list_dim,self.list_meas,self.list_mark,self.list_filter)
        
        frame_data_fil = tableManage.TableView.filter_add(frame_merge,self.row_list,self.column_list,select_toppic)
        self.frame_data = tableManage.TableView.filtermeasure_add(frame_data_fil,self.row_list,self.column_list,select_toppic)

        new_dict_frame_data = {}
        for key,value in self.frame_data.items():
            split_key = key.split(".")
            if len(split_key) > 1:
                new_key = key.replace(".", " ")
                print("new_key")
                new_dict_frame_data[new_key] = value
            else:
                new_dict_frame_data[key] = value

        self.frame_graph = pd.DataFrame(new_dict_frame_data)
        print("frame_graph",self.frame_graph)

        if len(self.list_dim) == 0:
            return

        if len(self.list_dim) == 1:
            self.alt_col = [alt.X, alt.Column, alt.Color]
            self.alt_row = [alt.Y, alt.Row, alt.Color]
        else:
            if self.list_dim[0] in self.column_list:
                self.alt_col = [alt.Column, alt.X, alt.Color]
                self.alt_row = [alt.Y, alt.Row, alt.Color]
            else:
                self.alt_col = [alt.X, alt.Column, alt.Color]
                self.alt_row = [alt.Row, alt.Y, alt.Color]

        self.check_type()

    @classmethod
    def check_type(self):
        if mainpage.mt.gr_combo.currentText() == 'BAR chart':
            self.plot_bar()

        elif mainpage.mt.gr_combo.currentText() == 'PIE chart':
            self.plot_pie()

        elif mainpage.mt.gr_combo.currentText() == 'LINE chart':
            self.plot_line()

    @classmethod
    def plot_bar(self):
        print('staring plot bar graph')
        alt_plot = []
        show_tooltip = []
        PLOT = []

        head = list(self.frame_graph.head(0))
        print('head file', head)

        list_meas_data = ['SUM', 'MIN', 'MAX' , 'MEAN' , 'MEDIAN' , 'COUNT']
        list_meas_new = []
        list_dim_data = ['Year','Quarter', 'Month', 'Date', 'Quarter']
        list_dim_new = []

        for i in range(len(head)):
            new_head_meas = head[i].split(' ')
            print('new head meas', new_head_meas)
            if new_head_meas[0] in list_meas_data:
                list_meas_new.append(head[i])
                print('list_meas_new', list_meas_new)
            else:
                list_dim_new.append(head[i])
                print('dim new', list_dim_new)


        for j in range(len(self.column_list)):
            new_col_dim = self.column_list[j].split('+')
        
        for k in range(len(self.row_list)):
            new_row_dim = self.row_list[k].split('+')
        print('row dim', new_row_dim[0])



        for dim in list_dim_new:
            # print('dim', dim) -> dim Year Order Date
            dim_ymd = dim.split(' ')
            # print('dim ymd', dim_ymd) -> dim ymd ['Year', 'Order', 'Date']
            if dim in self.column_list:
                # print('dim if', dim)
                alt_plot.append(self.alt_col[0](f"{dim}"))
                self.alt_col.pop(0)
            elif dim == new_col_dim[0]:
                # print('dim 1', dim)
                alt_plot.append(self.alt_col[0](f"{dim}"))
                self.alt_col.pop(0)
            elif dim_ymd[0] in list_dim_data:
                ymd_new = dim_ymd[1] + ' ' + dim_ymd[2]
                if ymd_new in self.column_list:
                    alt_plot.append(self.alt_col[0](f"{dim}"))
                    self.alt_col.pop(0)
                else:
                    alt_plot.append(self.alt_row[0](f"{dim}"))
                    self.alt_row.pop(0)
            elif dim == new_row_dim[0]:
                # print('dim 3', dim)
                alt_plot.append(self.alt_row[0](f"{dim}"))
                self.alt_row.pop(0)
            else:
                # print('dim else', dim)
                alt_plot.append(self.alt_row[0](f"{dim}"))
                self.alt_row.pop(0)
            show_tooltip.append(dim)

        new_data_list = []
        print('k', self.column_list)
        for a in range(len(self.column_list)):
            new_a_col = self.column_list[a].split(' ')
            new_b_col = self.column_list[a].split('.')
            # print('test new', new_a_col)
            # print('test new . ', new_b_col)
            if new_a_col[0] in list_meas_data:
                new_data_meas = new_a_col[0] + ' ' + new_a_col[1]
                # print('new data meas', new_data_meas)
            elif new_b_col[0] in list_meas_data:
                new_data_meas = new_b_col[0] + ' ' + new_b_col[1]
                # print('new data meas .', new_data_meas)
            else:
                new_data_meas = 'SUM' + ' ' + self.column_list[a]
                # print('test new data', new_data_meas)
        new_data_list.append(new_data_meas)
        # print('fin new data', new_data_list)


        for meas in list_meas_new:
            min_bar = 0
            max_bar = 0
            if min_bar > self.frame_graph[meas].min():
                min_bar = self.frame_graph[meas].min()
            if max_bar < self.frame_graph[meas].max():
                max_bar = self.frame_graph[meas].max()

            plt = alt_plot.copy()
            if meas in new_data_list:
                plt.append(self.alt_col[0](meas,scale=alt.Scale(domain=(min_bar, max_bar), clamp=True)))
            else:
                plt.append(self.alt_row[0](meas,scale=alt.Scale(domain=(min_bar, max_bar), clamp=True)))

            plt.append(alt.Tooltip(show_tooltip + [meas]))

            chart = (alt.Chart(self.frame_graph).mark_bar().encode(
                    *plt,
                    )
                    .resolve_scale(x="independent",y="independent")
                    .interactive()
                    .transform_filter(alt.FieldGTPredicate(field=str(meas),gt=-1e10))
                )
            PLOT.append(chart)



        if len(list_meas_new) > 0:
            if list_meas_new[0] in new_data_list:
                chart = alt.hconcat(*PLOT)
            else:
                chart = alt.vconcat(*PLOT)
            mainpage.mt.show_chart.updateChart(chart) #plot chart


    @classmethod
    def plot_pie(self):
        print('staring plot pie graph')
        CHART = []

        head = list(self.frame_graph.head(0))
        # print('head file', head)

        list_meas_data = ['SUM', 'MIN', 'MAX' , 'MEAN' , 'MEDIAN' , 'COUNT']
        list_meas_new = []
        list_dim_new = []

        for i in range(len(head)):
            new_head_meas = head[i].split(' ')
            if new_head_meas[0] in list_meas_data:
                list_meas_new.append(head[i])
            else:
                list_dim_new.append(head[i])
                print('dim new', list_dim_new)

        new_data_list = []
        print('k', self.column_list)
        for a in range(len(self.column_list)):
            new_a_col = self.column_list[a].split(' ')
            new_b_col = self.column_list[a].split('.')
            print('test new', new_a_col)
            print('test new . ', new_b_col)
            if new_a_col[0] in list_meas_data:
                new_data_meas = new_a_col[0] + ' ' + new_a_col[1]
                print('new data meas', new_data_meas)
            elif new_b_col[0] in list_meas_data:
                new_data_meas = new_b_col[0] + ' ' + new_b_col[1]
                print('new data meas .', new_data_meas)
            else:
                new_data_meas = 'SUM' + ' ' + self.column_list[a]
                print('test new data', new_data_meas)
        new_data_list.append(new_data_meas)
        print('fin new data', new_data_list)

        for dim in list_dim_new:
            sub_chart = []
            BASE = alt.Chart(self.frame_graph).mark_arc().encode(color=alt.Color(dim))
            for meas in list_meas_new:
                base = BASE.encode(
                    theta = alt.Theta(meas),
                    tooltip = alt.Tooltip([dim,meas])
                )
                sub_chart.append(base)
            CHART.append(sub_chart)

        print('dim new col check', list_dim_new)
        if len(list_meas_new) > 0:
            if list_meas_new[0] in new_data_list:
                # print('here')
                hchart = []
                for sub_chart in CHART:
                    hchart.append(alt.hconcat(*sub_chart).resolve_scale(theta="independent",color="independent"))
                chart = alt.vconcat(*hchart)
            else:
                vchart = []
                for sub_chart in CHART:
                    vchart.append(alt.vconcat(*sub_chart).resolve_scale(theta="independent",color="independent"))
                chart = alt.hconcat(*vchart)
            mainpage.mt.show_chart.updateChart(chart) #plot chart


    @classmethod
    def plot_line(self):
        print('staring plot line graph')
        alt_plot = []
        show_tooltip = []
        PLOT = []

        head = list(self.frame_graph.head(0))
        print('head file', head)

        list_meas_data = ['SUM', 'MIN', 'MAX' , 'MEAN' , 'MEDIAN' , 'COUNT']
        list_meas_new = []
        list_dim_data = ['Year','Quarter', 'Month', 'Date']
        list_dim_new = []

        for i in range(len(head)):
            new_head_meas = head[i].split(' ')
            # print('new head meas', new_head_meas)
            if new_head_meas[0] in list_meas_data:
                list_meas_new.append(head[i])
                print('list_meas_new', list_meas_new)
            else:
                list_dim_new.append(head[i])
                print('dim new', list_dim_new)


        for j in range(len(self.column_list)):
            new_col_dim = self.column_list[j].split('+')
        
        for k in range(len(self.row_list)):
            new_row_dim = self.row_list[k].split('+')
        print('row dim', new_row_dim[0])

        for dim in list_dim_new:
            # print('dim', dim)
            dim_ymd = dim.split(' ')
            # print('dim ymd', dim_ymd)
            if dim in self.column_list:
                # print('dim if', dim)
                alt_plot.append(self.alt_col[0](f"{dim}"))
                self.alt_col.pop(0)
            elif dim == new_col_dim[0]:
                # print('dim 1', dim)
                alt_plot.append(self.alt_col[0](f"{dim}"))
                self.alt_col.pop(0)
            elif dim_ymd[0] in list_dim_data:
                ymd_new = dim_ymd[1] + ' ' + dim_ymd[2]
                if ymd_new in self.column_list:
                    alt_plot.append(self.alt_col[0](f"{dim}"))
                    self.alt_col.pop(0)
                else:
                    alt_plot.append(self.alt_row[0](f"{dim}"))
                    self.alt_row.pop(0)
            elif dim == new_row_dim[0]:
                # print('dim 3', dim)
                alt_plot.append(self.alt_row[0](f"{dim}"))
                self.alt_row.pop(0)
            else:
                # print('dim else', dim)
                alt_plot.append(self.alt_row[0](f"{dim}"))
                self.alt_row.pop(0)
            show_tooltip.append(dim)

        new_data_list = []
        print('k', self.column_list)
        for a in range(len(self.column_list)):
            new_a_col = self.column_list[a].split(' ')
            new_b_col = self.column_list[a].split('.')
            # print('test new', new_a_col)
            # print('test new . ', new_b_col)
            if new_a_col[0] in list_meas_data:
                new_data_meas = new_a_col[0] + ' ' + new_a_col[1]
                # print('new data meas', new_data_meas)
            elif new_b_col[0] in list_meas_data:
                new_data_meas = new_b_col[0] + ' ' + new_b_col[1]
                # print('new data meas .', new_data_meas)
            else:
                new_data_meas = 'SUM' + ' ' + self.column_list[a]
                # print('test new data', new_data_meas)
        new_data_list.append(new_data_meas)
        # print('fin new data', new_data_list)


        for meas in list_meas_new:
            min_bar = 0
            max_bar = 0
            if min_bar > self.frame_graph[meas].min():
                min_bar = self.frame_graph[meas].min()
            if max_bar < self.frame_graph[meas].max():
                max_bar = self.frame_graph[meas].max()

            plt = alt_plot.copy()
            if meas in new_data_list:
                plt.append(self.alt_col[0](meas,scale=alt.Scale(domain=(min_bar, max_bar), clamp=True)))
            else:
                plt.append(self.alt_row[0](meas,scale=alt.Scale(domain=(min_bar, max_bar), clamp=True)))

            plt.append(alt.Tooltip(show_tooltip + [meas]))
        chart = (alt.Chart(self.frame_graph).mark_line().encode(
                    *plt,
                    )
                    .resolve_scale(x="independent",y="independent")
                    .interactive()
                ) 
        PLOT.append(chart)

        if len(list_meas_new) > 0:
            if list_meas_new[0] in new_data_list:
                chart = alt.hconcat(*PLOT)
            else:
                chart = alt.vconcat(*PLOT)
            mainpage.mt.show_chart.updateChart(chart) #plot chart