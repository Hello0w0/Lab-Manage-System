from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QHeaderView

import sys
sys.path.append("../")

import pymysql
import pandas as pd
import numpy as np

from utils.basic_pymysql import *

from windows.ParticipantWindow import Ui_Form as ParticipantWindow
from windows.ErrorPromptWindow import Ui_Form as ErrorPromptWindow



class Participant(ParticipantWindow):
    def __init__(self, parti_id, db_name = "Lab_Management_System"):
        self.db = Database()
        self.db.direct_connect(db = db_name)
        self.parti_id = parti_id
        self.parti_info = self.db.query("select * from participants where id  = '{}'".format(self.parti_id))[0]
        print(self.parti_info)

        self.setupUi(row_info=self.parti_info)

  



if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = Participant(parti_id='0001')
    win.show()
    sys.exit(app.exec())
