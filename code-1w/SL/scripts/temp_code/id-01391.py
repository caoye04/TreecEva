def analyze_readings(readings):
    cumulative = 0
    trend_flags = []
    for i, val in enumerate(readings):
        if val > 75:
            cumulative += val * 0.1
            trend_flags.append(i)
    return cumulative, set(trend_flags)

# Irrelevant auxiliary function (decoy)
def validate_sequence(seq):
    if len(seq) < 5:
        return False
    sorted_seq = sorted(seq)
    return all(sorted_seq[i] <= sorted_seq[i+1] for i in range(len(sorted_seq)-1))

# Unused transformation (dead code path)
transform_log = lambda x: [item * 1.5 for item in x if item > 0]

# Core data processing pipeline
def compute_baseline(signal):
    base = sum(signal) / len(signal)
    adjusted = [s - base for s in signal]
    return base, adjusted

def detect_anomalies(series, limit):
    anomalies = []
    for idx, point in enumerate(series):
        if abs(point) > limit:
            anomalies.append((idx, round(point, 3)))
    return anomalies

def process_metrics(data, config):
    # Step 1: Compute baseline and adjust
    raw_values = [d[1] for d in data]
    base_ref, corrected = compute_baseline(raw_values)
    
    # Step 2: Analyze high-value readings
    _, flagged_indices = analyze_readings(raw_values)
    
    # Step 3: Detect deviations in corrected signal
    deviants = detect_anomalies(corrected, config['tolerance'])
    
    # Step 4: Cross-reference with configuration zones
    zone_match = 0
    for d in data:
        loc = d[0]
        val = d[1]
        if loc in config['regions'] and val > config['threshold']:
            zone_match += 1
    
    # Step 5: Use zip to align indices and values for secondary check
    index_map = list(zip(range(len(raw_values)), raw_values))
    activation_score = sum(1 for i, v in index_map if v > config['threshold'] * 1.2)
    
    # Step 6: Apply conditional weighting
    weight = 2 if len(flagged_indices) > 2 else 1
    deviation_penalty = len(deviants) * 0.75
    
    # Step 7: Final diagnostic computation
    preliminary = (base_ref + activation_score) * weight - deviation_penalty
    
    # Distractor variables (irrelevant computations)
    shadow_metric = sum([x**2 for x in corrected]) / len(corrected)  # unused
    entropy_estimate = len(deviants) / len(raw_values) if raw_values else 0  # unused
    audit_trace = {i: v for i, v in enumerate(corrected) if v > 0}  # unused
    
    # Step 8: Final adjustment based on zone match
    final_diagnostic = int(preliminary + zone_match * 1.5)
    
    return final_diagnostic

# Input data
health_data = [
    ('north', 68),
    ('south', 85),
    ('east', 90),
    ('west', 70),
    ('north', 95),
    ('south', 50)
]

thresholds = {
    'tolerance': 12.0,
    'threshold': 70,
    'regions': ['north', 'east', 'south']
}

# Execution point
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")