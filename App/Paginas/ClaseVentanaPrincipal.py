import socket
import os


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread,pyqtSignal,pyqtSlot
from PyQt5.Qt import QMessageBox

from Paginas.VentanaConfiguraciones import Ui_Dialog
from Paginas.VentanaPrincipal import Ui_MainWindow

#import Pycnc
#from Pycnc.config import TABLE_SIZE_X_MM
#from Pycnc.hal_virtual import Signal

from Comunicacion.ClaseCliente import Cliente
from Maquina.ClaseMaquina import Maquina



class Ventana(QtWidgets.QMainWindow, Ui_MainWindow ):

        WCliente = Cliente()
        TCliente = QThread()
        
        WMaquina = Maquina()
        TMaquina = QThread()
        
        Signal = pyqtSignal(str)
        Sig_Control = pyqtSignal(str)
        Signal_conectar      = pyqtSignal(str,int)
        Signal_enviarmensaje = pyqtSignal(str)
        #Sig_archivo          = pyqtSignal(str)
        Sig_arch_flujo       = pyqtSignal(str)
        Sig_do_line          = pyqtSignal(str)
        Sig_abortar          = pyqtSignal()
        Sig_Gcom             = pyqtSignal(str)
        step = float
        progress = float
        
        acumx = 0
        acumy = 0
        acumz = 0
        
        def __init__(self):
            super().__init__()
                
            self.setupUi(self)

            
            #===================================================================
            # f = open("C:\\Users\Lucas\git\ProyectoFinal\Pycnc\config.py", "r")
            # print(f.read())
            #===================================================================
            self.InitWorkerThreadCliente()
            
            self.InitWorkerThreadMaquina()
                        
            self.InitGUI()

            #self.TMaquina.start()
            
            self.show()
        
        def InitGUI(self):
            
            ###            CONEXION DE SE�ALES            ####
           
            #self.Sig_archivo.connect(self.WMaquina.StartFile)
            self.Signal_enviarmensaje.connect(self.WCliente.SendMessage_to_server)

            
            ####            CONEXION DE BOTONES            ####
            self.ConectarBoton.clicked.connect(self.Boton_conectar_funcion)
            self.DesconectarBoton.clicked.connect(self.Boton_desconectar_funcion)
            self.StartBoton.clicked.connect(self.Boton_start_archivo_funcion)
            self.PauseBoton.clicked.connect(self.Boton_pausa_archivo_funcion)
            self.ResetBoton.clicked.connect(self.Boton_restart_archivo_funcion)
            self.StopBoton.clicked.connect(self.Boton_stop_archivo_funcion)
            self.HacerBoton.clicked.connect(self.Boton_hacer_funcion)
            
            ###        BORRAR LUEGO        ###
            self.IPtextline.setText(socket.gethostbyname(socket.gethostname()))
            self.PORTtextline.setText('1234')
            self.statusbar.showMessage("Bienvenido")
            
            ###        ACCIONES            ###
            self.actionAbrir_archivo_local.triggered.connect(self.openFileNameDialog)
            self.actionAbrirhardware.triggered.connect(self.Configuraciones_handler)
            #self.actionEnviar_archivo_actual.triggered.connect(self.Enviar_archivo_actual_handler)
            self.actionAbrirComandosG.triggered.connect(self.CodigosG_handler)
            
            ###        CONFIGURACIONES    ###

 
            ###        ESTADO INICIALES DE BOTONES         ####
            self.DesconectarBoton.setEnabled(False)
            self.StartBoton.setEnabled(False)
            self.PauseBoton.setEnabled(False)
            self.StopBoton.setEnabled(False)
            self.ResetBoton.setEnabled(False)
            #self.actionEnviar_archivo_actual.setEnabled(False)
            #self.actionAbrir_archivo_en_red.setEnabled(False)
            
            self.ArchivoProgressBar.setValue(0)
         
        def InitWorkerThreadCliente(self):
            
            self.WCliente.moveToThread(self.TCliente)
            
            self.WCliente.Signal_Mensaje.connect(self.Write_console)
            self.WCliente.Signal_status.connect(self.Write_status)
            self.Sig_Control.connect(self.WCliente.Control)
            
            self.TCliente.started.connect(self.WCliente.Run)

        def InitWorkerThreadMaquina(self):
            
            self.WMaquina.moveToThread(self.TMaquina)
            
            self.WMaquina.Signal_msg.connect(self.Write_console)
            self.WMaquina.Signal_status.connect(self.Write_status)
            self.WMaquina.Signal_progre.connect(self.Progress_bar)
            self.WMaquina.Signal_pos.connect(self.show_lcd_funcion)
            self.WMaquina.Sig_fin_archivo.connect(self.finWmaquina)
            self.WMaquina.gmachine.hal.Signal_msg.connect(self.show_lcd_funcion)
            
            self.Sig_abortar.connect(self.WMaquina.Abortar)
            self.Sig_Gcom.connect(self.WMaquina.gmachine.changeGcomands)
            self.Sig_arch_flujo.connect(self.WMaquina.Control)
            self.Sig_do_line.connect(self.WMaquina.do_line)
            
            self.TMaquina.started.connect(self.WMaquina.Start)
            
            
        @pyqtSlot(float,float,float)
        def show_lcd_funcion(self,posX: float,posY: float,posZ: float):
            self.acumx += posX
            self.acumy += posY
            self.acumz += posZ
            self.XlcdNumber.display(self.acumx//100)
            self.YlcdNumber.display(self.acumy//100)
            self.ZlcdNumber.display(self.acumz//400)
            
        @pyqtSlot(str,int)
        @pyqtSlot(str,int,int)
        def Write_console(self, mensaje: str, Columna: int, numRows : int = None):
            # Create a empty row at bottom of table
            #numRows = self.tableWidget.rowCount()
            
            if numRows == None:
                numRows = self.ConsolaTableWidget.rowCount()
                self.ConsolaTableWidget.insertRow(numRows)
            # Add text to the row
                self.ConsolaTableWidget.setItem(numRows,Columna, QtWidgets.QTableWidgetItem(mensaje))
            else:
                self.ConsolaTableWidget.setItem(numRows,Columna, QtWidgets.QTableWidgetItem(mensaje))
            
            #self.ConsolaTableWidget.scrollToBottom()
            self.ConsolaTableWidget.resizeColumnsToContents()
            #self.ConsolaTableWidget.resizeRowsToContents()
           
        def Erase_consola(self):
            self.ConsolaTableWidget.setRowCount(0)
        
        @pyqtSlot(str)
        def Write_status(self, Estado = str):
            self.statusbar.showMessage(Estado)                
        
        @pyqtSlot()
        def Progress_bar(self):
            self.progress += self.step
            if self.progress > 99.8: self.progress = 100
            self.ArchivoProgressBar.setValue(int(self.progress))
            if self.TCliente.isRunning() is True:
                msg = str(round(self.progress))+"%" +"\n"           
                self.Signal_enviarmensaje.emit(msg)
               
        def items_clear(self):
            for row in self.ConsolaTableWidget.rowCount():
                self.ConsolaTableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(""))        
            '''
            while (self.ConsolaTableWidget.rowCount() > 0):
                   self.ConsolaTableWidget.removeRow(0)
            '''

        def Boton_start_archivo_funcion(self):
            self.progress = 0
            
            self.WMaquina.StartFile(self.ArchivoTextLine.text(),"File")
            #self.Sig_archivo.emit(self.ArchivoTextLine.text()) 
            self.TMaquina.start()
            self.StartBoton.setEnabled(False)
            self.PauseBoton.setEnabled(True)
            self.StopBoton.setEnabled(True)
            self.ResetBoton.setEnabled(False)
            
        def Boton_pausa_archivo_funcion(self):
            self.Sig_arch_flujo.emit("Pausa")
            self.Write_status("Programa en pausa")
            self.StartBoton.setEnabled(False)
            self.PauseBoton.setEnabled(False)
            self.StopBoton.setEnabled(True)
            self.ResetBoton.setEnabled(True)
            
        def Boton_restart_archivo_funcion(self):
            self.Sig_arch_flujo.emit("Restart")
            self.Write_status("Resumiendo programa")
            self.StartBoton.setEnabled(False)
            self.PauseBoton.setEnabled(True)
            self.StopBoton.setEnabled(True)
            self.ResetBoton.setEnabled(False)
            
        def Boton_stop_archivo_funcion(self):
            self.Sig_arch_flujo.emit("Stop")
            self.Write_status("Programa detenido")
            #self.items_clear()
            self.StartBoton.setEnabled(True)
            self.PauseBoton.setEnabled(False)
            self.StopBoton.setEnabled(False)
            self.ResetBoton.setEnabled(False)
            self.Sig_abortar.emit()
            
        def Boton_hacer_funcion(self):
            
            #self.Sig_do_line.emit(self.ComandoTextLine.text(),1)
            
            if self.ComandoTextLine.text() != "":
                self.WMaquina.StartFile(self.ComandoTextLine.text(),"Comando")
                self.TMaquina.start()
                
                self.Write_console(self.ComandoTextLine.text(), 1)
                
        def Boton_desconectar_funcion(self):
            try:

                self.Sig_Control.emit("Detener")
                self.TCliente.quit()
                self.TCliente.wait()
                self.ConectarBoton.setEnabled(True)
                self.DesconectarBoton.setEnabled(False)

            except Exception as e:
                print(str(e))
                pass
            finally:
                self.statusbar.showMessage("Desconectado")
                self.actionEnviar_archivo_actual.setEnabled(False)
        
                    
        def Boton_conectar_funcion(self):
            host = self.IPtextline.text()
            port = int(self.PORTtextline.text())    
            if self.WCliente.Conectar_cliente(host,port) is True:
                self.TCliente.start()
                #self.statusbar.showMessage("Conectado a "+ host +" al puerto "+ self.PORTtextline.text())
                self.Sig_Control.emit("Start")
                #self.Write_console("prueba",1)
                self.ConectarBoton.setEnabled(False)
                self.DesconectarBoton.setEnabled(True)
                #self.actionEnviar_archivo_actual.setEnabled(True)
        
        def openFileNameDialog(self):
            options = QFileDialog.Options()
            #options |= QFileDialog.DontUseNativeDialog
            try:
                fileName, _ = QFileDialog.getOpenFileName(self,"Buscar Archivo", 'App\\Ejemplos gcode' ,"All Files (*);;Text Files (.txt);", options=options)
                if fileName:
                    self.ArchivoTextLine.setText(fileName)
                    self.StartBoton.setEnabled(True)
                    self.Erase_consola()
                    count = 0
                    with open(fileName, 'r') as f:
                        for line in f:     
                            line = line.strip()
                            self.Write_console(line, 1)
                            count += 1
                            #print(count)
                    self.step = 100/count
                    self.progress = 0
                    self.ArchivoProgressBar.setValue(0)
         
            except Exception as e:
                return 'Error'+str(e)        
            
        def closeEvent(self, event):
            print('close event')
            if self.TMaquina.isRunning() is True:
                print('Stopped TMaquina')
                self.WMaquina.gmachine.release()
                self.TMaquina.quit()
                self.TMaquina.wait()                

            if self.TCliente.isRunning() is True:
                #close = QMessageBox(self)
                close = QMessageBox.question(self, 'Aun hay conexiones pendientes       ', "Deseas salir?", QMessageBox.Yes | QMessageBox.No)
                
                if close == QMessageBox.Yes:
                    self.Sig_Control.emit("Detener")

                    self.TCliente.quit()
                    self.TCliente.wait(1000)
                    event.accept()
                if close == QMessageBox.No:
                    event.ignore()
            
            event.accept()    
            
        def finWmaquina(self):
                self.TMaquina.quit()
                self.TMaquina.wait()

                self.StartBoton.setEnabled(True)
                self.PauseBoton.setEnabled(False)
                self.StopBoton.setEnabled(False)
                self.ResetBoton.setEnabled(False)                    
                    
        def Save_handler(self):
            with open("Pycnc\\config.py","w") as f:
                numRows = self.ui.tableWidget.rowCount()
                count = 0
                while numRows > count:
                    f.write(self.ui.tableWidget.item(count,0).text() + " = " + self.ui.tableWidget.item(count,1).text()+ " \n")
                    count += 1

        def Enviar_archivo_actual_handler(self):
            
            if self.ArchivoTextLine.text() != "":
                with open(self.ArchivoTextLine.text(),"r") as f:
                    for line in f:
                        line = line.strip()
                        self.Signal_enviarmensaje.emit(line + "\n")

        def Configuraciones_handler(self):
            self.hardware = QtWidgets.QDialog()
            self.ui = Ui_Dialog()            
            self.ui.setupUi(self.hardware)
            self.hardware.setWindowTitle("Propiedades del hardware")            
            self.ui.Cfgsavebutton.accepted.connect(self.Save_handler)            
            numRows = 0
            Columna = 0
            
            try:
                f = open("Pycnc\\config.py","r")
                with f:
                    for line in f:
                            aux = line.strip()                       
                            if len(aux) != 0:
                                if aux[0] != "#":
                                    b = aux.split("=")
                                    self.ui.tableWidget.insertRow(numRows)
                                    self.ui.tableWidget.setItem(numRows,0, QtWidgets.QTableWidgetItem(b[0]))
                                    self.ui.tableWidget.setItem(numRows,1, QtWidgets.QTableWidgetItem(b[1]))
                                    numRows += 1                                
            except Exception as e:
                self.ui.tableWidget.insertRow(numRows)
                self.ui.tableWidget.setItem(numRows,0, QtWidgets.QTableWidgetItem(str(e)))               
            
            self.hardware.show()
                                        
        def CodigosG_handler(self):
            numRows = 0
            self.softwareG = QtWidgets.QDialog()
            self.ui2 = Ui_Dialog()
            self.ui2.setupUi(self.softwareG)
            self.softwareG.setWindowTitle("Propiedades G")
            self.ui2.Cfgsavebutton.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
            
            self.ui2.tableWidget.insertRow(numRows)
            self.ui2.tableWidget.setItem(numRows,0,QtWidgets.QTableWidgetItem("Magnitud"))
            if self.WMaquina.gmachine._convertCoordinates == 1.0:
                self.ui2.tableWidget.setItem(numRows,1,QtWidgets.QTableWidgetItem("mm"))
            else:
                self.ui2.tableWidget.setItem(numRows,1,QtWidgets.QTableWidgetItem("inches"))
            numRows += 1
            
            self.ui2.tableWidget.insertRow(numRows)
            self.ui2.tableWidget.setItem(numRows,0,QtWidgets.QTableWidgetItem("Plano"))
            self.ui2.tableWidget.setItem(numRows,1,QtWidgets.QTableWidgetItem(str(self.WMaquina.gmachine._plane)))
            
            numRows += 1
            
            self.ui2.tableWidget.insertRow(numRows)
            self.ui2.tableWidget.setItem(numRows,0,QtWidgets.QTableWidgetItem("Coordenadas"))
            if self.WMaquina.gmachine._absoluteCoordinates == True:
                self.ui2.tableWidget.setItem(numRows,1,QtWidgets.QTableWidgetItem("Absolutas"))
            else:
                self.ui2.tableWidget.setItem(numRows,1,QtWidgets.QTableWidgetItem("Relativas"))
            
            
            self.softwareG.show()
        
              
           
           
           
           
           
           
           
           