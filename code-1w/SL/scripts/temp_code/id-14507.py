import math

# Simulated biomedical signal processing pipeline
def analyze_waveform(signal):
    if not signal:
        return 0
    peak = max(signal)
    baseline = sum(signal) / len(signal)
    amplitude = peak - baseline
    return round(amplitude * 1.618, 3)  # Golden ratio weighting (irrelevant but looks meaningful)

# Irrelevant helper: spectrogram analysis (dead code path)
def compute_spectrogram(data):
    fft_result = []
    for i in range(len(data)):
        fft_component = sum(data[j] * math.cos(2 * math.pi * i * j / len(data)) for j in range(len(data)))
        fft_result.append(fft_component)
    normalized = [abs(x) / max(map(abs, fft_result)) for x in fft_result]
    return normalized

# Data quality scoring (distractor function - never called with real data)
def assess_data_quality(entries):
    quality_flags = {"low": 0, "medium": 0, "high": 0}
    for entry in entries:
        if len(entry) < 3:
            quality_flags["low"] += 1
        elif len(entry) < 6:
            quality_flags["medium"] += 1
        else:
            quality_flags["high"] += 1
    score = (quality_flags["high"] * 3 + quality_flags["medium"] * 2) / len(entries)
    return round(score, 2)

# Main diagnostic processor
def process_metrics(raw_data, config):
    processed = []
    anomalies = 0
    
    # Real logic starts here
    for record in raw_data:
        temp = record.get('temperature', 0)
        heart_rate = record.get('heart_rate', 0)
        o2 = record.get('o2_saturation', 0)
        
        # Validate critical vitals
        if temp > 37.5 and heart_rate > 100:
            severity_index = (temp - 37.5) * 2 + (heart_rate - 80) * 0.5
        elif o2 < 92:
            severity_index = (92 - o2) * 3.1
        else:
            severity_index = 0.75  # baseline metabolic index
        
        processed.append(severity_index)
        
        # Anomaly detection (red herring counter)
        if heart_rate < 50 or heart_rate > 120 or o2 < 90:
            anomalies += 1

    # Decoy accumulation (looks important but unused)
    total_power = sum([math.exp(x / 10) for x in processed if x > 1])
    weighted_sum = sum(x * (1.1 ** i) for i, x in enumerate(processed))
    
    # Actual answer derivation
    base_score = sum(processed) / len(processed) if processed else 0
    adjustment = len([p for p in processed if p > 2]) * 0.25
    final_index = base_score - adjustment
    
    # Multiple layers of conditional transformation
    if final_index < 1:
        category = 'stable'
    elif final_index < 3:
        category = 'monitoring'
    else:
        category = 'critical'
    
    # Destructuring assignment (real use)
    status_code, priority_level = (200, 1) if category == 'stable' else (409, 3)
    
    # Dictionary-based mapping (relevant)
    code_map = {'stable': 0.85, 'monitoring': 1.2, 'critical': 1.8}
    scaling_factor = code_map.get(category, 1.0)
    
    # Final computation chain
    diagnostic_value = (final_index * scaling_factor + priority_level) * 100
    calibration_offset = math.sin(math.pi / 6)  # Always 0.5
    final_diagnostic = int(diagnostic_value - calibration_offset * 20)
    
    # Dead code: hypothetical multi-parameter fusion (never reached in logic)
    if status_code == 500:
        fallback = 0
        for k, v in {'a': 3, 'b': 7}.items():
            fallback += v << 2
        final_diagnostic += fallback  # unreachable
    
    return final_diagnostic

# Simulated patient data stream
vital_readings = [
    {'temperature': 38.1, 'heart_rate': 108, 'o2_saturation': 94},
    {'temperature': 36.9, 'heart_rate': 76, 'o2_saturation': 98},
    {'temperature': 37.2, 'heart_rate': 88, 'o2_saturation': 89},  # triggers O2 branch
    {'temperature': 39.0, 'heart_rate': 115, 'o2_saturation': 93},
    {'temperature': 37.0, 'heart_rate': 82, 'o2_saturation': 96}
]

# Threshold configuration (some irrelevant keys)
alert_thresholds = {
    'fever': 38.0,
    'tachycardia': 100,
    'hypoxia': 92,
    'noise_floor': 0.3,  # unused
    'gain': 1.5  # unused
}

# Signal data (unused but looks important)
signals = [
    [1.2, 0.8, 1.5, 2.1, 1.7],
    [0.9, 1.0, 1.1, 0.8, 0.7]
]

# Irrelevant pre-processing
normalized_signals = [[x * 0.95 for x in s] for s in signals]
analysis_results = [analyze_waveform(s) for s in normalized_signals]

# Actual execution point
final_diagnostic = process_metrics(vital_readings, alert_thresholds)

# Output result
print(f"Target result: {final_diagnostic}")