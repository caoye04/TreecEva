from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic analysis
def analyze_sensor_network(raw_readings, calibration_factor):
    # Irrelevant preprocessing: normalize timestamps (unused later)
    normalized_times = [(t - raw_readings[0][0]) * 1.0 for t, _ in raw_readings]
    
    # Misleading aggregation: average per second (not used in final logic)
    second_bins = defaultdict(list)
    for timestamp, value in raw_readings:
        second_bins[int(timestamp)].append(value)
    avg_per_second = {sec: sum(vals)/len(vals) for sec, vals in second_bins.items()}

    # Distractor: detect spikes above 95 (never actually contributes to result)
    spike_moments = []
    for i in range(1, len(raw_readings)-1):
        if raw_readings[i][1] > 95 and raw_readings[i-1][1] < raw_readings[i][1] > raw_readings[i+1][1]:
            spike_moments.append(i)

    # Relevant path begins: filter valid readings below critical threshold
    valid_readings = [(t, v) for t, v in raw_readings if v < 88.5]
    
    # Apply calibration (red herring operation - only some values are actually used)
    calibrated = [(t, round(v * calibration_factor, 3)) for t, v in valid_readings]
    
    # Group by integer second (partially relevant, but only one group matters)
    grouped = defaultdict(list)
    for t, v in calibrated:
        grouped[int(t)].append(v)
    
    # Decoy statistical analysis (never used)
    stats_summary = {}
    for sec, vals in grouped.items():
        mean_val = sum(vals) / len(vals)
        variance = sum((x - mean_val)**2 for x in vals) / len(vals)
        stats_summary[sec] = {'mean': mean_val, 'variance': variance, 'count': len(vals)}
    
    # Key transformation: identify anomalous seconds based on value count
    anomaly_flags = {}
    for sec, vals in grouped.items():
        anomaly_flags[sec] = len(vals) > 3 and sum(vals) > 150
    
    # Hidden rule: only second 137 has both >3 entries and sum > 150 in this dataset
    filtered_data = grouped[137] if anomaly_flags.get(137) else [0]
    
    # Threshold configuration map (some keys are decoys)
    threshold_map = {
        'critical': 45.0,
        'warning': 30.0,
        'info': 10.0,  # unused
        'debug': 1.0   # unused
    }
    
    # Real computation hidden among distractions
    def process_readings(data_list, thresholds):
        total = sum(data_list)
        level = 'unknown'
        if total > thresholds['critical']:
            level = 'critical'
        elif total > thresholds['warning']:
            level = 'warning'
        else:
            level = 'normal'
        
        # Final diagnostic code: hash-based encoding of level + total
        code_map = {'critical': 500, 'warning': 250, 'normal': 100}
        return code_map[level] + round(total, 2)
    
    # Dead function: never called, adds confusion
    calculate_entropy = lambda data: sum(-v*__import__('math').log2(v) for v in data if v > 0)
    
    # Unused counter of reading patterns (distractor)
    pattern_counter = Counter(f'{int(v)}' for _, v in calibrated)
    
    # The actual key statement
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Additional red herring: transform filtered data in unused way
    transformed = list(map(lambda x: x * 2 - 1, filtered_data))
    
    return final_diagnostic

# Simulated input: sensor readings over time
readings = [
    (135.0, 87.2), (135.5, 86.1), (136.2, 87.9), (136.4, 86.7), (136.6, 85.3),
    (137.1, 40.5), (137.3, 41.2), (137.4, 42.8), (137.6, 43.1), (137.8, 44.3),
    (138.0, 87.7), (138.2, 86.9), (139.1, 88.1), (139.5, 87.4)
]

result = analyze_sensor_network(readings, calibration_factor=1.02)
print(f"Result: {result}")