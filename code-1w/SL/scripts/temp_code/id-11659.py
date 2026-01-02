import math

# Simulated biomedical signal processing pipeline
def analyze_waveform(signal):
    if not signal:
        return 0
    magnitude = sum([x ** 2 for x in signal]) ** 0.5
    normalized = [x / magnitude for x in signal if abs(x) > 0.1]
    return len(normalized)

# Irrelevant auxiliary function (dead code path)
def legacy_calibrate(x):
    return (x * 3.7 + 12) % 256

# Core metric processor
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Unused transformation (distractor)
def time_warp(sequence):
    return [sequence[i] for i in range(len(sequence)-1, -1, -1)]

# Main data refinement with red herring logic
def filter_artifacts(raw_readings, window=3):
    cleaned = []
    for i in range(len(raw_readings)):
        start = max(0, i - window)
        local_avg = sum(raw_readings[start:i+1]) / (i - start + 1)
        if abs(raw_readings[i] - local_avg) < 15:  # arbitrary threshold
            cleaned.append(raw_readings[i])
    return cleaned

# Diagnostic engine (key function)
def evaluate_risk_level(biomarkers):
    base_score = 0
    if 'glucose' in biomarkers and biomarkers['glucose'] > 140:
        base_score += 3
    if 'bp_systolic' in biomarkers and biomarkers['bp_systolic'] > 180:
        base_score += 4
    if 'cholesterol' in biomarkers and biomarkers['cholesterol'] > 240:
        base_score += 2
    return base_score

# Primary processing chain
def process_metrics(data, config):
    # Step 1: Extract flat feature array
    flat_features = []
    for key, values in data.items():
        if isinstance(values, list):
            flat_features.extend([x for x in values if x > 0])
        else:
            flat_features.append(abs(values))
    
    # Step 2: Compute derived metrics (some irrelevant)
    avg_val = sum(flat_features) / len(flat_features)
    peak = max(flat_features)
    entropy_metric = compute_entropy([int(x) for x in flat_features])
    waveform_analysis = analyze_waveform(flat_features[:50] if len(flat_features) > 50 else flat_features)
    
    # Distractor variables (not used in final result)
    temp_correction = [math.sin(x / 10) for x in flat_features]
    calibrated_sum = sum(temp_correction) * 1.8
    decay_factor = 0.95 ** len(temp_correction)
    artifact_filtered = filter_artifacts(flat_features)
    
    # Critical conditional logic tree (3-level nesting)
    adjustment = 0
    if config['strict_mode']:
        if entropy_metric > 3.0:
            if waveform_analysis >= 4:
                adjustment = 7
            elif avg_val > 85:
                adjustment = -3
            else:
                adjustment = 2
        else:
            if peak > 200:
                adjustment = 5
    else:
        adjustment = 1
    
    # Secondary decoy calculation (set operations - distractor)
    unique_magnitude = set([int(x) for x in flat_features])
    reference_set = set(range(10, 100, 3))
    overlap_count = len(unique_magnitude & reference_set)
    penalty_shift = len(unique_magnitude - reference_set) // 10
    
    # Final diagnostic formula (depends only on specific path)
    raw_index = int(avg_val // 10) + waveform_analysis
    final_diagnostic = raw_index * 2 + adjustment - penalty_shift  # actual computation
    
    # Dead code branch (never executed due to prior logic)
    if len(unique_magnitude) < 0:  # impossible
        final_diagnostic *= 0.5
    
    return final_diagnostic

# Simulated patient data (real input)
health_data = {
    'heart_rate': [72, 75, 78, 80, 76],
    'glucose_levels': [110, 118, 122, 135],
    'oxygen_sat': 97,
    'waveform_trace': [0.8, -0.2, 1.1, 0.9, -0.4, 1.3, 0.7],
    'neural_spikes': [5, 3, 8, 5, 3, 9, 4, 6]
}

# Configuration with misleading keys
thresholds = {
    'noise_floor': 0.05,
    'strict_mode': True,
    'calibration_required': False,
    'max_iter': 1000,
    'debug_trace': None
}

# Execute main logic
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")