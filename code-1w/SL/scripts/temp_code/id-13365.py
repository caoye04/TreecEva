from itertools import combinations
from math import log2

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.87
TEMPORAL_DAMPING = 0.93
BASELINE_DRIFT = [0.12, -0.05, 0.33, 0.01]

# System state monitors (some are red herrings)
cpu_load_history = [0.45, 0.67, 0.78, 0.81, 0.76]
memory_pressure = {'current': 0.68, 'peak': 0.94}
disk_io_ops = [(120, 'read'), (89, 'write'), (145, 'read')]

# Core diagnostic data
raw_readings = [
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1],
    [0, 0, 1, 1, 1, 1]
]

# Misleading intermediate transformations
def apply_dampening(data, factor):
    return [[cell * factor for cell in row] for row in data]

def calculate_entropy(vector):
    return sum(p * log2(1/p) for p in vector if p > 0)

# Dead function - never called
def analyze_io_pattern(ops):
    total = sum(op[0] for op in ops)
    avg = total / len(ops)
    return avg if avg > 100 else 0

# Another decoy function with bit manipulation red herring
def generate_checksum(value_list):
    checksum = 0
    for val in value_list:
        checksum ^= int(sum(val) * 100) & 0xFF
    return checksum

# Real processing begins here
status_flags = {
    'POWER_OK': True,
    'SENSOR_ARRAY_ACTIVE': False,
    'DIAGNOSTIC_LOCK': None
}

# Irrelevant flag mutation
def toggle_status(flags, key):
    if key in flags and isinstance(flags[key], bool):
        flags[key] = not flags[key]
    return flags

status_flags = toggle_status(status_flags, 'POWER_OK')

# Actual relevant data filtering
def filter_anomalies(readings_matrix):
    valid_rows = []
    for row in readings_matrix:
        # Only rows with exactly three 1s are valid
        if sum(row) == 3:
            valid_rows.append(row)
    return valid_rows

filtered_data = filter_anomalies(raw_readings)

# Complex threshold map with irrelevant entries
threshold_map = {
    'voltage': 0.75,
    'current_risk': 0.33,
    'temporal_window': 5,
    'critical_density': 0.6,
    'bit_pattern_key': [1, 0, 1],
    'aux_settings': {'mode': 'passive', 'gain': 2.1}
}

# Core processing with set operations and combinations
def process_readings(valid_rows, config):
    if not valid_rows:
        return -1
    
    # Extract column-wise patterns
    transposed = list(zip(*valid_rows))
    
    # Use set operations to find unique pattern signatures
    pattern_set = set()
    for col in transposed:
        pattern_set.add(col)
    
    # Generate all 2-element combinations of rows (distraction)
    combo_count = 0
    for combo in combinations(valid_rows, 2):
        xor_pair = [a ^ b for a, b in zip(combo[0], combo[1])]
        combo_count += sum(xor_pair)
    
    # Real logic: count how many columns have mixed values
    instability_count = 0
    for col in transposed:
        if len(set(col)) > 1:  # Both 0 and 1 present
            instability_count += 1
    
    # Use bit pattern from config as mask (only first 3 elements matter)
    mask = config['bit_pattern_key']
    masked_instability = instability_count
    for i, bit in enumerate(mask):
        if bit == 1:
            masked_instability ^= (1 << i)  # XOR with power of 2
    
    # Final transformation using only core variables
    primary_diagnostic = len(valid_rows) * 100
    secondary_factor = instability_count * 15
    
    # The real answer computation
    result = primary_diagnostic + secondary_factor - masked_instability
    
    # Dead code path - never reached due to return
    if result < 0:
        backup = generate_checksum(valid_rows)
        return backup % 100
        
    return result

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")