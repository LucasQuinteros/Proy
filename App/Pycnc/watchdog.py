import threading
import time

import Pycnc.hal as h

class HardwareWatchdog(threading.Thread):
    def __init__(self):
        """ Run feed loop for hardware watchdog.
        """
        super(HardwareWatchdog, self).__init__()
        self.setDaemon(True)
        self.__stop = True
        self.hal = h.hal()
        self.start()
        
    def run(self):
        print('Watchdog Started')
        self.__stop = True
        while self.__stop:
            #print('\nthread Watchdog feed')
            self.hal.watchdog_feed()
            time.sleep(3)
            

            
    def stop(self):
        print('watchdog stopped')
        self.__stop = False
        

# for test purpose
if __name__ == "__main__":
    
    #hal.init()
    #hal.fan_control(True)
    print("Fan is on, it should turn off automatically in ~15 seconds."
          "\nExiting...")
