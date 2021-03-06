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
        self.setWindowTitle("请输入您的信息")
        self.resize(230, 210)

        self.textEdit_1 = QtWidgets.QTextEdit(self)
        self.textEdit_1.setEnabled(False)
        self.textEdit_1.setGeometry(QtCore.QRect(30, 30, 50, 30))
        self.textEdit_1.setUndoRedoEnabled(False)
        self.textEdit_1.setObjectName("textEdit_1")

        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 70, 50, 30))
        self.textEdit_2.setUndoRedoEnabled(False)
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(self)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 110, 50, 30))
        self.textEdit_3.setUndoRedoEnabled(False)
        self.textEdit_3.setObjectName("textEdit_3")
       
        self.IdText = QtWidgets.QTextEdit(self)
        self.IdText.setGeometry(QtCore.QRect(100, 30, 100, 30))
        self.IdText.setObjectName("IdText")
        
        self.NameText = QtWidgets.QTextEdit(self)
        self.NameText.setGeometry(QtCore.QRect(100, 70, 100, 30))
        self.NameText.setObjectName("NameText")

        self.PasswordText = QtWidgets.QTextEdit(self)
        self.PasswordText.setGeometry(QtCore.QRect(100, 110, 100, 30))
        self.PasswordText.setObjectName("PasswordText")
       
        self.button_confirm = QtWidgets.QPushButton(self)
        self.button_confirm.setGeometry(QtCore.QRect(65, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.button_confirm.setFont(font)
        self.button_confirm.setObjectName("button_confirm")

        self.retranslateUi()
        self.info = None

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        
        self.button_confirm.setText(_translate("Form", "确认"))
        self.textEdit_1.setText(_translate("Form", "ID："))
        self.textEdit_2.setText(_translate("Form", "昵称："))
        self.textEdit_3.setText(_translate("Form", "密码："))

    def get_info(self):
        self.info = [self.IdText.toPlainText(), self.NameText.toPlainText(), self.PasswordText.toPlainText()]
