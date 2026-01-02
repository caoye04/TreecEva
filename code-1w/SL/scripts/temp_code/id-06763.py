import itertools

# Simulated sensor data processing pipeline for environmental monitoring station
def analyze_readings(readings):
    baseline = 23.7
    adjusted = [r * 1.02 + 0.5 for r in readings]
    anomalies = [i for i, val in enumerate(adjusted) if abs(val - baseline) > 5.0]
    
    # Irrelevant transformation chain (distractor)
    temp_buckets = {i: [] for i in range(5)}
    for v in adjusted:
        bucket = min(int(v // 10), 4)
        temp_buckets[bucket].append(v * 0.98)
    
    # Real computation buried in noise
    valid_data = [v for v in adjusted if v >= 15.0]
    deviation_sum = sum(abs(v - baseline) for v in valid_data)
    
    # Dead code path (never executed due to logic)
    if len(anomalies) > 100:
        smoothed = [sum(adjusted[max(0,i-1):i+2])/len(adjusted[max(0,i-1):i+2]) for i in range(len(adjusted))]
        return sum(smoothed)

    return deviation_sum

# Data validation and grouping utility (partially used)
def validate_and_group(entries):
    valid_groups = {}
    error_log = []
    
    for e in entries:
        group_key = e['site'][:2].upper() + '_' + str(e['sector'])
        
        # Complex filtering with red herring condition
        quality_flag = (e['reading'] > 10 and e['temp'] < 40 and 
                      e['humidity'] >= 30 and 'calibrated' in e.get('flags', []))
        
        if group_key not in valid_groups:
            valid_groups[group_key] = []
            
        if quality_flag or e['reading'] > 100:  # Misleading condition
            valid_groups[group_key].append(e['reading'])
        else:
            error_log.append(f"Invalid: {e['id']}")
    
    # Unused but plausible aggregation
    stats_summary = {
        k: {
            'count': len(v),
            'total': sum(v),
            'outliers': len([x for x in v if x > 90])
        } for k, v in valid_groups.items()
    }
    
    # Actual output used downstream
    return [sum(vals) for vals in valid_groups.values()]

# Core performance model
weights = {'precision': 0.4, 'stability': 0.3, 'coverage': 0.3}

# Heavily obfuscated metric computation with multiple distractions
def compute_stability_metric(signal_trace):
    # Real signal analysis
    diffs = [abs(signal_trace[i+1] - signal_trace[i]) for i in range(len(signal_trace)-1)]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    
    # Distractor: complex frequency analysis (unused)
    freq_components = {}
    for window_size in range(3, 7):
        windows = list(itertools.windowed(signal_trace, window_size))
        freq_components[window_size] = len(windows)
    
    # Another decoy structure
    trend_lines = []
    for i in range(0, len(signal_trace) - 4, 4):
        segment = signal_trace[i:i+4]
        if len(segment) == 4:
            slope = (segment[3] - segment[0]) / 3
            trend_lines.append(slope)
    
    # The actual stability score (buried)
    raw_stability = 100 / (1 + avg_diff) if avg_diff > 0 else 100
    return raw_stability

# Placeholder decorator (irrelevant but looks important)
def audit_step(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@audit_step
def compute_coverage_score(timestamps, duration=3600):
    if not timestamps:
        return 0
    
    # Real logic
    sorted_times = sorted(set(ts % duration for ts in timestamps))
    gaps = [sorted_times[i+1] - sorted_times[i] for i in range(len(sorted_times)-1)]
    if gaps:
        avg_gap = sum(gaps) / len(gaps)
        max_allowed = duration / len(sorted_times)
        coverage_ratio = min(avg_gap / max_allowed, 1.0) if max_allowed else 1.0
    else:
        coverage_ratio = 1.0
    
    # Fake redundancy calculation (dead end)
    redundant_windows = 0
    for combo in itertools.combinations(sorted_times, 2):
        if abs(combo[1] - combo[0]) < 30:
            redundant_windows += 1
    
    return (1 - coverage_ratio) * 100

# Main aggregation function
def aggregate_performance(metrics, w):
    # Metrics come from various sources with noise
    precision = metrics.get('precision', 0)
    stability = metrics.get('stability', 0)
    coverage = metrics.get('coverage', 0)
    
    # Red herring normalization (unused)
    all_vals = [precision, stability, coverage]
    normalized = [(v - min(all_vals)) / (max(all_vals) - min(all_vals) + 1e-8) for v in all_vals]
    
    # Real weighted combination
    weighted_sum = (
        precision * w['precision'] + 
        stability * w['stability'] + 
        coverage * w['coverage']
    )
    
    # Final adjustment based on phantom condition
    adjustment_factor = 1.0
    critical_flags = []
    for key, val in metrics.items():
        if val > 90:
            critical_flags.append(f"HIGH_{key.upper()}")
    
    if len(critical_flags) >= 2:
        adjustment_factor = 0.9
    
    return int(weighted_sum * adjustment_factor)

# Decoy data structures (look relevant but mostly unused)
diagnostic_codes = {
    'A1': 'Signal drift',
    'B4': 'Calibration offset',
    'C7': 'Sensor interference',
    'D9': 'Data saturation'
}

flag_hierarchy = ('basic', 'verified', 'calibrated', 'certified')

# Real input data
sensor_readings = [22.1, 24.3, 23.8, 25.1, 22.9, 23.0, 24.2, 23.7, 23.5, 24.0]
entry_data = [
    {'id': 'S1', 'site': 'north', 'sector': 1, 'reading': 88.2, 'temp': 38, 'humidity': 45, 'flags': ['calibrated']},
    {'id': 'S2', 'site': 'north', 'sector': 2, 'reading': 91.5, 'temp': 36, 'humidity': 50, 'flags': ['calibrated', 'verified']},
    {'id': 'S3', 'site': 'south', 'sector': 1, 'reading': 76.3, 'temp': 42, 'humidity': 28, 'flags': []},
    {'id': 'S4', 'site': 'south', 'sector': 2, 'reading': 85.0, 'temp': 34, 'humidity': 33, 'flags': ['calibrated']}
]
signal_sequence = [102, 105, 103, 104, 106, 108, 107, 105, 104, 103, 105, 107]
time_stamps = [120, 450, 900, 1350, 1800, 2250, 2700, 3150, 3600]

# Execute core computations
base_deviation = analyze_readings(sensor_readings)

# Generate partially used intermediate results
raw_groups = validate_and_group(entry_data)
coverage_input = [len(g) for g in raw_groups]  # Only length matters

stability_input = compute_stability_metric(signal_sequence)
coverage_time_score = compute_coverage_score(time_stamps)

# Build metrics dictionary with irrelevant fields
performance_metrics = {
    'precision': int(base_deviation),           # ~6.12 → 6
    'stability': int(stability_input),          # ~95.2 → 95
    'coverage': int(coverage_time_score),       # ~50.0 → 50
    'redundancy': len(time_stamps) // 3,         # Distractor
    'anomaly_count': len([]),                    # Unused
    'last_updated': '2023-11-05'                 # Noise
}

# Final computation step
final_score = aggregate_performance(performance_metrics, weights)
print(f"Result: {final_score}")