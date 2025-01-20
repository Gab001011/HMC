# Module.py Version 0.0.1 - 19 juillet 2023
#  Robert Lagace. Univ. Laval
#
# Class qui gere le fonctionnement associé à un point de mesure (lecture, sauvegarde et purge

from AMS_5915 import AMS5915
from machine import Pin, I2C
from Challenger_def import *
from Latching import Latching
from Bulleur_def import def_compresseurs, def_model_capteur, def_capteur_pression, def_latching_ponceau
import time

class Module :
    ''' '''
    
    def __init__(self, I2C, carac, def_gestion_eau) :
        " "
        
        self.capteur = AMS5915(I2C, carac)
        
        self.valve = Pin(carac['pin_valve'], Pin.OUT)
        
        self.nom_var = carac['nom_var']
        
        self.pompe = Pin(def_gestion_eau['pompe'], Pin.OUT)
        
        self.vanne_eau = Pin(def_gestion_eau['pompe'], Pin.OUT)
        
        self.enable = Pin(pin_enable, Pin.OUT)
        
        
    def lecture(self) :
        "Lecture du capteur de pression"
        
        pression = self.capteur.lit_sensor()
        
        return pression
        
        # traiter les données + sauvegarde
        
    def purge(self) : 
        " Purge la ligne"
        self.enable.value(1)
        
        # ferme latching valve pendant 5 sec
        latch = Latching(def_latching_ponceau)
        latch.close()
        
        # ouvre la mouse valve pendant 5 sec.
        self.valve.value(1)
        
        time.sleep(5)
        
        latch.open()
        self.valve.value(0)
        
        self.enable.value(0)
    
    def changement_eau(self):
        "changement d'eau"
        #8.7 secondes requise (arrondies à 10 secondes) pour vider le contenant
        self.vanne_eau.value(1)
        time.sleep(10)
        self.vanne_eau.value(0)
        
        #18 secondes requises pour remplir le contenant
        self.pompe.value(1)
        time.sleep(18)
        self.pompe.value(0)
        
        
        
i2c = I2C(1, scl = 19, sda = 18, freq = 400000)       
#a = Module(i2c, def_capteur_pression['amont_1'],def_gestion_eau)
#b = Module(i2c, def_capteur_pression['aval_1'])
#a.purge()
#b.purge()
#print('ça marche?')