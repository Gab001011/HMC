# umodbus/client.py
import time

class ModbusClient:
    def __init__(self, addr):
        self.addr = addr

    def build_request(self, function_code, register_addr, num_registers):
        request = bytearray(6)
        request[0] = self.addr
        request[1] = function_code
        request[2] = (register_addr >> 8) & 0xFF
        request[3] = register_addr & 0xFF
        request[4] = (num_registers >> 8) & 0xFF
        request[5] = num_registers & 0xFF
        #request += bytearray([0xCA, 0x25])  # Ajout manuel du CRC correct
        return request
    
    def read_holding_registers(self, register_addr, num_registers):
        request = self.build_request(0x03, register_addr, num_registers)
        print("Requête sans CRC : ", request)
        request += self.compute_crc(request) #à remmettre une fois le problème de crc résolu
        print("Requête avec CRC : ", request.hex())
        self.send(request)
        time.sleep(1)
        response = self.receive(5 + 2 * num_registers)
        return response[3:3 + 2 * num_registers]

    def send(self, frame):
        raise NotImplementedError

    def receive(self, size):
        raise NotImplementedError

    def compute_crc(self, data):
        raise NotImplementedError
    
    def read_input_registers(self, register_addr, num_registers):
        request = self.build_request(0x04, register_addr, num_registers)
        request += self.compute_crc(request)  #à remmettre une fois le problème de crc résolu
        self.send(request)
        response = self.receive(5 + 2 * num_registers)
        return response[3:3 + 2 * num_registers]
