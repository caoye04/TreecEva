from collections import defaultdict, Counter

# Simulated sensor data processing system
def collect_diagnostics():
    raw_samples = [145, 178, 132, 164, 189, 125, 141, 173]
    calibration_factor = 0.91
    offset_adjustment = 12
    
    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for i in range(len(raw_samples)):
        if i == 0:
            smoothed.append(raw_samples[i])
        else:
            smoothed.append(int(0.7 * raw_samples[i] + 0.3 * smoothed[i-1]))
    
    # Core transformation (relevant)
    adjusted_samples = [int(x * calibration_factor) + offset_adjustment for x in raw_samples]
    
    # Decoy frequency analysis (red herring)
    frequency_map = defaultdict(int)
    for val in raw_samples:
        frequency_map[val // 10] += 1
    
    # Actual threshold logic preparation
    mode_stats = Counter(adjusted_samples)
    dominant_value = mode_stats.most_common(1)[0][1]
    
    # Misleading anomaly detection (dead path)
    anomalies = []
    for idx, val in enumerate(raw_samples):
        if abs(val - smoothed[idx]) > 30:
            anomalies.append(idx)
    
    # Threshold bands setup (relevant)
    thresholds = {
        'low': 130,
        'high': 160,
        'critical': 175
    }
    
    # Sensor fusion simulation (partially relevant)
    sensor_data = {}
    for i, val in enumerate(adjusted_samples):
        sensor_id = f'sensor_{i % 4}'
        if sensor_id not in sensor_data:
            sensor_data[sensor_id] = []
        sensor_data[sensor_id].append(val)
    
    # Dummy aggregation (distraction)
    aggregated_averages = {}
    for k, v in sensor_data.items():
        aggregated_averages[k] = sum(v) / len(v)
    
    # Unused outlier removal (decoy function effect)
    def remove_outliers(data, factor=1.5):
        q1 = sorted(data)[len(data)//4]
        q3 = sorted(data)[3*len(data)//4]
        iqr = q3 - q1
        return [x for x in data if q1 - factor*iqr <= x <= q3 + factor*iqr]
    
    # Critical processing function
    def process_readings(readings_dict, limits):
        flat_vals = []
        for readings in readings_dict.values():
            flat_vals.extend(readings)
        
        # Real logic: count how many values are in high-risk zone
        high_count = 0
        critical_count = 0
        for v in flat_vals:
            if limits['high'] < v <= limits['critical']:
                high_count += 1
            if v > limits['critical']:
                critical_count += 1
        
        # Secondary distraction: unused statistical moment
        variance_proxy = sum((x - 150) ** 2 for x in flat_vals) // len(flat_vals)
        
        # Real diagnostic calculation
        risk_multiplier = 1.75 if critical_count > 0 else 1.0
        base_score = (high_count * 8) + (critical_count * 22)
        final_risk = int(base_score * risk_multiplier)
        
        # Tertiary decoy: bit manipulation on irrelevant metric
        debug_flag = 0
        for v in flat_vals:
            debug_flag ^= (v & 15) << 2
        
        return final_risk
    
    # Execute main logic
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Unrelated post-processing (distractor block)
    report_summary = []
    for k in sorted(aggregated_averages.keys()):
        band = 'unknown'
        avg_val = aggregated_averages[k]
        if avg_val < 140:
            band = 'A'
        elif avg_val < 155:
            band = 'B'
        else:
            band = 'C'
        report_summary.append(f'{k}:{band}')
    
    # Final print (required output format)
    print(f"Result: {final_diagnostic}")
    
    # Unused cryptographic hash mockup (heavy red herring)
    def pseudo_hash(data_list):
        acc = 17
        for num in data_list:
            acc = (acc * 31 + num) % 987654
        return acc
    
    return final_diagnostic

if __name__ == '__main__':
    collect_diagnostics()