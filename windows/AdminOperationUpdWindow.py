# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminAdd.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QDialog):
    def __init__(self, info):
        super().__init__()
        self.info = info
        self.setWindowTitle('请输入修改后的信息')
        self.resize(640, 180)

        self.GenderComboBox = QtWidgets.QComboBox(self)
        self.GenderComboBox.setGeometry(QtCore.QRect(270, 80, 100, 30))
        self.GenderComboBox.setEditable(False)
        self.GenderComboBox.setMaxVisibleItems(3)
        self.GenderComboBox.setMaxCount(3)
        self.GenderComboBox.setObjectName("GenderComboBox")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(150, 30, 100, 30))
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(390, 30, 100, 30))
        self.textEdit_2.setUndoRedoEnabled(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self)
        self.textEdit_3.setEnabled(False)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 30, 100, 30))
        self.textEdit_3.setUndoRedoEnabled(False)
        self.textEdit_3.setObjectName("textEdit_3")
        self.IdText = QtWidgets.QTextEdit(self)
        self.IdText.setGeometry(QtCore.QRect(30, 80, 100, 30))
        self.IdText.setObjectName("IdText")
        self.textEdit_5 = QtWidgets.QTextEdit(self)
        self.textEdit_5.setEnabled(False)
        self.textEdit_5.setGeometry(QtCore.QRect(270, 30, 100, 30))
        self.textEdit_5.setUndoRedoEnabled(False)
        self.textEdit_5.setObjectName("textEdit_5")
        self.NameText = QtWidgets.QTextEdit(self)
        self.NameText.setGeometry(QtCore.QRect(150, 80, 100, 30))
        self.NameText.setObjectName("NameText")
        self.AgeText = QtWidgets.QTextEdit(self)
        self.AgeText.setGeometry(QtCore.QRect(390, 80, 100, 30))
        self.AgeText.setObjectName("AgeText")
        self.textEdit_4 = QtWidgets.QTextEdit(self)
        self.textEdit_4.setEnabled(False)
        self.textEdit_4.setGeometry(QtCore.QRect(510, 30, 100, 30))
        self.textEdit_4.setUndoRedoEnabled(False)
        self.textEdit_4.setObjectName("textEdit_4")
        self.ResultText = QtWidgets.QTextEdit(self)
        self.ResultText.setGeometry(QtCore.QRect(510, 80, 100, 30))
        self.ResultText.setObjectName("ResultText")
        self.ConfirmButton = QtWidgets.QPushButton(self)
        self.ConfirmButton.setGeometry(QtCore.QRect(470, 130, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setObjectName("ConfirmButton")

        self.retranslateUi(self)
        self.info = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        #Form.setWindowTitle(_translate("Form", "Form"))
        self.GenderComboBox.setItemText(0, _translate("Form", "男"))
        self.GenderComboBox.setItemText(1, _translate("Form", "女"))
        self.GenderComboBox.setItemText(2, _translate("Form", "其他"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">姓名</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">年龄</span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">ID</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">性别</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">测试结果</span></p></body></html>"))
        
        self.IdText.setText(_translate("Form", self.info[0]))
        self.NameText.setText(_translate("Form", self.info[1]))
        if self.info[2] == "女":
                currentIndex = 1
        elif self.info[2] == "其他":
                currentIndex = 2
        else:
                currentIndex = 0
        self.GenderComboBox.setCurrentIndex(currentIndex)
        self.AgeText.setText(_translate("Form", self.info[3]))
        self.ResultText.setText(_translate("Form", self.info[4]))
        self.ConfirmButton.setText(_translate("Form", "确认保存"))

    def get_info(self):
        self.info = [self.IdText.toPlainText(), self.NameText.toPlainText(), self.GenderComboBox.currentText(), self.AgeText.toPlainText(), self.ResultText.toPlainText()]
