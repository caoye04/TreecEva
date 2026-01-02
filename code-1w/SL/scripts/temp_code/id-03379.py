from collections import defaultdict, Counter

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 26.7, 22.3, 20.4, 27.1, 28.0, 21.9]
humidity_readings = [45, 48, 52, 58, 61, 47, 50, 63, 66, 49]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1010, 1014, 1007, 1003, 1011]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 35, 30, 45, 50, 33, 38, 42, 29, 31]
lux_values = [400, 380, 420, 350, 300, 390, 410, 370, 430, 360]

# Data preprocessing with red herrings
data_matrix = []
for i in range(len(temperature_readings)):
    data_matrix.append((
        temperature_readings[i],
        humidity_readings[i],
        pressure_readings[i],
        sound_levels[i],  # unused field (distractor)
        lux_values[i]     # unused field (distractor)
    ))

def extract_thermal_metrics(data):
    temps = [row[0] for row in data]
    return {
        'avg': sum(temps) / len(temps),
        'min': min(temps),
        'max': max(temps),
        'range': max(temps) - min(temps)
    }

def filter_outliers(values, threshold=2.0):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

# Misleading transformation chain (dead path)
dummy_aggregate = 0
for temp in temperature_readings:
    if temp > 25:
        dummy_aggregate += temp * 0.1
    else:
        dummy_aggregate -= temp * 0.05

dummy_aggregate = round(dummy_aggregate, 2)  # irrelevant result

# Real processing begins here
thermal_stats = extract_thermal_metrics(data_matrix)
filtered_temps = filter_outliers(temperature_readings, threshold=1.5)

# Generate auxiliary maps with decoy logic
threshold_map = defaultdict(lambda: 0)
threshold_map['temp_high'] = 26.0
threshold_map['temp_low'] = 20.5
threshold_map['humid_thresh'] = 60
threshold_map['press_trend'] = -3

status_flags = []
for t in filtered_temps:
    if t > threshold_map['temp_high']:
        status_flags.append('HIGH')
    elif t < threshold_map['temp_low']:
        status_flags.append('LOW')
    else:
        status_flags.append('NORMAL')

flag_count = Counter(status_flags)

# Decoy sorting operation on irrelevant tuple structure
mixed_signals = [(p, h, t) for p, h, t in zip(pressure_readings, humidity_readings, temperature_readings)]
mixed_signals.sort(key=lambda x: x[1])  # sort by humidity, never used again
mixed_signals.sort(key=lambda x: x[2], reverse=True)  # sort by temp, not used

# Another red herring: slicing with no downstream use
slice_a = mixed_signals[1:7:2]
slice_b = mixed_signals[::-1]
slice_c = mixed_signals[2:8]

# Core logic embedded within noise
baseline_ref = thermal_stats['avg']
correction_factor = 0.85 if flag_count['HIGH'] > 1 else 1.15
adjusted_baseline = baseline_ref * correction_factor

# Simulate calibration offset (distractor)
offset_stack = []
for i in range(3):
    offset_stack.append(adjusted_baseline * (0.98 + i * 0.01))
final_offset = sum(offset_stack) / len(offset_stack)
residual_error = final_offset - adjusted_baseline  # computed but unused

# Critical data filtering
valid_indices = []
for i, t in enumerate(temperature_readings):
    if threshold_map['temp_low'] <= t <= threshold_map['temp_high']:
        valid_indices.append(i)

filtered_data = [temperature_readings[i] for i in valid_indices]

# Additional misleading computation
shadow_copy = filtered_data[:]
for i in range(len(shadow_copy)):
    shadow_copy[i] += 0.5
    shadow_copy[i] = round(shadow_copy[i], 1)
# shadow_copy is never used

# Actual diagnostic processor
prev_state = ''
diagnostic_log = []
for val in filtered_data:
    if val > thermal_stats['avg']:
        current_state = 'ABOVE_BASELINE'
    elif val < thermal_stats['avg'] * 0.95:
        current_state = 'BELOW_WARNING'
    else:
        current_state = 'STABLE'
    
    if prev_state and prev_state != current_state:
        diagnostic_log.append('TRANSITION')
    prev_state = current_state

diagnostic_score = len(diagnostic_log) * 100

# Final integration with multiple concepts
def process_readings(data, thresholds):
    if not data:
        return -1
    
    # Bit manipulation red herring
    magic_seed = len(data) ^ 255
    magic_seed = (magic_seed << 2) | (magic_seed >> 6)
    magic_seed = magic_seed & 0xFF
    
    base_value = sum(data) / len(data)
    trend = data[-1] - data[0]
    
    # Real decision logic
    if trend > 1.5:
        adjustment = thresholds['temp_high'] * 0.1
    elif trend < -1.5:
        adjustment = -thresholds['temp_low'] * 0.1
    else:
        adjustment = 0.5
    
    # Final computation
    result = (base_value + adjustment) * 10
    return int(result)

# Execute key statement
temp_snapshot = filtered_data[:]
final_diagnostic = process_readings(filtered_data, threshold_map)

print(f"Result: {final_diagnostic}")