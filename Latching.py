# Latching.py Version 0.0.1 - 19 juillet 2023
#  Robert Lagace. Univ. Laval
#
# Oération de latching valves Clippard E3L10-7W012
# durée de la pulse 10 ms

from Bulleur_def import def_latching_ponceau
import time
from machine import Pin

class Latching :
    ''' '''
    
    def __init__(self, desc) :
        " "
        self.pin_ON = Pin(desc['pin_ON'], Pin.OUT)
        self.pin_OFF = Pin(desc['pin_OFF'], Pin.OUT)
        
        # Par défaut, la valve est fermée
        self.close()
        
    def open(self) :
        "ouvre la valve"
        
        self.pin_OFF.value(0)
        self.pin_ON.value(1)
        time.sleep(0.01)#wait 10 ms
        self.pin_ON.value(0)
        pass
    
    def close(self) :
        "ferme la valve"
        
        self.pin_ON.value(0)
        self.pin_OFF.value(1)
        time.sleep(0.01)#wait 10 ms
        self.pin_OFF.value(0)
        
        pass
        
time.sleep(3)
a = Latching(def_latching_ponceau)
a.open()
time.sleep(3)
a.close()

        
