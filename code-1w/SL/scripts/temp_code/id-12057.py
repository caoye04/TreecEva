import math

# Simulated sensor data with noise and irrelevant entries
data_stream = [
    {'id': 1, 'val': 15, 'type': 'A', 'err': False},
    {'id': 2, 'val': -3, 'type': 'B', 'err': True},
    {'id': 3, 'val': 8, 'type': 'A', 'err': False},
    {'id': 4, 'val': 12, 'type': 'C', 'err': False},
    {'id': 5, 'val': 0, 'type': 'B', 'err': False},
    {'id': 6, 'val': 22, 'type': 'A', 'err': False},
    {'id': 7, 'val': -5, 'type': 'D', 'err': False},
    {'id': 8, 'val': 17, 'type': 'A', 'err': False}
]

# Irrelevant auxiliary mapping (distractor)
type_codes = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'X': 88}

# Noise threshold and filtering logic
threshold = 4
valid_types = ['A', 'B']

# Preprocessing: filter out erroneous or irrelevant data
filtered_data = []
for entry in data_stream:
    if not entry['err'] and abs(entry['val']) > threshold:
        filtered_data.append(entry['val'])

# Dead code path - never used (red herring)
def legacy_transform(x):
    return (x << 2) ^ 7

# Unused intermediate statistics (distractor variables)
sum_all = sum(d['val'] for d in data_stream)
max_val = max(d['val'] for d in data_stream)
avg_val = sum_all / len(data_stream)

# Bitmask simulation for signal integrity (partially relevant)
signal_mask = 0b1101
masked_values = [v & signal_mask for v in filtered_data if v > 0]

# Configuration dictionary - critical for processing logic
config = {
    'gain': 1.5,
    'offset': -2,
    'active': True,
    'mode': 'calibrated'
}

# Core processing function with multiple concerns
def process_signals(values, cfg):
    if not cfg['active']:
        return -999
    
    # Intermediate transformation chain
    adjusted = []
    for v in values:
        temp = v * cfg['gain'] + cfg['offset']
        if temp < 0:
            temp = abs(temp) ** 0.5  # sqrt for negative-origin values
        adjusted.append(round(temp, 3))
    
    # Additional filtering based on transformed range
    cleaned = [x for x in adjusted if x >= 3.0]
    
    # Decoy sorting operation (sorting occurs but result not fully used)
    sorted_cleaned = sorted(cleaned, reverse=True)
    
    # Weighted combination using position-based coefficients (key logic)
    final_sum = 0.0
    for i, val in enumerate(sorted_cleaned):
        weight = 1.0 + (0.1 * i)  # increasing weight per rank
        final_sum += val * weight
    
    # Secondary adjustment using bitwise checksum (minor contribution)
    checksum = 0
    for v in [int(x) for x in cleaned]:
        checksum ^= v  # XOR accumulation
    
    # Final composition
    result = int(final_sum) + (checksum & 0b111)  # last 3 bits only
    return result

# Misleading standalone computation (distractor)
temp_analysis = [math.log(abs(x) + 1) for x in filtered_data]

# Key execution point
final_output = process_signals(filtered_data, config)

# Output the target result
print(f"Target result: {final_output}")