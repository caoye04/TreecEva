import math

# Simulated sensor data with noise and redundant readings
temperature_readings = [23.4, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9]
humidity_readings = [45, 48, 50, 55, 60, 58, 52]
pressure_readings = [1013, 1012, 1015, 1010, 1008, 1014, 1016]  # Irrelevant for final score

# Misleading preprocessing: unused transformation
def apply_kalman_filter(data):
    smoothed = []
    for i in range(len(data)):
        if i == 0:
            smoothed.append(data[i])
        else:
            smoothed.append(0.8 * data[i] + 0.2 * smoothed[i-1])
    return smoothed

# Distractor function that is never called
def calculate_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Redundant normalization (some used, some not)
def normalize_minmax(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def normalize_zscore(data):
    mean = sum(data) / len(data)
    std = (sum((x - mean)**2 for x in data) / len(data)) ** 0.5
    return [(x - mean) / std for x in data]  # Computed but unused

# Weight mapping – only some keys matter
weights = {
    'temp': 0.6,
    'humidity': 0.4,
    'pressure': 0.0,  # Explicitly ignored
    'noise_floor': 0.1  # Unused
}

# Simulated calibration offset (distractor)
calibration_matrix = [[1.01, -0.02], [0.03, 0.99]]

# Main processing pipeline
data = {
    'raw_temp': temperature_readings,
    'raw_humid': humidity_readings,
    'timestamp_count': len(temperature_readings)
}

# Step 1: Filter valid range entries (distraction: pressure skipped)
valid_indices = [i for i in range(len(temperature_readings)) if temperature_readings[i] > 23.0]
filtered_temp = [temperature_readings[i] for i in valid_indices]
filtered_humid = [humidity_readings[i] for i in valid_indices]

# Step 2: Normalize relevant inputs
norm_temp = normalize_minmax(filtered_temp)
norm_humid = normalize_minmax(filtered_humid)

# Step 3: Apply weighted fusion using lambda and conditional logic
fusion_rule = lambda t, h: t * weights['temp'] + h * weights['humidity'] if t + h > 1.0 else 0.5
fused_values = [fusion_rule(t, h) for t, h in zip(norm_temp, norm_humid)]

# Step 4: Aggregate with outlier rejection
trimmed = [x for x in fused_values if 0.2 <= x <= 0.9]
avg_fused = sum(trimmed) / len(trimmed) if trimmed else 0.0

# Step 5: Adjust based on system health (dummy check)
system_uptime = 97  # Percent
health_boost = 1.1 if system_uptime > 95 else 1.0
adjusted_score = avg_fused * health_boost

# Step 6: Apply non-linear boost using string-based condition (python idiom)
mode_flag = 'high_precision'
boost_factor = 1.25 if 'high' in mode_flag else 1.0
enhanced_score = adjusted_score * boost_factor

# Step 7: Final scaling with rounding to nearest 0.001
final_score = round(enhanced_score * 1000) / 1000

# Irrelevant data structure transformations below
record_log = []
for i, val in enumerate(fused_values):
    record_log.append({
        'seq': i,
        'value': val,
        'status': 'OK' if val > 0.3 else 'LOW',
        'meta': f"LOG_{str(i+1).zfill(2)}"
    })

# Unused sorting operation (distractor)
sorted_logs = sorted(record_log, key=lambda x: x['value'], reverse=True)

# Another decoy: character counting in status flags
count_ok = sum(1 for entry in record_log if entry['status'] == 'OK')
flag_chars = sum(len(entry['meta']) for entry in record_log)

# Critical statement
final_score = process_results(data, weights)

# Dummy function to mislead control flow analysis
def process_results(sensor_data, config):
    raw_t = sensor_data['raw_temp']
    raw_h = sensor_data['raw_humid']
    n = sensor_data['timestamp_count']
    
    # Re-calculate filtered set using list comprehension and conditional expression
    filtered_pairs = [
        (raw_t[i], raw_h[i]) 
        for i in range(n) 
        if 22.5 < raw_t[i] < 26.0 and raw_h[i] < 60
    ]
    
    # Extract and normalize again (redundant but correct path)
    temps = [pair[0] for pair in filtered_pairs]
    humids = [pair[1] for pair in filtered_pairs]
    
    # Use of string method to determine processing mode
    mode_str = "Calibration Mode Active"
    use_extended = 'Extended' in mode_str.upper()  # False
    
    # Normalization using min-max (same as before)
    min_t, max_t = min(temps), max(temps)
    min_h, max_h = min(humids), max(humids)
    
    normalized_t = [(t - min_t) / (max_t - min_t) for t in temps] if max_t != min_t else [0.5] * len(temps)
    normalized_h = [(h - min_h) / (max_h - min_h) for h in humids] if max_h != min_h else [0.5] * len(humids)
    
    # Weighted combination using config weights
    combined = [
        nt * config['temp'] + nh * config['humidity']
        for nt, nh in zip(normalized_t, normalized_h)
    ]
    
    # Trim outliers (values below 0.1 or above 0.95)
    cleaned = [c for c in combined if 0.1 <= c <= 0.95]
    
    # Compute mean
    mean_clean = sum(cleaned) / len(cleaned) if cleaned else 0.0
    
    # Apply uptime and mode boosts (same as earlier path)
    boosted = mean_clean * (1.1 if system_uptime > 95 else 1.0)
    boosted *= (1.25 if 'high' in mode_flag else 1.0)
    
    # Final rounding
    result = round(boosted * 1000) / 1000
    
    # Dead code branch (never reached due to return)
    if len(cleaned) > 100:
        fallback = sum(normalized_t) / len(normalized_t)
        result = fallback * 0.5
    
    return result

print(f"Target result: {final_score}")