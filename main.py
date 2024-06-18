# main.py Version 0.0.1 - 18 juillet 2023
#
# programme principal

# importation
import raspberry_Pi_pico_def
from Buller_def import def_model_capteur, def_compresseurs, def_capteur_pression, def_latching, pin_scl, pin_sda
from Compresseur import Compresseurs


# Initialisation du système

i2c = I2C(0, scl = pin_scl, sda = pin_sda, freq = 400000)
pression=Compresseurs(i2c,'compr_1')

# Initialisation compresseur

pression.set_pression_cible(10)
pression.mesure_pression()
if pression.press_1<1.2*pression.pression_cible:
    pression.accroit_pression()

# Initialisation class Gestion


#Set timer acquistion données aux 15 minutes
#
# exécute Compresseur.test_pression() et Gestion.lit_capteurs()

#Set timer purge au 24 heures
#
# exécute Compresseur.ON() et Gestion.purge()

