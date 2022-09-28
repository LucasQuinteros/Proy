# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Configuraciones.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 376)
        self.Cfgsavebutton = QtWidgets.QDialogButtonBox(Dialog)
        self.Cfgsavebutton.setGeometry(QtCore.QRect(10, 330, 411, 32))
        self.Cfgsavebutton.setOrientation(QtCore.Qt.Horizontal)
        self.Cfgsavebutton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.Cfgsavebutton.setObjectName("Cfgsavebutton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 411, 311))
        self.tableWidget.setMinimumSize(QtCore.QSize(411, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(411, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(204)

        self.retranslateUi(Dialog)
        self.Cfgsavebutton.accepted.connect(Dialog.accept)
        self.Cfgsavebutton.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Propiedad"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Valor"))
        

