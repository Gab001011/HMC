# RP_Pico.py Version 0.0.1 - 3 juin 2024
#
# Définition de l'atrribution des ports sur le Challenger pour le projet de bulleur

bus_I2C = 1  # a definir
pin_scl = 7 # a definir
pin_sda = 6 # a definir

pin_compr_1 = 3

pins_latch = [1, 2] # Pin 1 high, pin 2 low -> ouvre valve, inverse ferme valve

pin_valve_AM_1 = 17

pin_valve_AV_1 = 16

pin_enable = 0

#def de l'attribution des pins du système pompage

pin_pompe = 4

pin_vanne_eau = 5

#def de l'attribution des pins pour les sondes

#i2c
ID = 1
SDA = 22
SCL = 23

#Modbus
u_id = 1
u_tx = 24
u_rx = 21
