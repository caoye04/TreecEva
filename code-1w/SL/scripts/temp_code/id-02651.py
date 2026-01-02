def sensor_calibration(raw_values):
    calibrated = []
    offset = 0.87
    gain = 1.03
    temp_cache = []
    
    for val in raw_values:
        if val < 0:
            val = abs(val)
        adjusted = (val * gain) + offset
        calibrated.append(round(adjusted, 4))
        
    # Irrelevant transformation path (dead logic)
    if len(calibrated) > 10:
        temp_cache = [x * 0.95 for x in calibrated if x > 5]
    else:
        temp_cache = [x + 1.1 for x in calibrated if x < 3]
    
    scaling_factor = sum(calibrated) / len(calibrated) if calibrated else 1
    normalized = [round(x / scaling_factor, 4) for x in calibrated]
    
    return normalized


def filter_anomalies(data_stream):
    cleaned = []
    outlier_count = 0
    window_size = 3
    
    for i in range(len(data_stream)):
        start = max(0, i - window_size)
        end = min(i + window_size + 1, len(data_stream))
        local_window = data_stream[start:end]
        
        mean_val = sum(local_window) / len(local_window)
        deviation = abs(data_stream[i] - mean_val)
        
        if deviation > 2.5:
            outlier_count += 1
            continue
        else:
            cleaned.append(data_stream[i])
    
    # Distractor: unused statistical metrics
    if cleaned:
        variance = sum((x - sum(cleaned)/len(cleaned))**2 for x in cleaned) / len(cleaned)
        peak_noise_ratio = max(cleaned) / (sum(cleaned) + 1e-8)
    
    return cleaned


def compute_entropy(sequence):
    from math import log2
    freq_map = {}
    total = len(sequence)
    
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    
    entropy = 0.0
    for count in freq_map.values():
        prob = count / total
        entropy -= prob * log2(prob)
    
    return round(entropy, 4)


def analyze_readings(data, threshold):
    diagnostics = []n    critical_flags = 0
    base_score = 100
    adjustment = 0
    
    # Real processing path
    for reading in data:
        if reading > threshold:
            adjustment += 5
            status = 'ELEVATED'
        elif reading < threshold * 0.5:
            adjustment -= 3
            status = 'LOW'
        else:
            adjustment += 1
            status = 'NORMAL'
            
        # String method used as part of meaningful but slightly distracting formatting
        status_code = status.lower().replace('elevated', 'high').upper()
        diagnostics.append({
            'value': reading,
            'status': status_code,
            'flagged': 'HIGH' in status_code
        })
        
        if 'HIGH' in status_code:
            critical_flags += 1
    
    # Decoy calculation with misleading intermediate result
    if critical_flags > 0:
        phantom_risk = (critical_flags / len(data)) * 1000
        dummy_offset = phantom_risk % 7
        base_score -= int(dummy_offset)
    
    # Actual answer derivation
    final_score = base_score + adjustment - critical_flags
    
    # Multiple returns — only one is logically reachable
    if len(diagnostics) == 0:
        return 0
    else:
        return final_score

# Main execution flow
raw_sensor_data = [0.12, -0.34, 0.56, 0.78, 1.21, 2.33, 4.55, 6.77, 8.99, 0.05, 1.11]

# Step 1: Calibration (relevant)
baseline_corrected = sensor_calibration(raw_sensor_data)

# Step 2: Anomaly filtering (relevant)
filtered_readings = filter_anomalies(baseline_corrected)

# Step 3: Entropy analysis (distractor - not used later)
entropy_metric = compute_entropy([round(x, 2) for x in filtered_readings])
decision_entropy = entropy_metric * 100

# Step 4: Prepare for analysis (relevant)
processed_data = [round(x, 3) for x in filtered_readings if x > 0.1]

# Step 5: Threshold logic (relevant)
thresh_reference = 'THRESH_75'
threshold_lookup = {'THRESH_75': 1.75, 'THRESH_50': 1.5}
thresh_value_str = thresh_reference.replace('THRESH_', '').replace('_', '.')
threshold = threshold_lookup[thresh_reference]

# Step 6: Final diagnostic computation (target)
final_diagnostic = analyze_readings(processed_data, threshold)

# Print result
print(f"Result: {final_diagnostic}")