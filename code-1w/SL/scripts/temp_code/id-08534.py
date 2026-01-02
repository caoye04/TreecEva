def analyze_system_performance(raw_data, threshold_config):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in raw_data if x > 0]
    filtered = [x for x in normalized if x < 1000]
    baseline_adjustment = sum(filtered) / len(filtered) if filtered else 0

    # Red herring function
    def calibrate_sensor(x):
        return (x ** 0.5) * 2.3  # Unused later

    # Actual relevant logic starts here
    log_entries = []
    for idx, val in enumerate(raw_data):
        if val > threshold_config['warning_level']:
            status_flag = 1 << 3
            # Bit manipulation and conditional expression mix
            category = 'CRITICAL' if val > threshold_config['critical_level'] else 'WARNING'
            log_entries.append((idx, val, category, status_flag))

    # Decoy data structure
    audit_trail = {}
    for i in range(len(raw_data) + 5):
        audit_trail[i] = f"log_segment_{i % 7}"
    # Dead code path
    if len(audit_trail) > 100:
        del audit_trail[0]

    # Key processing with lambda and zip
    indices, values, categories, flags = zip(*log_entries) if log_entries else ([], [], [], [])
    
    # Complex transformation chain
    severity_map = {'WARNING': 1, 'CRITICAL': 3}
    weighted_scores = list(map(lambda c, v: severity_map[c] * (v // 100), categories, values))
    
    # Distractor: unused accumulator
    temp_accumulator = 0
    for w in weighted_scores:
        temp_accumulator += w * 0.95

    # Real computation path
    def process_metrics(entries, tresh):
        total_risk = 0
        decay_factor = 0.8
        for i, (idx, val, cat, flag) in enumerate(entries):
            # Nested conditionals and arithmetic
            base_score = val / 100.0
            if cat == 'CRITICAL':
                base_score *= 2.5
            if idx % 2 == 1:
                base_score *= 1.2
            adjustment = decay_factor ** i
            total_risk += base_score * adjustment
            # Bitwise interference (irrelevant)
            flag ^= (flag << 2) & 0xFF
        # Min/max smoothing
        final_penalty = max(min(total_risk, 450), 100)
        return int(final_penalty) + len(entries)

    # Misleading intermediate
    preliminary_diagnostic = sum(weighted_scores) * 10

    # Critical execution point
    final_diagnostic = process_metrics(log_entries, system_threshold)

    # Unused complex list comprehension
    anomaly_report = [
        f"Anomaly at {i}: {v} ({c})" 
        for i, v, c, f in log_entries 
        if 'CRITICAL' in c and v > 500
    ]

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate input
system_threshold = {'warning_level': 300, 'critical_level': 450}
data_stream = [200, 320, 460, 150, 480, 310, 500]

# Execute
result = analyze_system_performance(data_stream, system_threshold)