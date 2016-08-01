# -*- coding: utf-8 -*-
import os
from openpyxl import load_workbook
import pandas as pd
class DataProcess():
    def __init__(self,root):
        self.root=root
    def split_table(self):
        for f in os.listdir(self.root):
            if f.endswith(".xlsx"):
                fileName=f
                f=os.path.join(dir,f)
                wb=load_workbook(f)
                for sheetName in wb.get_sheet_names():
                    if sheetName!="Knight":
                        df=pd.read_excel(f,sheetname=sheetName)
                        companies=df["稽核对象"].drop_duplicates().iteritems()
                        for company in companies:
                            dirName=os.path.join(dir,company[1])
                            if not os.path.exists(dirName):
                                os.mkdir(dirName)
                            filePath=os.path.join(dirName,fileName)
                            df[df["稽核对象"]==company[1]].to_excel(filePath)

if "__name__" == "__main__":

    zhiGongsi = "E:\\大数据北京\\code\\拆分\\省公司、直属单位"
    d=DataProcess(zhiGongsi)
    d.split_table()