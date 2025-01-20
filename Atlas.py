import machine
import time
import re  # Pour utiliser des expressions régulières
from System_def import *

class Atlas:
    """
    Classe pour interagir avec les capteurs Atlas via I2C.
    """
    
    def __init__(self):
        self.i2c = machine.I2C(0, sda=machine.Pin(4), scl=machine.Pin(5), freq=400000)
        self.num_of_bytes = 31
        self.adr_CE = def_sonde_atlas['adr_CE']
        self.adr_pH = def_sonde_atlas['adr_pH']
        
    def read_i2c(self, address):
        """
        Lit un nombre spécifié d'octets depuis l'interface I2C.
        """
        try:
            response = self.i2c.readfrom(address, self.num_of_bytes)
            return response
        except Exception as e:
            print(f"Erreur de lecture depuis l'appareil à l'adresse {hex(address)}: ", e)
            return None

    def send_i2c(self, address, cmd):
        """
        Envoie une commande au capteur via I2C.
        """
        cmd += "\00"  # ajoute un caractère nul
        try:
            self.i2c.writeto(address, cmd.encode('latin-1'))
            return True
        except Exception as e:
            print(f"Erreur d'envoi à l'appareil à l'adresse {hex(address)}: ", e)
            return None

    def lecture_conductivite(self):
        """
        Lit plusieurs fois la conductivité électrique et calcule une moyenne.
        """
        valeurs = []  # Liste pour stocker les valeurs numériques

        for _ in range(5):
            self.send_i2c(self.adr_CE, "R")  # Envoie la commande
            time.sleep(1.3)  # Délai pour que le capteur réponde
            response = self.read_i2c(self.adr_CE)  # Lecture de la réponse
            
            if response:
                try:
                    # Décodage de la réponse et suppression des caractères non numériques
                    valeur_str = response.decode('utf-8').strip()
                    valeur_str = re.sub(r'[^\d.]+', '', valeur_str)  # Supprime tout sauf les chiffres et le point

                    # Conversion en float
                    valeur = float(valeur_str)
                    valeurs.append(valeur)  # Ajoute la valeur numérique à la liste
                except ValueError:
                    pass

        # Calcul de la moyenne si au moins une valeur valide a été capturée
        if valeurs:
            moyenne = sum(valeurs) / len(valeurs)
            return round(moyenne, 2)
        else:
            return None
        
    def lecture_pH(self):
        """
        Lit plusieurs fois la conductivité électrique et calcule une moyenne.
        """
        valeurs = []  # Liste pour stocker les valeurs numériques

        for _ in range(5):
            self.send_i2c(self.adr_pH, "R")  # Envoie la commande
            time.sleep(1.3)  # Délai pour que le capteur réponde
            response = self.read_i2c(self.adr_pH)  # Lecture de la réponse
            
            if response:
                try:
                    # Décodage de la réponse et suppression des caractères non numériques
                    valeur_str = response.decode('utf-8').strip()
                    valeur_str = re.sub(r'[^\d.]+', '', valeur_str)  # Supprime tout sauf les chiffres et le point

                    # Conversion en float
                    valeur = float(valeur_str)
                    valeurs.append(valeur)  # Ajoute la valeur numérique à la liste
                except ValueError:
                    pass

        # Calcul de la moyenne si au moins une valeur valide a été capturée
        if valeurs:
            moyenne = sum(valeurs) / len(valeurs)
            return round(moyenne, 2)
        else:
            return None
