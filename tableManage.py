from datetime import *
from datetime import datetime
from doctest import master
from posixpath import split
from tracemalloc import stop
from PyQt5.QtWidgets import QListWidgetItem,QFileDialog,QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QDesktopWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QWindow
from PyQt5.QtCore import pyqtSlot,QSize
from functools import reduce
import calendar
import json
import sys
import os
import hashlib
import pandas as pd
import mainpage

 
class TableView(QWindow):

    @classmethod
    def importFile(self):

        pathfile = QFileDialog.getOpenFileName(mainpage.mainApp , 'Open File', os.getenv('HOME'), 'Excel File(*.csv *.xlsx *.xls)')

        if pathfile[0] != '':
            self.list_data(pathfile[0])


    
    @classmethod
    def reset_data(self): #select name file
        data = mainpage.mt.data_box.selectedItems()
        select_topic = []
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        if len(data) == 0: #check list select
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)
            mainpage.mt.table_box.setColumnCount(0)
            mainpage.mt.dim_box.clear()
            mainpage.mt.meas_box.clear()
            mainpage.mt.row_box.clear()
            mainpage.mt.col_box.clear()
            mainpage.mt.fil_box.clear()
            mainpage.mt.drill_box.clear()
        else:
            #select data ,add data in table,add list dimension and measure,list mark ,list filter 
            mainpage.mt.table_box.clear()
            mainpage.mt.row_box.clear()
            mainpage.mt.col_box.clear()
            mainpage.mt.table_box.setRowCount(0)
            for path in select_topic:
                self.list_data(path)
            self.union_show()
            file_read = self.read_data(select_topic)
            self.list_dimen(file_read)
            self.list_measure(file_read)
            self.filter_boxadd()
            self.add_list_drill()

    @classmethod
    def list_data(self,pathfile): # add path data in list_box
        namedata = pathfile.split("/") 
        md5_hash = hashlib.md5()
        file_md5 = open(pathfile, "rb")
        file_md5_read = file_md5.read()
        md5_hash.update(file_md5_read)
        code_md5 = md5_hash.hexdigest()
        self.meta_file(pathfile,code_md5)
        self.filter_file(pathfile,code_md5)
        self.filtermeasure_file(pathfile,code_md5)
        mainpage.mainTableau.dictpathfile[namedata[-1]] = pathfile
        list_data_box = []
        for i in range(mainpage.mt.data_box.count()):
            list_data_box.append(mainpage.mt.data_box.item(i).text())
        if pathfile not in list_data_box:
            mainpage.mt.data_box.insertItem(0, pathfile)
    
    @classmethod
    def path_start(self): # add path data in list_box from metadata
        try:
            with open('metadata.json', 'r') as file_readjson:
                read_json = file_readjson.read()
                read_data = json.loads(read_json)
            path_md5 = list(read_data.keys())
            mainpage.mt.data_box.clear()
            for a in range(len(path_md5)): 
                toppic_ml = QListWidgetItem(read_data[path_md5[a]]['path file'])
                mainpage.mt.data_box.insertItem(a, toppic_ml)
        except:
            dict_data = {}
            with open('metadata.json', 'w') as file_json:
                json.dump(dict_data, file_json)
    
    @classmethod
    def meta_file(self,pathfile,code_md5): # file metadata
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
    
    @classmethod
    def filter_file(self,pathfile,code_md5): # file filter dimensions
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
            dict_data[code_md5]["filter"] = {}
            with open('filterdata.json', 'w') as file_json:
                json.dump(dict_data, file_json)
    
    @classmethod
    def filtermeasure_file(self,pathfile,code_md5): # file filter measure
        try:
            with open('filtermeasure.json', 'r') as file_readjson:
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
            with open('filtermeasure.json', 'w') as file_json:
                json.dump(dict_data, file_json)
        except:            
            dict_data = {}
            dict_data[code_md5] = {}
            dict_data[code_md5]["path file"] = pathfile
            dict_data[code_md5]["filter"] = {}
            with open('filtermeasure.json', 'w') as file_json:
                json.dump(dict_data, file_json)

    @classmethod
    def read_data(self,select_toppic): # read file data
        list_union = []    
        for path in select_toppic:
            datapath = path       
            namedata_type = datapath.split(".")
            if namedata_type[-1] == 'csv': # read file follow type
                file_read = pd.read_csv(datapath, encoding = 'windows-1254')
            else:
                file_read = pd.read_excel(datapath,index_col=None)
            col_name = list(file_read.head(0))            
            check_head = [head_name for head_name in col_name if "DATE" in head_name.upper()] # set Date time data
            for head_namedate in check_head:
                data_date = [datetime.strftime(date, '%d/%m/%Y') if type(date) == datetime else datetime.strftime(datetime.strptime(date, "%d/%m/%Y").date(), '%d/%m/%Y') for date in file_read[head_namedate]]
                file_read[head_namedate] = data_date               
            list_union.append(file_read)

        frame = pd.concat(list_union, ignore_index=True, sort=False) # read union 
        col_sort = list(frame.head(0))
        union_frame = frame.sort_values(col_sort)
        dup = union_frame.drop_duplicates() # check same value
        set_dup = dup.reset_index(drop=True) # reset index file new

        return set_dup
       
    @classmethod
    def list_checkpath_meta(self): # read metadata
        select_topic = []
        with open('metadata.json', 'r') as file_readjson:
            read_json = file_readjson.read()
            read_data = json.loads(read_json)
        data = mainpage.mt.data_box.selectedItems()
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
            return read_data,select_topic

    @classmethod
    def list_dimen(self,file_read): # all dimention in file
        
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
           
    @classmethod # all all dimention in list
    def add_list_dim(self,dimList):
        mainpage.mt.dim_box.clear()
        for a in range(len(dimList)): 
            toppic_ml = QListWidgetItem(dimList[a])
            mainpage.mt.dim_box.insertItem(a, toppic_ml)
    
    @classmethod
    def list_measure(self,file_read): # all measure in file
        
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
    def add_list_measure(self,measList): # all all measure in list
        mainpage.mt.meas_box.clear()
        for a in range(len(measList)): 
            toppic_ml = QListWidgetItem(measList[a])
            mainpage.mt.meas_box.insertItem(a, toppic_ml)
    
    @classmethod
    def list_drilldown(self,data_drill): # all drilldown in file   
        read_data,select_topic = self.list_checkpath_meta() 
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "drilldown" in list(read_data[code_md5].keys()):
                read_data[code_md5]["drilldown"].append(data_drill)
            else:
                read_data[code_md5]["drilldown"] = []
                read_data[code_md5]["drilldown"].append(data_drill)
                datadrill = read_data[code_md5]["drilldown"]
            with open('metadata.json', 'w') as file_json:
                json.dump(read_data, file_json)  
    
    @classmethod
    def del_list_drilldown(self,data): # delete drilldown in file        
        read_data,select_topic = self.list_checkpath_meta() 
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "drilldown" in list(read_data[code_md5].keys()):
                read_data[code_md5]["drilldown"].remove(data)
                with open('metadata.json', 'w') as file_json:
                    json.dump(read_data, file_json)
                
  
    @classmethod
    def add_list_drill(self): # add drilldown in box  
        read_data,select_topic = self.list_checkpath_meta()
        mainpage.mt.drill_box.clear() 
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "drilldown" in list(read_data[code_md5].keys()): 
                key_drill = list(read_data[code_md5]["drilldown"])
                for n in range(len(key_drill)):               
                    toppic_ml = QListWidgetItem(key_drill[n])
                    mainpage.mt.drill_box.insertItem(n, toppic_ml)
            

    @classmethod
    def show_data(self): #show data in table
        
        row_list,column_list = self.row_column_list()
        select_topic = []
        data = mainpage.mt.data_box.selectedItems()

        for i in range(len(data)): # data select
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        file_read = self.read_data(select_topic)

        # dimensions measure mark filter all data in row and column
        list_dim,list_meas,list_mark,list_filter = self.dim_meas_rc(row_list,column_list) 

        # Check to mange frame data
        if len(list_dim) == 0 and len(list_meas) == 0 and len(list_mark) == 0:
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)  
            mainpage.mt.table_box.setColumnCount(0)
        elif  len(list_dim) == 0 and len(list_meas) != 0 and len(list_mark) != 0:
                    mainpage.mt.table_box.clear()
                    mainpage.mt.table_box.setRowCount(0)   
                    mainpage.mt.table_box.setColumnCount(0)  
        else:
            if len(list_mark) == 0 and len(list_meas) == 0:
                frame_merge = self.show_dim_meas(file_read,list_dim,list_meas,list_filter)
            else:
                new_file_read,list_dimfil = self.check_date_filter(file_read,list_dim,list_filter) # check data dimensions date time
                frame_merge = self.check_mark(new_file_read,list_dimfil,list_meas,list_mark) # check mark
            
            frame_data_add = self.filter_add(frame_merge,row_list,column_list,select_topic) # add filter dimensions
            frame_data = self.filtermeasure_add(frame_data_add,row_list,column_list,select_topic) # add filter measure

            # insert to table
            head_col = list(frame_data.head(0))
            len_file_column = len(head_col)
            len_file_row = len(frame_data)
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
    def filter_add(self,frame_merge,row_list,column_list,select_topic): #check filter data to add in frame data
        all_list = row_list+column_list
        with open('filterdata.json', 'r') as file_readjson:
            read_json = file_readjson.read()
            read_data = json.loads(read_json)
        name_col = list(frame_merge.keys())
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "filter" in list(read_data[code_md5].keys()):
                filter_key = list(read_data[code_md5]["filter"].keys())
                for fil_name in all_list:
                    drill_split = fil_name.split("+")
                    fil_split = drill_split[0].split(".")
                    if fil_name in filter_key: # compare all filter data and data from filter
                        filter_list = read_data[code_md5]["filter"][fil_name]
                        if len(fil_split) > 1:
                            frame_merge = frame_merge.loc[frame_merge[drill_split[0]].isin(filter_list)]
                        else:
                            frame_merge = frame_merge.loc[frame_merge[drill_split[0]].isin(filter_list)]          
                new_frame = frame_merge                 
            else:
                new_frame = frame_merge
        return new_frame
    
    
    @classmethod
    def filtermeasure_add(self,frame_merge,row_list,column_list,select_topic): # check filter data to add in frame data

        all_list = row_list+column_list
        with open('filtermeasure.json', 'r') as file_readjson:
            read_json = file_readjson.read()
            read_data = json.loads(read_json)

        name_col = list(frame_merge.keys())
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "filter" in list(read_data[code_md5].keys()):
                for fil_name in name_col: 
                    drill_split = fil_name.split("+")
                    fil_split = drill_split[0].split(".")
                    filter_key = list(read_data[code_md5]["filter"].keys())
                    if fil_name in filter_key: # compare all filter data and data from filter
                        filter_list = read_data[code_md5]["filter"][fil_name]
                        frame_merge = frame_merge.loc[(frame_merge[fil_name] >= float(filter_list[0])) & (frame_merge[fil_name] <= float(filter_list[1]))]
                new_frame = frame_merge                 
            else:
                new_frame = frame_merge
        return new_frame
    


    @classmethod
    def show_dim_meas(self,file_read,list_dim,list_meas,list_filter): # no measure add to table
        dict_add = {}
        for s_fil in range(len(list_dim)):
            
            upper_filter = list_filter[s_fil].upper()
            dim_name = list_dim[s_fil]
            dim_fil = list_filter[s_fil]
            if "DATE" in dim_name.upper(): # check dimensions date time
                data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in file_read[dim_name]]
                if  upper_filter == 'YEAR' or upper_filter == 'NONE':
                    fil_date = list(pd.DatetimeIndex(data_date).year)
                    dim_fil = 'Year'
                if upper_filter == 'QUARTER':
                    fil_date = list(pd.DatetimeIndex(data_date).quarter) 
                if upper_filter == 'MONTH':
                    fil_date = list(pd.DatetimeIndex(data_date).month) 
                if upper_filter == 'DATE':
                    fil_date = list(pd.DatetimeIndex(data_date).day)
                data_infil = [str(date_time) for date_time in fil_date]      
                dict_add[dim_fil+"."+dim_name] = data_infil         
            else:
                dict_add[dim_name] = file_read[dim_name]
            
        frame_data = pd.DataFrame.from_dict(dict_add)
        frame_merge = frame_data.drop_duplicates().sort_values(frame_data.keys()[0]) # sort

        for n, key in enumerate(frame_data.keys()):
            list_month = frame_merge[key]
            # month int to month name
            if "DATE" in key.upper() and 'MONTH' in key.upper():
                fil_date = [calendar.month_name[int(date_time)] for date_time in list_month]  
                frame_merge[key]  = fil_date
            elif "DATE" in key.upper() and 'MONTH' not in key.upper():
                fil_data = [str(data) for data in list_month]  
                frame_merge[key]  = fil_data
 
        return frame_merge
    
    @classmethod
    def check_mark(self,file_read,list_dimfil,list_meas,list_mark): # check mark measure
        frame_mark_list = []
        
        group_data = file_read.groupby(list_dimfil,as_index=False)
        for s_mark in range(len(list_mark)):# mark data
            upper_mark = list_mark[s_mark].upper() 
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
                list_mark[s_mark] = 'SUM'
            if upper_mark == 'MEDIAN':
                data_s_mark = group_data[list_meas[s_mark]].median()
            
            data_s_mark[list_mark[s_mark]+"."+list_meas[s_mark]] = data_s_mark[list_meas[s_mark]]
            del data_s_mark[list_meas[s_mark]]

            frame_mark_list.append(data_s_mark)

        if len(frame_mark_list) >= 1: # reduce all fream data measure
            frame_merge = reduce(lambda left, right: pd.merge(left,right), frame_mark_list)
        else:
            frame_merge = data_s_mark
        
        for n, key in enumerate(frame_merge.keys()): # month int to month name
            list_month = frame_merge[key]
            if "DATE" in key.upper() and "MONTH" in key.upper():
                fil_date = [calendar.month_name[int(date_time)] for date_time in list_month]  
                frame_merge[key]  = fil_date
            elif "DATE" in key.upper() and 'MONTH' not in key.upper():
                fil_data = [str(data) for data in list_month]  
                frame_merge[key]  = fil_data


        return frame_merge
    

    @classmethod
    def check_date_filter(self,file_read,list_dim,list_filter): # check data filter 

        list_dimfil = []
        for s_fil in range(len(list_dim)):
            upper_filter = list_filter[s_fil].upper()
            dim_name = list_dim[s_fil]
            dim_fil = list_filter[s_fil]
            
            if "DATE" in dim_name.upper():
                data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in file_read[dim_name]]
                if  upper_filter == 'YEAR' or upper_filter == 'NONE':
                    fil_date = list(pd.DatetimeIndex(data_date).year)
                    dim_fil = 'Year'
                if upper_filter == 'QUARTER':
                    fil_date = list(pd.DatetimeIndex(data_date).quarter) 
                if upper_filter == 'MONTH':
                    fil_date = list(pd.DatetimeIndex(data_date).month) 
                if upper_filter == 'DATE':
                    fil_date = list(pd.DatetimeIndex(data_date).day)
                file_read[dim_fil+"."+dim_name] = fil_date
                data_infil = [int(date_time) for date_time in fil_date]   
                list_dimfil.append(dim_fil+"."+dim_name)         
            else:
                file_read[dim_name] = file_read[dim_name]
                list_dimfil.append(dim_name)
            
        frame_data = pd.DataFrame.from_dict(file_read)
        frame_merge = frame_data.drop_duplicates().sort_values(frame_data.keys()[0])
            
        return file_read,list_dimfil


    
    @classmethod
    def dim_meas_rc(self,row_list,column_list): # list dimensions measure mark filter in data
        dimension,measure = self.dim_meas_list()
        list_dim = []
        list_meas = []
        list_mark = []
        list_filter = []

        for namerow in row_list:
            list_drill_row = namerow.split("+")
            list_namerow = list_drill_row[0].split(".")
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
            list_drill_col = namecolumn.split("+")
            list_namecolumn = list_drill_col[0].split(".")
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
    def dim_meas_list(self): # all list data dimensions and measure in data file
        dim_list = []
        meas_list = []
        for i in range(mainpage.mt.meas_box.count()):
            meas_list.append(mainpage.mt.meas_box.item(i).text())

        for i in range(mainpage.mt.dim_box.count()):
            dim_list.append(mainpage.mt.dim_box.item(i).text())                

        return dim_list,meas_list


    @classmethod
    def row_column_list(self): # row and column in GUI
        row_list = []
        for i in range(mainpage.mt.row_box.count()):
            row_list.append(mainpage.mt.row_box.item(i).text())
        column_list = []
        for a in range(mainpage.mt.col_box.count()):
            column_list.append(mainpage.mt.col_box.item(a).text())
        return row_list,column_list


    @classmethod
    def union_show(self): # list file union
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
    def fil_select_dim(self,col_select): # data filter select dimensions
        data = mainpage.mt.data_box.selectedItems()
        select_topic = []
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        file_read = self.read_data(select_topic)
        
        data_infil = []
        drill_select = col_select.split("+")
        split_select = drill_select[0].split(".")

        # check date time type
        if "DATE" not in drill_select[0].upper():
            data_list = file_read[split_select[0]]
            for set_data in data_list:
                if set_data not in data_infil:
                    data_infil.append(set_data)
            data_infil.sort()      
        elif "DATE" in col_select.upper():
            if len(split_select) > 1:
                data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in file_read[split_select[1]]]
                file_read[split_select[1]] = data_date
                if split_select[0] == 'Month':
                    fil_date = list(pd.DatetimeIndex(file_read[split_select[1]]).month.drop_duplicates())
                    data_int_fil = [int(date_time) for date_time in fil_date]    
                    data_int_fil.sort()    
                    data_infil = [str(calendar.month_name[date_time]) for date_time in data_int_fil] 
                else:
                    if  split_select[0] == 'Year':
                        fil_date = list(pd.DatetimeIndex(file_read[split_select[1]]).year.drop_duplicates())                
                    if split_select[0] == 'Quarter':
                        fil_date = list(pd.DatetimeIndex(file_read[split_select[1]]).quarter.drop_duplicates())    
                    if split_select[0] == 'Date':
                        fil_date = list(pd.DatetimeIndex(file_read[split_select[1]]).day.drop_duplicates())
                    data_int_fil = [int(date_time) for date_time in fil_date]    
                    data_int_fil.sort()    
                    data_infil = [str(date_time) for date_time in data_int_fil]  
            else:
                data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in file_read[split_select[0]]]
                file_read[split_select[0]] = data_date
                year_date = list(pd.DatetimeIndex(file_read[split_select[0]]).year.drop_duplicates())                
                data_infil = [str(date_time) for date_time in year_date]
                data_infil.sort()
 
        return data_infil
    
    @classmethod
    def fil_select_meas(self,col_select): # filter select measure
        split_select = col_select.split(".")
        if len(split_select) > 1:
            mark_fil = split_select[0]
            meas_fil = split_select[1]
        else:
            mark_fil = "NONE"
            meas_fil = split_select[0]
        
        return mark_fil,meas_fil


    @classmethod
    def list_checkpath_filter(self): # list path filter
        select_topic = []
        with open('filterdata.json', 'r') as file_readjson:
            read_json = file_readjson.read()
            read_data = json.loads(read_json)
        data = mainpage.mt.data_box.selectedItems()
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        return read_data,select_topic

    @classmethod
    def list_filter_dim(self,fil_list_data,data_select): # list filter dimensions
        read_data,select_topic = self.list_checkpath_filter()
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if data_select in list(read_data[code_md5]["filter"].keys()):
                filList = read_data[code_md5]["filter"][data_select]
            else:
                filList = fil_list_data
        return filList
    
    @classmethod
    def path_filtermeas(self):# path measure
        select_topic = []
        with open('filtermeasure.json', 'r') as file_readjson:
            read_json = file_readjson.read()
            read_data = json.loads(read_json)
        data = mainpage.mt.data_box.selectedItems()
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        return read_data,select_topic
   
    
    @classmethod
    def filter_boxadd(self): # add all name data filter in filter box 
        read_data,select_topic = self.list_checkpath_filter()
        read_datameas,select_topicmeas = self.path_filtermeas()
        mainpage.mt.fil_box.clear() 
        for path in select_topic:
            md5_hash = hashlib.md5()
            file_md5 = open(path, "rb")
            file_md5_read = file_md5.read()
            md5_hash.update(file_md5_read)
            code_md5 = md5_hash.hexdigest()
            if "filter" in list(read_data[code_md5].keys()): 
                list_filname = list(read_data[code_md5]["filter"].keys())                
            if "filter" in list(read_datameas[code_md5].keys()): 
                list_filnamemeas = list(read_datameas[code_md5]["filter"].keys())
            list_all = list_filname + list_filnamemeas
            if len(list_all) > 0:
                for fil_name in range(len(list_all)):               
                    toppic_ml = QListWidgetItem(list_all[fil_name])
                    mainpage.mt.fil_box.insertItem(fil_name, toppic_ml)
    

    @classmethod
    def data_graph(self): # mange frame data graph
        select_topic = []
        data = mainpage.mt.data_box.selectedItems()
        for i in range(len(data)):
            select_topic.append(str(mainpage.mt.data_box.selectedItems()[i].text()))
        file_read = self.read_data(select_topic)
        row_list,column_list = self.row_column_list()
        list_dim,list_meas,list_mark,list_filter = self.dim_meas_rc(row_list,column_list)

        if len(list_dim) == 0 and len(list_meas) == 0 and len(list_mark) == 0:
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)  
            mainpage.mt.table_box.setColumnCount(0)
        elif  len(list_dim) == 0 and len(list_meas) != 0 and len(list_mark) != 0:
            mainpage.mt.table_box.clear()
            mainpage.mt.table_box.setRowCount(0)   
            mainpage.mt.table_box.setColumnCount(0)  
        else:
            if len(list_mark) == 0 and len(list_meas) == 0:
                frame_merge = self.show_dim_meas(file_read,list_dim,list_meas,list_filter)
            else:
                new_file_read,list_dimfil = self.check_date_filter(file_read,list_dim,list_filter)
                frame_merge = self.check_mark(new_file_read,list_dimfil,list_meas,list_mark)
            
            frame_data_add = self.filter_add(frame_merge,row_list,column_list,select_topic)
            frame_data = self.filtermeasure_add(frame_data_add,row_list,column_list,select_topic)
        new_dict_frame_data = {}

        for key,value in frame_data.items():
            split_key = key.split(".")
            if len(split_key) > 1:
                new_key = key.replace(".", " ")
                new_dict_frame_data[new_key] = value
            else:
                new_dict_frame_data[key] = value
        
        frame_graph = pd.DataFrame(new_dict_frame_data)
        return frame_graph
        