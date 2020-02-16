# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCursor, QPainter, QPixmap, QIcon, QFont
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
import GetForkSummary as getForkSummary


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("ForkXplore：a tool of Fork Summary Generation")
        self.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setupUi()

        getF=getForkSummary
        input_1,input_2,commit_summary_list,fork_summary=getF.init_Summary()
        self.setData(input_1,input_2,commit_summary_list,fork_summary)
        #self.label_4.setText("sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")


    def setData(self,input_1,input_2,commit_summary_list,fork_summary):
        self.lineEdit.setText(input_1)
        self.lineEdit_2.setText(input_2)
        str_commit_summary=''
        for i in commit_summary_list:
            str_commit_summary=str_commit_summary+i+'\n'
        self.label_4.setText(str_commit_summary)
        self.label_3.setText(fork_summary)

    def setupUi(self):
        self.centralwidget.setObjectName("centralwidget")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 30, 500, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 70, 500, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 100, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 100, 16))
        self.label_2.setObjectName("label_2")




        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 100, 600, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_fork_title = QtWidgets.QLabel(self.frame)
        self.label_fork_title.setGeometry(QtCore.QRect(0, 0, 600, 20))
        self.label_fork_title.setText("Fork Summary：")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 600, 80))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")




        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(70, 200, 600, 500))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.label_commit_title = QtWidgets.QLabel(self.frame_2)
        self.label_commit_title.setGeometry(QtCore.QRect(0, 0, 461, 20))
        self.label_commit_title.setText("CommitSummary：")

        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(0, 20, 600, 100))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ForkXplore：a tool of Fork Summary Generation"))
        self.label.setText(_translate("MainWindow", "CommitAddress_1:"))
        self.label_2.setText(_translate("MainWindow", "CommitAddress_2:"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    app.exit(app.exec_())