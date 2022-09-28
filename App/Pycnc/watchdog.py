import threading
import time

from Pycnc.hal import hal1


class HardwareWatchdog(threading.Thread):
    def __init__(self):
        """ Run feed loop for hardware watchdog.
        """
        #super(HardwareWatchdog, self).__init__()
        super(HardwareWatchdog, self).__init__()
        self.setDaemon(True)
        self.start()
        self.hal = hal1()
    def run(self):
        while True:
            #self.hal.watchdog_feed()
            #self.hal.watchdog_feed()
            time.sleep(3)

# for test purpose
if __name__ == "__main__":
    
    #hal.init()
    #hal.fan_control(True)
    print("Fan is on, it should turn off automatically in ~15 seconds."
          "\nExiting...")
