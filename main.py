import time
from machine import I2C
import json

from Gestion import Gestion
from Compresseur import Compresseurs
#from Bulleur_def import*
from data import data

#initialiser i2c pression
i2c_pression = I2C(1, scl = 19, sda = 18, freq = 400000)

#initialisation i2c atlas

#initialisation des sondes JXBS

#Initialisation de la sonde à temprérature d'air
#rtu_pins = (Pin(28), Pin(29))  # (TX, RX) GPIO 4 pour TX et GPIO 5 pour RX
#uart_id = 0
#slave_addr_ext = 1  # Adresse du capteur extérieur
#slave_addr_int = 2  # Adresse du capteur intérieur

#T_ext = Sonde_air(rtu_pins, uart_id, slave_addr_ext, baudrate = 9600 , uart_id)
#T_int = Sonde_air(rtu_pins, uart_id, slave_addr_int, baudrate = 9600 , uart_id)

# Initialisation compresseur
#Compresseur = Compresseurs(i2c,def_compresseurs)


# Initialisation class Gestion
Gestion = Gestion(i2c_pression)

# Enregistrer les intervalles en secondes
INTERVALLE_15_MIN = 15 * 60/60      # 15 minutes en secondes
INTERVALLE_24_H = 24 * 60    # 24 heures en secondes 


# Initialisation des dernières exécutions
dernier_execution_15_min = time.time()  # Lancer la première exécution à temps zéro
dernier_execution_24_h = time.time() # Lancer la première exécution à temps zéro


# Boucle principale
while True:
    
    #Remplir réservoir jusqu'à pression souhaitée
    #Compresseur.accroit_pression()
    
    
    # Obtenir le temps actuel
    temps_actuel = time.time()
    
    # Vérifier si 15 minutes se sont écoulées depuis le dernier changement d'eau
    if temps_actuel - dernier_execution_15_min >= INTERVALLE_15_MIN:
        dernier_execution_15_min = temps_actuel  # Mettre à jour l'heure de la dernière exécution
        Gestion.mesures()
        print("Dernière exécution 15 min :", dernier_execution_15_min)

    # Vérifier si 24 heures se sont écoulées depuis la dernière exécution de flush
    #if temps_actuel - dernier_execution_24_h >= INTERVALLE_24_H:
        #dernier_execution_24_h = temps_actuel  # Mettre à jour l'heure de la dernière exécution
       # Gestion.Purge
        #print("Dernière exécution 24 h :", dernier_execution_24_h)

    # Petite pause pour éviter d'utiliser trop de ressources CPU
    time.sleep(1)
    print('yo')
