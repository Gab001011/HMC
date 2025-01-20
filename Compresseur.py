# Compresseurs.py Version 0.0.2 - 4 juin 2024
#
# Class qui gère les compresseurs

from Bulleur_def import def_compresseurs
from AMS_5915 import AMS5915
import time
from machine import Pin, I2C

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=100000)

class Compresseurs :
    '''class qui gere les compresseurs'''
    
    def __init__(self, I2C, compresseurs) :
        
        self.compr_1 = Pin(compresseurs['compr_1']['pin_relay'], Pin.OUT )
        
        self.capteur_1 = AMS5915(I2C, compresseurs['capteur_1'])
        
        self.nom_pression_1 = compresseurs['capteur_1']['nom_var']
        
        self.compres_OK = [self.compr_1]
        
        self.capteurs_OK = [self.capteur_1]
        
        self.compres_ON = self.compres_OK[0]
        
        self.pression_cible = 20 # pression cible initiale
        
    def mesure_pression(self) :
        #mesure pression des capteurs actifs'''
        
        self.press_1 = self.capteur_1.lit_sensor()
        print(self.press_1)
        #print(self.temp_1)
     
    def test_pression(self) :
        # Logique de vérification de la pression'''
        
        #implantation initiale simpliste
        pass
    
    def set_pression_cible(self, pression_cible) :
        
        self.pression_cible = pression_cible
    
    def accroit_pression(self) :
        #accroit la pression jusqu'a 120% pression cible
        
        # selection du compresseur - un seul compresseur pour E24
        
        # boucle de verification de la pression à toutes les 5 ou 10 sec.
        n=0
        self.t_acc_p = 0  # temps d'accroit_pression
        while n==0:
            self.mesure_pression()
            if self.press_1<1.2*self.pression_cible:
               
               # activation du compresseur
                self.compr_1.value(1)
                n=0
                self.t_acc_p = self.t_acc_p + 5
                time.sleep(5)
            else:
                #désactivation du compresseur
                n=1
                self.compr_1.value(0)
        
        pass
        
a = Compresseurs(i2c,def_compresseurs)
#a.accroit_pression()