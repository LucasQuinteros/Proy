from __future__ import division
import time


from Pycnc.pulses import *
from Pycnc.config import *
from Paginas.ClaseVentanaPrincipal import *
#from Pycnc.gmachine import GMachine
from PyQt5.QtCore import pyqtSignal
from PyQt5.Qt import QObject,QApplication,pyqtSlot

""" This is virtual device class which is very useful for debugging.
    It checks PulseGenerator with some tests.
"""
class hal1(QObject):
    Signal_msg = pyqtSignal(float,float,float)
    Sig_finish = pyqtSignal()
    
    
    def __init__(self):
        """ Initialize GPIO pins and machine itself.
        """
        super().__init__()
        logging.info("initialize hal")
        print("initialize hal")
        self.__detener = False
        self.acum = 0
    def spindle_control(self,percent):
        """ Spindle control implementation 0..100.
        :param percent: Spindle speed in percent.
        """
        logging.info("spindle control: {}%".format(percent))
        print("spindle control: {}%".format(percent))
    
    
    def disable_steppers(self):
        """ Disable all steppers until any movement occurs.
        """
        logging.info("hal disable steppers")
        print("hal disable steppers")
    
    def calibrate(self,x, y, z):
        """ Move head to home position till end stop switch will be triggered.
        Do not return till all procedures are completed.
        :param x: boolean, True to calibrate X axis.
        :param y: boolean, True to calibrate Y axis.
        :param z: boolean, True to calibrate Z axis.
        :return: boolean, True if all specified end stops were triggered.
        """
        logging.info("hal calibrate, x={}, y={}, z={}".format(x, y, z))
        print("hal calibrate, x={}, y={}, z={}".format(x, y, z))
        return True
    
    
    # noinspection PyUnusedLocal
    
    def move(self,generator):
        """ Move head to specified position.
        :param generator: PulseGenerator object.
        """
        
        delta = generator.delta()
        ix = iy = iz = ie = 0
        lx, ly, lz, le = None, None, None, None
        dx, dy, dz, de = 0, 0, 0, 0
        mx, my, mz, me = 0, 0, 0, 0
        cx, cy, cz, ce = 0, 0, 0, 0
        direction_x, direction_y, direction_z, direction_e = 1, 1, 1, 1
        st = time.time()
        direction_found = False
        pulsos = list()
        for direction, tx, ty, tz, te in generator:
            QApplication.instance().processEvents()
            px=0
            py=0
            pz=0               
            if self.__detener == False:
                if direction:
                    direction_found = True
                    direction_x, direction_y, direction_z, direction_e = tx, ty, tz, te
                    if STEPPER_INVERTED_X:
                        direction_x = -direction_x
                    if STEPPER_INVERTED_Y:
                        direction_y = -direction_y
                    if STEPPER_INVERTED_Z:
                        direction_z = -direction_z
                    if STEPPER_INVERTED_E:
                        direction_e = -direction_e
                    if isinstance(generator, PulseGeneratorLinear):
                        assert ((direction_x < 0 and delta.x < 0)
                                or (direction_x > 0 and delta.x > 0) or delta.x == 0)
                        assert ((direction_y < 0 and delta.y < 0)
                                or (direction_y > 0 and delta.y > 0) or delta.y == 0)
                        assert ((direction_z < 0 and delta.z < 0)
                                or (direction_z > 0 and delta.z > 0) or delta.z == 0)
                        assert ((direction_e < 0 and delta.e < 0)
                                or (direction_e > 0 and delta.e > 0) or delta.e == 0)
                    continue
                if tx is not None:
                    if tx > mx:
                        mx = tx
                    tx = int(round(tx * 1000000))
                    ix += direction_x
                    cx += 1
                    #self.Signal_msg.emit(direction_x,0,0)
                    px=direction_x
                    if lx is not None:
                        dx = tx - lx
                        assert dx > 0, "negative or zero time delta detected for x"
                    lx = tx
                else:
                    dx = None
                if ty is not None:
                    if ty > my:
                        my = ty
                    ty = int(round(ty * 1000000))
                    iy += direction_y
                    cy += 1
                    #self.Signal_msg.emit(0,direction_y,0)
                    py=direction_y
                    if ly is not None:
                        dy = ty - ly
                        assert dy > 0, "negative or zero time delta detected for y"
                    ly = ty
                else:
                    dy = None
                if tz is not None:
                    if tz > mz:
                        mz = tz
                    tz = int(round(tz * 1000000))
                    iz += direction_z
                    cz += 1
                    #self.Signal_msg.emit(0,0,direction_z)
                    pz=direction_z
                    if lz is not None:
                        dz = tz - lz
                        assert dz > 0, "negative or zero time delta detected for z"
                    lz = tz
                else:
                    dz = None
                if te is not None:
                    if te > me:
                        me = te
                    te = int(round(te * 1000000))
                    ie += direction_e
                    ce += 1
                    if le is not None:
                        de = te - le
                        assert de > 0, "negative or zero time delta detected for e"
                    le = te
                else:
                    de = None
                # very verbose, uncomment on demand
                # logging.debug("Iteration {} is {} {} {} {}".
                #               format(max(ix, iy, iz, ie), tx, ty, tz, te))
                f = list(x for x in (tx, ty, tz, te) if x is not None)
                pulsos.append([px,py,pz])
                
                assert f.count(f[0]) == len(f), "fast forwarded pulse detected"
        
        if self.__detener == False:        
            pt = time.time()
            assert direction_found, "direction not found"
            assert round(ix / STEPPER_PULSES_PER_MM_X, 10) == delta.x,\
                "x wrong number of pulses"
            assert round(iy / STEPPER_PULSES_PER_MM_Y, 10) == delta.y,\
                "y wrong number of pulses"
            assert round(iz / STEPPER_PULSES_PER_MM_Z, 10) == delta.z, \
                "z wrong number of pulses"
            assert round(ie / STEPPER_PULSES_PER_MM_E, 10) == delta.e, \
                "e wrong number of pulses"
            assert max(mx, my, mz, me) <= generator.total_time_s(), \
                "interpolation time or pulses wrong"
            
            for x in pulsos:
                print(x)               
                self.Signal_msg.emit(x[0],x[1],x[2])
                time.sleep(1/1000)
            #=======================================================================
            # print("Moved {}, {}, {}, {} iterations".format(ix, iy, iz, ie))
            # print("prepared in " + str(round(pt - st, 2)) + "s, estimated "
            #              + str(round(generator.total_time_s(), 2)) + "s")
            # self.Signal_msg.emit("Moved {}, {}, {}, {} iterations".format(ix, iy, iz, ie))
            # 
            #=======================================================================
            logging.debug("Moved {}, {}, {}, {} iterations".format(ix, iy, iz, ie))
            logging.info("prepared in " + str(round(pt - st, 2)) + "s, estimated "
                         + str(round(generator.total_time_s(), 2)) + "s")
            self.Sig_finish.emit()
            pulsos.clear()
        self.__detener = False
    
    
    
    def join(self):
        """ Wait till motors work.
        """
        logging.info("hal join()")
        print("hal join()")
    
    def deinit(self):
        """ De-initialise.
        """
        logging.info("hal deinit()")
        print("hal deinit()")
    
    def watchdog_feed(self):
        """ Feed hardware watchdog.
        """
        print("1")
        pass
    @pyqtSlot()
    def Detener(self):
        pass
        #self.__detener = True
