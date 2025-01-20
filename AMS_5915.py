from machine import I2C, Pin
from Bulleur_def import def_model_capteur, def_compresseurs

class AMS5915:
    '''Capteur de pression AMS 5915'''
    # Toutes les unités sont en mb et °C
    
    def __init__(self, i2c, capteur_def):
        """
        Initialisation du capteur AMS5915.
        """
        self.i2c = i2c  # Instance I2C
        self.Digoutp_min = 1638
        self.Digoutp_max = 14745
        self.p_min, self.p_max = def_model_capteur[capteur_def['model']]
        self.i2c_adr = capteur_def['adr_I2C']  # Adresse I2C du capteur
    
    def lit_sensor(self):
        """
        Lecture des données du capteur (pression uniquement).
        """
        # Vérification de l'adresse I2C
        if not isinstance(self.i2c_adr, int):
            raise TypeError(f"Adresse I2C invalide : {self.i2c_adr} (Type : {type(self.i2c_adr)})")

        # Lire les données brutes depuis le capteur
        try:
            data = self.i2c.readfrom(self.i2c_adr, 4)
            pression_MSB, pression_LSB = data[0], data[1]
        except OSError as e:
            print(f"Erreur de communication I2C : {e}")
            return None

        # Conversion de la pression numérique en unités physiques
        pression = pression_LSB + (pression_MSB << 8)
        self.sensp = (self.Digoutp_max - self.Digoutp_min) / (self.p_max - self.p_min)
        pression = self.p_min + ((pression - self.Digoutp_min) / self.sensp)
        return pression

# Initialisation du bus I2C
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=100000)  # Fréquence réduite à 100 kHz

# Initialisation du capteur
a = AMS5915(i2c, def_compresseurs['capteur_1'])

# Lecture de la pression
pression = a.lit_sensor()
print(f"Pression mesurée : {pression:.2f} mbar")
print(f"Adresse I2C utilisée : {a.i2c_adr}")
