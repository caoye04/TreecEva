import math

# Simulated sensor network diagnostics with noise filtering and anomaly detection
def collect_sensor_data():
    raw_readings = [14.2, 18.7, 22.5, 19.3, 16.8, 25.1, 20.0, 17.9]
    timestamps = [100, 101, 102, 103, 104, 105, 106, 107]
    statuses = ['OK', 'OK', 'FAULT', 'OK', 'OK', 'OK', 'FAULT', 'OK']
    return list(zip(timestamps, raw_readings, statuses))


def filter_noise(data, threshold=1.5):
    filtered = []
    temp_values = [x[1] for x in data if x[2] == 'OK']
    median_val = sorted(temp_values)[len(temp_values)//2]
    for item in data:
        ts, val, stat = item
        if abs(val - median_val) <= threshold or stat == 'FAULT':
            filtered.append(item)
    return filtered

# Irrelevant helper - decoy function
def calculate_compression_ratio(data):
    original = len(str(data))
    compressed = original * 0.65
    return round(compressed / original, 3)

# Data transformation pipeline
def normalize_readings(filtered_data):
    values = [x[1] for x in filtered_data]
    min_v, max_v = min(values), max(values)
    normalized = [(v - min_v) / (max_v - min_v) for v in values]
    return normalized

# Dead code path - never executed but looks relevant
def legacy_calibration(sequence):
    adjusted = []
    for x in sequence:
        adjusted.append(x * 0.98 + 0.5)
    return adjusted

# Bit manipulation for checksum simulation (red herring)
def generate_checksum(value_list):
    chk = 0
    for v in value_list:
        int_val = int(v * 10) % 256
        chk ^= int_val
        chk = (chk << 1 | chk >> 7) & 255
    return chk

# Set-based duplicate detection (actually used)
def detect_anomalies(raw_data):
    seen_values = set()
    duplicates = set()
    for entry in raw_data:
        reading = round(entry[1], 1)
        if reading in seen_values:
            duplicates.add(reading)
        else:
            seen_values.add(reading)
    return duplicates

# Main processing chain
def process_logs(sensor_data):
    # Step 1: Filter out noisy readings
    clean_data = filter_noise(sensor_data)
    
    # Step 2: Normalize the clean values
    norm_vals = normalize_readings(clean_data)
    
    # Step 3: Detect repeated raw values (using set logic)
    anomalies = detect_anomalies(sensor_data)
    
    # Step 4: Create processed log structure
    processed = []
    for i, item in enumerate(clean_data):
        proc_entry = {
            'index': i,
            'timestamp': item[0],
            'raw': item[1],
            'norm': norm_vals[i],
            'status': item[2]
        }
        processed.append(proc_entry)
    
    # Decoy computation - unused result
    compression_metric = calculate_compression_ratio(processed)
    
    # Simulate derived metrics
    derived_scores = []
    for p in processed:
        score = p['norm'] * 100
        if p['status'] == 'FAULT':
            score *= 0.8
        derived_scores.append(round(score, 2))
    
    return {
        'entries': processed,
        'scores': derived_scores,
        'anomalies_detected': len(anomalies),
        'checksum': generate_checksum([x[1] for x in sensor_data])
    }

# Complex analysis with multiple logic branches
def analyze_readings(log_summary):
    entries = log_summary['entries']
    scores = log_summary['scores']
    anomaly_count = log_summary['anomalies_detected']
    
    # Compute quartiles
    sorted_scores = sorted(scores)
    q1_idx = len(sorted_scores) // 4
    q3_idx = 3 * len(sorted_scores) // 4
    q1 = sorted_scores[q1_idx]
    q3 = sorted_scores[q3_idx]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers = [s for s in scores if s < lower_bound or s > upper_bound]
    
    # Bitwise weighting based on anomaly presence
    base_weight = 100
    if anomaly_count > 0:
        base_weight |= 32  # Add flag
    if len(outliers) > 1:
        base_weight ^= 16  # Toggle outlier penalty
    
    # Multiple assignment red herring
    total_norm, valid_count = 0, 0
    for e in entries:
        if e['norm'] > 0.1:
            total_norm += e['norm']
            valid_count += 1
    avg_normalized = total_norm / valid_count if valid_count else 0
    
    # Final diagnostic calculation
    severity_factor = len(outliers) * 10
    stability_score = 100 - severity_factor
    adjustment = (base_weight & 7) * 0.25
    
    # Key statement
    final_diagnostic = int(stability_score - adjustment + (anomaly_count * 5))
    
    # Unused intermediate - misleading
    projected_reliability = round(avg_normalized * stability_score / 100, 3)
    
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    # Initial data collection
    sensor_logs = collect_sensor_data()
    
    # Irrelevant string operation - distractor
    log_id = "SNR-" + "-".join(str(ts) for ts in range(100, 108, 2))
    parts = log_id.split('-')
    merged = ''.join(parts[:2]) + parts[2]
    
    # Processing pipeline
    processed_logs = process_logs(sensor_logs)
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_logs)
    
    print(f"Result: {final_diagnostic}")