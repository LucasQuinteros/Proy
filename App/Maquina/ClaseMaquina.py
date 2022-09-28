
import sys
import Pycnc.logging_config as logging_config
from Pycnc.gcode import GCode, GCodeException
from Pycnc.gmachine import GMachine, GMachineException
from PyQt5.Qt import QObject, pyqtSlot, pyqtSignal, QApplication
from Pycnc.hal_virtual import *


class Maquina(QObject):
    #se�ales:
    Signal_msg    = pyqtSignal((str,int,int),(str,int))
    Signal_status = pyqtSignal(str)
    Signal_progre = pyqtSignal()
    Signal_pos    = pyqtSignal(float,float,float)
    Sig_fin_archivo = pyqtSignal()
    Signal_abort    = pyqtSignal()
    #variables
    CNC = GMachine()
    
    line = ''
    File = None
    #inicio
    
    def __init__(self):
        super().__init__()
        self.__Startfile = False
        self.__Stopfile  = False
        self.__Pausefile = False
        self.archivo = None
        self.comando = None
        self.numberLine = 0
        self.CNC.Signal_msg.connect(self.posicion_funcion)
        self.CNC.Signal_fin.connect(self.fin_handler)
        #self.Signal_abort.connect(self.CNC.hal.Detener)
        self.x = 0
        self.y = 0
        self.z = 0

    def Start(self):
  
            if self.archivo != None:
                print(self.archivo)
                try: 
                    a = list()
                    f =  open(self.archivo, 'r')
                    for line in f:
                        line = line.strip()
                        a.append(line)
                    lenght = len(a)
                    self.numberLine = 0
                except Exception as e:
                    self.Signal_status.emit('Error al leer archivo: ' + str(e))
                    self.__Startfile = False
                    
                    pass

                while self.__Startfile:

                    while lenght > self.numberLine:    
                        QApplication.instance().processEvents() 
                        if self.__Stopfile is False:
                            if self.__Pausefile is False:
                                
                                if lenght>self.numberLine:
                                    print(a[self.numberLine])
                                    if not self.do_line(a[self.numberLine],self.numberLine):
                                        break
                                    self.Signal_progre.emit()
                                    self.Signal_msg.emit('OK ',2,self.numberLine)
                                self.numberLine += 1                    
                        elif self.__Stopfile == True:
                            self.do_line("g28",None)
                            self.Signal_msg.emit('Se detuvo el programa',2,self.numberLine)
                            self.numberLine += 1
                            break
                    print(self.numberLine)    
                    self.__Startfile = False
                    self.archivo = None
                    self.Signal_status.emit("Programa finalizado")
      
            elif self.comando != None:

                print(self.comando)
                self.do_line(self.comando,self.numberLine)
                #self.Signal_msg.emit('OK ',2,self.numberLine)
                self.numberLine = self.numberLine + 1

                self.comando = None     
                self.Signal_status.emit("Comando finalizado")
   
            print("\r\nExiting...")
                
            self.CNC.release()
            self.Sig_fin_archivo.emit()
        
    def do_line(self, line, numberLine):
        try:
            g = GCode.parse_line(line)
            res = self.CNC.do_command(g)
            print(g)
        except (GCodeException, GMachineException) as e:
            if numberLine is not None:
                self.Signal_msg.emit('ERROR ' + str(e),2, numberLine)
            print('ERROR ' + str(e))
            return False
        if res is not None:
            if numberLine is not None:
                self.Signal_msg.emit('OK ' + res,2,numberLine)
            print('OK ' + "res")
        else:
            pass
            if numberLine is not None:
                self.Signal_msg.emit('OK ',2,numberLine)
            #print('OK')
            
        return True

    def StartFile(self, File: str, Modo = str):
        print("Startfile funcion")
        
        self.__Startfile = True
        self.__Stopfile = False
        self.__Pausefile = False
        
        if Modo == "File":
            self.archivo  = File
            self.Signal_status.emit("Realizando Archivo")
        elif Modo == "Comando":
            self.Signal_status.emit("Realizando comando")
            self.comando = File
    @pyqtSlot(str)
    def Control(self, Comando: str):
        print(Comando)
        if Comando == 'Pausa':
            self.__Stopfile = True
        if Comando == 'Stop':
            self.__Stopfile = True      
        if Comando == 'Restart':
            self.__Stopfile = False
    
    @pyqtSlot(float,float,float)
    def posicion_funcion(self, posX : float, posY : float, posZ : float):
        self.x += posX
        self.y += posY
        self.z += posZ
        #print(self.x)
        self.Signal_pos.emit(self.x,self.y,self.z)
        
        #print(str(self.x) + "FUnciones")
    @pyqtSlot()
    def fin_handler(self):
        self.__Pausefile = False
        print("Termino el comando")
    
    @pyqtSlot()
    def Abortar(self):
        self.Signal_abort.emit()
        self.CNC.release()
        print("abortar");
        