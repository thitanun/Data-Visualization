from datetime import *
from datetime import datetime
from doctest import master
from tracemalloc import stop
from PyQt5.QtWidgets import QListWidgetItem,QFileDialog,QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QDesktopWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QWindow
from PyQt5.QtCore import pyqtSlot,QSize
from functools import reduce
import json
import sys
import os
import hashlib
# import fileManage
import pandas as pd
# from soupsieve import select
# from xlsxwriter import Workbook
import mainpage
# import markGUI
# import filterGUI

 
class TableView(QWindow):
    # @classmethod
    # def __init__(self):
    #     self.measList = []
    #     self.dimList = []

    @classmethod
    def importFile(self):
        #path file
        pathfile = QFileDialog.getOpenFileName(mainpage.mainApp , 'Open File', os.getenv('HOME'), 'Excel File(*.csv *.xlsx *.xls)')

        if pathfile[0] != '':
            # self.list_data(pathfile)
            self.list_data(pathfile[0])

    
    @classmethod
    def reset_data(self): #select name file
        data = mainpage.mt.data_box.selectedItems()
        select_topic = []
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        # print(data) -> [<PyQt5.QtWidgets.QListWidgetItem object at 0x123B3268>, <PyQt5.QtWidgets.QListWidgetItem object at 0x0920ED18>]
        if len(data) == 0: #check list select
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)
            mainpage.mt.dim_box.clear()
            mainpage.mt.meas_box.clear()
            mainpage.mt.row_box.clear()
            mainpage.mt.col_box.clear()
            # mainpage.mt.table_box.raise_()
        else:
            #select data ,add data in table,add list dimension and measure,list mark ,list filter 
            mainpage.mt.table_box.clear()
            mainpage.mt.row_box.clear()
            mainpage.mt.col_box.clear()
            mainpage.mt.table_box.setRowCount(0)
            for path in select_topic:
                self.list_data(path)
            self.union_show()
            file_read = self.read_data(data)
            self.list_dimen(file_read)
            self.list_measure(file_read)
            self.filter_boxadd()

    @classmethod
    def list_data(self,pathfile): #add data in list
        namedata = pathfile.split("/") 
        # print(namedata) -> ['D:', 'ttx', 'softdev2', 'cate', 'Tableau', 'Superstore.csv']
        # toppic_qlist = QListWidgetItem(namedata[-1])
        md5_hash = hashlib.md5()
        file_md5 = open(pathfile, "rb")
        file_md5_read = file_md5.read()
        md5_hash.update(file_md5_read)
        code_md5 = md5_hash.hexdigest()
        # print("code_md5",code_md5)
        self.meta_file(pathfile,code_md5)
        self.filter_file(pathfile,code_md5)
        mainpage.mainTableau.dictpathfile[namedata[-1]] = pathfile
        list_data_box = []
        for i in range(mainpage.mt.data_box.count()):
            list_data_box.append(mainpage.mt.data_box.item(i).text())
        if pathfile not in list_data_box:
            mainpage.mt.data_box.insertItem(0, pathfile)
    
    @classmethod
    def meta_file(self,pathfile,code_md5):
        try:
            with open('metadata.json', 'r') as file_readjson:
                read_json = file_readjson.read()
                dict_data = json.loads(read_json)
            list_md5 = list(dict_data.keys())
            for k_data in list_md5:   
                if pathfile != dict_data[k_data]["path file"] and code_md5 == k_data:
                    dict_data[k_data].clear()
                    dict_data[k_data]["path file"] = pathfile         
            if code_md5 not in list_md5:
                dict_data[code_md5] = {}
                dict_data[code_md5]["path file"] = pathfile
            with open('metadata.json', 'w') as file_json:
                json.dump(dict_data, file_json)
        except:            
            dict_data = {}
            dict_data[code_md5] = {}
            dict_data[code_md5]["path file"] = pathfile
            with open('metadata.json', 'w') as file_json:
                json.dump(dict_data, file_json)
    
    """@classmethod
    def meta_file(self,pathfile,code_md5):
        try:
            with open('metadata.json', 'r') as file_readjson:
                read_json = file_readjson.read()
                dict_data = json.loads(read_json)
            list_path = list(dict_data.keys())
            for k_data in list_path:   
                if code_md5 != dict_data[k_data]["md5"]:
                    dict_data[k_data].clear()
                    dict_data[k_data]["md5"] = code_md5         
            if pathfile not in list_path:
                dict_data[pathfile] = {}
                dict_data[pathfile]["md5"] = code_md5
            with open('metadata.json', 'w') as file_json:
                json.dump(dict_data, file_json)
        except:            
            dict_data = {}
            dict_data[pathfile] = {}
            dict_data[pathfile]["md5"] = code_md5
            with open('metadata.json', 'w') as file_json:
                json.dump(dict_data, file_json)"""

    """@classmethod
    def filter_file(self,pathfile,code_md5):
        try:
            with open('filterdata.json', 'r') as file_readjson:
                read_json = file_readjson.read()
                dict_data = json.loads(read_json)
            list_path = list(dict_data.keys())
            for k_data in list_path:   
                if code_md5 != dict_data[k_data]["md5"]:
                    dict_data[k_data].clear()
                    dict_data[k_data]["md5"] = code_md5  
                    dict_data[k_data]["filter"] = {}
            if pathfile not in list_path:
                dict_data[pathfile] = {}
                dict_data[pathfile]["md5"] = code_md5
                dict_data[pathfile]["filter"] = {}
            with open('filterdata.json', 'w') as file_json:
                json.dump(dict_data, file_json)
        except:            
            dict_data = {}
            dict_data[pathfile] = {}
            dict_data[pathfile]["md5"] = code_md5
            dict_data[pathfile]["filter"] = {}
            with open('filterdata.json', 'w') as file_json:
                json.dump(dict_data, file_json)"""
    
    @classmethod
    def filter_file(self,pathfile,code_md5):
        try:
            with open('filterdata.json', 'r') as file_readjson:
                read_json = file_readjson.read()
                dict_data = json.loads(read_json)
            list_md5 = list(dict_data.keys())
            for k_data in list_md5:   
                if pathfile != dict_data[k_data]["path file"] and code_md5 == k_data:
                    dict_data[k_data].clear()
                    dict_data[k_data]["path file"] = pathfile
                    dict_data[k_data]["filter"] = {}         
            if code_md5 not in list_md5:
                dict_data[code_md5] = {}
                dict_data[code_md5]["path file"] = pathfile
                dict_data[code_md5]["filter"] = {}
            with open('filterdata.json', 'w') as file_json:
                json.dump(dict_data, file_json)
        except:            
            dict_data = {}
            dict_data[code_md5] = {}
            dict_data[code_md5]["path file"] = pathfile
            with open('filterdata.json', 'w') as file_json:
                json.dump(dict_data, file_json)

    @classmethod
    def read_data(self,data):#read file data
        # data = mainpage.mt.data_box.selectedItems()
        # print(data)
        select_toppic = []
        for i in range(len(data)): #all pathfile
            select_toppic.append(str(data[i].text())) #get text name file
        list_union = []    
        for path in select_toppic:
            # datapath = mainpage.mt.dictpathfile[path]
            datapath = path
            # print(datapath) path file
            namedata_type = datapath.split(".")
            # print(namedata_type) type path file like csv, xlsx
            if namedata_type[-1] == 'csv': #read file
                file_read = pd.read_csv(datapath, encoding = 'windows-1254')
                # print(file_read) data in csv file that can read
            else:
                file_read = pd.read_excel(datapath,index_col=None)
                # print(file_read)  data in xlsx file that can read
            col_name = list(file_read.head(0))            
            check_head = [head_name for head_name in col_name if "DATE" in head_name.upper()]
            for head_namedate in check_head:
                data_date = [datetime.strftime(date, '%d/%m/%Y') if type(date) == datetime else datetime.strftime(datetime.strptime(date, "%d/%m/%Y").date(), '%d/%m/%Y') for date in file_read[head_namedate]]
                file_read[head_namedate] = data_date               
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
    def list_checkpath_meta(self):
        select_topic = []
        with open('metadata.json', 'r') as file_readjson:
            read_json = file_readjson.read()
            read_data = json.loads(read_json)
        data = mainpage.mt.data_box.selectedItems()
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
            return read_data,select_topic

    """@classmethod
    def list_dimen(self,file_read): #add dimention in list
        
        read_data,select_topic = self.list_checkpath_meta() 
        for path in select_topic:
            if "dimensions" in list(read_data[path].keys()):
                self.dimList = read_data[path]["dimensions"]
            else:
                self.dimList = []
                col_name = file_read.head(0)
                list_toppic = list(col_name)
                for k_data in list_toppic: 
                    check_toppic = list(file_read[k_data])
                    check_list = all(isinstance(item, (int,float)) for item in check_toppic)
                    if check_list == True:
                        k_data_upper = k_data.upper()
                        if "ID" in k_data_upper or "CODE" in k_data_upper: #check int float not number
                            self.dimList.append(k_data)
                    else:
                        self.dimList.append(k_data)
                read_data[path]["dimensions"] = self.dimList
                with open('metadata.json', 'w') as file_json:
                    json.dump(read_data, file_json)  
        self.add_list_dim(self.dimList)"""

    @classmethod
    def list_dimen(self,file_read): #add dimention in list
        
        read_data,select_topic = self.list_checkpath_meta() 
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "dimensions" in list(read_data[code_md5].keys()):
                self.dimList = read_data[code_md5]["dimensions"]
            else:
                self.dimList = []
                col_name = file_read.head(0)
                list_toppic = list(col_name)
                for k_data in list_toppic: 
                    check_toppic = list(file_read[k_data])
                    check_list = all(isinstance(item, (int,float)) for item in check_toppic)
                    if check_list == True:
                        k_data_upper = k_data.upper()
                        if "ID" in k_data_upper or "CODE" in k_data_upper: #check int float not number
                            self.dimList.append(k_data)
                    else:
                        self.dimList.append(k_data)
                read_data[code_md5]["dimensions"] = self.dimList
                with open('metadata.json', 'w') as file_json:
                    json.dump(read_data, file_json)  
        self.add_list_dim(self.dimList)
           
    @classmethod
    def add_list_dim(self,dimList):
        mainpage.mt.dim_box.clear()
        for a in range(len(dimList)): 
            toppic_ml = QListWidgetItem(dimList[a])
            mainpage.mt.dim_box.insertItem(a, toppic_ml)

    """@classmethod
    def list_measure(self,file_read): #add measure in list
        
        read_data,select_topic = self.list_checkpath_meta()         
        for path in select_topic:
            if "measure" in list(read_data[path].keys()):
                self.measList = read_data[path]["measure"]
            else: 
                list_toppic = list(file_read.head(0))
                self.measList = []
                for k_data in list_toppic:
                    check_toppic = list(file_read[k_data])
                    check_list = all(isinstance(item, (int,float)) for item in check_toppic)
                    if check_list == True:
                        k_data_upper = k_data.upper()
                        if "ID" in k_data_upper or "CODE" in k_data_upper: #check int float not number
                            pass
                        else:
                            self.measList.append(k_data)
                read_data[path]["measure"] = self.measList
                with open('metadata.json', 'w') as file_json:
                    json.dump(read_data, file_json)
            self.add_list_measure(self.measList)"""
    
    @classmethod
    def list_measure(self,file_read): #add measure in list
        
        read_data,select_topic = self.list_checkpath_meta()         
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "measure" in list(read_data[code_md5].keys()):
                self.measList = read_data[code_md5]["measure"]
            else: 
                list_toppic = list(file_read.head(0))
                self.measList = []
                for k_data in list_toppic:
                    check_toppic = list(file_read[k_data])
                    check_list = all(isinstance(item, (int,float)) for item in check_toppic)
                    if check_list == True:
                        k_data_upper = k_data.upper()
                        if "ID" in k_data_upper or "CODE" in k_data_upper: #check int float not number
                            pass
                        else:
                            self.measList.append(k_data)
                read_data[code_md5]["measure"] = self.measList
                with open('metadata.json', 'w') as file_json:
                    json.dump(read_data, file_json)
            self.add_list_measure(self.measList)
              
    @classmethod
    def add_list_measure(self,measList):
        mainpage.mt.meas_box.clear()
        for a in range(len(measList)): 
            toppic_ml = QListWidgetItem(measList[a])
            mainpage.mt.meas_box.insertItem(a, toppic_ml)
            

    @classmethod
    def show_data(self): #show data in table
        data = mainpage.mt.data_box.selectedItems()
        file_read = self.read_data(data)
        row_list,column_list = self.row_column_list()
        
        # print("row_list",row_list)
        # print("column_list",column_list)
        list_dim,list_meas,list_mark,list_filter = self.dim_meas_rc(file_read,row_list,column_list)
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
                    frame_merge = self.show_dim_meas(file_read,list_dim,list_meas,list_filter)
            else:
                    frame_merge = self.check_mark(file_read,list_dim,list_meas,list_mark,list_filter)
            # self.filter_add(frame_merge)
            frame_data = self.filter_add(frame_merge)
            # print('fd', frame_data)

            # print("merge",frame_merge)
            head_col = list(frame_data.head(0))
            len_file_column = len(head_col)

            len_file_row = len(frame_data)
            # print('fd len', len_file_row)
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)   
            mainpage.mt.table_box.setColumnCount(len_file_column)
            mainpage.mt.table_box.setRowCount(len_file_row)
            for n, key in enumerate(frame_data.keys()): # add item
                for m, item in enumerate(frame_data[key]):
                    if type(item) == float:
                        float_item = round(item,3)
                        newitem = QTableWidgetItem(str(float_item))
                    else:
                        newitem = QTableWidgetItem(str(item))
                    mainpage.mt.table_box.setItem(m, n, newitem)
            mainpage.mt.table_box.setHorizontalHeaderLabels(head_col)
            mainpage.mt.table_box.verticalHeader().hide()      
            mainpage.mt.table_box.show()
    
    @classmethod
    def filter_add(self,frame_merge):
        select_topic = []
        data = mainpage.mt.data_box.selectedItems()
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        with open('filterdata.json', 'r') as file_readjson:
            read_json = file_readjson.read()
            read_data = json.loads(read_json)
        name_col = list(frame_merge.keys())
        # print("name_col",name_col)
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "filter" in list(read_data[code_md5].keys()):
                for fil_name in read_data[code_md5]["filter"].keys():
                    if fil_name in name_col:
                        filter_list = read_data[code_md5]["filter"][fil_name]
                        frame_merge = frame_merge.loc[frame_merge[fil_name].isin(filter_list)]
                new_frame = frame_merge                 
            else:
                new_frame = frame_merge

        return new_frame
             

    
    @classmethod
    def show_dim_meas(self,file_read,list_dim,list_meas,list_filter):
        all_dim_meas = list_dim + list_meas
        # print(all_dim_meas)
        for s_fil in range(len(list_dim)):
            upper_filter = list_filter[s_fil].upper()
            dim_name = list_dim[s_fil]
            if "DATE" in dim_name.upper():
                data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in file_read[dim_name]]
                file_read[dim_name] = data_date
                if  upper_filter == 'YEAR' or upper_filter == 'NONE':
                    fil_date = list(pd.DatetimeIndex(file_read[dim_name]).year)                
                if upper_filter == 'QUARTER':
                    fil_date = list(pd.DatetimeIndex(file_read[dim_name]).quarter)  
                if upper_filter == 'MONTH':
                    fil_date = list(pd.DatetimeIndex(file_read[dim_name]).month)  
                if upper_filter == 'DATE':
                    fil_date = list(pd.DatetimeIndex(file_read[dim_name]).day)  
                data_infil = [str(date_time) for date_time in fil_date]
                file_read[dim_name] = data_infil

        frame_data = file_read[all_dim_meas]
        # print(frame_data)
        frame_merge = frame_data.drop_duplicates().sort_values(all_dim_meas[0])

        # print(frame_merge)
        return frame_merge
    
    @classmethod
    def check_mark(self,file_read,list_dim,list_meas,list_mark,list_filter):
        frame_mark_list = []
        new_file_read = self.check_date_filter(file_read,list_dim,list_filter)
        group_data = new_file_read.groupby(list_dim,as_index=False)
        for s_mark in range(len(list_mark)):#mark data
            # print(s_mark)
            upper_mark = list_mark[s_mark].upper()
            # print(upper_mark) 
            if  upper_mark == 'MEAN':
                data_s_mark = group_data[list_meas[s_mark]].mean()
            if upper_mark == 'MAX':
                data_s_mark = group_data[list_meas[s_mark]].max()
            if upper_mark == 'MIN':
                data_s_mark = group_data[list_meas[s_mark]].min()
            if upper_mark == 'COUNT':
                data_s_mark = group_data[list_meas[s_mark]].count()
            if upper_mark == 'SUM' or upper_mark == 'NONE':
                data_s_mark = group_data[list_meas[s_mark]].sum()
            if upper_mark == 'MEDIAN':
                data_s_mark = group_data[list_meas[s_mark]].median()
            frame_mark_list.append(data_s_mark)

        if len(frame_mark_list) >= 1:
            frame_merge = reduce(lambda left, right: pd.merge(left,right), frame_mark_list)

        return frame_merge
    
    @classmethod
    def check_date_filter(self,file_read,list_dim,list_filter):

        for s_fil in range(len(list_dim)):
            upper_filter = list_filter[s_fil].upper()
            dim_name = list_dim[s_fil]
            if "DATE" in dim_name.upper():
                data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in file_read[dim_name]]
                file_read[dim_name] = data_date
                if  upper_filter == 'YEAR' or upper_filter == 'NONE':
                    fil_date = list(pd.DatetimeIndex(file_read[dim_name]).year)                
                if upper_filter == 'QUARTER':
                    fil_date = list(pd.DatetimeIndex(file_read[dim_name]).quarter)  
                if upper_filter == 'MONTH':
                    fil_date = list(pd.DatetimeIndex(file_read[dim_name]).month)  
                if upper_filter == 'DATE':
                    fil_date = list(pd.DatetimeIndex(file_read[dim_name]).day)  
                data_infil = [str(date_time) for date_time in fil_date]
                file_read[dim_name] = data_infil

        return file_read


    
    @classmethod
    def dim_meas_rc(self,file_read,row_list,column_list):
        dimension,measure = self.dim_meas_list()
        list_dim = []
        list_meas = []
        list_mark = []
        list_filter = []

        for namerow in row_list:
            list_namerow = namerow.split(".")
            if len(list_namerow) > 1:
                if list_namerow[-1] in dimension:
                    list_dim.append(list_namerow[-1])
                    list_filter.append(list_namerow[0])
                if list_namerow[-1] in measure:
                    list_meas.append(list_namerow[-1])
                    list_mark.append(list_namerow[0])
            else:
                if list_namerow[0] in dimension:
                    list_dim.append(list_namerow[0])
                    list_filter.append("NONE")
                if list_namerow[0] in measure:
                    list_meas.append(list_namerow[0])
                    list_mark.append("NONE")
                
        for namecolumn in column_list:
            list_namecolumn = namecolumn.split(".")
            if len(list_namecolumn) > 1:
                if list_namecolumn[-1] in dimension:
                    list_dim.append(list_namecolumn[-1])
                    list_filter.append(list_namecolumn[0])
                if list_namecolumn[-1] in measure:
                    list_meas.append(list_namecolumn[-1])
                    list_mark.append(list_namecolumn[0])
            else:
                if list_namecolumn[0] in dimension:
                    list_dim.append(list_namecolumn[0])
                    list_filter.append("NONE")
                if list_namecolumn[0] in measure:
                    list_meas.append(list_namecolumn[0])
                    list_mark.append("NONE")
        
        return list_dim,list_meas,list_mark,list_filter

    
    @classmethod
    def dim_meas_list(self):
        # list_toppic = list(file_read.head(0)) 

        dim_list = []
        meas_list = []
        for i in range(mainpage.mt.meas_box.count()):
            meas_list.append(mainpage.mt.meas_box.item(i).text())

        for i in range(mainpage.mt.dim_box.count()):
            dim_list.append(mainpage.mt.dim_box.item(i).text())        
        

        return dim_list,meas_list


    @classmethod
    def row_column_list(self): #select dimention
        row_list = []
        for i in range(mainpage.mt.row_box.count()):
            row_list.append(mainpage.mt.row_box.item(i).text())
        # print("row_list",row_list)
        column_list = []
        for a in range(mainpage.mt.col_box.count()):
            column_list.append(mainpage.mt.col_box.item(a).text())
        # print("column_list",column_list)
        return row_list,column_list


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


    @classmethod
    def fil_select(self,col_select):
        data = mainpage.mt.data_box.selectedItems()
        file_read = self.read_data(data)
        data_list = file_read[col_select]
        data_infil = []
        if "DATE" not in col_select.upper():
            for set_data in data_list:
                if set_data not in data_infil:
                    data_infil.append(set_data)            
        if "DATE" in col_select.upper():
            data_listnew = pd.DataFrame(data_list)
            data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in data_listnew[col_select]]
            data_listnew[col_select] = data_date
            year_date = list(pd.DatetimeIndex(data_listnew[col_select]).year.drop_duplicates())
            data_infil = [str(date_time) for date_time in year_date]
        data_infil.sort()                   
        return data_infil


    @classmethod
    def list_checkpath_filter(self):
        select_topic = []
        with open('filterdata.json', 'r') as file_readjson:
            read_json = file_readjson.read()
            read_data = json.loads(read_json)
        data = mainpage.mt.data_box.selectedItems()
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        return read_data,select_topic

    @classmethod
    def list_filter(self,fil_list_data,data_select):
        read_data,select_topic = self.list_checkpath_filter()
        for path in select_topic:
            # if "filter" in list(read_data[path].keys()):
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if data_select in list(read_data[code_md5]["filter"].keys()):
                filList = read_data[code_md5]["filter"][data_select]
            else:
                # if "DATE" in data_select.upper():
                #     filList = date_data
                # else:
                filList = fil_list_data
                # read_data[path]["filter"][data_select] = filList
                # with open('filterdata.json', 'w') as file_json:
                #     json.dump(read_data, file_json)  
            # else:
            #     if "DATE" in data_select.upper():
            #         filList = date_data
            #     else:
            #         filList = fil_list_data
            #     read_data[path]["filter"] = {}
            #     read_data[path]["filter"][data_select] = filList
            #     with open('filterdata.json', 'w') as file_json:
            #         json.dump(read_data, file_json)  

        return filList
    
    @classmethod
    def filter_boxadd(self):
        read_data,select_topic = self.list_checkpath_filter()
        mainpage.mt.fil_box.clear() 
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "filter" in list(read_data[code_md5].keys()): 
                list_filname = list(read_data[code_md5]["filter"].keys())
                for fil_name in range(len(list_filname)):               
                    toppic_ml = QListWidgetItem(list_filname[fil_name])
                    mainpage.mt.fil_box.insertItem(fil_name, toppic_ml)
    
    @classmethod
    def save_dim_meas(self):
        read_data,select_toppic = self.list_checkpath_meta()  
        dimension,measure = self.dim_meas_list()
        for path in select_toppic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            read_data[code_md5]["measure"] = measure
            read_data[code_md5]["dimensions"] = dimension
            with open('metadata.json', 'w') as file_json:
                json.dump(read_data, file_json)