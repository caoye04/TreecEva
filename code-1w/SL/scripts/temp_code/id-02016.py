from collections import defaultdict, Counter

# Simulated sensor data with noise and metadata
data_stream = [
    ('sensor_A', 12), ('sensor_B', 8), ('sensor_A', 15), ('sensor_C', 3),
    ('sensor_B', 11), ('sensor_D', 19), ('sensor_A', 7), ('sensor_C', 4),
    ('sensor_E', 22), ('sensor_B', 9), ('sensor_F', 14), ('sensor_D', 16)
]

# Irrelevant mapping - distractor
decoys = {k: v * 1.5 for k, v in [('x', 2), ('y', 4), ('z', 6)]}

# Real processing setup
raw_counts = defaultdict(int)
for sensor, value in data_stream:
    raw_counts[sensor] += value

# Extract top sensors by occurrence (not value) - red herring computation
tokenized = [entry[0][7:] for entry in data_stream]
occurrence_counter = Counter(tokenized)
top_sensors_by_freq = [k for k, v in occurrence_counter.most_common(2)]

# Threshold policy based on average - relevant
average_values = {sensor: total / data_stream.count((f'sensor_{sensor}', 0)) + 1 
                  for sensor, total in raw_counts.items()}

def apply_offset(signal_name, base_val):
    # Complex but partially irrelevant logic
    offsets = {'A': 3, 'B': -1, 'C': 2, 'D': 0, 'E': 5, 'F': -2}
    modifier = len(signal_name) * 0.5
    return base_val + offsets.get(signal_name, 0) + modifier

# Apply offset to averages - only some are used later
adjusted_thresholds = {}
for s, avg in average_values.items():
    adjusted_thresholds[f'thr_{s}'] = apply_offset(s, avg)

# Build actual threshold map - this is critical
threshold_map = {s: int(adjusted_thresholds[f'thr_{s}']) for s in 'ABCDEF'}

# Filtering logic with string operations as distraction
decoded_labels = [f"label_{s.lower()}".upper().replace('_', '') for s in top_sensors_by_freq]
valid_prefixes = [lbl[5:] for lbl in decoded_labels if lbl.startswith('LABEL')]

# Actual filter: only sensors above threshold * 1.1
filtered_data = []
cumulative_noise = 0
for item in data_stream:
    s_name = item[0][-1]
    s_value = item[1]
    if s_value > threshold_map[s_name] * 1.1:
        filtered_data.append((s_name, s_value))
    else:
        cumulative_noise += s_value * 0.1  # unused dead-end

# Decoy function - never called
def analyze_pattern(seq):  
    if len(seq) < 3:
        return sum(len(word) for word in seq) % 7
    return None

# Real processing function
def process_signals(data, thresholds):
    result = 0
    history = []  # decoy list
    for name, val in data:
        # Complex conditional
        if name in ['A', 'C', 'E']:
            result += val * 2
        elif name in ['B', 'D'] and val > thresholds[name]:
            result += val + 5
        else:
            result -= val // 3
        # Fake tracking
        history.append(result % 100)
    
    # Secondary adjustment based on character properties
    for ch in 'CE':
        if any(name == ch for name, _ in data):
            result = int(result * 1.1) if result > 0 else result
    
    return result + len(history)  # len(history) = len(filtered_data)

# Execute main logic
intermediate_checksum = sum(threshold_map.values()) % 1000  # looks important

final_output = process_signals(filtered_data, threshold_map)

# Output the target result
print(f"Target result: {final_output}")