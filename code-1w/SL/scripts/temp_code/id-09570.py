from collections import defaultdict, Counter

# Simulated sensor data and system parameters
sensor_data = [1048, 2067, 3045, 1052, 2065, 3044, 1049, 2068, 3043, 1050, 2069, 3042]
threshold = 1050
baseline_offset = 50
scaling_factor = 0.95
diagnostic_mode = 'deep'

# Irrelevant auxiliary data (distractor)
user_preferences = {'theme': 'dark', 'auto_save': True, 'refresh_rate': 60}
temp_cache = [x ** 0.5 for x in range(100, 110)]
metadata_index = {'version': '2.1.0', 'build': 4521}

# Unused function (dead code path - distractor)
def legacy_calibrate(data):
    return [int(x * 0.8) for x in data if x > 2000]

# Another decoy transformation (misleading intermediate result)
shadow_copy = [x + baseline_offset for x in sensor_data]
avg_shadow = sum(shadow_copy) / len(shadow_copy)
adjusted_avg = avg_shadow * scaling_factor  # Looks important but unused

# Real processing begins here

# Filter anomalies based on threshold (relevant logic)
def filter_anomalies(data, limit):
    above_threshold = [x for x in data if x > limit]
    count_per_prefix = defaultdict(int)
    for val in above_threshold:
        prefix = val // 1000  # Extract sensor group (1xxx, 2xxx, 3xxx)
        count_per_prefix[prefix] += 1
    return dict(count_per_prefix)

# Diagnostic processor with bit manipulation twist (relevant)
def encode_diagnostic(code, level):
    if level == 'critical':
        return (code << 2) | 3
    elif level == 'warning':
        return (code << 2) | 2
    else:
        return (code << 2) | 1

# Complex processing with list comprehension and counter (relevant)
def process_readings(filtered_counts, log_buffer):
    # Simulate diagnostic signature generation
    signatures = []
    total_anomalies = sum(filtered_counts.values())
    
    # Bit manipulation and arithmetic combo
    for sensor_id, count in filtered_counts.items():
        base_sig = sensor_id * 100 + count
        encoded = encode_diagnostic(base_sig, 'warning')
        signatures.append(encoded)
    
    # Use of Counter for aggregation (relevant)
    sig_counter = Counter(signatures)
    primary_sig = max(sig_counter, default=0)
    
    # Final computation with character counting red herring (distractor below)
    mode_chars = ''.join([diagnostic_mode])
    char_count = len(mode_chars)  # Distraction: looks like it should matter
    
    # Actual final computation (non-obvious due to noise)
    result = primary_sig - (total_anomalies * char_count) + 100
    
    # Dead branch - never executed (distractor)
    if len(user_preferences) > 10:
        result *= 2
        
    return result

# Unused statistical summary (misleading intermediate)
stat_summary = {
    'max': max(sensor_data),
    'min': min(sensor_data),
    'range': max(sensor_data) - min(sensor_data)
}

# Key execution point
filtered_results = filter_anomalies(sensor_data, threshold)
diagnostics_log = []  # Unused placeholder (distractor)
final_diagnostic = process_readings(filtered_results, diagnostics_log)

# Output the required result
print(f"Result: {final_diagnostic}")