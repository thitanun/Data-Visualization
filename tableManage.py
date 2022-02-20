from datetime import *
from datetime import datetime
from doctest import master
from tracemalloc import stop
from PyQt5.QtWidgets import QListWidgetItem,QFileDialog,QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QDesktopWidget
from PyQt5.QtGui import QIcon, QWindow
from PyQt5.QtCore import pyqtSlot,QSize
import sys
import os
# import fileManage
import pandas as pd
# from xlsxwriter import Workbook
import mainpage
import marksGUI

 
class TableView(QWindow):
    @classmethod
    def __init__(self):
        self.measList = []
        self.dimList = []

    @classmethod
    def importFile(self):
        #path file
        pathfile = QFileDialog.getOpenFileName(mainpage.mt , 'Open File', os.getenv('HOME'), 'Excel File(*.csv *.xlsx *.xls)')

        if pathfile[0] != '':
            self.list_data(pathfile)

    
    @classmethod
    def reset_data(self): #select name file
        data = mainpage.mt.data_box.selectedItems()
        # print(data) -> [<PyQt5.QtWidgets.QListWidgetItem object at 0x123B3268>, <PyQt5.QtWidgets.QListWidgetItem object at 0x0920ED18>]
        if len(data) == 0: #check list select
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)
            mainpage.mt.dim_box.clear()
            mainpage.mt.meas_box.clear()
            # mainpage.mt.table_box.raise_()
        else:
            #select data ,add data in table,add list dimension and measure,list mark ,list filter 
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)
            self.list_filter()
            self.list_marks()
            self.union_show()
            file_read = self.read_data()
            # self.show_data(file_read)
            self.show_data()
            self.list_dimen(file_read)
            # self.list_category(file_read)
            self.list_measure(file_read)

    
    @classmethod
    def read_data(self):#read file data
        data = mainpage.mt.data_box.selectedItems()
        # print(data)
        select_toppic = []
        for i in range(len(data)): #all pathfile
            select_toppic.append(str(mainpage.mt.data_box.selectedItems()[i].text())) #get text name file
        list_union = []    
        for path in select_toppic:
            datapath = mainpage.mt.dictpathfile[path]
            # print(datapath) path file
            namedata_type = datapath.split(".")
            # print(namedata_type) type path file like csv, xlsx
            if namedata_type[-1] == 'csv': #read file
                file_read = pd.read_csv(datapath, encoding = 'windows-1254')
                # print(file_read) data in csv file that can read          
            else:
                file_read = pd.read_excel(datapath,index_col=None)
                # print(file_read)  data in xlsx file that can read     
            list_union.append(file_read)

        #union data
        frame = pd.concat(list_union, ignore_index=True, sort=False)
        col_sort = list(frame.head(0))
        # print(col_sort) -> ['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country/Region', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit']
        union_frame = frame.sort_values(col_sort)
        dup = union_frame.drop_duplicates()
        set_dup = dup.reset_index(drop=True) 
        return set_dup
       
    @classmethod
    def list_dimen(self,file_read): #add dimention in list
        file_read = file_read
        mainpage.mt.dim_box.clear()
        col_name = file_read.head(0)
        list_toppic = list(col_name)
        a = 0
        for k_data in list_toppic: 
            check_toppic = list(file_read[k_data])
            check_list = all(isinstance(item, (int,float)) for item in check_toppic)
            if check_list == True:
                k_data_upper = k_data.upper()
                if "ID" in k_data_upper or "CODE" in k_data_upper: #check int float not number
                    toppic_ml = QListWidgetItem(k_data)
                    mainpage.mt.dim_box.insertItem(a, toppic_ml)
                    a += 1
            else:
                toppic_ml = QListWidgetItem(k_data)
                mainpage.mt.dim_box.insertItem(a, toppic_ml)
                a += 1   
    
    @classmethod
    def list_data(self,pathfile): #add data in list
        namedata = pathfile[0].split("/") 
        # print(namedata) -> ['D:', 'ttx', 'softdev2', 'cate', 'Tableau', 'Superstore.csv']
        toppic_qlist = QListWidgetItem(namedata[-1])
        mainpage.mt.dictpathfile[namedata[-1]] = pathfile[0]
        mainpage.mt.data_box.insertItem(1, toppic_qlist)


    @classmethod
    def list_measure(self,file_read): #add measure in list
        mainpage.mt.meas_box.clear()
        # file_read = self.read_data()    
        file_read = file_read  
        list_toppic = list(file_read.head(0))
        a = 0  
        for k_data in list_toppic: 
            check_toppic = list(file_read[k_data])
            check_list = all(isinstance(item, (int,float)) for item in check_toppic)
            if check_list == True:
                k_data_upper = k_data.upper()
                if "ID" in k_data_upper or "CODE" in k_data_upper: #check int float not number
                    pass
                else:
                    toppic_ml = QListWidgetItem(k_data)
                    mainpage.mt.meas_box.insertItem(a, toppic_ml)
                    # self.measList.append(toppic_ml)
                    # print(self.measList)
                    a += 1   


    @classmethod
    def list_filter(self): #all filter list
        mainpage.mt.fil_box.clear()
        data_list = ["Years","Months","Date"]
        a = 0
        for i in range(len(data_list)):
            toppic_filter = QListWidgetItem(data_list[i])
            # print(toppic_filter) ->
            # <PyQt5.QtWidgets.QListWidgetItem object at 0x0910DDF0>
            # <PyQt5.QtWidgets.QListWidgetItem object at 0x0910DDA8>
            # <PyQt5.QtWidgets.QListWidgetItem object at 0x0910DD60>
            mainpage.mt.fil_box.insertItem(a, toppic_filter)
            a += 1       

    
    @classmethod
    def show_data(self): #show data in table
        file_read = self.read_data()
        row_list,column_list = self.row_column_list()
        all_dim_meas = self.dim_meas_rc(file_read,row_list,column_list)
        print(all_dim_meas)
        
        mark = "None"
        if mark == "None":
            user_list = {}
            #data select        
            for d in all_dim_meas:
                select_data = file_read[d]
                user_list[d] = select_data
            len_file_column = len(user_list)

            len_file_row = len(file_read)
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)   
            mainpage.mt.table_box.setColumnCount(len_file_column)
            mainpage.mt.table_box.setRowCount(len_file_row)
            for n, key in enumerate(user_list.keys()): # add item
                for m, item in enumerate(user_list[key]):
                    newitem = QTableWidgetItem(str(item))
                    mainpage.mt.table_box.setItem(m, n, newitem)
            mainpage.mt.table_box.setHorizontalHeaderLabels(all_dim_meas)        
            mainpage.mt.table_box.show()

    @classmethod
    def dim_meas_rc(self,file_read,row_list,column_list):
        dim_list,meas_list = self.dim_meas_list(file_read)
        data_dim = []
        data_meas = []
        for i in row_list:
            if i in dim_list:
                data_dim.append(i)
            elif i in meas_list:
                data_meas.append(i)
        for i in column_list:
            if i in dim_list:
                data_dim.append(i)
            elif i in meas_list:
                data_meas.append(i)
        
        all_dim_meas = []
        for i in data_dim:
            all_dim_meas.append(i)
        for i in data_meas:
            all_dim_meas.append(i)

        return all_dim_meas
    
    @classmethod
    def dim_meas_list(self,file_read):

        list_toppic = list(file_read.head(0)) 

        dim_list = []
        meas_list = []
        # for i in range(mainpage.mt.meas_box.count()):
        #     meas_list.append(mainpage.mt.meas_box.item(i).text())
        for k_data in range(len(list_toppic)):
            check_toppic = list(file_read[list_toppic[k_data]]) 
            check_list = all(isinstance(item, (int,float)) for item in check_toppic)
            if check_list == True:
                k_data_upper = list_toppic[k_data].upper()
                if "ID" in k_data_upper or "CODE" in k_data_upper: 
                    dim_list.append(list_toppic[k_data])
                else:
                    meas_list.append(list_toppic[k_data])
            else:
                dim_list.append(list_toppic[k_data])
                
        # for i in range(mainpage.mt.dim_box.count()):
        #     dim_list.append(mainpage.mt.dim_box.item(i).text())        
        

        return dim_list,meas_list



    @classmethod
    def row_column_list(self): #select dimention

        row_list = []
        for i in range(mainpage.mt.row_box.count()):
            row_list.append(mainpage.mt.row_box.item(i).text())

        column_list = []
        for i in range(mainpage.mt.col_box.count()):
            column_list.append(mainpage.mt.col_box.item(i).text())

        return row_list,column_list


    @classmethod
    def dim_select(self): #select dimention
        file_read = self.read_data()
        data = mainpage.mt.dim_box.selectedItems()
        # data = mainpage.mt.col_box_table.currentItem()
        select_toppic = []
        for i in range(len(data)):#path file
            select_toppic.append(str(mainpage.mt.dim_box.selectedItems()[i].text()))
            # select_toppic.append(str(mainpage.mt.col_box_table.currentItem()[i].text()))
        user_list = {}        
        for a in select_toppic:#data select
            select_data = file_read[a]
            user_list[a] = select_data            
        len_file_column = len(user_list)
        len_file_row = len(file_read)
        #selected tabel
        mainpage.mt.table_box.clear()
        mainpage.mt.table_box.setRowCount(0)   
        mainpage.mt.table_box.setColumnCount(len_file_column)
        mainpage.mt.table_box.setRowCount(len_file_row)
        for n, key in enumerate(user_list.keys()): # add item
            for m, item in enumerate(user_list[key]):
                newitem = QTableWidgetItem(str(item))
                mainpage.mt.table_box.setItem(m, n, newitem)
        mainpage.mt.table_box.setHorizontalHeaderLabels(select_toppic)        
        mainpage.mt.table_box.show()
    

    @classmethod
    def measure_select(self): #select measure
        file_read = self.read_data()
        data = mainpage.mt.meas_box.selectedItems()
        select_toppic = []
        for i in range(len(data)):#path file
            select_toppic.append(str(mainpage.mt.meas_box.selectedItems()[i].text()))
        user_list = {}        
        for a in select_toppic:#data select
            select_data = file_read[a]
            user_list[a] = select_data            
        len_file_column = len(user_list)
        len_file_row = len(file_read)
        #selected tabel   
        mainpage.mt.table_box.clear()
        mainpage.mt.table_box.setRowCount(0)
        mainpage.mt.table_box.setColumnCount(len_file_column)
        mainpage.mt.table_box.setRowCount(len_file_row)
        for n, key in enumerate(user_list.keys()): # add item
            for m, item in enumerate(user_list[key]):
                newitem = QTableWidgetItem(str(item))
                mainpage.mt.table_box.setItem(m, n, newitem)
        mainpage.mt.table_box.setHorizontalHeaderLabels(select_toppic)        
        mainpage.mt.table_box.show()


    @classmethod
    def union_show(self):#list file union
        data = mainpage.mt.data_box.selectedItems()
        select_topic = []
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        namefile = ""
        a = 0
        if len(data) > 1:
            for name in select_topic:
                mainpage.mt.uni_box.clear()
                namedata = name.split(".") 
                namefile += namedata[0] + "\n"
                mainpage.mt.uni_box.insertItem(a, namefile)
                a += 1  
        elif len(data) == 1:
            mainpage.mt.uni_box.clear() 

    # @classmethod
    # def mange_Union_file(self):
    #     data = mainpage.mt.data_box.selectedItems()
    #     select_toppic = []
    #     for i in range(len(data)):
    #         select_toppic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
    #     frame = self.read_data()
    #     namefile = ""
    #     for name in select_toppic:
    #         namedata_type = name.split(".")
    #         namefile += namedata_type[0] + "_"
    #     name_csv = "./"+ namefile + ".xlsx"
    #     col_name = list(frame.head(0))           
    #     dict_file = pd.DataFrame.from_dict(frame)
    #     dict_file.to_excel(name_csv,index=False)
    #     absolute_path = os.path.abspath(os.path.dirname(name_csv))
    #     path_union =  absolute_path + "\\" + name_csv 
    #     mainpage.mt.unionpathfile[name_csv] = path_union
         
    @classmethod
    def list_marks(self): #all filter list
        mainpage.mt.cat_box.clear()
        data_list = ["mean","mid","max","min","sum","count"]
        a = 0
        for i in range(len(data_list)):
            toppic_filter = QListWidgetItem(data_list[i])
            mainpage.mt.cat_box.insertItem(a, toppic_filter)
            a += 1       


    @classmethod
    def marks_set(self):
        file_read = self.read_data()

        #data dimension select
        data_dim = mainpage.mt.dim_box.selectedItems()
        if len(data_dim) == 0:
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)
        else:
            select_toppic_dim = []
            for i in range(len(data_dim)):
                select_toppic_dim.append(str(mainpage.mt.dim_box.selectedItems()[i].text()))

        #data measure select
        data_meas = mainpage.mt.meas_box.selectedItems()
        if len(data_meas) == 0:
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)
        else:
            select_toppic_meas = []
            for i in range(len(data_meas)):
                select_toppic_meas.append(str(mainpage.mt.meas_box.selectedItems()[i].text()))

        #data mark select    
        data_mark = mainpage.mt.cat_box.selectedItems()

        data_s_mark = self.marks_check(data_mark,file_read,select_toppic_dim,select_toppic_meas)#get data mark
        self.marks_add(data_s_mark) #add data mark in table

        return data_s_mark
    

    @classmethod
    def marks_check(self,data_mark,file_read,select_toppic_dim,select_toppic_meas):

        if len(data_mark) == 0:#check list mark select
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)
            pass
        else:
            select_toppic_mark = []
            for i in range(len(data_mark)):
                select_toppic_mark.append(str(mainpage.mt.cat_box.selectedItems()[i].text()))
            list_subcat = file_read.groupby(select_toppic_dim,as_index=False)

            for s_mark in select_toppic_mark:#mark data 
                if s_mark == 'mean':
                    data_s_mark = list_subcat[select_toppic_meas].mean()
                if s_mark == 'max':
                    data_s_mark = list_subcat[select_toppic_meas].max()
                if s_mark == 'min':
                    data_s_mark = list_subcat[select_toppic_meas].min()
                if s_mark == 'count':
                    data_s_mark = list_subcat[select_toppic_meas].count()
                if s_mark == 'sum':
                    data_s_mark = list_subcat[select_toppic_meas].sum()
                if s_mark == 'mid':
                    data_s_mark = list_subcat[select_toppic_meas].median()       

        return data_s_mark
            

    @classmethod
    def marks_add(self,data_s_mark):
        frame_data = pd.DataFrame.from_dict(data_s_mark)
        # frame_data_tran = frame_data.transpose()
        # col_name = list(frame_data.head(0))
        len_file_column = len(frame_data.columns)
        len_file_row = len(frame_data.index)
        #add data in table
        mainpage.mt.table_box.clear()
        mainpage.mt.table_box.setRowCount(0)
        mainpage.mt.table_box.setColumnCount(len_file_column)
        mainpage.mt.table_box.setRowCount(len_file_row)
        # print(frame_data)
        for n, key in enumerate(frame_data.keys()):
            for m, item in enumerate(frame_data[key]):
                newitem = QTableWidgetItem(str(item))
                mainpage.mt.table_box.setItem(m, n, newitem)