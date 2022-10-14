from __future__ import division

import Pycnc.logging_config as logging_config
import Pycnc.hal as h
from Pycnc.pulses import *
from Pycnc.coordinates import *
from Pycnc.enums import *
from Pycnc.watchdog import *
from PyQt5.Qt import pyqtSignal, QObject,pyqtSlot
from Pycnc.move import pulses_to_move
from PyQt5.QtCore import QThread

class GMachineException(Exception):
    """ Exceptions while processing gcode line.
    """
    pass


class GMachine(QObject):
    """ Main object which control and keep state of whole machine: steppers,
        spindle, extruder etc
    """
    AUTO_FAN_ON = AUTO_FAN_ON
    Signal_msg = pyqtSignal(float,float,float)
    
    Wmove = pulses_to_move()
    Tmove = QThread()
    Signal_fin    = pyqtSignal()
    
    def __init__(self):
        """ Initialization.
        """
        super().__init__()
        self._position = Coordinates(0.0, 0.0, 0.0, 0.0)
        #init variables
        self._velocity = 0
        self._spindle_rpm = 0
        self._local = None
        self._convertCoordinates = 0
        self._absoluteCoordinates = 0
        self._plane = None
        self._fan_state = False
        self._heaters = dict()
        self.reset()
        print('Gmachine hal1')
        self.hal = h.hal()
        print('halvirtual watchdog ')
        self.watchdog = HardwareWatchdog()
        #self.hal.Signal_msg.connect(self.pos_instantanea_funcion)
        #self.Wmove.moveToThread(self.Tmove)
        #self.Wmove.Sig_msg_m.connect(self.pos_instantanea_funcion)
        #self.hal.Signal_msg.connect(self.pos_instantanea_funcion)
        #self.hal.Sig_finish.connect(self.comando_terminado)
        #self.Wmove.Sig_finish.connect(self.comando_terminado)
        #self.Tmove.started.connect(self.Wmove.Run)
        
    @pyqtSlot(float,float,float)  
    def pos_instantanea_funcion(self, posX : float, posY : float, posZ : float):
        self.Signal_msg.emit(posX,posY,posZ)

        
    @pyqtSlot()
    def comando_terminado(self):
        
        
        self.Tmove.quit()
        self.Tmove.wait()
        self.Signal_fin.emit()
        print("killed Tmove")
        
    def release(self):
        """ Free all resources.
        """
        #self.watchdog.stop()
        self.hal.deinit()
        

    def reset(self):
        """ Reinitialize all program configurable thing.
        """
        self._velocity = min(MAX_VELOCITY_MM_PER_MIN_X,
                             MAX_VELOCITY_MM_PER_MIN_Y,
                             MAX_VELOCITY_MM_PER_MIN_Z,
                             MAX_VELOCITY_MM_PER_MIN_E)
        self._spindle_rpm = 1000
        self._local = Coordinates(0, 0, 0, 0.0)
        self._convertCoordinates = 1.0
        self._absoluteCoordinates = True
        self._plane = PLANE_XY
        

    # noinspection PyMethodMayBeStatic
    
    def _spindle(self, spindle_speed):
        self.hal.join()
        self.hal.spindle_control(100.0 * spindle_speed / SPINDLE_MAX_RPM)

    def __check_delta(self, delta):
        pos = self._position + delta
        if not pos.is_in_aabb(Coordinates(0.0, 0.0, 0.0, 0.0),          #funcion en coordinates
                              Coordinates(TABLE_SIZE_X_MM, TABLE_SIZE_Y_MM,
                                          TABLE_SIZE_Z_MM, 0)):
            self.Signal_fin.emit()
            raise GMachineException("out of effective area")

    # noinspection PyMethodMayBeStatic
    def __check_velocity(self, max_velocity):
        if max_velocity.x > MAX_VELOCITY_MM_PER_MIN_X \
                or max_velocity.y > MAX_VELOCITY_MM_PER_MIN_Y \
                or max_velocity.z > MAX_VELOCITY_MM_PER_MIN_Z \
                or max_velocity.e > MAX_VELOCITY_MM_PER_MIN_E:
            raise GMachineException("out of maximum speed")

    def _move_linear(self, delta, velocity):
        
        delta = delta.round(1.0 / STEPPER_PULSES_PER_MM_X,  #round esta en coordinates Busca definir el delta en pasos enteros de motor
                            1.0 / STEPPER_PULSES_PER_MM_Y,  # 1/100 0.01
                            1.0 / STEPPER_PULSES_PER_MM_Z,  # 1/400 0.0025
                            1.0 / STEPPER_PULSES_PER_MM_E)  
        
        if delta.is_zero():
            self.Signal_fin.emit()
            return
            
        self.__check_delta(delta)
        
        logging.info("Moving linearly {}".format(delta))
        gen = PulseGeneratorLinear(delta, velocity)     # paso unidades de paso a pulsos
        self.__check_velocity(gen.max_velocity())
        self.hal.move(gen)
        #print("movestart")
        #=======================================================================
        # self.Wmove.load_generator(gen)
        # self.Tmove.start()
        #=======================================================================
        #save position
        self._position = self._position + delta         #modifico la posicion de la maquina

    @staticmethod
    def __quarter(pa, pb):
        if pa >= 0 and pb >= 0:
            return 1
        if pa < 0 and pb >= 0:
            return 2
        if pa < 0 and pb < 0:
            return 3
        if pa >= 0 and pb < 0:
            return 4

    def __adjust_circle(self, da, db, ra, rb, direction, pa, pb, ma, mb):
        r = math.sqrt(ra * ra + rb * rb) 
        if r == 0:
            raise GMachineException("circle radius is zero")
        sq = self.__quarter(-ra, -rb) #en que cuadrante de los ejes se encuentra el circulo
        if da == 0 and db == 0:  # full circle  si los delta son cero el circulo es completo
            ea = da
            eb = db
            eq = 5  # mark as non-existing to check all
        else:                   # Si el circulo no es completo
            if da - ra == 0:    
                ea = 0
            else:
                b = (db - rb) / (da - ra)
                ea = math.copysign(math.sqrt(r * r / (1.0 + abs(b))), da - ra)
                    
            eb = math.copysign(math.sqrt(r * r - ea * ea), db - rb)
            eq = self.__quarter(ea, eb)
            ea += ra
            eb += rb
        # iterate coordinates quarters and check if we fit table
        q = sq
        pq = q
        for _ in range(0, 4):
            if direction == CW:
                q -= 1
            else:
                q += 1
                
            if q <= 0:
                q = 4
            elif q >= 5:
                q = 1
            if q == eq:
                break
            is_raise = False
            if (pq == 1 and q == 4) or (pq == 4 and q == 1):
                is_raise = (pa + ra + r > ma)
            elif (pq == 1 and q == 2) or (pq == 2 and q == 1):
                is_raise = (pb + rb + r > mb)
            elif (pq == 2 and q == 3) or (pq == 3 and q == 2):
                is_raise = (pa + ra - r < 0)
            elif (pq == 3 and q == 4) or (pq == 4 and q == 3):
                is_raise = (pb + rb - r < 0)
            if is_raise:
                raise GMachineException("out of effective area")
            pq = q
        return ea, eb

    def _move_circular(self, delta, radius, velocity, direction):
        delta = delta.round(1.0 / STEPPER_PULSES_PER_MM_X,#round esta en coordinates Busca definir el delta en pasos enteros de motor
                            1.0 / STEPPER_PULSES_PER_MM_Y,
                            1.0 / STEPPER_PULSES_PER_MM_Z,
                            1.0 / STEPPER_PULSES_PER_MM_E)
        radius = radius.round(1.0 / STEPPER_PULSES_PER_MM_X,
                              1.0 / STEPPER_PULSES_PER_MM_Y,
                              1.0 / STEPPER_PULSES_PER_MM_Z,
                              1.0 / STEPPER_PULSES_PER_MM_E)
        self.__check_delta(delta)
        # get delta vector and put it on circle
        circle_end = Coordinates(0, 0, 0, 0)
        if self._plane == PLANE_XY:
            circle_end.x, circle_end.y = \
                self.__adjust_circle(delta.x, delta.y, radius.x, radius.y,
                                     direction, self._position.x,
                                     self._position.y, TABLE_SIZE_X_MM,
                                     TABLE_SIZE_Y_MM)
            circle_end.z = delta.z
        elif self._plane == PLANE_YZ:
            circle_end.y, circle_end.z = \
                self.__adjust_circle(delta.y, delta.z, radius.y, radius.z,
                                     direction, self._position.y,
                                     self._position.z, TABLE_SIZE_Y_MM,
                                     TABLE_SIZE_Z_MM)
            circle_end.x = delta.x
        elif self._plane == PLANE_ZX:
            circle_end.z, circle_end.x = \
                self.__adjust_circle(delta.z, delta.x, radius.z, radius.x,
                                     direction, self._position.z,
                                     self._position.x, TABLE_SIZE_Z_MM,
                                     TABLE_SIZE_X_MM)
            circle_end.y = delta.y
        circle_end.e = delta.e
        circle_end = circle_end.round(1.0 / STEPPER_PULSES_PER_MM_X,
                                      1.0 / STEPPER_PULSES_PER_MM_Y,
                                      1.0 / STEPPER_PULSES_PER_MM_Z,
                                      1.0 / STEPPER_PULSES_PER_MM_E)
        logging.info("Moving circularly {} {} {} with radius {}"
                     " and velocity {}".format(self._plane, circle_end,
                                               direction, radius, velocity))
        gen = PulseGeneratorCircular(circle_end, radius, self._plane,
                                     direction, velocity)
        self.__check_velocity(gen.max_velocity())
        # if finish coords is not on circle, move some distance linearly
        linear_delta = delta - circle_end
        linear_gen = None
        if not linear_delta.is_zero():
            logging.info("Moving additionally {} to finish circle command".
                         format(linear_delta))
            linear_gen = PulseGeneratorLinear(linear_delta, velocity)
            self.__check_velocity(linear_gen.max_velocity())
        # do movements
        #self.hal.move(gen)
        #=======================================================================
        # self.Wmove.load_generator(gen)
        # self.Tmove.start()
        #=======================================================================
        self.hal.move(gen)
        if linear_gen is not None:
            self.hal.move(linear_gen)
            print("Problema 1")
        # save position
        self._position = self._position + circle_end + linear_delta

    def safe_zero(self, x=True, y=True, z=True):
        """ Move head to zero position safely.
        :param x: boolean, move X axis to zero
        :param y: boolean, move Y axis to zero
        :param z: boolean, move Z axis to zero
        """
        if z:
            d = Coordinates(0, 0, -self._position.z, 0)
            self._move_linear(d, MAX_VELOCITY_MM_PER_MIN_Z)
        
        if x and not y:
            self._move_linear(Coordinates(-self._position.x, 0, 0, 0),
                              MAX_VELOCITY_MM_PER_MIN_X)

        elif y and not x:
            self._move_linear(Coordinates(0, -self._position.y, 0, 0),
                              MAX_VELOCITY_MM_PER_MIN_X)
        elif x and y:
            d = Coordinates(-self._position.x, -self._position.y, 0, 0)
            self._move_linear(d, min(MAX_VELOCITY_MM_PER_MIN_X,
                                     MAX_VELOCITY_MM_PER_MIN_Y))

    def position(self):
        """ Return current machine position (after the latest command)
            Note that hal might still be moving motors and in this case
            function will block until motors stops.
            This function for tests only.
            :return current position.
        """
        self.hal.join()
        return self._position

    def plane(self):
        """ Return current plane for circular interpolation. This function for
            tests only.
            :return current plane.
        """
        return self._plane

    def do_command(self, gcode):
        """ Perform action.
        :param gcode: GCode object which represent one gcode line
        :return String if any answer require, None otherwise.
        """
        
        if gcode is None:
            self.Signal_fin.emit()
            return None
        answer = None
        logging.debug("got command " + str(gcode.params))
        # read command
        c = gcode.command()
        
        if c is None and gcode.has_coordinates():
            c = 'G1'
        # read parameters
        if self._absoluteCoordinates:
            coord = gcode.coordinates(self._position - self._local, #gcode coordinates devuelve los params del gcode si se le envia 
                                      self._convertCoordinates)        #un objeto coordinates no le interesan los valores
            #print(self._position - self._local, self._position , self._local, coord)
            coord = coord + self._local                             #solo sirve si se usa G92
            delta = coord - self._position                          
        else:
            delta = gcode.coordinates(Coordinates(0.0, 0.0, 0.0, 0.0),  # Al ser relativas no necesita referencia de donde esta la maquina
                                      self._convertCoordinates)
            #coord = self._position + delta
        
        velocity = gcode.get('F', self._velocity)
        radius = gcode.radius(Coordinates(0.0, 0.0, 0.0, 0.0), # I, J ,K segun gcode params
                              self._convertCoordinates)
        
        # check parameters
        if velocity < MIN_VELOCITY_MM_PER_MIN:      #chequeo que la vel del gcode sea superior a la minima
            self.Signal_fin.emit()
            raise GMachineException("feed speed too low")
        
        # select command and run it
        if c == 'G0':  # rapid move
            vl = max(MAX_VELOCITY_MM_PER_MIN_X,
                     MAX_VELOCITY_MM_PER_MIN_Y,
                     MAX_VELOCITY_MM_PER_MIN_Z,
                     MAX_VELOCITY_MM_PER_MIN_E)
            l = delta.length()
            if l > 0:
                proportion = abs(delta) / l
                if proportion.x > 0:
                    v = int(MAX_VELOCITY_MM_PER_MIN_X / proportion.x)
                    if v < vl:
                        vl = v
                if proportion.y > 0:
                    v = int(MAX_VELOCITY_MM_PER_MIN_Y / proportion.y)
                    if v < vl:
                        vl = v
                if proportion.z > 0:
                    v = int(MAX_VELOCITY_MM_PER_MIN_Z / proportion.z)
                    if v < vl:
                        vl = v
                if proportion.e > 0:
                    v = int(MAX_VELOCITY_MM_PER_MIN_E / proportion.e)
                    if v < vl:
                        vl = v
            self._move_linear(delta, vl)
            
        elif c == 'G1':  # linear interpolation
            self._move_linear(delta, velocity)
            
            
        elif c == 'G2':  # circular interpolation, clockwise
            self._move_circular(delta, radius, velocity, CW)
            
            
        elif c == 'G3':  # circular interpolation, counterclockwise
            self._move_circular(delta, radius, velocity, CCW)
            
            
        elif c == 'G4':  # delay in s
            if not gcode.has('P'):
                self.Signal_fin.emit()
                raise GMachineException("P is not specified")
            pause = gcode.get('P', 0)
            if pause < 0:
                raise GMachineException("bad delay")
            self.hal.join()
            time.sleep(pause)
            self.Signal_fin.emit()
            
        elif c == 'G17':  # XY plane select
            self._plane = PLANE_XY
            self.Signal_fin.emit()
            
        elif c == 'G18':  # ZX plane select
            self._plane = PLANE_ZX
            self.Signal_fin.emit()
            
        elif c == 'G19':  # YZ plane select
            self._plane = PLANE_YZ
            self.Signal_fin.emit()
            
        elif c == 'G20':  # switch to inches
            self._convertCoordinates = 25.4
            self.Signal_fin.emit()
            
        elif c == 'G21':  # switch to mm
            self._convertCoordinates = 1.0
            self.Signal_fin.emit()
            
        elif c == 'G28':  # home
            axises = gcode.has('X'), gcode.has('Y'), gcode.has('Z')
            if axises == (False, False, False):
                axises = True, True, True
            self.safe_zero(*axises)
            self.hal.join()
            self.Signal_fin.emit()
            if not self.hal.calibrate(*axises):
                self.Signal_fin.emit()
                raise GMachineException("failed to calibrate")
            
        elif c == 'G53':  # switch to machine coords
            self._local = Coordinates(0.0, 0.0, 0.0, 0.0)
            self.Signal_fin.emit()
            
        elif c == 'G90':  # switch to absolute coords
            self._absoluteCoordinates = True
            print("coordenadas absolutas")
            self.Signal_fin.emit()
            
        elif c == 'G91':  # switch to relative coords
            self._absoluteCoordinates = False
            print("coordenadas relativas")
            self.Signal_fin.emit()
            
        elif c == 'G92':  # switch to local coords
            if gcode.has_coordinates():
                self._local = self._position - gcode.coordinates(
                    Coordinates(self._position.x - self._local.x,
                                self._position.y - self._local.y,
                                self._position.z - self._local.z,
                                self._position.e - self._local.e),
                    self._convertCoordinates)
            else:
                self._local = self._position
            self.Signal_fin.emit()
            
        elif c == 'M3':  # spindle on
            spindle_rpm = gcode.get('S', self._spindle_rpm)
            if spindle_rpm < 0 or spindle_rpm > SPINDLE_MAX_RPM:
                self.Signal_fin.emit()
                raise GMachineException("bad spindle speed")
            self._spindle(spindle_rpm)
            self._spindle_rpm = spindle_rpm
            self.Signal_fin.emit()
            
        elif c == 'M5':  # spindle off
            self._spindle(0)
            self.Signal_fin.emit()
            
        elif c == 'M2' or c == 'M30':  # program finish, reset everything.
            self.reset()
            self.Signal_fin.emit()
            
        elif c == 'M84':  # disable motors
            self.hal.disable_steppers()
            self.Signal_fin.emit()
            

            
        elif c == 'M105':  # get temperature
            try:
                et = self.hal.get_extruder_temperature()
            except (IOError, OSError):
                et = None
            try:
                bt = self.hal.get_bed_temperature()
            except (IOError, OSError):
                bt = None
            if et is None and bt is None:
                self.Signal_fin.emit()
                raise GMachineException("can not measure temperature")
            answer = "E:{} B:{}".format(et, bt)
            self.Signal_fin.emit()
            
        elif c == 'M106':  # fan control
            if gcode.get('S', 1) != 0:
                self._fan(True)
            else:
                self._fan(False)
            self.Signal_fin.emit()
            
        elif c == 'M107':  # turn off fan
            self._fan(False)
            self.Signal_fin.emit()
            
        elif c == 'M111':  # enable debug
            logging_config.debug_enable()
            self.Signal_fin.emit()
            
        elif c == 'M114':  # get current position
            self.hal.join()
            p = self.position()
            answer = "X:{} Y:{} Z:{} E:{}".format(p.x, p.y, p.z, p.e)
            print("X:{} Y:{} Z:{} E:{}".format(p.x, p.y, p.z, p.e))
            self.Signal_fin.emit()
            
        elif c is None:  # command not specified(ie just F was passed)
            self.Signal_fin.emit()
            pass
        # commands below are added just for compatibility
        elif c == 'M82':  # absolute mode for extruder
            if not self._absoluteCoordinates:
                self.Signal_fin.emit()
                raise GMachineException("Not supported, use G90/G91")
            
        elif c == 'M83':  # relative mode for extruder
            if self._absoluteCoordinates:
                self.Signal_fin.emit()
                raise GMachineException("Not supported, use G90/G91")
        else:
            self.Signal_fin.emit()
            raise GMachineException("unknown command")

        # save parameters on success
        self._velocity = velocity
        logging.debug("position {}".format(self._position))
        
        return answer

    pyqtSlot(str)
    def changeGcomands(self,msj=None):
        
        
        print("OK")
        
        
        
        
        