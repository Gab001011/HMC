# umodbus/utils.py
def compute_crc(data):
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            if (crc & 1):
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    # Retourner le CRC en little-endian
    return crc.to_bytes(2, 'little')