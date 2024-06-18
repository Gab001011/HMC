# Gestion.py Version 0.0.2 - 4 juin 2024
#  Gabriel.Baillargeon. Univ. Laval
#
# Class pour gérer la lecture des capteurs et faire la purge

#
from Bulleur_def import *
from Latching import Latching
from Module import Module

class Gestion :
    ''' '''
    
    def __init__(self, I2C) :
        " "
        
        self.liste_grp_ponceau = []
        
        self.liste_grp_deversoir = []
        
        # init latching et les module associés (valves et capteurs) associé au ponceau
        
        self.latching_ponceau = Latching(def_latching_ponceau)
        
        for cas in def_latching_ponceau['liste_valves'] :
            module = Module(I2C, def_capteur_pression[cas])
            self.liste_grp_ponceau.append(module)
        
        # init latching et les module associés (valves et capteurs) associé au deversoir
        
        self.latching_dever = Latching(def_latching_dever)
        
        for cas in def_latching_dever['liste_valves'] :
            module = Module(I2C, def_capteur_pression[cas])
            self.liste_grp_deversoir.append(module)
        
        # latchig defaut ??
        
        self.grp_dever = False
    
    def lit_capteurs(self) :
        "Lecture des capteurs"
        
        for capteur in self.liste_grp_ponceau :
            capteur.lecture()
        
        if self.grp_dever == True :
            for capteur in self.liste_grp_deversoir :
                capteur.lecture()
    
    def purge(self) :
        "Purge de cahcune des lignes"
        
        for cas in self.liste_grp_ponceau :
            cas.purge()
        
        for cas in self.liste_grp_deversoir :
            cas.purge()
                
                