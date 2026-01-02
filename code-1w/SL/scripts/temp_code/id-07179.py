import math

# Simulated sensor data and calibration parameters
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.7]
humidity_readings = [45, 47, 50, 44, 52, 48, 46, 51]
pressure_readings = [1013, 1012, 1015, 1010, 1014, 1016, 1009, 1011]

# Irrelevant baseline metrics (distractor)
baseline_metrics = {
    'voltage': [3.3, 3.4, 3.35, 3.38],
    'current': [0.2, 0.21, 0.19, 0.22],
    'frequency': 50
}

# Signal configuration (mixed relevant and irrelevant)
signal_config = {
    'amplification': 2.5,
    'noise_threshold': 1.8,
    'sampling_rate': 1000,
    'filter_enabled': True,
    'debug_mode': False
}

# Misleading intermediate transformation (dead path)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [math.log(abs(x - mean_val) + 1) for x in data]

# Unused recursive function (red herring)
def calculate_entropy_recursive(lst, depth=0):
    if depth > 3 or len(lst) == 1:
        return 0.0
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    return math.log(len(lst)) + calculate_entropy_recursive(left, depth+1)

# Real processing begins here
raw_signal = [t * (h / 10) for t, h in zip(temperature_readings, humidity_readings)]

# Apply amplification but only if filter is enabled (relevant)
if signal_config['filter_enabled']:
    amplified_signal = [val * signal_config['amplification'] for val in raw_signal]
else:
    amplified_signal = raw_signal

# Slice only the central portion of interest
trimmed_signal = amplified_signal[2:6]

# Introduce bit manipulation decoy (irrelevant)
decoys = []
for i in range(4):
    decoy_val = (i << 3) | 7  # Bit shift and OR (not used later)
    decoys.append(decoy_val * 0.1)

# Compute moving average window (distraction)
window_size = 2
moving_averages = [
    sum(trimmed_signal[i:i+window_size]) / window_size
    for i in range(len(trimmed_signal) - window_size + 1)
]

# Actual critical transformation
processed_data = []
for x in trimmed_signal:
    if x > signal_config['noise_threshold']:
        processed_data.append(math.sin(x) * math.sqrt(x))
    else:
        processed_data.append(math.cos(x) ** 2)

# Dictionary-based state tracker (partially relevant)
status_flags = {
    'stable': len([x for x in processed_data if x > 1.0]) < 2,
    'noisy': False,
    'calibrated': True
}

# Another red-herring function that's defined but not used
def validate_checksum(data):
    checksum = 0
    for d in data:
        checksum ^= int(d * 10)  # Bitwise XOR
    return checksum % 7 == 0

# Real analysis function
def analyze_signal(signal_list):
    # Nested logic with slicing and dictionary use
    summary_stats = {
        'count': len(signal_list),
        'peak': max(signal_list),
        'trough': min(signal_list)
    }
    
    # Multi-step inference
    adjusted_values = [v * 1.5 for v in signal_list]
    squared_devs = [(v - sum(adjusted_values)/len(adjusted_values))**2 for v in adjusted_values]
    
    # Use of slicing to isolate middle two elements
    mid_vals = adjusted_values[1:3]
    
    # Final computation chain
    base_score = sum(mid_vals)
    penalty = 0
    if summary_stats['peak'] > 2.0:
        penalty += 0.5
    if summary_stats['trough'] < 0.5:
        penalty += 0.3
    
    # Key formula
    diagnostic_value = (base_score * math.pi) / (1 + penalty)
    
    # Dead branch (never taken due to data)
    if status_flags['noisy'] and signal_config['debug_mode']:
        diagnostic_value *= 0.1  # This does not execute
    
    return diagnostic_value

# Execute main logic
temp_snapshot = temperature_readings[-3:]
hum_snapshot = humidity_readings[1::2]

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

# Output result
print(f"Result: {final_diagnostic}")