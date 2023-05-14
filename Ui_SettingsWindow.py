# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(874, 348)
        SettingsWindow.setMinimumSize(QtCore.QSize(874, 348))
        SettingsWindow.setMaximumSize(QtCore.QSize(874, 348))
        self.adminInfo_tableWidget = QtWidgets.QTableWidget(SettingsWindow)
        self.adminInfo_tableWidget.setGeometry(QtCore.QRect(10, 30, 511, 261))
        self.adminInfo_tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.adminInfo_tableWidget.setObjectName("adminInfo_tableWidget")
        self.adminInfo_tableWidget.setColumnCount(2)
        self.adminInfo_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.adminInfo_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminInfo_tableWidget.setHorizontalHeaderItem(1, item)
        self.manageAdmin_lbl = QtWidgets.QLabel(SettingsWindow)
        self.manageAdmin_lbl.setGeometry(QtCore.QRect(30, 10, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.manageAdmin_lbl.setFont(font)
        self.manageAdmin_lbl.setObjectName("manageAdmin_lbl")
        self.label_2 = QtWidgets.QLabel(SettingsWindow)
        self.label_2.setGeometry(QtCore.QRect(550, 20, 101, 16))
        self.label_2.setObjectName("label_2")
        self.add_admin_btn = QtWidgets.QPushButton(SettingsWindow)
        self.add_admin_btn.setGeometry(QtCore.QRect(680, 140, 113, 32))
        self.add_admin_btn.setObjectName("add_admin_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(SettingsWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(550, 50, 251, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.username_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.gridLayout.addWidget(self.username_lineEdit, 0, 1, 1, 1)
        self.username_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.username_lbl.setObjectName("username_lbl")
        self.gridLayout.addWidget(self.username_lbl, 0, 0, 1, 1)
        self.password_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout.addWidget(self.password_lineEdit, 1, 1, 1, 1)
        self.password_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.password_lbl.setObjectName("password_lbl")
        self.gridLayout.addWidget(self.password_lbl, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(SettingsWindow)
        self.label.setGeometry(QtCore.QRect(550, 190, 91, 16))
        self.label.setObjectName("label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(SettingsWindow)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(550, 210, 251, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.username_del_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.username_del_lineEdit.setObjectName("username_del_lineEdit")
        self.gridLayout_2.addWidget(self.username_del_lineEdit, 0, 1, 1, 1)
        self.username_del_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.username_del_lbl.setObjectName("username_del_lbl")
        self.gridLayout_2.addWidget(self.username_del_lbl, 0, 0, 1, 1)
        self.password_del_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.password_del_lineEdit.setObjectName("password_del_lineEdit")
        self.gridLayout_2.addWidget(self.password_del_lineEdit, 1, 1, 1, 1)
        self.password_del_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.password_del_lbl.setObjectName("password_del_lbl")
        self.gridLayout_2.addWidget(self.password_del_lbl, 1, 0, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(SettingsWindow)
        self.delete_btn.setGeometry(QtCore.QRect(680, 300, 113, 32))
        self.delete_btn.setObjectName("delete_btn")

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Form"))
        item = self.adminInfo_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SettingsWindow", "adminUserName"))
        item = self.adminInfo_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SettingsWindow", "adminPassword"))
        self.manageAdmin_lbl.setText(_translate("SettingsWindow", "Manage Administrators"))
        self.label_2.setText(_translate("SettingsWindow", "Add Admin"))
        self.add_admin_btn.setText(_translate("SettingsWindow", "Add"))
        self.username_lbl.setText(_translate("SettingsWindow", "username: "))
        self.password_lbl.setText(_translate("SettingsWindow", "password"))
        self.label.setText(_translate("SettingsWindow", "Delete Admin"))
        self.username_del_lbl.setText(_translate("SettingsWindow", "username: "))
        self.password_del_lbl.setText(_translate("SettingsWindow", "password"))
        self.delete_btn.setText(_translate("SettingsWindow", "Delete"))
