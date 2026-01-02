import math

# Simulated sensor diagnostics for a thermal regulation system
def analyze_temperature_profile(raw_readings):
    smoothed = []
    for i in range(1, len(raw_readings) - 1):
        smoothed.append(sum(raw_readings[i-1:i+2]) / 3)
    return [round(x, 2) for x in smoothed]

# Irrelevant helper - dead code path (distractor)
def legacy_calibrate(x):
    return (x * 0.97) + 3.2

# Core processing function with meaningful computation
def compute_stability_index(seq):
    if len(seq) < 2:
        return 0.0
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return round(math.sqrt(sum(d ** 2 for d in diffs) / len(diffs)), 4)

# Misleading auxiliary function (looks important but unused in final path)
def assess_outlier_score(data):
    mean_val = sum(data) / len(data)
    outliers = [x for x in data if abs(x - mean_val) > 2 * (sum((d - mean_val)**2 for d in data) / len(data))**0.5]
    return len(outliers)

# Central aggregation logic
def aggregate_phase_data(phases):
    results = {}
    for idx, p in enumerate(phases):
        key_metric = compute_stability_index(p)
        # Decoy assignment - not used later
        temp_flag = key_metric > 1.5
        results[f'phase_{idx}'] = {
            'index': key_metric,
            'status': 'stable' if key_metric < 1.0 else 'volatile'
        }
    return results

# Main diagnostic processor
def process_metrics(logs, limits):
    # Step 1: Extract valid segments
    filtered_logs = [x for x in logs if 15 <= x <= 85]
    
    # Step 2: Smooth and analyze
    profile = analyze_temperature_profile(filtered_logs + [70, 72, 71])  # Extended for edge handling
    
    # Step 3: Compute primary index
    stability = compute_stability_index(profile)
    
    # Step 4: Simulate phase segmentation (irrelevant structure)
    segmented = [profile[:4], profile[4:8], profile[8:]]
    phase_analysis = aggregate_phase_data(segmented)
    
    # Step 5: Apply threshold logic (key step)
    critical_count = sum(1 for p in phase_analysis.values() if p['index'] >= limits['critical'])
    warning_count = sum(1 for p in phase_analysis.values() if limits['warning'] <= p['index'] < limits['critical'])
    
    # Step 6: Generate composite score (uses lambda - required feature)
    scorer = lambda c, w: 10 * c + 5 * w
    raw_score = scorer(critical_count, warning_count)
    
    # Step 7: Apply nonlinear correction using string-based switch (distractor pattern)
    method_flag = 'quadratic'
    if method_flag in ['linear', 'quadratic', 'exponential']:
        if method_flag == 'quadratic':
            adjusted = raw_score ** 2
        elif method_flag == 'exponential':
            adjusted = raw_score ** 3
        else:
            adjusted = raw_score
    else:
        adjusted = raw_score
    
    # Step 8: Final normalization with rounding (answer depends on this)
    normalized = round(adjusted / (stability + 1e-8), 4)
    
    # Step 9: Red herring - complex bit manipulation (unused)
    decoy_value = 0
    for i, val in enumerate([normalized, stability, raw_score]):
        shifted = int(val * 100) << 2
        masked = shifted & 0xFF
        decoy_value ^= masked
    
    # Step 10: Final diagnostic output (this is the target)
    final_diagnostic = int(normalized) + 1000
    
    # Print required result format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Auxiliary data transformation (distractor)
def prepare_input_stream(records):
    indexed = list(enumerate(records))
    paired = list(zip([r[1] for r in indexed[::2]], [r[1] for r in indexed[1::2]]))
    flattened = [item for pair in paired for item in pair]
    return flattened

# Real input data
sensor_data = [20, 22, 23, 25, 30, 45, 55, 60, 62, 61, 59, 58, 60, 63, 65, 70, 72, 71, 73, 72]
config_thresholds = {'warning': 0.8, 'critical': 1.2}

# String processing distraction (required feature)
data_tags = ['T1', 'T2', 'T3']
valid_tags = [t for t in data_tags if t.startswith('T') and len(t) == 2 and t.endswith('1')]

# Actual execution flow
processed_profile = analyze_temperature_profile(sensor_data)
diagnostics = prepare_input_stream([(i, v) for i, v in enumerate(sensor_data)])
final_diagnostic = process_metrics(diagnostics, config_thresholds)