from collections import defaultdict, Counter

# Simulated sensor array data from environmental monitoring station
def collect_sensor_data():
    raw_readings = [
        (101, 'temp', 23.5), (102, 'humidity', 65), (103, 'co2', 410),
        (104, 'temp', 24.1), (105, 'light', 800), (106, 'humidity', 67),
        (107, 'co2', 425), (108, 'temp', 22.9), (109, 'co2', 405),
        (110, 'pressure', 1013), (111, 'temp', 25.3), (112, 'humidity', 70)
    ]
    return raw_readings

# Irrelevant helper - simulates GPS triangulation (unused in final logic)
def calculate_coverage_area(sensors):
    area = 0
    for i in range(len(sensors)):
        for j in range(i+1, len(sensors)):
            x1, y1 = sensors[i][0] % 10, sensors[i][0] // 10
            x2, y2 = sensors[j][0] % 10, sensors[j][0] // 10
            area += ((x2-x1)**2 + (y2-y1)**2)**0.5
    return round(area, 2)

# Misleading preprocessing path - appears useful but not used
def legacy_normalization(data_list):
    norm_map = {}
    for item in data_list:
        sensor_id, param, val = item
        if param not in norm_map:
            norm_map[param] = []
        norm_map[param].append(val * 0.95 if param == 'co2' else val)
    return {k: sum(v)/len(v) for k, v in norm_map.items()}

# Core processing with distractors
def filter_anomalies(raw_data):
    # Distractor variables
    anomaly_log = []
    debug_stats = defaultdict(int)
    temporal_gaps = []
    
    # Real filtering logic
    readings_by_type = defaultdict(list)
    for sid, param, val in raw_data:
        readings_by_type[param].append((sid, val))
        debug_stats['total'] += 1  # red herring counter
    
    # Simulate time-series gap detection (unused)
    sensor_ids = sorted([r[0] for r in raw_data])
    for i in range(1, len(sensor_ids)):
        if sensor_ids[i] - sensor_ids[i-1] > 5:
            temporal_gaps.append((sensor_ids[i-1], sensor_ids[i]))
    
    # Actual relevant filtering: remove outliers more than 1.5*IQR
    filtered = []
    for param, records in readings_by_type.items():
        values = [v for _, v in records]
        q1, q3 = sorted(values)[len(values)//4], sorted(values)[3*len(values)//4]
        iqr = q3 - q1
        lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
        for sid, val in records:
            if lower <= val <= upper:
                filtered.append((sid, param, val))
    
    # Dead code path: simulation of decay factor adjustment
    if len(temporal_gaps) > 3:
        for i in range(len(filtered)):
            _, p, v = filtered[i]
            if p == 'temp':
                filtered[i] = (_, p, v * 0.98)
    
    return filtered

# Main processing function
def generate_threshold_template(measurements):
    # Complex but partially irrelevant setup
    template = defaultdict(lambda: {'base': 0, 'tolerance': 0})
    count_dist = Counter(param for _, param, _ in measurements)
    
    # Real threshold logic
    for param in count_dist:
        if param == 'temp':
            template[param]['base'] = 24.0
            template[param]['tolerance'] = 2.0
        elif param == 'humidity':
            template[param]['base'] = 66
            template[param]['tolerance'] = 5
        elif param == 'co2':
            template[param]['base'] = 410
            template[param]['tolerance'] = 15
        else:
            template[param]['base'] = 900
            template[param]['tolerance'] = 200
    
    # Distractor: unused spatial weighting
    weights = {}
    for sid, param, val in measurements:
        sector = sid // 10
        weights[sector] = weights.get(sector, 0) + 1
    normalized_weights = {k: v/sum(weights.values()) for k, v in weights.items()}
    
    return dict(template)

# Final diagnostic engine
def process_readings(data, thresholds):
    # Multi-step diagnostic with red herrings
    diagnostics = []
    status_flags = []
    cumulative_score = 0
    
    # Complex enumeration with zip - actual signal extraction
    params = list(set(param for _, param, _ in data))
    baselines = [thresholds[p]['base'] for p in params]
    tolerances = [thresholds[p]['tolerance'] for p in params]
    
    for (param, base), tol in zip(zip(params, baselines), tolerances):
        values = [v for _, p, v in data if p == param]
        avg_val = sum(values) / len(values)
        deviation = abs(avg_val - base)
        
        # Critical decision logic
        if deviation <= tol:
            flag = 1
            score_delta = 10
        elif deviation <= tol * 1.5:
            flag = 2
            score_delta = 5
        else:
            flag = 3
            score_delta = 2
        
        diagnostics.append({
            'param': param,
            'deviation': deviation,
            'flag': flag
        })
        status_flags.append(flag)
        cumulative_score += score_delta
    
    # Distractor: unused correlation analysis
    if len(diagnostics) > 2:
        ordered = sorted(diagnostics, key=lambda x: x['deviation'])
        mid_idx = len(ordered) // 2
        pivot = ordered[mid_idx]['deviation']
        high_corr = sum(1 for d in ordered if abs(d['deviation'] - pivot) < 0.5)
    
    # Final computation - this is the real answer source
    weighted_sum = 0
    for df, sf in zip(diagnostics, status_flags):
        weighted_sum += df['deviation'] * sf
    
    # The actual answer
    final_diagnostic = int(cumulative_score * (weighted_sum / (len(diagnostics) or 1)))
    
    # Dead code - looks important but unused
    if all(sf == 1 for sf in status_flags):
        final_diagnostic = int(final_diagnostic * 0.8)
    elif any(sf == 3 for sf in status_flags):
        final_diagnostic = int(final_diagnostic * 1.15)
    
    return final_diagnostic

# Execution workflow
if __name__ == '__main__':
    # Step 1: Collect raw sensor data
    sensor_data = collect_sensor_data()
    
    # Step 2: Apply anomaly filtering (real path)
    filtered_data = filter_anomalies(sensor_data)
    
    # Step 3: Generate threshold map (real path)
    threshold_map = generate_threshold_template(filtered_data)
    
    # Step 4: Compute final diagnostic score (target point)
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")