from collections import defaultdict, Counter

# Simulated sensor data ingestion pipeline
def ingest_sensor_stream():
    raw_stream = [
        (1001, [23.4, 24.1, -999, 25.6, 26.0]),
        (1002, [18.5, -999, 19.0, -999, 20.1]),
        (1003, [30.2, 29.8, 31.0, -999, 32.1]),
        (1004, [-999, 35.6, 36.0, 35.8, -999])
    ]
    return raw_stream

# Legacy function - unused but looks relevant
def legacy_calibrate(x):
    return [val * 0.98 + 0.5 for val in x if val > 0]

# Irrelevant transformation chain
def transform_sequence(seq):
    a = [x ** 0.5 for x in seq if x > 0]
    b = [y * 2 for y in a]
    c = sum(b) / len(b) if b else 0
    return [round(z - c, 2) for z in b]

# Decoy statistical analysis
def compute_magnitude(data):
    total = 0
    count = 0
    for _, readings in data:
        for r in readings:
            if r > 0:
                total += r ** 2
                count += 1
    return int((total / count) ** 0.5) if count else 0

# Real processing begins here
def clean_readings(readings_list):
    cleaned = []
    for sensor_id, readings in readings_list:
        valid = [r for r in readings if r != -999]
        avg = sum(valid) / len(valid) if valid else 0
        cleaned.append((sensor_id, valid, avg))
    return cleaned

def filter_by_stability(dataset):
    stable_set = []
    for sid, vals, mean in dataset:
        variance = sum((v - mean) ** 2 for v in vals) / len(vals) if vals else 0
        if variance <= 1.5 and len(vals) >= 3:
            stable_set.append((sid, vals, mean, variance))
    return stable_set

def generate_threshold_map(sensors):
    # Complex-looking but partially irrelevant mapping
    base_map = defaultdict(lambda: (20.0, 35.0))
    priority_offsets = {'high': 5.0, 'medium': 2.5, 'low': 0}
    
    # Dummy classification logic with red herring
    classifications = {}
    for s_id, _, avg, _ in sensors:
        if avg > 30:
            classifications[s_id] = 'high'
        elif avg > 25:
            classifications[s_id] = 'medium'
        else:
            classifications[s_id] = 'low'
    
    # Actual threshold adjustment
    for s_id, _, avg, _ in sensors:
        offset = priority_offsets[classifications[s_id]]
        base_map[s_id] = (20.0, 30.0 + offset)  # Upper bound adjusted
    
    return base_map, classifications  # Only map is used later

def process_readings(stable_data, thresholds):
    results = []
    spike_count = 0
    
    for s_id, vals, avg, var in stable_data:
        low_t, high_t = thresholds[s_id]
        # Count how many readings exceed dynamic threshold
        flagged = [v for v in vals if v > high_t]
        spike_count += len(flagged)
        score = len(flagged) * 100 // len(vals) if vals else 0
        results.append({'id': s_id, 'anomalies': len(flagged), 'severity': score})
    
    # Secondary distraction: entropy-like calculation
    entropy_proxy = 0
    if spike_count > 0:
        distribution = [r['anomalies'] for r in results]
        freqs = Counter(distribution)
        entropy_proxy = sum(-(f/len(results)) * (f/len(results)) for f in freqs.values())
    
    # Final diagnostic is based on total anomaly-adjusted mean
    total_adjusted = 0
    total_weight = 0
    for _, vals, avg, _ in stable_data:
        penalty = 1 + (sum(1 for v in vals if v > thresholds[1][1]) * 0.1)
        total_adjusted += avg / penalty
        total_weight += 1 / penalty
    
    final_diagnostic = int((total_adjusted / total_weight) * 100) if total_weight else 0
    return final_diagnostic

# Orchestration with misleading intermediate steps
if __name__ == '__main__':
    # Step 1: Ingest raw data
    stream = ingest_sensor_stream()
    
    # Step 2: Clean and compute averages (relevant)
    cleaned_dataset = clean_readings(stream)
    
    # Step 3: Filter stable sensors (relevant)
    stable_sensors = filter_by_stability(cleaned_dataset)
    
    # Step 4: Generate threshold map (partially relevant)
    threshold_map, category_map = generate_threshold_map(stable_sensors)
    
    # Step 5: Compute irrelevant magnitude metric (distractor)
    magnitude_score = compute_magnitude(stream)
    
    # Step 6: Transform data using obsolete method (dead path)
    transformed_diagnostics = []
    for _, readings, _ in cleaned_dataset:
        if readings:
            transformed_diagnostics.append(transform_sequence(readings))
    
    # Step 7: Main analysis (critical execution point)
    final_diagnostic = process_readings(stable_sensors, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")