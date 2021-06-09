from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

import sys
sys.path.append("../")

import pymysql
import pandas as pd
import numpy as np

from utils.basic_pymysql import *

from windows.SetAccountWindow import Ui_MainWindow as SetAccountWindow
from windows.SetAccountAddAdminWindow import Ui_Form as SetAccountAddAdminWindow
from windows.SetAccountDelAdminWindow import Ui_Form as SetAccountDelAdminWindow
from windows.SetAccountChangePasswordWindow import Ui_Form as SetAccountChangePasswordWindow
from windows.LoginAdminWindow import Ui_Form as LoginAdminWindow
from windows.ErrorPromptWindow import Ui_Form as ErrorPromptWindow



class SetAccount(QMainWindow, SetAccountWindow):
    backtologin_signal = pyqtSignal()
    def __init__(self, admin_id, db_name = "Lab_Management_System"):
        super(SetAccount, self).__init__()
        self.db = Database()
        self.db.direct_connect(db = db_name)
        self.admin_id = admin_id
        self.admin_name = self.db.query("select name from admins where id = '{}'".format(self.admin_id))[0][0]
        self.admin_info = [self.admin_id, self.admin_name]

        self.setupUi(self, admin_name = self.admin_name)
        
        self.button_newaccount.clicked.connect(self.NewAccount)
        self.button_changepassword.clicked.connect(self.ChangePassword)
        self.button_delaccount.clicked.connect(self.DelAccount)

        self.info = None
        self.LoginMode = None
        self.LoginInfo = None

        self.change_permission = False
        
    def NewAccount(self):
        self.newaccountwindow = SetAccountAddAdminWindow() 
        self.newaccountwindow.button_confirm.clicked.connect(self.NewAccountSet)
        self.newaccountwindow.exec_()
    
    def NewAccountSet(self):
        self.newaccountwindow.get_info()
        self.info = self.newaccountwindow.info
        self.change_permission = True

        current_ids = self.db.query("select id from admins")
        if current_ids:
            current_ids = np.array(current_ids).squeeze()
            if self.info[0] in current_ids:
                self.change_permission = False
                self.prompttext = "id已被使用，请使用其他id"
                self.errorwindow = ErrorPromptWindow(self.prompttext)
                self.errorwindow.exec_()

        if self.change_permission:
            self.db.insert_into_table("admins", "'{}', '{}'".format(self.info[0], self.info[1]))
            self.db.insert_into_table("admin_passwords", "'{}', '{}'".format(self.info[0], self.info[2]))
            self.prompttext = "管理员账户创建成功"
            self.errorwindow = ErrorPromptWindow(self.prompttext)
            self.errorwindow.exec_()
            
    
    def ChangePassword(self):
        self.changepasswordwindow = SetAccountChangePasswordWindow(admin_info = self.admin_info)
        self.changepasswordwindow.button_confirm.clicked.connect(self.ChangePasswordCheck)
        self.changepasswordwindow.exec_()
    
    def ChangePasswordCheck(self):
        self.changepasswordwindow.get_info()
        self.info = self.changepasswordwindow.info
        self.change_permission = True
        if self.info[0]:
            if self.info[0] != self.info[1]:
                self.change_permission = False
                self.prompttext = "两次输入的密码不一致，请检查后输入"
                self.errorwindow = ErrorPromptWindow(self.prompttext)
                self.errorwindow.exec_()
        else:
            self.change_permission = False
            self.prompttext = "还未输入密码"
            self.errorwindow = ErrorPromptWindow(self.prompttext)
            self.errorwindow.exec_()

        if self.change_permission:
            self.db.update_table("admin_passwords","password = '{}'".format(self.info[1]),"id = '{}'".format(self.admin_info[0]))
            self.prompttext = "密码修改成功"
            self.errorwindow = ErrorPromptWindow(self.prompttext)
            self.errorwindow.exec_()

    def DelAccount(self):
        self.delaccountwindow = SetAccountDelAdminWindow(admin_info = self.admin_info)
        self.delaccountwindow.button_confirm.clicked.connect(self.DirectDelAccount)
        self.delaccountwindow.button_cancel.clicked.connect(self.CancelDelAccount)
        self.delaccountwindow.button_transfer.clicked.connect(self.TransAccount)
        self.delaccountwindow.exec_()
    
    def DirectDelAccount(self):
        self.db.delete_from_table("participants", "id = (select id from (select * from participants inner join responsible on participants.id = responsible.participant_id having admin_id = {}) as a)".format(self.admin_id))
        # self.db.delete_from_table("responsible", "admin_id = '{}'".format(self.admin_id))
        # self.db.delete_from_table("admin_passwords", "id = '{}'".format(self.admin_id))
        self.db.delete_from_table("admins", "id = {}".format(self.admin_id))
        
        errorwindow = ErrorPromptWindow("删除账户成功")
        errorwindow.show()
        self.delaccountwindow.close()
        self.BackToLogin()

    def CancelDelAccount(self):
        self.delaccountwindow.close()

    def TransAccount(self):
        self.transaccountwindow = LoginAdminWindow(reminder="请输入记录转移对象管理员的id与密码")
        self.transaccountwindow.button_login.clicked.connect(self.DoTransAccount)
        self.delaccountwindow.close()
        self.transaccountwindow.show()
    
    def DoTransAccount(self):
        self.transaccountwindow.get_info()
        info = self.transaccountwindow.info
        id = info[0]
        password = info[1]

        stored_password = self.db.query("select password from admin_passwords where id='{}'".format(id))
        try:
            stored_password = stored_password[0][0]
        except:
            stored_password = None

        if stored_password:
            if stored_password == password:
                self.db.update_table("responsible","admin_id = '{}'".format(id), "admin_id = '{}'".format(self.admin_id))
                self.db.delete_from_table("admin_passwords", "id = '{}'".format(self.admin_id))
                self.db.delete_from_table("admins", "id = '{}'".format(self.admin_id))
                errorwindow = ErrorPromptWindow("记录迁移成功")
                errorwindow.show()
                self.transaccountwindow.close()
                self.BackToLogin()
                
            else:
                prompttext = "id或密码输入错误"
                self.errorwindow = ErrorPromptWindow(prompttext)
                self.errorwindow.exec_()
        else:
            prompttext = "id或密码输入错误"
            self.errorwindow = ErrorPromptWindow(prompttext)
            self.errorwindow.exec_()
    
    def BackToLogin(self):
        self.backtologin_signal.emit()


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = SetAccount(admin_id='0002')
    win.show()
    sys.exit(app.exec())
