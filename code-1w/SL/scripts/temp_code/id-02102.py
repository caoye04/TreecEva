import math

# Simulated sensor array data with noise and calibration offsets
data_stream = [145, 178, 203, 129, 255, 98, 167, 201, 113, 188]
calibration_map = {'offset': 12, 'gain': 0.85, 'threshold': 150}

# Irrelevant preprocessing: unused transformation chain
buffer_cache = list(map(lambda x: (x + 5) ** 0.5, data_stream))
shadow_buffer = [x for x in buffer_cache if x > 10]
rolling_avg = sum(buffer_cache[3:7]) / 4  # Dead computation

# Core signal processing pipeline
filtered_data = []
for val in data_stream:
    corrected = (val - calibration_map['offset']) * calibration_map['gain']
    if corrected >= calibration_map['threshold']:
        corrected = calibration_map['threshold'] + (corrected - calibration_map['threshold']) * 0.6
    filtered_data.append(round(corrected))

# Data enhancement via bit manipulation (amplify significant bits)
enhanced_data = []
for val in filtered_data:
    transformed = val ^ 25  # XOR mask to normalize sensitivity
    transformed = (transformed << 1) & 255  # Left shift and clamp
    enhanced_data.append(min(transformed, 255))

# Decoy function: appears important but unused
def analyze_pattern(seq):
    return sum(x * (i+1) for i, x in enumerate(seq)) // len(seq)

# Destructuring configuration parameters
def process_config(params):
    offset = params.get('offset')
    gain = params.get('gain')
    thresh = params.get('threshold')
    mode_flag = params.get('mode', 'standard')
    return (offset, gain, thresh), mode_flag

config_values, _ = process_config(calibration_map)

# Real-time normalization using set operations to deduplicate transient spikes
unique_readings = list(set(enhanced_data))
sorted_readings = sorted(unique_readings, reverse=True)

# Spurious sorting and filtering path (dead branch)
deviation_pool = []
if len(sorted_readings) > 5:
    mean_val = sum(sorted_readings[:5]) / 5
    deviation_pool = [abs(x - mean_val) for x in sorted_readings[:5]]

# Critical transformation: apply dynamic scaling based on distribution spread
spread = sorted_readings[0] - sorted_readings[-1] if sorted_readings else 0
dynamic_factor = 1.0 + (spread / 100.0)

transformed_data = []
for val in enhanced_data:
    scaled = val * dynamic_factor
    if scaled > 200:
        scaled = 200 + math.log(scaled - 199)  # Soft ceiling
    transformed_data.append(round(scaled, 2))

# Secondary decoy: unused anomaly detection
anomaly_flags = []
window_size = 3
for i in range(len(transformed_data) - window_size + 1):
    window = transformed_data[i:i+window_size]
    if max(window) - min(window) > 50:
        anomaly_flags.append(i)

# Main diagnostic processor combining multiple logic paths
def process_metrics(data_list, cfg):
    base_threshold = cfg['threshold'] * 0.8
    high_count = sum(1 for x in data_list if x > base_threshold)
    low_count = len(data_list) - high_count
    
    # Boolean logic cascade with short-circuiting
    if high_count > low_count and base_threshold > 0:
        if spread < 80 or dynamic_factor < 1.2:
            score = high_count * 12.5
        else:
            score = (high_count * 10) + (len(data_list) // 2)
    else:
        score = low_count * 5
    
    # Final adjustment using lambda-weighted average
    weights = list(map(lambda w: w / sum(data_list), data_list))
    weighted_avg = sum(data_list[i] * weights[i] for i in range(len(data_list)))
    
    # Determine final diagnostic level
    if score >= 50 and weighted_avg > 100:
        result = int(score * (weighted_avg / 150))
    elif score >= 30:
        result = int(score * 1.2)
    else:
        result = 10
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(transformed_data, calibration_map)

# Red herring output (unused)
temp_snapshot = { 'data': tuple(transformed_data), 'meta': 'diagnostic_mode' }
summary_code = hash(temp_snapshot['meta']) % 1000

# Correct output
print(f"Target result: {final_diagnostic}")