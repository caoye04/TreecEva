import math

# Irrelevant helper function (dead code path)
def unused_checksum(arr):
    return sum(x ^ 255 for x in arr) % 100

# Misleading transformation chain
def transform_signal(x):
    if x < 0:
        return abs(x) * 3
    elif x % 2 == 0:
        return x + 10
    else:
        return x * 2

# Distractor: Unused state tracker
class StateBuffer:
    def __init__(self):
        self.history = []
        self.counter = 0

    def update(self, val):
        self.history.append(val)
        self.counter += 1

# Core processing functions
def decode_frame(frame):
    result = 0
    for i, byte in enumerate(frame):
        result += (byte & 0xF) ^ i
    return result

def validate_entry(key, value):
    return key in ['sensor_7', 'sensor_9'] and value > 50

def accumulate_readings(readings_dict):
    total = 0
    for k, v in readings_dict.items():
        if 'sensor' in k:
            base_val = int(k.split('_')[-1])
            if base_val % 3 == 0:
                total += v // 2
            else:
                total += v
    return total

def apply_correction(values):
    corrected = []
    for v in values:
        if v % 4 == 0:
            corrected.append(v + 7)
        elif v % 5 == 0:
            corrected.append(v - 3)
        else:
            corrected.append(v)
    return corrected

# Complex pipeline with red herrings
def process_pipeline(stream):
    temp_buffer = []
    meta_info = {'version': '2.1', 'mode': 'debug'}  # Distractor dict
    debug_log = []  # Unused logging array

    for segment in stream:
        # Extract only valid frames based on checksum
        checksum = sum(segment) % 256
        if checksum % 7 != 0:
            continue
        
        decoded = decode_frame(segment)
        temp_buffer.append(decoded)
    
    # Apply correction to buffer (relevant)
    adjusted = apply_correction(temp_buffer)
    
    # Simulate sensor mapping (partially irrelevant)
    sensor_data = {}
    for i, val in enumerate(adjusted):
        sensor_id = f"sensor_{(i + 3) % 13}"
        sensor_data[sensor_id] = val * (i % 4 + 1)
    
    # Accumulate only specific sensors (key logic step)
    raw_sum = accumulate_readings(sensor_data)
    
    # Final adjustment using mathematical operations
    multiplier = len([x for x in temp_buffer if x > 20])
    scaling_factor = math.log(multiplier + 2) if multiplier > 0 else 1.0
    
    # Introduce decoy calculation (misleading intermediate)
    decoy_result = 0
    for k, v in sensor_data.items():
        if '9' in k:
            decoy_result += int(math.sqrt(v))
    
    # Actual final output computation
    final_output = int(raw_sum * scaling_factor) - 15
    
    # Dead branch with no effect
    if final_output < 0:
        backup_state = StateBuffer()
        for v in adjusted:
            backup_state.update(v)
    
    return final_output

# Setup realistic data stream (simulated IoT sensor packets)
data_stream = [
    [0x1A, 0x2B, 0x3C, 0x4D],
    [0x5E, 0x6F, 0x70, 0x81],
    [0x92, 0xA3, 0xB4, 0xC5],
    [0xD6, 0xE7, 0xF8, 0x09],
    [0x1B, 0x2C, 0x3D, 0x4E]
]

# Execute main logic
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")