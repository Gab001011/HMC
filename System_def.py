# Bulleur_def.py Version 0.0.2 - 19 juillet 2023
#
# Definition de la structure de la carracterisation du fonctionnement du bulleur

from Challenger_def import *

# definition des pression minimum et maximum de chaque modèle.
def_model_capteur = {
    'AMS-5915-2000-D': (0, 2000),
    'AMS-5915-0350-D': (0, 350),
    'AMS-5915-0050-D': (0, 50)
}

def_compresseurs = {
    'compr_1': {'pin_relay': pin_compr_1},
    'capteur_1': {
        'model': 'AMS-5915-2000-D',
        'adr_I2C': 0x0b,
        'nom_var': 'P_compr_1'
    }
}

def_capteur_pression = {
    'amont_1': {
        'model': 'AMS-5915-0350-D',
        'pin_valve': pin_valve_AM_1,
        'adr_I2C': 0x6A,
        'nom_var': 'P_amont_1'
    },
    'aval_1': {
        'model': 'AMS-5915-0350-D',
        'pin_valve': pin_valve_AV_1,
        'adr_I2C': 0x2A,
        'nom_var': 'P_aval_1'
    }
}

def_latching_ponceau = {
    'pin_ON': 10,
    'pin_OFF': 11,
    'liste_valves': ['amont_1', 'aval_1']
}

def_gestion_eau = {
    'pompe': 10,
    'vanne_eau': 11,
    'liste_contenants': ['contenant_1']
}

def_sonde_atlas = {
    'adr_pH': 0x64,
    'adr_CE': 0x32,
    'adr_T_eau' : 0x25,
    'ID' : ID,
    'SDA' : SDA,
    'SCL' : SCL
}


def_sondes_RS485 = {
    'Tx' : u_tx,
    'Rx' : u_rx,
    'id' : u_id,
    'adr_ext' : 42,
    'adr_int' : 43,
    'adr_OD': 0,
    'adr_Turb': 0
}
