def process_segment(segment, factor):
    # Irrelevant transformation
    temp = [x * 1.1 for x in segment]
    shifted = temp[1:] + [temp[0]]  # Circular shift - misleading
    normalized = [x / sum(temp) for x in temp]  # Normalization not used later

    # Actual relevant computation
    weighted = sum(x * (i + 1) for i, x in enumerate(segment))
    return weighted * factor


def validate_sequence(seq):
    # Complex but irrelevant validation logic
    if len(seq) < 3:
        return False
    for i in range(len(seq) - 2):
        if seq[i] + seq[i+1] != seq[i+2]:
            return False
    return True

# Simulate sensor data segments
data = {
    'sensor_a': [3, 6, 9, 12],
    'sensor_b': [4, 8, 12],
    'sensor_c': [5, 10]
}

def analyze_patterns(values):
    # Extract every second element - slicing distraction
    pattern = values[::2]
    base_sum = sum(values)
    
    # Dummy state tracking
    history = []
    for v in values:
        if v % 2 == 0:
            history.append(v * 0.5)
    
    # Core logic: product of indices where value > average
    avg = sum(values) / len(values)
    index_product = 1
    for idx, val in enumerate(values):
        if val > avg:
            index_product *= (idx + 1)
    
    return index_product

config = {
    'scale_factor': 2,
    'threshold': 7,
    'mode': 'aggressive'
}

# Misleading pre-processing
buffer = []
for k in data:
    buffer.extend(data[k])

# Unnecessary sorting and filtering
sorted_buffer = sorted([x for x in buffer if x > config['threshold']])
duplicates_removed = list(dict.fromkeys(sorted_buffer))

# State variables with partial relevance
accumulator = 0
contributions = {}

for key, readings in data.items():
    if len(readings) >= 3:
        # Only sensor_a passes this
        score = process_segment(readings, config['scale_factor'])
    else:
        # Handle shorter sequences
        score = len(readings) * sum(readings)
    
    # Analyze internal pattern - only used for sensor_c
    pattern_value = analyze_patterns(readings)
    
    # Mixed weighting scheme
    if key == 'sensor_a':
        weight = 1.5
    elif key == 'sensor_b':
        weight = 1.0
    else:
        weight = 0.8
    
    contributions[key] = score * weight + pattern_value

# Final aggregation
raw_total = sum(contributions.values())

# Modular adjustment based on total length
length_flag = len(duplicates_removed) % 4
final_mod = raw_total % 17 if length_flag > 2 else raw_total % 13

# Key statement
result = int(final_mod * config['scale_factor'])

print(f"Result: {result}")