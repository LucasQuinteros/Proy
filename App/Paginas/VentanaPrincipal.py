# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ModoTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.ModoTabWidget.setGeometry(QtCore.QRect(10, 10, 591, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModoTabWidget.sizePolicy().hasHeightForWidth())
        self.ModoTabWidget.setSizePolicy(sizePolicy)
        self.ModoTabWidget.setObjectName("ModoTabWidget")
        self.ModoArchivo = QtWidgets.QWidget()
        self.ModoArchivo.setObjectName("ModoArchivo")
        self.widget = QtWidgets.QWidget(self.ModoArchivo)
        self.widget.setGeometry(QtCore.QRect(0, 0, 581, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LabelArchivo = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelArchivo.sizePolicy().hasHeightForWidth())
        self.LabelArchivo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelArchivo.setFont(font)
        self.LabelArchivo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LabelArchivo.setObjectName("LabelArchivo")
        self.horizontalLayout_2.addWidget(self.LabelArchivo)
        self.ArchivoTextLine = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArchivoTextLine.sizePolicy().hasHeightForWidth())
        self.ArchivoTextLine.setSizePolicy(sizePolicy)
        self.ArchivoTextLine.setObjectName("ArchivoTextLine")
        self.horizontalLayout_2.addWidget(self.ArchivoTextLine)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LabelProgreso = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelProgreso.setFont(font)
        self.LabelProgreso.setObjectName("LabelProgreso")
        self.horizontalLayout.addWidget(self.LabelProgreso)
        self.ArchivoProgressBar = QtWidgets.QProgressBar(self.widget)
        self.ArchivoProgressBar.setProperty("value", 24)
        self.ArchivoProgressBar.setObjectName("ArchivoProgressBar")
        self.horizontalLayout.addWidget(self.ArchivoProgressBar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ControlGroupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ControlGroupBox.sizePolicy().hasHeightForWidth())
        self.ControlGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ControlGroupBox.setFont(font)
        self.ControlGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ControlGroupBox.setFlat(False)
        self.ControlGroupBox.setObjectName("ControlGroupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.ControlGroupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 551, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.StartBoton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartBoton.sizePolicy().hasHeightForWidth())
        self.StartBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StartBoton.setFont(font)
        self.StartBoton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StartBoton.setAutoFillBackground(False)
        self.StartBoton.setObjectName("StartBoton")
        self.horizontalLayout_3.addWidget(self.StartBoton)
        self.PauseBoton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PauseBoton.sizePolicy().hasHeightForWidth())
        self.PauseBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.PauseBoton.setFont(font)
        self.PauseBoton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PauseBoton.setAutoFillBackground(False)
        self.PauseBoton.setObjectName("PauseBoton")
        self.horizontalLayout_3.addWidget(self.PauseBoton)
        self.StopBoton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopBoton.sizePolicy().hasHeightForWidth())
        self.StopBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.StopBoton.setFont(font)
        self.StopBoton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StopBoton.setAutoFillBackground(False)
        self.StopBoton.setObjectName("StopBoton")
        self.horizontalLayout_3.addWidget(self.StopBoton)
        self.ResetBoton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetBoton.sizePolicy().hasHeightForWidth())
        self.ResetBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ResetBoton.setFont(font)
        self.ResetBoton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ResetBoton.setAutoFillBackground(False)
        self.ResetBoton.setObjectName("ResetBoton")
        self.horizontalLayout_3.addWidget(self.ResetBoton)
        self.verticalLayout.addWidget(self.ControlGroupBox)
        self.ModoTabWidget.addTab(self.ModoArchivo, "")
        self.ModoComando = QtWidgets.QWidget()
        self.ModoComando.setObjectName("ModoComando")
        self.layoutWidget = QtWidgets.QWidget(self.ModoComando)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 569, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.HacerBoton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HacerBoton.sizePolicy().hasHeightForWidth())
        self.HacerBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.HacerBoton.setFont(font)
        self.HacerBoton.setObjectName("HacerBoton")
        self.horizontalLayout_4.addWidget(self.HacerBoton)
        self.ComandoTextLine = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComandoTextLine.sizePolicy().hasHeightForWidth())
        self.ComandoTextLine.setSizePolicy(sizePolicy)
        self.ComandoTextLine.setObjectName("ComandoTextLine")
        self.horizontalLayout_4.addWidget(self.ComandoTextLine)
        self.ModoTabWidget.addTab(self.ModoComando, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 300, 591, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ConsolaTableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.ConsolaTableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ConsolaTableWidget.setAlternatingRowColors(True)
        self.ConsolaTableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.ConsolaTableWidget.setShowGrid(True)
        self.ConsolaTableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.ConsolaTableWidget.setColumnCount(3)
        self.ConsolaTableWidget.setObjectName("ConsolaTableWidget")
        self.ConsolaTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ConsolaTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        #self.ConsolaTableWidget.setColumnWidth(sel,1,500)
        self.ConsolaTableWidget.setHorizontalHeaderItem(1, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.ConsolaTableWidget.setHorizontalHeaderItem(2, item)
        self.ConsolaTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.ConsolaTableWidget.verticalHeader().setMinimumSectionSize(23)
        self.ConsolaTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.ConsolaTableWidget.setColumnWidth(1,300)

        
        
        self.verticalLayout_2.addWidget(self.ConsolaTableWidget)
        self.ConexionPCGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ConexionPCGroupBox.setGeometry(QtCore.QRect(10, 210, 591, 91))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ConexionPCGroupBox.setFont(font)
        self.ConexionPCGroupBox.setObjectName("ConexionPCGroupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ConexionPCGroupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 571, 60))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.IPtextline = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.IPtextline.setObjectName("IPtextline")
        self.gridLayout_2.addWidget(self.IPtextline, 0, 1, 1, 1)
        self.LabelPORT = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelPORT.setFont(font)
        self.LabelPORT.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelPORT.setObjectName("LabelPORT")
        self.gridLayout_2.addWidget(self.LabelPORT, 1, 0, 1, 1)
        self.PORTtextline = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.PORTtextline.setObjectName("PORTtextline")
        self.gridLayout_2.addWidget(self.PORTtextline, 1, 1, 1, 1)
        self.LabelIP = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.LabelIP.setFont(font)
        self.LabelIP.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelIP.setObjectName("LabelIP")
        self.gridLayout_2.addWidget(self.LabelIP, 0, 0, 1, 1)
        self.ConectarBoton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ConectarBoton.setFont(font)
        self.ConectarBoton.setObjectName("ConectarBoton")
        self.gridLayout_2.addWidget(self.ConectarBoton, 0, 2, 1, 1)
        self.DesconectarBoton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DesconectarBoton.setFont(font)
        self.DesconectarBoton.setObjectName("DesconectarBoton")
        self.gridLayout_2.addWidget(self.DesconectarBoton, 1, 2, 1, 1)
        self.PosicionGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.PosicionGroupBox.setGeometry(QtCore.QRect(610, 10, 341, 291))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PosicionGroupBox.setFont(font)
        self.PosicionGroupBox.setObjectName("PosicionGroupBox")
        self.widget1 = QtWidgets.QWidget(self.PosicionGroupBox)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 311, 131))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(6, 0, 6, 0)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.LabelX = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelX.sizePolicy().hasHeightForWidth())
        self.LabelX.setSizePolicy(sizePolicy)
        self.LabelX.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.LabelX.setFont(font)
        self.LabelX.setObjectName("LabelX")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.LabelX)
        self.XlcdNumber = QtWidgets.QLCDNumber(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.XlcdNumber.sizePolicy().hasHeightForWidth())
        self.XlcdNumber.setSizePolicy(sizePolicy)
        self.XlcdNumber.setSizeIncrement(QtCore.QSize(0, 0))
        self.XlcdNumber.setObjectName("XlcdNumber")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.XlcdNumber)
        self.LabelY = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelY.sizePolicy().hasHeightForWidth())
        self.LabelY.setSizePolicy(sizePolicy)
        self.LabelY.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.LabelY.setFont(font)
        self.LabelY.setObjectName("LabelY")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.LabelY)
        self.YlcdNumber = QtWidgets.QLCDNumber(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YlcdNumber.sizePolicy().hasHeightForWidth())
        self.YlcdNumber.setSizePolicy(sizePolicy)
        self.YlcdNumber.setSizeIncrement(QtCore.QSize(0, 0))
        self.YlcdNumber.setObjectName("YlcdNumber")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.YlcdNumber)
        self.LabelZ = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelZ.sizePolicy().hasHeightForWidth())
        self.LabelZ.setSizePolicy(sizePolicy)
        self.LabelZ.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.LabelZ.setFont(font)
        self.LabelZ.setObjectName("LabelZ")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.LabelZ)
        self.ZlcdNumber = QtWidgets.QLCDNumber(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZlcdNumber.sizePolicy().hasHeightForWidth())
        self.ZlcdNumber.setSizePolicy(sizePolicy)
        self.ZlcdNumber.setSizeIncrement(QtCore.QSize(0, 0))
        self.ZlcdNumber.setObjectName("ZlcdNumber")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ZlcdNumber)
        self.widget2 = QtWidgets.QWidget(self.PosicionGroupBox)
        self.widget2.setGeometry(QtCore.QRect(10, 160, 311, 121))
        self.widget2.setObjectName("widget2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(6, 0, 6, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.AvanzarYBoton = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AvanzarYBoton.sizePolicy().hasHeightForWidth())
        self.AvanzarYBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AvanzarYBoton.setFont(font)
        self.AvanzarYBoton.setObjectName("AvanzarYBoton")
        self.gridLayout.addWidget(self.AvanzarYBoton, 0, 1, 1, 1)
        self.RetrocederYBoton = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RetrocederYBoton.sizePolicy().hasHeightForWidth())
        self.RetrocederYBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RetrocederYBoton.setFont(font)
        self.RetrocederYBoton.setObjectName("RetrocederYBoton")
        self.gridLayout.addWidget(self.RetrocederYBoton, 2, 1, 1, 1)
        self.AvanzarXBoton = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AvanzarXBoton.sizePolicy().hasHeightForWidth())
        self.AvanzarXBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AvanzarXBoton.setFont(font)
        self.AvanzarXBoton.setObjectName("AvanzarXBoton")
        self.gridLayout.addWidget(self.AvanzarXBoton, 1, 2, 1, 1)
        self.RetrocederXBoton = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RetrocederXBoton.sizePolicy().hasHeightForWidth())
        self.RetrocederXBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RetrocederXBoton.setFont(font)
        self.RetrocederXBoton.setObjectName("RetrocederXBoton")
        self.gridLayout.addWidget(self.RetrocederXBoton, 1, 0, 1, 1)
        self.RetrocederZBoton = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RetrocederZBoton.sizePolicy().hasHeightForWidth())
        self.RetrocederZBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.RetrocederZBoton.setFont(font)
        self.RetrocederZBoton.setObjectName("RetrocederZBoton")
        self.gridLayout.addWidget(self.RetrocederZBoton, 2, 3, 1, 1)
        self.AvanzarZBoton = QtWidgets.QPushButton(self.widget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AvanzarZBoton.sizePolicy().hasHeightForWidth())
        self.AvanzarZBoton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.AvanzarZBoton.setFont(font)
        self.AvanzarZBoton.setObjectName("AvanzarZBoton")
        self.gridLayout.addWidget(self.AvanzarZBoton, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        #=======================================================================
        # self.menuPC = QtWidgets.QMenu(self.menubar)
        # self.menuPC.setObjectName("menuPC")
        #=======================================================================
        
        #=======================================================================
        # self.menuHelp = QtWidgets.QMenu(self.menubar)
        # self.menuHelp.setObjectName("menuHelp")
        #=======================================================================
        
        self.menuConfiguraciones = QtWidgets.QMenu(self.menubar)        
        self.menuConfiguraciones.setObjectName("menuConfiguraciones")
        
        MainWindow.setMenuBar(self.menubar)                
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionAbrirhardware = QtWidgets.QAction(MainWindow)
        self.actionAbrirhardware.setObjectName("actionAbrir_Configuraciones")
        
        self.actionAbrirComandosG = QtWidgets.QAction(MainWindow)
        self.actionAbrirComandosG.setObjectName("actionAbrir_Comandos_G")
        
        #=======================================================================
        # self.actionAbrirComandosM = QtWidgets.QAction(MainWindow)
        # self.actionAbrirComandosM.setObjectName("actionAbrir_Comandos_M")
        #=======================================================================

        self.actionAbrir_archivo_local = QtWidgets.QAction(MainWindow)
        self.actionAbrir_archivo_local.setObjectName("actionAbrir_archivo_local")
        
        #=======================================================================
        # self.actionAbrir_archivo_en_red = QtWidgets.QAction(MainWindow)
        # self.actionAbrir_archivo_en_red.setObjectName("actionAbrir_archivo_en_red")
        #=======================================================================
        
        #=======================================================================
        # self.actionModificar_archivo = QtWidgets.QAction(MainWindow)
        # self.actionModificar_archivo.setObjectName("actionModificar_archivo")
        #=======================================================================
        
        #=======================================================================
        # self.actionEnviar_archivo_actual = QtWidgets.QAction(MainWindow)
        # self.actionEnviar_archivo_actual.setObjectName("actionEnviar_archivo_actual")
        #=======================================================================
        
        
        self.menuFile.addAction(self.actionAbrir_archivo_local)
        #self.menuFile.addAction(self.actionAbrir_archivo_en_red)
        #self.menuFile.addAction(self.actionModificar_archivo)
        #self.menuPC.addAction(self.actionEnviar_archivo_actual)
        self.menuConfiguraciones.addAction(self.actionAbrirhardware)
        self.menuConfiguraciones.addAction(self.actionAbrirComandosG)
        #self.menuConfiguraciones.addAction(self.actionAbrirComandosM)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuConfiguraciones.menuAction())
        #self.menubar.addAction(self.menuPC.menuAction())
        #self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.ModoTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CNC"))
        self.LabelArchivo.setText(_translate("MainWindow", "Archivo:"))
        self.LabelProgreso.setText(_translate("MainWindow", "Progreso del programa:"))
        self.ControlGroupBox.setTitle(_translate("MainWindow", "Control:"))
        self.StartBoton.setText(_translate("MainWindow", "Start"))
        self.PauseBoton.setText(_translate("MainWindow", "Pause"))
        self.StopBoton.setText(_translate("MainWindow", "Stop"))
        self.ResetBoton.setText(_translate("MainWindow", "Resume"))
        self.ModoTabWidget.setTabText(self.ModoTabWidget.indexOf(self.ModoArchivo), _translate("MainWindow", "Modo Archivo:"))
        self.HacerBoton.setText(_translate("MainWindow", "Hacer"))
        self.ModoTabWidget.setTabText(self.ModoTabWidget.indexOf(self.ModoComando), _translate("MainWindow", "Modo Comando:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Consola:"))
        self.ConsolaTableWidget.setSortingEnabled(False)
        item = self.ConsolaTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Linea"))
        item = self.ConsolaTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Comando"))
        item = self.ConsolaTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Realizado"))
        self.ConexionPCGroupBox.setTitle(_translate("MainWindow", "Conexion con la PC:"))
        self.LabelPORT.setText(_translate("MainWindow", "PORT:"))
        self.LabelIP.setText(_translate("MainWindow", "IP:"))
        self.ConectarBoton.setText(_translate("MainWindow", "Conectar"))
        self.DesconectarBoton.setText(_translate("MainWindow", "Desconectar"))
        self.PosicionGroupBox.setTitle(_translate("MainWindow", "Posicion:"))
        self.LabelX.setText(_translate("MainWindow", "X :"))
        self.LabelY.setText(_translate("MainWindow", "Y :"))
        self.LabelZ.setText(_translate("MainWindow", "Z :"))
        self.AvanzarYBoton.setText(_translate("MainWindow", "+Y"))
        self.RetrocederYBoton.setText(_translate("MainWindow", "-Y"))
        self.AvanzarXBoton.setText(_translate("MainWindow", "+X"))
        self.RetrocederXBoton.setText(_translate("MainWindow", "-X"))
        self.RetrocederZBoton.setText(_translate("MainWindow", "-Z"))
        self.AvanzarZBoton.setText(_translate("MainWindow", "+Z"))
        self.menuFile.setTitle(_translate("MainWindow", "Archivo"))
        #self.menuPC.setTitle(_translate("MainWindow", "PC"))
        #self.menuHelp.setTitle(_translate("MainWindow", "Ayuda"))
        self.menuConfiguraciones.setTitle(_translate("MainWindow", "Maquina"))
        self.actionAbrir_archivo_local.setText(_translate("MainWindow", "Abrir archivo local"))
        #self.actionAbrir_archivo_en_red.setText(_translate("MainWindow", "Abrir archivo en red"))
        #self.actionModificar_archivo.setText(_translate("MainWindow", "Modificar archivo"))
        #self.actionEnviar_archivo_actual.setText(_translate("MainWindow", "Enviar archivo actual"))
        self.actionAbrirhardware.setText("Abrir propiedades")
        self.actionAbrirComandosG.setText("Abrir comandos G")
        #self.actionAbrirComandosM.setText("Abrir comandos M")


#===============================================================================
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
#===============================================================================