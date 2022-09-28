'''
Created on 23 ene. 2019

@author: Lucas
'''
from Pycnc.pulses import *
from Pycnc.config import *
from PyQt5.QtCore import pyqtSignal, QObject
import time

class pulses_to_move(QObject):
    '''
    classdocs
    '''
    Sig_msg_m = pyqtSignal(float,float,float)
    Sig_finish = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.generator = None
        self.doing_a_command = False
        
    def Run(self):
        
            print("Tmove started")
            x=0
            y=0
            z=0
            if self.doing_a_command is True:
                acumx = 0
                acumy = 0
                acumz = 0
                delta = self.generator.delta()
                ix = iy = iz = ie = 0
                lx, ly, lz, le = None, None, None, None
                dx, dy, dz, de = 0, 0, 0, 0
                mx, my, mz, me = 0, 0, 0, 0
                cx, cy, cz, ce = 0, 0, 0, 0
                direction_x, direction_y, direction_z, direction_e = 1, 1, 1, 1
                st = time.time()
                direction_found = False
                for direction, tx, ty, tz, te in self.generator:
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
                        if isinstance(self.generator, PulseGeneratorLinear):
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
                       
                        
                        if (cx//1)>acumx:
                            #self.Sig_msg_m.emit(direction_x)
                            x = direction_x
                            acumx += 1
                            self.Sig_msg_m.emit(x,0,0)
                        
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

                        if (cy//1)>acumy:
                            #self.Sig_msg_m.emit(direction_x)
                            y = direction_y
                            acumy += 1
                            self.Sig_msg_m.emit(0,y,0)
                        
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
                        
                        if(cz//10)>acumz:
                            z = direction_z
                            acumz += 1
                            self.Sig_msg_m.emit(0,0,z)                            
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
                    #very verbose, uncomment on demand
                    logging.debug("Iteration {} is {} {} {} {}".
                                  format(max(ix, iy, iz, ie), tx, ty, tz, te))
                    
                    x=0
                    y=0
                    z=0
                    f = list(x for x in (tx, ty, tz, te) if x is not None)
                    time.sleep(1/1000)
                    assert f.count(f[0]) == len(f), "fast forwarded pulse detected"
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
                assert max(mx, my, mz, me) <= self.generator.total_time_s(), \
                    "interpolation time or pulses wrong"
                    
                print("Moved {}, {}, {}, {} iterations".format(ix, iy, iz, ie))
                print("prepared in " + str(round(pt - st, 2)) + "s, estimated "
                             + str(round(self.generator.total_time_s(), 2)) + "s")
                #self.Signal_msg.emit("Moved {}, {}, {}, {} iterations".format(ix, iy, iz, ie))
                 
                logging.debug("Moved {}, {}, {}, {} iterations".format(ix, iy, iz, ie))
                logging.info("prepared in " + str(round(pt - st, 2)) + "s, estimated "
                             + str(round(self.generator.total_time_s(), 2)) + "s")

                self.Sig_finish.emit()
                self.doing_a_command = False
                self.generator = None
                pass
        
    def load_generator(self,gen):
        self.generator = gen
        self.doing_a_command = True
        print("Carga exitosa a Tmove")