import math

# Simulated sensor data processing system
def collect_sensor_readings():
    raw_values = [3.1, 4.7, 2.8, 5.5, 6.3, 1.9, 7.2, 8.0, 0.5]
    scaling_factor = 1.8
    adjusted = [v * scaling_factor for v in raw_values]
    return adjusted

# Irrelevant helper - distractor
def smooth_data(signal):
    if len(signal) < 3:
        return signal
    smoothed = [signal[0]]
    for i in range(1, len(signal) - 1):
        smoothed.append((signal[i-1] + signal[i] + signal[i+1]) / 3)
    smoothed.append(signal[-1])
    return smoothed  # Never used

# Redundant transformation - misleading path
def transform_magnitude(x):
    if x < 4:
        return int(math.log(x + 1) * 2)
    else:
        return int(x ** 0.5)

# Unused recursive function - dead code path
def recursive_peak_detect(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr[0]
    return max(arr[n-1], recursive_peak_detect(arr, n-1))

# Real processing begins here
raw_data = collect_sensor_readings()
filtered_data = [x for x in raw_data if x > 2.5]  # Filter noise

# Distractor: complex but unused data structure
stats_summary = {
    'count': len(filtered_data),
    'mean': sum(filtered_data) / len(filtered_data),
    'variance': sum((x - sum(filtered_data)/len(filtered_data))**2 for x in filtered_data) / len(filtered_data),
    'max_val': max(filtered_data),
    'min_val': min(filtered_data)
}

# Slicing operation - relevant
window_slice = filtered_data[1:-1]  # Exclude edge values

# Another irrelevant string-based computation - red herring
status_flags = ['OK', 'ERROR', 'WARNING']
data_status = ''.join([flag[0] for flag in status_flags])  # Yields 'OEW'
hash_value = sum(ord(c) for c in data_status)  # 79+69+87 = 235, unused

# Dictionary mapping - actually used later
threshold_map = {
    'low': 3.0,
    'medium': 5.0,
    'high': 7.0
}

# Complex conditional logic with nesting
processed_data = []
for val in window_slice:
    category = 'unknown'
    if val < threshold_map['medium']:
        if val < threshold_map['low']:
            category = 'low'
        else:
            category = 'medium'
    else:
        if val > threshold_map['high']:
            category = 'critical'
        else:
            category = 'high'
    
    # Bit manipulation decoy
    shift_key = len(category) << 1  # e.g., 4<<1 = 8, not used
    mask = 0b1101 & int(val)  # bitwise AND, result ignored
    
    # Actual transformation
    normalized = round(val / (len(category) + 1), 3)
    processed_data.append(normalized)

# Decoy function call - never executed
if False:
    anomaly_score = recursive_peak_detect(processed_data)

# Real analysis function with multiple concepts
def analyze_signal(signal, thresholds):
    # String method used idiomatically
    debug_tag = "DIAGNOSTIC_RUN_2024".lower().replace('_', '-')  # 'diagnostic-run-2024'
    tag_sum = sum(ord(c) for c in debug_tag if c.isdigit())  # Only digits: '2','0','2','4' -> 50+48+50+52=200
    
    # Set usage - filtering unique categories
    magnitude_levels = set()
    for x in signal:
        if x < 3.0:
            magnitude_levels.add('minor')
        elif x < 5.0:
            magnitude_levels.add('moderate')
        else:
            magnitude_levels.add('severe')
    
    # Recursive reduction - real use
    def reduce_energy(seq, index=0):
        if index >= len(seq):
            return 0.0
        current_energy = seq[index] ** 2
        return current_energy + reduce_energy(seq, index + 1)
    
    total_energy = reduce_energy(signal)
    level_count = len(magnitude_levels)
    
    # Final computation - this is the answer
    diagnostic_code = int(total_energy * level_count + tag_sum)
    
    # Multiple assignments - distractor
    final_status, error_id, timestamp = 'FINALIZED', hash_value, 1717536000
    return diagnostic_code

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")