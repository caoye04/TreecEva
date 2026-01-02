from collections import defaultdict, Counter

# Simulated sensor data with noise and irrelevant entries
def collect_diagnostics():
    raw_signals = [
        (1, 'temp', 98.6), (2, 'hr', 72), (3, 'spo2', 97),
        (4, 'temp', 99.1), (5, 'hr', 75), (6, 'spo2', 96),
        (7, 'temp', 101.3), (8, 'hr', 88), (9, 'spo2', 92),
        (10, 'temp', 97.8), (11, 'hr', 70), (12, 'spo2', 98)
    ]

    # Irrelevant transformation: mapping to hex codes (dead path)
    signal_hex = {i: hex(int(val)) for i, typ, val in raw_signals if typ == 'temp'}

    # Distractor: unused statistical summary
    temp_vals = [val for _, typ, val in raw_signals if typ == 'temp']
    hr_vals = [val for _, typ, val in raw_signals if typ == 'hr']
    spo2_vals = [val for _, typ, val in raw_signals if typ == 'spo2']
    avg_temp = sum(temp_vals) / len(temp_vals)
    median_hr = sorted(hr_vals)[len(hr_vals)//2]
    mode_spo2 = Counter(spo2_vals).most_common(1)[0][0]

    # Actual processing begins: categorize by type
    readings = defaultdict(list)
    for seq_id, r_type, value in raw_signals:
        readings[r_type].append((seq_id, value))

    # Misleading filter: excludes based on arbitrary sequence rules (not used later)
    filtered_by_seq = {
        k: [(sid, v) for sid, v in vs if sid % 2 == 1] 
        for k, vs in readings.items()
    }

    # Key filter: only high-temp readings above threshold
    high_fever = [v for sid, v in readings['temp'] if v > 100.0]
    fever_count = len(high_fever)

    # Decoy calculation: entropy-like metric (unused)
    import math
    if fever_count > 0:
        p_fever = fever_count / len(readings['temp'])
        entropy = -p_fever * math.log(p_fever) if p_fever > 0 else 0

    # Real logic: prepare data for processing
    critical_flags = []
    for r_type, records in readings.items():
        for seq_id, value in records:
            if r_type == 'temp' and value >= 100.4:
                critical_flags.append((seq_id, 'fever_alert'))
            elif r_type == 'hr' and value > 85:
                critical_flags.append((seq_id, 'tachycardia'))
            elif r_type == 'spo2' and value < 95:
                critical_flags.append((seq_id, 'hypoxia'))

    # Build threshold map (used later)
    threshold_map = {
        'temp': (99.5, 104.0),
        'hr': (60, 100),
        'spo2': (95, 100)
    }

    # Filtered data: only keep entries that are flagged or abnormal
    filtered_data = []
    for r_type, records in readings.items():
        low_t, high_t = threshold_map[r_type]
        for seq_id, value in records:
            if value < low_t or value > high_t:
                filtered_data.append((r_type, seq_id, value))

    # Another red herring: correlation attempt between hr and temp (unused)
    temp_dict = {sid: v for sid, v in readings['temp']}
    hr_dict = {sid: v for sid, v in readings['hr']}
    temp_hr_corr = []
    for sid in temp_dict:
        if sid in hr_dict:
            temp_hr_corr.append((temp_dict[sid] - avg_temp) * (hr_dict[sid] - median_hr))

    # Core processing function
    def process_readings(data, thresholds):
        score = 0
        type_count = defaultdict(int)
        
        for dtype, sid, val in data:
            min_val, max_val = thresholds[dtype]
            if dtype == 'temp':
                if val > max_val:
                    score += 3
                elif val < min_val:
                    score -= 1
            elif dtype == 'hr':
                deviation = abs(val - 75)  # baseline normal
                if deviation > 25:
                    score += 2
                type_count['hr_anomaly'] += 1
            elif dtype == 'spo2':
                if val < min_val:
                    score += round(5 * (min_val - val) / 5, 1)  # penalty per point below
                
        # Bonus logic: if multiple anomaly types, add interaction term
        if len(type_count) >= 2:
            score += 4
            
        # Final adjustment based on total entries (distraction: capped)
        entry_count = len(data)
        if entry_count > 5:
            score += 1  # small compensation
            
        return int(score * 100)  # scale for precision

    # Execution point of interest
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Dead code: serialization mockup
    export_format = 'json'
    if export_format == 'xml':
        payload = "<data></data>"
    elif export_format == 'csv':
        payload = "seq_id,type,value\n"

    # Print result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute and capture
result = collect_diagnostics()