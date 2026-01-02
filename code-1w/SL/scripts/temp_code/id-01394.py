def process_turbine_readings(raw_samples):
    # Irrelevant preprocessing: Normalize sensor IDs (not used in final logic)
    sensor_ids = [s % 127 for s in range(90, 100)]
    normalized = {sid: idx for idx, sid in enumerate(sensor_ids)}

    # Distractor: Frequency correction map (unused)
    freq_correction = dict(zip(sensor_ids, [1.0 + (i * 0.02) for i in range(len(sensor_ids))]))

    # Core transformation: Extract valid power readings above noise floor
    valid_readings = []
    noise_floor = 15.5
    for sample in raw_samples:
        timestamp, readings = sample[0], sample[1]
        if timestamp % 2 == 0:  # Only even timestamps contribute
            filtered = [r for r in readings if r > noise_floor]
            valid_readings.extend(filtered)

    # Distractor: Simulate backup buffer (never accessed later)
    backup_buffer = [v * 0.98 for v in valid_readings[::-1]]
    checksum = sum(backup_buffer) % 1000

    # Real processing path: categorize by magnitude bands
    bands = {'low': [], 'medium': [], 'high': []}
    for v in valid_readings:
        if v < 30:
            bands['low'].append(v)
        elif v < 70:
            bands['medium'].append(v)
        else:
            bands['high'].append(v)

    # Compute band statistics (only medium is actually used later)
    stats = {}
    for key, vals in bands.items():
        if vals:
            avg_val = sum(vals) / len(vals)
            peak = max(vals)
            count = len(vals)
            stats[key] = {'average': avg_val, 'peak': peak, 'count': count}
        else:
            stats[key] = {'average': 0, 'peak': 0, 'count': 0}

    return stats


def detect_anomalies(signal_chain):
    # Dead function: uses XOR pattern analysis (no impact on output)
    anomalies = 0
    for i in range(1, len(signal_chain)):
        delta = signal_chain[i] ^ signal_chain[i-1]
        if bin(delta).count('1') > 3:
            anomalies += 1
    return anomalies  # Never called


def aggregate_metrics(data_source, config_map):
    # Misleading parameter: config_map has unused fields
    baseline = config_map.get('baseline', 25)
    window_size = config_map.get('window', 5)  # Unused
    sensitivity = config_map.get('sensitivity', 1.5)  # Unused

    # Real computation begins
    processed = process_turbine_readings(data_source)

    # Only 'medium' band average is used
    medium_avg = processed['medium']['average']
    medium_count = processed['medium']['count']

    # Red herring: entropy calculation based on counts (not used)
    total = sum(processed[b]['count'] for b in processed)
    entropy = 0
    if total > 0:
        from math import log2
        for b in processed:
            p = processed[b]['count'] / total
            if p > 0:
                entropy -= p * log2(p)

    # Critical logic chain
    score = medium_avg * medium_count
    adjustment_factor = 1.0
    if medium_count > 10:
        adjustment_factor = 0.85
    elif medium_count > 5:
        adjustment_factor = 0.92
    else:
        adjustment_factor = 1.1

    # Apply bitwise tweak based on score's parity
    if int(score) & 1:
        score = score * 1.05
    else:
        score = score * 0.98

    # Final transformation
    diagnostic_value = round(score * adjustment_factor, 4)

    # Decoy assignment
    temp_result = diagnostic_value + 1000

    return diagnostic_value

# Simulated turbine sensor data: (timestamp, [power_readings...])
turbine_data = [
    (0, [12, 18, 22, 35, 45, 75]),
    (1, [14, 20, 28]),
    (2, [16, 24, 30, 40, 50, 60, 80]),
    (3, [19, 26]),
    (4, [17, 23, 33, 44, 55, 65]),
    (5, [21]),
    (6, [15, 25, 31, 41, 51, 61, 71]),
    (7, [13])
]

# Configuration with decoy entries
threshold_map = {
    'baseline': 20,
    'window': 7,
    'sensitivity': 2.0,
    'calibration': 'auto',  # unused
    'version': 'v3.1'         # unused
}

# Key execution point
final_diagnostic = aggregate_metrics(turbine_data, threshold_map)
print(f"Target result: {final_diagnostic}")