# Gestion.py Version 0.0.2 - 4 juin 2024
#  Gabriel.Baillargeon. Univ. Laval
#
# Class pour gérer la lecture des capteurs et faire la purge

from machine import I2C, RTC##
from System_def import *
from Latching import Latching
from Module import Module
from AMS_5915 import AMS5915
from data import data##
import json
from Temp_air import Temp_air
from Atlas import Atlas


class Gestion :
    ''' '''
    
    def __init__(self, I2C) :
        " "
        
        self.liste_grp_ponceau = []
        
        # init latching et les module associés (valves et capteurs) associé au ponceau
        
        self.latching_ponceau = Latching(def_latching_ponceau)
        
        for cas in def_latching_ponceau['liste_valves'] :
            module = Module(I2C, def_capteur_pression[cas], def_gestion_eau)
            self.liste_grp_ponceau.append(module)
        
        # Initialisation des sondes T_air
        self.slave_addr_ext = def_sondes_RS485['adr_ext']
        self.slave_addr_int = def_sondes_RS485['adr_int']

        # Initialisation des sondes de température extérieure et intérieure
        self.T_ext = Sonde_air(self.slave_addr_ext)
        self.T_int = Sonde_air(self.slave_addr_int)
        
        # Initialisation Atlas
        self.atlas = Atlas()
        
    def mesures(self) :
        # Récupérer l'heure actuelle
        current_time = rtc.datetime()

        # Format compact pour la date et l'heure (AAAAMMJJHHMMSS)
        date_time_str = "{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}".format(
            current_time[0], current_time[1], current_time[2],
            current_time[4], current_time[5], current_time[6]
        )

        # Mesures des pressions
        pressions = []
        for capteur in self.liste_grp_ponceau :
            pression = capteur.lecture()
            print(pression) #enlever
            pressions.append(pression)
        print(pressions) #enlever
            
        #data['Pam'] = pressions[0]
        #data['Pav'] = 0 #pressions[1]
        
        #fonction sondes de Température
        #data['Teau'] = 3
        data['Text'] = self.T_ext.T_air()
        data['Tint'] = self.T_int.T_air()
        
        #fonction sondes atlas
        #data['Tce'] = 4
        #data['Tph'] = 5
        data['CE'] = atlas.lecture_conductivite()
        data['pH'] = atlas.pH()
        
        #Fonction sondes JXBS
        #data['Tod'] = 6
        #data['Tt'] = 7
        #data['OD'] = 10
        #data['T'] = 11

        # Créer un nouveau dictionnaire `ordered_data` en suivant l'ordre souhaité
        ordered_data = {'datetime': date_time_str}  # Commence avec la date et l'heure
        for key in data:
            ordered_data[key] = data[key]

        # Convertir `ordered_data` en JSON
        data_json = json.dumps(ordered_data)
        print("Chaîne JSON finale avec date en premier:", data_json)

        # Sauvegarder la chaîne JSON dans un fichier en ajoutant à la fin
        filename = "data.json"  # Nom du fichier dans la mémoire du microcontrôleur
        try:
            with open(filename, "a") as file:  # Utiliser le mode "a" pour ajouter à la fin
                file.write(data_json + "\n")  # Ajouter chaque JSON sur une nouvelle ligne
                print(f"Les données JSON ont été ajoutées dans {filename}")
        except OSError as e:
            print("Erreur lors de l'enregistrement du fichier :", e)
            
    
    def purge(self) :
        "Purge de cahcune des lignes"
        
        for ponceau in self.liste_grp_ponceau :
            ponceau.purge()
    
    def changement_eau(self):
        "changement d'eau dans chacun des contenant d'eau"
        changement_eau()
        
rtc = RTC()
i2c = I2C(1, scl = Pin(7), sda = Pin(6), freq = 400000)
a = Gestion(i2c)
a.mesures()