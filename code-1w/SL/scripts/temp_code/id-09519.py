from itertools import combinations, chain

# Sensor calibration and diagnostic simulation
sensor_ids = [101, 102, 103, 104, 105]
base_offsets = {sid: (sid % 7) * 0.1 for sid in sensor_ids}
raw_readings = {
    101: [23.5, 24.1, 22.8, 25.0, 23.9],
    102: [19.3, 18.9, 20.1, 19.7, 19.0],
    103: [31.2, 32.0, 30.8, 31.5, 31.0],
    104: [45.6, 44.9, 46.2, 45.3, 45.8],
    105: [12.4, 13.1, 12.7, 12.9, 13.0]
}

# Irrelevant signal processing path (dead code)
def analyze_frequency(signal):
    fft_components = []
    for i in range(len(signal)):
        component = 0
        for j in range(len(signal)):
            component += signal[j] * (i * j % 3)
        fft_components.append(component % 100)
    return fft_components

# Unused transformation function
def normalize_logscale(data_list):
    import math
    return [math.log(x + 1) for x in data_list if x > 0]

# Distractor: historical metadata (not used)
historical_max = {101: 26.5, 102: 21.0, 103: 33.0, 104: 48.0, 105: 14.5}
historical_min = {101: 20.0, 102: 17.5, 103: 29.0, 104: 40.0, 105: 10.0}

# Simulated environmental interference factors
interference_mask = [0.98, 1.02, 0.99, 1.01, 1.00]
temp_compensation = lambda t: t * (1 + (25 - t) * 0.002)

# Real processing begins here
adjusted_readings = {}
for sid, readings in raw_readings.items():
    adjusted = [temp_compensation(r + base_offsets[sid]) for r in readings]
    adjusted_readings[sid] = adjusted

# Bitwise flag simulation for sensor health (some bits irrelevant)
sensor_health_flags = {}
for sid in sensor_ids:
    raw_flag = (sid << 2) ^ 0b1010
    parity = bin(raw_flag).count('1') % 2
    health_word = (raw_flag << 1) | parity
    sensor_health_flags[sid] = health_word

# Misleading aggregation path
aggregated_stats = {}
for sid, vals in adjusted_readings.items():
    mean_val = sum(vals) / len(vals)
    variance = sum((v - mean_val) ** 2 for v in vals) / len(vals)
    aggregated_stats[sid] = {'mean': mean_val, 'var': variance}

# Threshold map based on dynamic criteria (only some are used later)
thresh_scale = 1.25
critical_thresholds = {sid: 30.0 * thresh_scale if sid in [103, 104] else 20.0 * thresh_scale for sid in sensor_ids}
thresh_map = {sid: critical_thresholds[sid] * 0.9 for sid in sensor_ids}

# Filtering logic with red herring combination generation
all_combinations = list(combinations(sensor_ids, 3))
filtered_data = {}
for sid, values in adjusted_readings.items():
    # Only sensors above health flag threshold 400 are fully trusted
    if sensor_health_flags[sid] > 400:
        filtered_data[sid] = [v for v in values if v < thresh_map[sid]]
    else:
        # Less reliable sensors require tighter filtering
        cutoff = thresh_map[sid] * 0.95
        filtered_data[sid] = [v for v in values if v < cutoff]

# Decoy statistical analysis
effective_lengths = [len(v) for v in filtered_data.values()]
length_combinations = list(combinations(effective_lengths, 2))

# Real final processing function
def process_readings(data_dict, thresholds):
    total_anomalies = 0
    cumulative_score = 0
    
    # Complex interdependent logic
    for sensor_id, clean_vals in data_dict.items():
        expected_base = 20.0 if sensor_id < 103 else 30.0
        offset_correction = base_offsets[sensor_id]
        
        # Simulate bit-aware anomaly detection
        flagged_bits = 0
        for val in clean_vals:
            int_part = int(val)
            fractional_bit = int((val - int_part) * 10) & 0b111
            if (int_part ^ fractional_bit) & 0b101:
                flagged_bits += 1
        
        # Actual anomaly count based on value drift
        drift_count = 0
        for v in clean_vals:
            if abs(v - expected_base - offset_correction) > 2.0:
                drift_count += 1
        
        # Weighted contribution
        if sensor_id in [104, 105]:
            weight = 1.5
        else:
            weight = 1.0
        
        # Cross-sensor dependency via XOR of IDs
        dependency_key = 0
        for other_id in data_dict.keys():
            if other_id != sensor_id:
                dependency_key ^= (other_id & sensor_id)
        
        adjustment_factor = (dependency_key % 5) * 0.1
        total_anomalies += drift_count * weight + adjustment_factor
        
        # Cumulative score uses ignored aggregated_stats pattern
        local_sum = sum(clean_vals)
        cumulative_score += local_sum * (1 + adjustment_factor)
    
    # Final diagnostic is a derived integer from complex state
    final_state = int(cumulative_score / (total_anomalies + 1)) ^ int(sum(thresholds.values()) / 10)
    return final_state

# Execute key statement
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")