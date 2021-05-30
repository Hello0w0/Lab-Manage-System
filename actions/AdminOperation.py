from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

import sys
sys.path.append("../")

import pymysql
import pandas as pd
import numpy as np

from utils.basic_pymysql import *

from windows.AdminOperationWindow import Ui_MainWindow as AdminOperationWindow
from windows.AdminOperationAddWindow import Ui_Form as AdminOperationAddWindow
from windows.AdminOperationDelWindow import Ui_Form as AdminOperationDelWindow
from windows.AdminOperationUpdWindow import Ui_Form as AdminOperationUpdWindow



class AdminOperation(QMainWindow, AdminOperationWindow):
    def __init__(self, admin_id, db_name = "Lab_Management_System"):
        super(AdminOperation, self).__init__()
        self.db = Database()
        self.db.direct_connect(db = db_name)
        self.admin_id = admin_id

        #找到这位管理员(admin)所负责的所有受试(participants)
        admin_query = "select * from participants inner join responsible on participants.id = responsible.participant_id having admin_id = {}".format(admin_id)

        self.df = pd.DataFrame(np.array(self.db.query(admin_query))[:,:5], columns=["ID", "姓名", "性别", "年龄", "测试结果"])
        self.setupUi(self)
        print(self.df)
        self.show_df()
        

        # search
        self.button_search.clicked.connect(self.search)
        # add
        self.button_add.clicked.connect(self.add)
        # delete
        self.button_delete.clicked.connect(self.delete)
        # update
        self.button_update.clicked.connect(self.update)

        self.button_confirm.clicked.connect(self.save)

        self.tableWidget.clicked.connect(self.get_current_item)


        # 用于更新数据
        self.info = None
        self.newinfo = False

        # 用于存储当前选择的行、列
        self.selected_row = 0
        self.selected_column = 0


    def show_df(self):
        """
        show the contents of self.df(pandas dataframes)
        """
        self.tableWidget.clear()

        self.tableWidget.setHorizontalHeaderLabels(['ID', '姓名', '性别', '年龄', '测试结果'])

        row, column = self.df.shape
        df_values = self.df.values
        for i in range(row):
            for j in range(column):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(df_values[i,j])))
    
    def get_current_item(self,index):
        self.selected_column = index.column()
        self.selected_row = index.row()

        
    def search(self):
        """
        查找功能
        """
        search_id = self.IdText.toPlainText()
        search_name = self.NameText.toPlainText()
        search_gender = self.GenderComboBox.currentText()
        search_age = self.AgeText.toPlainText()
        search_outcome = self.OutcomeText.toPlainText()

        search_condition = "select * from {} where (True"
        if search_id:
            search_condition + " and id like '%{}%'".format(search_id)
        if search_name:
            search_condition + " and name like '%{}%'".format(search_name)
        if search_gender != "不限":
            search_condition + " and gender = '{}'".format(search_gender)
        if search_age:
            search_condition + " and age {}".format(search_gender)
        if search_outcome:
            search_condition + " and outcome = {}".format(search_outcome)
        search_condition + ")"

        print(search_condition)


    
    def add(self):
        """
        添加一条记录
        """
        self.newinfo = False
        self.addwindow = AdminOperationAddWindow()
        self.addwindow.ConfirmButton.clicked.connect(self.get_add_info)
        self.addwindow.exec_()

        if self.newinfo:
            row_number = self.df.shape[0]
            self.df.loc[row_number] = self.info
            self.show_df()
        
    def get_add_info(self):
        self.addwindow.get_info()
        self.info = self.addwindow.info
        self.newinfo = True
        self.addwindow.close()



    def delete(self):
        """
        删除一条记录
        """
        self.newinfo = False
        now_selected_rowindex = self.selected_row
        if self.df.shape[0] <= now_selected_rowindex:
            return

        now_selected_item = self.df.loc[now_selected_rowindex].tolist()
        self.deletewindow = AdminOperationDelWindow(now_selected_item)
        self.deletewindow.ConfirmButton.clicked.connect(self.get_del_info)
        self.deletewindow.exec_()
        
        if self.newinfo:
            self.df.drop(index = now_selected_rowindex, inplace = True)
            self.df.reset_index(drop = True, inplace = True)
            self.show_df()

    def get_del_info(self):
        self.deletewindow.close()
        self.newinfo = True


    def update(self):
        """
        更新一条记录
        """
        self.newinfo = False
        now_selected_rowindex = self.selected_row
        if self.df.shape[0] <= now_selected_rowindex:
            return

        now_selected_item = self.df.loc[now_selected_rowindex].tolist()
        self.updatewindow = AdminOperationUpdWindow(now_selected_item)
        self.updatewindow.ConfirmButton.clicked.connect(self.get_upd_info)
        self.updatewindow.exec_()
        
        if self.newinfo:
            self.df.loc[now_selected_rowindex] = self.info
            self.show_df()

    def get_upd_info(self):
        self.updatewindow.get_info()
        self.info = self.updatewindow.info
        self.newinfo = True
        self.updatewindow.close()

    def save(self):
        pass
        


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = AdminOperation(admin_id = '0001')
    win.show()
    sys.exit(app.exec())
