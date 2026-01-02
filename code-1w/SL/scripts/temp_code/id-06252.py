from collections import defaultdict, Counter

# Simulate sensor readings with some noise and validity flags
def preprocess_sensor_data(raw_readings):
    processed = []
    temp_stats = defaultdict(int)
    for reading in raw_readings:
        value, timestamp, sensor_id, valid = reading
        if not valid:
            continue
        normalized = (value ** 0.5) * 1.05
        temp_stats[sensor_id] += 1
        if normalized > 50:
            normalized = 50 + (normalized - 50) / 2  # compress high values
        processed.append((normalized, timestamp, sensor_id))
    
    # Distractor computation: analyze timestamp gaps (not used later)
    sorted_times = sorted([r[1] for r in raw_readings])
    gaps = [t2 - t1 for t1, t2 in zip(sorted_times, sorted_times[1:])]
    avg_gap = sum(gaps) / len(gaps) if gaps else 0
    gap_variance = sum((g - avg_gap) ** 2 for g in gaps) / len(gaps) if gaps else 0

    return processed

# Identify anomalies based on frequency and magnitude
def detect_anomalies(data):
    counts = Counter()
    magnitudes = []
    for val, _, sid in data:
        counts[sid] += 1
        magnitudes.append(val)
    
    # Thresholds for anomaly (somewhat arbitrary)
    freq_threshold = 3
    magnitude_threshold = 40
    
    rare_sensors = [sid for sid, cnt in counts.items() if cnt < freq_threshold]
    large_values = [val for val in magnitudes if val > magnitude_threshold]
    
    # Misleading intermediate: compute correlation-like metric (unused)
    if len(rare_sensors) > 0 and len(large_values) > 0:
        pseudo_correlation = (len(rare_sensors) * len(large_values)) / (sum(magnitudes) + 1)
    else:
        pseudo_correlation = 0
    
    return len(rare_sensors), len(large_values)

# Main scoring logic
def calculate_final_score(data, thresholds):
    base_score = 0
    adjustment = 0.0
    
    # Unpack thresholds
    min_valid, max_penalty, boost_factor = thresholds
    
    # Track per-sensor contribution
    sensor_contributions = defaultdict(float)
    total_entries = len(data)
    
    for val, ts, sid in data:
        contrib = val * 0.8
        sensor_contributions[sid] += contrib
        
        # Apply time-based decay (simulated via XOR manipulation of timestamp)
        time_flag = (ts ^ 2023) & 1  # alternate every other second
        if time_flag:
            contrib *= 0.95
        
        base_score += int(contrib)
        
    # Additional logic path that influences adjustment
    if total_entries > min_valid:
        adjustment = (total_entries - min_valid) * boost_factor
    else:
        adjustment = -max_penalty
    
    # Distractor block: analyze contribution distribution (not used in final score)
    contrib_values = list(sensor_contributions.values())
    mean_contrib = sum(contrib_values) / len(contrib_values) if contrib_values else 0
    variance = sum((x - mean_contrib) ** 2 for x in contrib_values) / len(contrib_values) if contrib_values else 0
    peak_contrib = max(contrib_values) if contrib_values else 0
    
    # Another red herring: simulate false dependency
    checksum = 0
    for val, _, _ in data:
        checksum ^= int(val)
    checksum %= 100
    
    final_score = base_score + int(adjustment)
    return final_score

# Generate synthetic input
def main():
    raw_data = [
        (121.0, 1001, 'S1', True),
        (256.0, 1002, 'S2', True),
        (81.0,  1003, 'S1', True),
        (361.0, 1004, 'S3', False),  # invalid
        (144.0, 1005, 'S2', True),
        (64.0,  1006, 'S4', True),
        (169.0, 1007, 'S4', True),
        (400.0, 1008, 'S5', True)
    ]
    
    thresholds = (5, 100, 3.5)  # min_valid, max_penalty, boost_factor
    
    cleaned = preprocess_sensor_data(raw_data)
    anomaly_counts = detect_anomalies(cleaned)
    
    # Key statement
    final_score = calculate_final_score(cleaned, thresholds)
    
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()