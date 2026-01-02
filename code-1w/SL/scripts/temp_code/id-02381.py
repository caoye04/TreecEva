from collections import defaultdict, Counter
import math

# Simulated sensor data stream with multiple channels
data_stream = [
    {'time': 0.1, 'sensor_A': 5, 'sensor_B': 3, 'sensor_C': 8},
    {'time': 0.2, 'sensor_A': 7, 'sensor_B': 1, 'sensor_C': 12},
    {'time': 0.3, 'sensor_A': 6, 'sensor_B': 4, 'sensor_C': 10},
    {'time': 0.4, 'sensor_A': 8, 'sensor_B': 2, 'sensor_C': 14},
    {'time': 0.5, 'sensor_A': 9, 'sensor_B': 3, 'sensor_C': 16}
]

# Irrelevant baseline calibration map (distractor)
calibration_map = {
    'gain_A': 1.05, 'gain_B': 0.98, 'gain_C': 1.02,
    'offset_A': 0.1, 'offset_B': -0.05, 'offset_C': 0.08
}

# Thresholds for anomaly detection (used later)
threshold_map = defaultdict(lambda: 0)
threshold_map['A_high'] = 8.5
threshold_map['B_low'] = 2.5
threshold_map['C_growth'] = 3.0  # per 0.1 sec

# Dead code path: Unused transformation function (red herring)
def deprecated_transform(x):
    return (x ** 2 + 3 * x + 1) % 17

# Auxiliary statistical tracker (partially relevant)
stats_tracker = defaultdict(list)
for entry in data_stream:
    stats_tracker['A_values'].append(entry['sensor_A'])
    stats_tracker['B_values'].append(entry['sensor_B'])
    stats_tracker['C_values'].append(entry['sensor_C'])

# Compute rolling growth rate for sensor C (relevant)
growth_rates = []
for i in range(1, len(data_stream)):
    delta_c = data_stream[i]['sensor_C'] - data_stream[i-1]['sensor_C']
    delta_t = data_stream[i]['time'] - data_stream[i-1]['time']
    rate = delta_c / delta_t if delta_t > 0 else 0
    growth_rates.append(rate)

# Transform raw data into diagnostic features
transformed_data = []
for idx, entry in enumerate(data_stream):
    # Complex derived metrics
    a_norm = entry['sensor_A'] / (entry['sensor_B'] + 1)
    b_power = entry['sensor_B'] ** 2
    c_accel = growth_rates[idx-1] if idx > 0 else 0
    
    # Bitwise signature (irrelevant but looks important)
    signature = (entry['sensor_A'] << 2) ^ (entry['sensor_B'] | int(entry['time']*100))
    
    # Only some fields are actually used later
    transformed_data.append({
        'idx': idx,
        'a_norm': a_norm,
        'c_accel': c_accel,
        'raw_C': entry['sensor_C'],
        'temp_flag': bool(signature & 0x1),  # unused
        'timestamp': entry['time']
    })

# Unused counter analysis (dead path)
useless_counter = Counter()
for item in transformed_data:
    useless_counter[item['temp_flag']] += 1

# Another red herring: entropy calculation (never used)
def shannon_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs if p > 0)

entropy_A = shannon_entropy(stats_tracker['A_values'])
entropy_B = shannon_entropy(stats_tracker['B_values'])

# Core analysis function


# Misleading intermediate function (looks important, not called)
def validate_consistency(data, thresholds):
    errors = 0
    for d in data:
        if d['a_norm'] > thresholds['A_high']:
            errors += 1
    return errors < 3

# Actual analysis logic
def analyze_pattern(processed, limits):
    alert_count = 0
    
    # Check normalized A against high threshold
    for record in processed:
        if record['a_norm'] > limits['A_high']:
            alert_count += 1
    
    # Check acceleration of C
    for record in processed:
        if record['c_accel'] > limits['C_growth']:
            alert_count += 2  # higher weight
    
    # Suppressed condition (never triggered due to data)
    stable_A = all(abs(processed[i+1]['a_norm'] - processed[i]['a_norm']) < 0.5 
                   for i in range(len(processed)-1))
    
    # Final logic
    if alert_count >= 3:
        return 867
    elif alert_count == 2:
        return 432
    else:
        return 195

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")