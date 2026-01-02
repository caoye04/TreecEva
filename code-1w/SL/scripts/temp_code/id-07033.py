def transform_value(x):
    # Irrelevant transformation (dead logic path)
    if x < 0:
        return x * 2
    return x + 1

def helper_func(data):
    # Misleading computation with no effect on final result
    temp_sum = 0
    for k in data:
        temp_sum += len(k) * data[k]
    return temp_sum // 2  # Never used in actual logic

def decode_sequence(seq):
    # Actual relevant recursive function
    if not seq:
        return 0
    return seq[0] + decode_sequence(seq[1:])

def process_data(structure, flag):
    # Core logic hidden among distractions
    accumulator = 0
    decoy_counter = 0  # Distractor variable
    debug_log = []   # Unused logging array

    # Red herring: complex but unused dictionary traversal
    for key, value in structure.items():
        if isinstance(value, dict):
            for subkey, subval in value.items():
                if subval % 2 == 0:
                    decoy_counter += 1
                    debug_log.append(subkey)

    # Relevant logic begins here — nested conditional with real impact
    if flag and 'level_1' in structure:
        level_data = structure['level_1'].get('values', [])
        intermediate = decode_sequence(level_data)
        
        # Bit manipulation distraction
        masked = intermediate ^ 0xFF
        normalized = masked & 0xFFFF
        
        # Real calculation path
        scaling_factor = structure['level_1'].get('scale', 1)
        accumulator = intermediate * scaling_factor

        # Fake branching that looks important
        if accumulator > 100:
            accumulator -= 50
        elif accumulator < 50:
            accumulator += 25

        # Additional red herring: modifying a decoy list
        history = []
        for i in range(3):
            history.append({'step': i, 'value': accumulator >> i})

        # Final override based on secondary condition
        if structure.get('meta', {}).get('override', False):
            accumulator = 999  # This will NOT trigger due to data setup

    return accumulator

# Main execution block
config_map = {
    'level_1': {
        'values': [4, 8, 15, 16],  # Input to recursive decoder
        'scale': 3
    },
    'level_2': {
        'values': [23, 42],
        'scale': 2
    },
    'meta': {
        'version': '2.1',
        'override': False  # Prevents final override
    },
    'debug_mode': True,
    'timeout': 300
}

# Unused auxiliary structures (distractors)
network_buffer = [0] * 10
checksum_table = {i: (i * 27) % 19 for i in range(15)}
control_mask = 0b1101

# Simulated sensor readings — irrelevant
sensor_data = {
    'temp': 22.5,
    'pressure': 1013.25,
    'humidity': 45
}

# Control flag influenced by fake logic
control_flag = len(config_map['level_1']['values']) > 3  # Evaluates to True

# Execute main logic
final_output = process_data(config_map, control_flag)

# Output result as required
print(f"Result: {final_output}")