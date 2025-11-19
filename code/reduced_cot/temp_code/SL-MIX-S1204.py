import itertools

def process_sensor_data(readings):
    states = ['IDLE', 'SYNC_START', 'DATA_CAPTURE', 'CHECKSUM_VERIFY', 'TERMINATE']
    current_state = 'IDLE'
    decoded_output = 0
    sync_pattern = [0xAA, 0x55]
    term_pattern = [0xFF, 0x00]
    buffer = []
    checksum = 0
    
    for idx, reading in enumerate(readings):
        if current_state == 'IDLE':
            if reading == sync_pattern[0]:
                current_state = 'SYNC_START'
                buffer = [reading]
        elif current_state == 'SYNC_START':
            if reading == sync_pattern[1]:
                current_state = 'DATA_CAPTURE'
                buffer.append(reading)
            else:
                current_state = 'IDLE'
                buffer = []
        elif current_state == 'DATA_CAPTURE':
            if len(buffer) < 8:
                buffer.append(reading)
                checksum ^= reading
            else:
                if reading == term_pattern[0]:
                    current_state = 'CHECKSUM_VERIFY'
                else:
                    current_state = 'IDLE'
                    buffer = []
                    checksum = 0
        elif current_state == 'CHECKSUM_VERIFY':
            if reading == term_pattern[1] and (checksum & 0xFF) == 0:
                current_state = 'TERMINATE'
                # Process captured data
                data_values = buffer[2:]  # Skip sync bytes
                decoded_output = sum(v << (i*8) for i, v in enumerate(data_values))
                break
            else:
                current_state = 'IDLE'
                buffer = []
                checksum = 0
    return decoded_output

# Sensor readings sequence
sensor_readings = [0x12, 0xAA, 0x55, 0x10, 0x20, 0x30, 0x40, 0x01, 0xFF, 0x00, 0xAB]
result = process_sensor_data(sensor_readings)
print(f"Result: {result}")