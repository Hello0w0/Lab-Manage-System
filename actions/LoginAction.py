from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

import sys
sys.path.append("../")

import pymysql
import pandas as pd
import numpy as np

from utils.basic_pymysql import *

from windows.LoginWindow import Ui_MainWindow as LoginWindow
from windows.LoginAdminWindow import Ui_Form as LoginAdminWindow
from windows.LoginPartiWindow import Ui_Form as LoginPartiWindow
from windows.ErrorPromptWindow import Ui_Form as ErrorPromptWindow



class Login(QMainWindow, LoginWindow):
    login_signal = pyqtSignal(str,str)
    def __init__(self, db_name = "Lab_Management_System"):
        super(Login, self).__init__()
        self.db = Database()
        self.db.direct_connect(db = db_name)
        self.setupUi(self)
        
        self.button_adminlogin.clicked.connect(self.AdminLogin)
        self.button_partilogin.clicked.connect(self.PartiLogin)
        self.button_setaccount.clicked.connect(self.SetAccount)

        self.info = None
        self.login_mode = None
        self.login_info = None
        

    def AdminLogin(self):
        self.adminwindow = LoginAdminWindow() 
        self.adminwindow.button_login.clicked.connect(self.AdminLoginCheck)
        self.adminwindow.exec_()
    
    def AdminLoginCheck(self):
        self.newinfo = True
        self.adminwindow.get_info()
        info = self.adminwindow.info
        id = info[0]
        password = info[1]

        stored_password = self.db.query("select password from admin_passwords where id='{}'".format(id))
        try:
            stored_password = stored_password[0][0]
        except:
            stored_password = None

        if stored_password:
            if stored_password == password:
                self.login_mode = "admin"
                self.login_info = id
                self.adminwindow.close()
                self.RaiseLogin()
            else:
                prompttext = "id或密码输入错误"
                self.errorwindow = ErrorPromptWindow(prompttext)
                self.errorwindow.exec_()
        else:
            prompttext = "id或密码输入错误"
            self.errorwindow = ErrorPromptWindow(prompttext)
            self.errorwindow.exec_()

        # self.adminwindow.close()
    
    def PartiLogin(self):
        self.participantwindow = LoginPartiWindow() 
        self.participantwindow.button_login.clicked.connect(self.PartiLoginCheck)
        self.participantwindow.exec_()
    
    def PartiLoginCheck(self):
        self.participantwindow.get_info()
        info = self.participantwindow.info
        id = info[0]

        parti_info = self.db.query("select id from participants where id ='{}'".format(id))

        if parti_info:
            self.login_mode = "participant"
            self.login_info = id
            self.participantwindow.close()
            self.RaiseLogin()
        else:
            prompttext = "未找到指定id的受试者"
            self.errorwindow = ErrorPromptWindow(prompttext)
            self.errorwindow.exec_()


        # self.adminwindow.close()
    
    def SetAccount(self):
        self.accountwindow = LoginAdminWindow() 
        self.accountwindow.button_login.clicked.connect(self.AccountLoginCheck)
        self.accountwindow.exec_()
    
    def AccountLoginCheck(self):
        self.newinfo = True
        self.accountwindow.get_info()
        info = self.accountwindow.info
        id = info[0]
        password = info[1]

        stored_password = self.db.query("select password from admin_passwords where id='{}'".format(id))
        try:
            stored_password = stored_password[0][0]
        except:
            stored_password = None

        if stored_password:
            if stored_password == password:
                self.login_mode = "setaccount"
                self.login_info = id
                self.accountwindow.close()
                self.RaiseLogin()
            else:
                prompttext = "id或密码输入错误"
                self.errorwindow = ErrorPromptWindow(prompttext)
                self.errorwindow.exec_()
        else:
            prompttext = "id或密码输入错误"
            self.errorwindow = ErrorPromptWindow(prompttext)
            self.errorwindow.exec_()
    
    def RaiseLogin(self):
        self.login_signal.emit(self.login_mode, self.login_info)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec())
