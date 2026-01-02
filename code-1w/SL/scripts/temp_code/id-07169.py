def analyze_performance(log, thresh):
    # Irrelevant transformation (distractor)
    normalized = [x * 0.95 for x in log if x > 10]
    filtered = [x for x in log if x >= thresh]
    
    # Misleading intermediate calculation (red herring)
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    anomaly_count = 0
    for i, val in enumerate(log):
        if val < 0:
            anomaly_count += 1
    
    # Dead code path - never executed due to logic (decoy)
    if anomaly_count > 100:
        return -999

    # Real logic starts here: count transitions above/below threshold
    cross_count = 0
    for i in range(1, len(log)):
        if (log[i-1] < thresh <= log[i]) or (log[i-1] > thresh >= log[i]):
            cross_count += 1

    # Use of zip to pair consecutive elements (relevant)
    trend_pairs = list(zip(log, log[1:]))
    increasing_trends = sum(1 for a, b in trend_pairs if b > a + 2)

    # Secondary distraction: complex but unused bitwise analysis
    bit_analysis = 0
    for x in log[:5]:
        bit_analysis ^= (x & 31) | (x >> 3)

    # Conditional expression with slicing (relevant to final result)
    base_score = sum(filtered) / len(filtered) if filtered else 0
    adjustment = increasing_trends * 0.75 if cross_count > 4 else -1.25
    
    # Key assignment - this is where the answer is determined
    efficiency_score = base_score + adjustment

    # Unused recursive side-path (distraction)
    def recursive_dip_detect(data, idx=0, dips=0):
        if idx >= len(data) - 1:
            return dips
        return recursive_dip_detect(data, idx + 1, dips + (1 if data[idx] > data[idx+1] else 0))
    
    # Final irrelevant dictionary construction (noise)
    summary = {
        'total': len(log),
        'anomalies': anomaly_count,
        'first_peak': max(log) if log else 0,
        'bit_metric': bit_analysis
    }

    return efficiency_score

# Main execution context
sensor_readings = [12, 15, 14, 18, 16, 20, 22, 19, 24, 25]
config_threshold = 17

# Unused alternate data sets (red herring variables)
data_backup_a = [8, 11, 13, 16, 15]
data_backup_b = [21, 23, 20, 22, 26]

# Critical statement that produces the target variable
efficiency_score = analyze_performance(sensor_readings, config_threshold)

# Output result as required
print(f"Result: {efficiency_score}")