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
from windows.ErrorPromptWindow import Ui_Form as ErrorPromptWindow



class AdminOperation(QMainWindow, AdminOperationWindow):
    def __init__(self, admin_id, db_name = "Lab_Management_System"):
        super(AdminOperation, self).__init__()
        self.db = Database()
        self.db.direct_connect(db = db_name)
        self.admin_id = admin_id
        self.admin_name = self.db.query("select name from admins where id = '{}'".format(self.admin_id))[0][0]
        #找到这位管理员(admin)所负责的所有受试(participants)
        self.admin_query = "select * from participants inner join responsible on participants.id = responsible.participant_id having admin_id = '{}'".format(admin_id)
        admin_participants = self.db.query(self.admin_query)
        if admin_participants:
            self.df = pd.DataFrame(np.array(admin_participants)[:,:5], columns=["ID", "姓名", "性别", "年龄", "测试结果"])
        else:
            self.df = pd.DataFrame(columns=["ID", "姓名", "性别", "年龄", "测试结果"])
        self.setupUi(self, self.admin_name)
        self.show_df()
        

        # search
        self.button_search.clicked.connect(self.search)
        # add
        self.button_add.clicked.connect(self.add)
        # delete
        self.button_delete.clicked.connect(self.delete)
        # update
        self.button_update.clicked.connect(self.update)

        self.tableWidget.clicked.connect(self.get_current_item)


        # 用于更新数据
        self.info = None
        self.change_permission = False

        # 用于存储当前选择的行、列
        self.selected_row = 0
        self.selected_column = 0

        # 用于发送提示
        self.prompttext = None


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
        search_result = self.ResultText.toPlainText()

        search_condition = "select * from ({}) as a where (True"
        if search_id:
            search_condition = search_condition + " and id like '%{}%'".format(search_id)
        if search_name:
            search_condition = search_condition + " and name like '%{}%'".format(search_name)
        if search_gender != "不限":
            search_condition = search_condition + " and gender = '{}'".format(search_gender)
        if search_age:
            search_condition = search_condition + " and age {}".format(search_age)
        if search_result:
            search_condition = search_condition + " and result = '{}'".format(search_result)
        search_condition = search_condition + ")"

        search_condition = search_condition.format(self.admin_query)

        print(search_condition)

        admin_participants = self.db.query(search_condition)
        if admin_participants:
            self.df = pd.DataFrame(np.array(admin_participants)[:,:5], columns=["ID", "姓名", "性别", "年龄", "测试结果"])
        else:
            self.df = pd.DataFrame(columns=["ID", "姓名", "性别", "年龄", "测试结果"])
        
        self.show_df()

    
    def add(self):
        """
        添加一条记录
        """
        self.newinfo = False
        self.addwindow = AdminOperationAddWindow()
        self.addwindow.ConfirmButton.clicked.connect(self.get_add_info)
        self.addwindow.exec_()            
            
    def get_add_info(self):
        self.addwindow.get_info()
        self.info = self.addwindow.info
        self.change_permission = True
        current_ids = self.db.query("select id from participants")
        if current_ids:
            current_ids = np.array(current_ids).squeeze()
            if self.info[0] in current_ids:
                self.change_permission = False
                self.prompttext = "id已被使用，请使用其他id"
            else:
                try:
                    age = int(self.info[3])
                    if age < 0:
                        self.change_permission = False
                        self.prompttext = "年龄输入不符合规范，请检查后输入"
                except:
                    self.change_permission = False
                    self.prompttext = "年龄输入不符合规范，请检查后输入"
            
        if self.change_permission:
            self.db.insert_into_table('participants', "'{}','{}','{}',{},'{}'".format(self.info[0], self.info[1], self.info[2], self.info[3], self.info[4]))
            self.db.insert_into_table('responsible', "'{}','{}'".format(self.admin_id, self.info[0]))
            admin_participants = self.db.query(self.admin_query)
            self.df = pd.DataFrame(np.array(admin_participants)[:,:5], columns=["ID", "姓名", "性别", "年龄", "测试结果"])
            self.addwindow.close()
            self.show_df()
        else:
            self.errorwindow = ErrorPromptWindow(self.prompttext)
            self.errorwindow.exec_()

    def delete(self):
        """
        删除一条记录
        """
        now_selected_rowindex = self.selected_row
        if self.df.shape[0] <= now_selected_rowindex:
            return

        self.info = self.df.loc[now_selected_rowindex].tolist()
        self.deletewindow = AdminOperationDelWindow(self.info)
        self.deletewindow.ConfirmButton.clicked.connect(self.get_del_info)
        self.deletewindow.exec_()

    def get_del_info(self):
        # self.db.delete_from_table('responsible', "participant_id = {}".format(self.info[0]))
        self.db.delete_from_table('participants',"id = {}".format(self.info[0]))
        self.deletewindow.close()

        admin_participants = self.db.query(self.admin_query)
        if admin_participants:
            self.df = pd.DataFrame(np.array(admin_participants)[:,:5], columns=["ID", "姓名", "性别", "年龄", "测试结果"])
        else:
            self.df = pd.DataFrame(columns=["ID", "姓名", "性别", "年龄", "测试结果"])
        self.show_df()


    def update(self):
        """
        更新一条记录
        """
        self.newinfo = False
        now_selected_rowindex = self.selected_row
        if self.df.shape[0] <= now_selected_rowindex:
            return

        self.info = self.df.loc[now_selected_rowindex].tolist()
        self.updatewindow = AdminOperationUpdWindow(self.info)
        self.updatewindow.ConfirmButton.clicked.connect(self.get_upd_info)
        self.updatewindow.exec_()

    def get_upd_info(self):
        self.updatewindow.get_info()
        previous_info = self.info
        self.info = self.updatewindow.info
        self.change_permission = True
        
        if self.info[0] != previous_info[0]:
            current_ids = self.db.query("select id from participants")
            if current_ids:
                current_ids = np.array(current_ids).squeeze()
                if self.info[0] in current_ids:
                    self.change_permission = False
                    self.prompttext = "id已被使用，请使用其他id"

        if self.info[3] != previous_info[3]: 
            try:
                age = int(self.info[3])
                if age < 0:
                    self.change_permission = False
                    self.prompttext = "年龄输入不符合规范，请检查后输入"
            except:
                self.change_permission = False
                self.prompttext = "年龄输入不符合规范，请检查后输入"

        if self.change_permission:
            if self.info[0] != previous_info[0]:
            #更换了id的情况
            # update_table(self, table_name, info, condition, show = False):
                self.db.delete_from_table('responsible', "participant_id = {}".format(previous_info[0]))
                self.db.update_table('participants', "id = '{}',name = '{}',gender = '{}', age = {}, result = '{}'".format(self.info[0], self.info[1], self.info[2], self.info[3], self.info[4]), "id = {}".format(previous_info[0]))
                self.db.insert_into_table('responsible', "'{}','{}'".format(self.admin_id, self.info[0]))
            else:
                self.db.update_table('participants', "name = '{}',gender = '{}', age = {}, result = '{}'".format(self.info[1], self.info[2], self.info[3], self.info[4]), "id = {}".format(previous_info[0]))
            
            admin_participants = self.db.query(self.admin_query)
            self.df = pd.DataFrame(np.array(admin_participants)[:,:5], columns=["ID", "姓名", "性别", "年龄", "测试结果"])
            self.updatewindow.close()
            self.show_df()

        else:
            self.errorwindow = ErrorPromptWindow(self.prompttext)
            self.errorwindow.exec_()

    def LogOut(self):
        return

        


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = AdminOperation(admin_id = '0001')
    win.show()
    sys.exit(app.exec())
