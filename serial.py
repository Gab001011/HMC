# umodbus/serial.py

from machine import UART
from client import ModbusClient
from utils import compute_crc

class ModbusRTU(ModbusClient):
    def __init__(self, addr, pins, baudrate=9600, data_bits=8, stop_bits=1, parity=None, ctrl_pin=None, uart_id=1):
        self.uart = UART(uart_id, baudrate=baudrate, bits=data_bits, parity=parity, stop=stop_bits, tx=pins[0], rx=pins[1])
        self.ctrl_pin = ctrl_pin
        if self.ctrl_pin:
            self.ctrl_pin.init(self.ctrl_pin.OUT, value=0)
        super().__init__(addr)

    def send(self, frame):
        if self.ctrl_pin:
            self.ctrl_pin.value(1)
        print(f"Sending frame: {frame.hex()}")
        self.uart.write(frame)
        if self.ctrl_pin:
            self.ctrl_pin.value(0)

    def receive(self, size):
        data = self.uart.read(size)
        print(f"Received data: {data}")
        return data


    def compute_crc(self, data):
        return compute_crc(data)
