import itertools

# Simulated sensor array data from environmental monitoring station
def collect_sensor_data():
    raw_readings = [14.3, 15.1, 13.9, 16.2, 15.5, 14.8, 13.7, 16.0]
    calibration_offset = 0.8
    adjusted = [r + calibration_offset for r in raw_readings]
    return adjusted

# Signal processing: filter and normalize
def process_signals(data):
    filtered = [x for x in data if 14.0 <= x <= 16.0]  # Remove outliers
    mean_val = sum(filtered) / len(filtered)
    normalized = [round((x - mean_val) * 10) / 10 for x in filtered]
    
    # Irrelevant transformation (distractor)
    inverted = [1.0 / (1 + x) for x in normalized if x != 0]
    shadow_copy = inverted[:]
    
    # Dummy sorting with no impact
    dummy_sorted = sorted(shadow_copy, reverse=True)
    
    return normalized

# Secondary analysis chain (mostly dead code path)
def legacy_diagnostic(seq):
    if len(seq) < 5:
        return sum(seq) * 0.1
    else:
        temp = 0
        for i in range(len(seq)):
            if i % 2 == 0:
                temp += seq[i] * 1.5
            else:
                temp -= seq[i] * 0.7
        return temp * 0.3  # Never actually used

# Core diagnostic logic
def compute_stability_index(seq):
    diffs = [abs(seq[i] - seq[i+1]) for i in range(len(seq)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return round(100 * (1 - avg_diff / 2.0), 4)

# Advanced pattern detection using itertools
def detect_cyclic_patterns(seq):
    window_size = 3
    triplets = list(itertools.pairwise(itertools.accumulate([0]*window_size + seq)))
    cyclic_score = 0
    for t in triplets:
        if len(set(t)) == len(t):  # All distinct
            cyclic_score += 1
    return cyclic_score

# Final analysis combining multiple metrics
def analyze_readings(processed_signals):
    base_index = compute_stability_index(processed_signals)
    
    # Red herring computation
    phantom_metric = sum([x**2 for x in processed_signals]) / (base_index + 1e-8)
    adjustment_factor = 0.9 if phantom_metric > 50 else 1.1
    
    # Unused intermediate calculations
    mirrored = processed_signals[::-1]
    correlation_proxy = sum(a*b for a,b in zip(processed_signals, mirrored))
    
    # Real signal: detect subtle patterns
    pattern_strength = detect_cyclic_patterns(processed_signals)
    
    # Final formula (only this matters)
    final_diagnostic = int(base_index * 10 + pattern_strength)
    
    # Dead code branch (never reached due to prior assignment)
    if False:
        fallback = legacy_diagnostic(processed_signals)
        final_diagnostic = int(fallback)
    
    return final_diagnostic

# Execution flow
sensor_data = collect_sensor_data()
processed_signals = process_signals(sensor_data)
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")