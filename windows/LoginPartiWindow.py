# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminAdd.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('请输入您的id')
        self.resize(230, 170)

        self.textEdit_1 = QtWidgets.QTextEdit(self)
        self.textEdit_1.setEnabled(False)
        self.textEdit_1.setGeometry(QtCore.QRect(30, 30, 50, 30))
        self.textEdit_1.setUndoRedoEnabled(False)
        self.textEdit_1.setObjectName("textEdit_1")

       
        self.IdText = QtWidgets.QTextEdit(self)
        self.IdText.setGeometry(QtCore.QRect(100, 30, 100, 30))
        self.IdText.setObjectName("IdText")
        
        self.button_login = QtWidgets.QPushButton(self)
        self.button_login.setGeometry(QtCore.QRect(65, 70, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")

        self.retranslateUi()
        self.info = None

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.button_login.setText(_translate("Form", "登录"))
        self.textEdit_1.setText(_translate("Form", "ID："))

    def get_info(self):
        self.info = [self.IdText.toPlainText()]