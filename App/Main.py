'''
Created on 10 ene. 2019

@author: revolution
'''
import sys
from PyQt5.QtWidgets import QApplication
from Paginas.ClaseVentanaPrincipal import Ventana

app = QApplication([])
#QApplication.instance().processEvents()
app.instance().processEvents()
Window = Ventana()

sys.exit(app.exec_())