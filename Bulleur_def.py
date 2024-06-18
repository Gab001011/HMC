# Bulleur_def.py Version 0.0.2 - 19 juillet 2023
#
# Definition de la structure de la carracterisation du fonctionnement du bulleur

from raspberry_Pi_pico_def import *

# definition des pression mimimum et maximum de chaque modèle.
def_model_capteur = {
    'AMS-5915-2000-D' : (0, 2000),
    'AMS-5915-0350-D' : (0, 0350),
    'AMS-5915-0050-D' : (0, 0050)
}

def_compresseurs = {
    'compr_1' : {'pin_relay' : pin_compr_1
                 },

    'capteur_1' : {'model' : 'AMS-5915-2000-D',
                   'adr_I2C' : 0x0b,
                   'nom_var' : 'P_compr_1'
                   }  
    }

def_capteur_pression = {
    'amont_1' : {'model' : 'AMS-5915-0350-D',
                 'pin_valve' : pin_valve_AM_1,
                 'adr_I2C' : 0x0A,
                 'nom_var' : 'P_amont_1'

        },
    'aval_1' : {'model' : 'AMS-5915-0350-D',
                 'pin_valve' : pin_valve_AV_1,
                 'adr_I2C' : 0x4A,
                 'nom_var' : 'P_aval_1'
        }         
    }

def_latching_ponceau = {'pin_ON' : 10,
                        'pin_OFF' :11,
                        'liste_valves' : ['amont','aval' ]}
                



