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
        data_file = mainpage.mt.data_box.selectedItems()
        file_read = tableManage.TableView.read_data(data_file)
        self.row_list,self.column_list = tableManage.TableView.row_column_list()
        self.list_dim,self.list_meas,self.list_mark,self.list_filter = tableManage.TableView.dim_meas_rc(self.row_list,self.column_list)
        # print('dim',self.list_dim)
        # print('fil',self.list_filter)

        if len(self.list_dim) == 0:
            return

        if len(self.list_dim) == 1:
            self.alt_col = [alt.X, alt.Column, alt.Color]
            self.alt_row = [alt.Y, alt.Row, alt.Color]
        else:
            if self.list_dim[0] in self.column_list:
                # print(self.list_dim[0])
                self.alt_col = [alt.Column, alt.X, alt.Color]
                self.alt_row = [alt.Y, alt.Row, alt.Color]
            else:
                self.alt_col = [alt.X, alt.Column, alt.Color]
                self.alt_row = [alt.Row, alt.Y, alt.Color]

        if len(self.list_mark) == 0:
            if len(self.list_meas) == 0:
                frame_merge = tableManage.TableView.show_dim_meas(file_read,self.list_dim,self.list_meas,self.list_filter)
        else:
                frame_merge = tableManage.TableView.check_mark(file_read,self.list_dim,self.list_meas,self.list_mark,self.list_filter)
            
        self.frame_data = tableManage.TableView.filter_add(frame_merge)

        self.head_frame = list(self.frame_data.head(0))
        # print('head', self.head_frame)
        # print('fm', self.frame_data)

        self.check_type()

    @classmethod
    def check_type(self):
        if mainpage.mt.gr_combo.currentText() == 'NONE':
            print("You didn't choose any type")

        elif mainpage.mt.gr_combo.currentText() == 'BAR chart':
            self.plot_bar()

        elif mainpage.mt.gr_combo.currentText() == 'PIE chart':
            self.plot_pie()

        elif mainpage.mt.gr_combo.currentText() == 'LINE chart':
            self.plot_line()

    @classmethod
    def plot_bar(self):
        alt_plot = []
        show_tooltip = []
        PLOT = []
        for dim in self.list_dim:
            if dim in self.column_list:
                alt_plot.append(self.alt_col[0](f"{dim}"))
                self.alt_col.pop(0)
            else:
                alt_plot.append(self.alt_row[0](f"{dim}"))
                self.alt_row.pop(0)
            show_tooltip.append(dim)
        for meas in self.list_meas:
            min_bar = 0
            max_bar = 0
            if min_bar > self.frame_data[meas].min():
                min_bar = self.frame_data[meas].min()
            if max_bar < self.frame_data[meas].max():
                max_bar = self.frame_data[meas].max()

            plt = alt_plot.copy()
            if meas in self.column_list:
                plt.append(self.alt_col[0](meas,scale=alt.Scale(domain=(min_bar, max_bar), clamp=True)))
            else:
                plt.append(self.alt_row[0](meas,scale=alt.Scale(domain=(min_bar, max_bar), clamp=True)))

            plt.append(alt.Tooltip(show_tooltip + [meas]))

            chart = (alt.Chart(self.frame_data).mark_bar().encode(*plt,)
                    .resolve_scale(x="independent",y="independent")
                    .interactive()
                    .transform_filter(alt.FieldGTPredicate(field=str(meas),gt=-1e10))
                )
            PLOT.append(chart)

        if len(self.list_meas) > 0:
            if self.list_meas[0] in self.column_list:
                chart = alt.hconcat(*PLOT)
            else:
                chart = alt.vconcat(*PLOT)
            mainpage.mt.show_chart.updateChart(chart) # plot chart

    @classmethod
    def plot_pie(self):
        CHART = []
        for dim in self.list_dim:
            sub_chart = []
            BASE = alt.Chart(self.frame_data).mark_arc().encode(color=alt.Color(dim))
            for meas in self.list_meas:
                base = BASE.encode(
                    theta = alt.Theta(meas),
                    show_tooltip = alt.Tooltip([dim,meas])
                )
                sub_chart.append(base)
            CHART.append(sub_chart)

        if len(self.list_meas) > 0:
            if self.list_meas[0] in self.column_list:
                hchart = []
                for sub_chart in CHART:
                    hchart.append(alt.hconcat(*sub_chart).resolve_scale(theta="independent",color="independent"))
                chart = alt.vconcat(*hchart)
            else:
                vchart = []
                for sub_chart in CHART:
                    vchart.append(alt.vconcat(*sub_chart).resolve_scale(theta="independent",color="independent"))
                chart = alt.hconcat(*vchart)
            mainpage.mt.show_chart.updateChart(chart) # plot chart

    @classmethod
    def plot_line(self):
        alt_plot = []
        show_tooltip = []
        PLOT = []
        for dim in self.list_dim:
            if dim in self.column_list:
                alt_plot.append(self.alt_col[0](f"{dim}"))
                self.alt_col.pop(0)
                # print(alt_col)
            else:
                alt_plot.append(self.alt_row[0](f"{dim}"))
                self.alt_row.pop(0)
            show_tooltip.append(dim)
        for meas in self.list_meas:
            # data = frame_data
            min_bar = 0
            max_bar = 0
            if min_bar > self.frame_data[meas].min(): 
                min_bar = self.frame_data[meas].min()
            if max_bar < self.frame_data[meas].max():
                max_bar = self.frame_data[meas].max()

            plt = alt_plot.copy()
            # print('heyy',plt)
            if meas in self.column_list:
                plt.append(self.alt_col[0](meas,scale=alt.Scale(domain=(min_bar, max_bar), clamp=True)))
            else:
                plt.append(self.alt_row[0](meas,scale=alt.Scale(domain=(min_bar, max_bar), clamp=True)))

            plt.append(alt.Tooltip(show_tooltip + [meas]))
        chart = (alt.Chart(self.frame_data).mark_line().encode(*plt)
                    .resolve_scale(x="independent",y="independent")
                    .interactive()
                ) 
        PLOT.append(chart)

        if len(self.list_meas) > 0:
            if self.list_meas[0] in self.column_list:
                chart = alt.hconcat(*PLOT)
            else:
                chart = alt.vconcat(*PLOT)
            mainpage.mt.show_chart.updateChart(chart) # plot chart



