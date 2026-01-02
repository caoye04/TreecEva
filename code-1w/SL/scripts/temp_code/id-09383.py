from collections import defaultdict

# Simulated sensor data processing pipeline for environmental monitoring
data_stream = [
    ('temp', 23.5), ('hum', 65), ('temp', 24.1), ('co2', 410), ('hum', 68),
    ('temp', 22.9), ('co2', 395), ('hum', 70), ('co2', 420), ('temp', 25.3)
]

# Misleading initialization of irrelevant statistics
idle_count = 0
baseline_offset = 1.2
aggregated_noise = 0.0

# Data filtering based on type
sensor_buffer = defaultdict(list)
for sensor_type, reading in data_stream:
    sensor_buffer[sensor_type].append(reading)
    if reading < 30:  # Irrelevant condition (never true for valid sensors)
        idle_count += 1

# Extraneous transformation: normalize all values (not used later)
normalized = {}
for stype, readings in sensor_buffer.items():
    mean_val = sum(readings) / len(readings)
    normalized[stype] = [round((r - mean_val) * 0.9, 2) for r in readings]

# Focus on temperature and CO2 only
filtered_data = {
    'temp': sensor_buffer['temp'],
    'co2': sensor_buffer['co2']
}

# Threshold logic with red herring parameters
min_threshold = 20.0
max_threshold = 450.0
threshold_map = {
    'temp': (min_threshold, 30.0),
    'co2': (350.0, max_threshold)
}

# Helper lambda for range validation (used once)
in_range = lambda x, lim: lim[0] <= x <= lim[1]

# State tracker with unused fields
status_log = []
alert_counter = 0
consistency_score = 0.0

# Process each reading and compute diagnostic score
diagnostic_weights = {'temp': 1.5, 'co2': 2.0}
weight_sum = 0.0
score_accum = 0.0

for sensor, values in filtered_data.items():
    low, high = threshold_map[sensor]
    weight = diagnostic_weights[sensor]
    weight_sum += weight
    
    valid_count = 0
    total_deviation = 0.0
    
    for v in values:
        # Check bounds
        if v < low:
            deviation = low - v
        elif v > high:
            deviation = v - high
        else:
            deviation = 0.0
        
        total_deviation += deviation
        
        # Logging side effect (mostly irrelevant)
        status_log.append(f'{sensor}: {"ALERT" if deviation > 0 else "OK"}')
        
        if in_range(v, (low, high)):
            valid_count += 1
    
    # Compute ratio (only last one matters but we recalc each time)
    if len(values) > 0:
        consistency_ratio = valid_count / len(values)
        consistency_score += consistency_ratio  # Accumulated but only final has meaning?

    # Weighted contribution to score (this is key)
    score_accum += (valid_count * weight)

# Apply bitwise adjustment based on alert patterns (obscure but deterministic)
alert_signature = len([s for s in status_log if 'ALERT' in s])
masked_alerts = alert_signature ^ 0b1101  # XOR with magic number
bitwise_tuning = (masked_alerts & 0b1010) >> 1  # Extract bits

# Final diagnostic combines weighted score and bit-adjusted alerts
temp_avg = sum(filtered_data['temp']) / len(filtered_data['temp'])
co2_avg = sum(filtered_data['co2']) / len(filtered_data['co2'])

baseline_diagnostic = (temp_avg * 1.1) + (co2_avg * 0.05)

# Core computation
weighted_consistency = score_accum / weight_sum if weight_sum else 0
final_diagnostic = int(baseline_diagnostic + weighted_consistency - bitwise_tuning)

# Print result as required
print(f"Result: {final_diagnostic}")