from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView

import sys

from actions.AdminAction import AdminOperation
from actions.LoginAction import Login
from actions.SetAccountAction import SetAccount
from actions.ParticipantAction import Participant
#from .initialize import initialize

from windows.ErrorPromptWindow import Ui_Form as ErrorPromptWindow

class Lab_Management_System(object):
    def __init__(self):
        self.info = None
    


    
    def ShowLoginWindow(self):
        try:
            self.admin.close()
        except:
            pass
        try:
            self.account.close()
        except:
            pass
        try:
            self.parti.close()
        except:
            pass
        self.login = Login()
        self.login.login_signal.connect(self.DoLogin)
        self.login.show()

    

    def ShowAdminWindow(self, admin_id):
        try:
            self.login.close()
        except:
            pass
        try:
            self.parti.close()
        except:
            pass
        try:
            self.admin.close()
        except:
            pass

        self.admin = AdminOperation(admin_id = admin_id)
        self.admin.button_logout.clicked.connect(self.ShowLoginWindow)
        self.admin.show()


    def ShowPartiWindow(self, parti_id):
        try:
            self.login.close()
        except:
            pass
        try:
            self.account.close()
        except:
            pass
        try:
            self.admin.close()
        except:
            pass

        self.parti = Participant(parti_id = parti_id)
        self.parti.button_logout.clicked.connect(self.ShowLoginWindow)
        self.parti.show()


    def ShowAccountWindow(self, admin_id):
        try:
            self.login.close()
        except:
            pass
        try:
            self.parti.close()
        except:
            pass
        try:
            self.admin.close()
        except:
            pass
        self.account = SetAccount(admin_id = admin_id)
        self.account.backtologin_signal.connect(self.ShowLoginWindow)
        self.account.button_logout.clicked.connect(self.ShowLoginWindow)
        self.account.show()


    
    
    def DoLogin(self, login_mode, login_info):
        if login_mode == "admin":
            self.ShowAdminWindow(login_info)
        elif login_mode == "participant":
            self.ShowPartiWindow(login_info)
        elif login_mode == "setaccount":
            self.ShowAccountWindow(login_info)
        else:
            errorwindow = ErrorPromptWindow("出现未知登录模式")
            errorwindow.exec_()



if __name__ == "__main__":
    lab_management_system = Lab_Management_System()
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    
    lab_management_system.ShowLoginWindow()
    sys.exit(app.exec())
    
    