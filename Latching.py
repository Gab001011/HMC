# Latching.py Version 0.0.1 - 19 juillet 2023
#  Robert Lagace. Univ. Laval
#
# Oération de latching valves Clippard E3L10-7W012
# durée de la pulse 10 ms

class Latching :
    ''' '''
    
    def __init__(self, desc) :
        " "
        
        self.pin_ON = desc['pin_ON']
        self.pin_OFF = desc['pin_OFF']
        
        # defaut fermé
        
        self.close()
        
    def open(self) :
        "ouvre la valve"
        
        self.pin_OFF.value(0)
        self.pin_ON.value(1)
        #wait 10 ms
        self.pin_ON.value(0)
        pass
    
    def close(self) :
        "ferme la valve"
        
        self.pin_ON.value(0)
        self.pin_OFF.value(1)
        #wait 10 ms
        self.pin_OFF.value(0)
        
        pass
        
        
        
