from machine import Pin, UART
from serial import ModbusRTU
import utime as time  # Compatible MicroPython
from System_def import *


class Temp_air:
    
    def __init__(self, slave_addr):

        self.rtu_pins = (Pin(def_sondes_RS485['Tx']), Pin(def_sondes_RS485['Rx']))  
        self.uart_id = def_sondes_RS485['id']

        # Initialisation d'un seul client Modbus RTU
        self.client = ModbusRTU(
            addr = None,  # L'adresse sera définie dynamiquement
            pins = self.rtu_pins,
            baudrate = 9600,  # Vitesse par défaut de la sonde
            uart_id = self.uart_id
        )

    # Lecture de la température en utilisant read_holding_registers
    def read_temperature(self, slave_addr):
        """Lecture de la température via les registres de maintien (holding registers)."""
        try:
            self.client.addr = slave_addr  # Définir l'adresse de l'esclave
            result = self.client.read_holding_registers(0x0000, 1)  # Registre 0x0000 pour la température
            if result:
                temperature = int.from_bytes(result, 'big') / 100  # Conversion selon la documentation
                return temperature
        except Exception as e:
            print(f"Erreur lors de la lecture de l'adresse {slave_addr} : {e}")
        return None
