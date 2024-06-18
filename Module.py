# Module.py Version 0.0.1 - 19 juillet 2023
#  Robert Lagace. Univ. Laval
#
# Class qui gere le fonctionnement associé à un point de mesure (lecture, sauvegarde et purge

from AMS_5915 import AMS5915
from machine import Pin

class Module :
    ''' '''
    
    def _init__(self, I2C, carac) :
        " "
        
        self.capteur = AMS5915(I2C, carac)
        
        self.valve = Pin(carac['pin_valve'], Pin.OUT)
        
        self.nom_var = carac['nom_var']
        
    def lecture(self) :
        "Lecture du capteur de pression"
        
        pression, temp = self.capteur.lit_sensor()
        
        # traiter les données + sauvegarde
        
    def purge(self) : 
        " Purge la ligne"
        
        # ouvre la valve pendant 5 sec.
        
        #self.valve.value(1)
        # wait 5 sec
        #self.valve.value(0)