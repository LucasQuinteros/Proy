'''
Created on 14 ene. 2019

@author: revolution
'''
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.Qt import QObject, QApplication, QCoreApplication
from _socket import SHUT_RDWR
from time import sleep
import socket
import errno
import pickle
import time
class Cliente(QObject):
    Signal_Mensaje = pyqtSignal(str,int,int)
    Signal_Abortar = pyqtSignal()
    Signal_status  = pyqtSignal(str)
    rpi = None
    
    def __init__(self):
        super().__init__()
        self.Flag_abortar = False
        self.Flag_pausa = False
        self.__Archivo = False
        self.namefile = None
        self.file = list()
    
    @pyqtSlot()
    def Run(self):
        while self.Flag_abortar == False:          
            QApplication.instance().processEvents()
            if self.Flag_pausa== False:           
                try:
                    aux = self.rpi.recv(2048).decode()
                    if aux :
                        other = aux.strip()
                        print(other)
                        if other == "#FILE":
                            self.__Archivo = True
                            print("FILE")     
                        if other == "#FINFILE":
                            self.__Archivo = False
                            self.Save_file()
                             
                        if self.__Archivo == True:
                             
                            if other != "":
                                self.file.append(other)
                             
                        #self.Signal_Mensaje.emit("Friend: "+ aux,1)
                except socket.error as e:
                    pass
                    #print(str(e))
                    
        print("Cliente Terminado")
        self.rpi.close()
    
    def Save_file(self):
        #self.namefile ="Archivos\\"+ str(datetime.now())

        try:
            timestr = time.strftime("%Y%m%d-%H%M%S")
            print(self.namefile)
            f = open(timestr,"x")
            for line in self.file:
                print(line)
                line = line.strip()
                f.write(line+" \n")   
        except Exception as e:
            print(str(e))
        f.close()
        self.file.clear()
        
    @pyqtSlot(str)
    def Control(self,Orden: str):
        #print(Orden)
        if Orden == 'Detener':
            self.rpi.shutdown(SHUT_RDWR)
            #self.rpi.close()           
            self.Flag_pausa = True
            self.Flag_abortar = True
            #self.sig_msg.emit("Conexion Finalizada")
            #print("Thread Tsocket finalizado")
            
        if Orden == 'Pausa':
            self.Flag_pausa = True
            self.rpi.shutdown(SHUT_RDWR)
            self.rpi.close()
            #self.sig_msg.emit("Conexion Finalizada")
            
        if Orden == 'Start':
            self.Flag_pausa = False
            self.Flag_abortar = False
            #self.sig_msg.emit("Conexion Iniciada")
        
    @pyqtSlot(str,int)
    def Conectar_cliente(self, host, port):
        self.host = host
        self.port = port
        self.Flag_pausa = False
        self.Flag_abortar = False
        self.rpi = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.rpi.settimeout(1)
        try:
            self.rpi.connect((self.host,self.port))
        except socket.error as e:
            print(str(e))
            self.Signal_status.emit("Error al conectar revise la direccion")
            return False
        self.Signal_status.emit("Conectado a "+ host +" al puerto "+ str(self.port))
        return True
    
    @pyqtSlot(str)
    def SendMessage_to_server(self, msg1):
            self.rpi.send(msg1.encode(encoding='utf_8', errors='strict'))