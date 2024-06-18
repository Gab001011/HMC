# AMS_5915.py Version 0.0.1 - 17 juillet 2023
#
# base sur AMS_sensor.py par Sebastian Gutierez-Pacheco
#
# Definition des capteurs AMS_5915

from machine import I2C, Pin
from Bulleur_def import def_model_capteur

class AMS5915 :
    '''Capteur de pression AMS 5915 '''
    # toutes les unités son en mb et oC
    
    def __init__(self, I2C, capteur_def) :
        " "
        # I2C = bus I2C utilise
        # capteur_def = {'model' : , 'adr_I2C'}
        
        self.i2c = I2C
        self.Digoutp_min = 1638
        self.Digoutp_max = 14745
        self.p_min = def_model_capteur[capteur_def['model']][0]
        self.p_max = def_model_capteur[capteur_def['model']][1]
        self.i2c_adr = capteur_def['adr_I2C']
    
    def lit_sensor(self) :
        " "
        pression_MSB, pression_LSB, temp_MSB, temp_LSB = self.i2c.readfrom(self.i2c_adr, 4)
        pression = pression_LSB + (pression_MSB << 8);
        self.sensp = (self.Digoutp_max - self.Digoutp_min) / (self.p_max - self.p_min)    
        pression = self.p_min + ((pression - self.Digoutp_min) / self.sensp)

        temp = (temp_LSB >> 5) + (temp_MSB << 3);
        temp = ((temp*200) / 2048) - 50 
        
        return pression, temp
        
        