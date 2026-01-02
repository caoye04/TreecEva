import itertools

# Simulated bio-signal processing pipeline with diagnostic analysis
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 < x < 90]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) * 100 for x in filtered]
    return normalized

# Irrelevant auxiliary function (distractor)
def calculate_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log(count / total, 2) for count in freq.values())
    return round(entropy, 4)

# Data transformation with slicing and pattern masking
def apply_temporal_mask(signal, window_size=3):
    masked = []
    for i in range(len(signal)):
        segment = signal[max(0, i - window_size):i + window_size + 1]
        center_weight = signal[i] * 0.5
        neighbor_avg = sum(segment) / len(segment) * 0.5
        masked.append(center_weight + neighbor_avg)
    return masked[::2]  # Slicing: every second element

# Pattern analyzer using itertools to generate combinations (core relevant logic)
def generate_phase_shifts(binned_signal):
    shifts = []
    for a, b in itertools.pairwise(binned_signal):  # pairwise from itertools
        if a < b:
            shifts.append(1)
        elif a > b:
            shifts.append(-1)
        else:
            shifts.append(0)
    return shifts

# Main analysis function with early return (key control flow)
def analyze_pattern(processed):
    if not processed or len(processed) < 5:
        return -999
    
    # Binning signal into discrete levels
    binned = [int(x // 10) for x in processed]
    
    # Generate temporal direction shifts
    trends = generate_phase_shifts(binned)
    
    # Count trend transitions (up, down, flat)
    transition_count = 0
    for i in range(1, len(trends)):
        if trends[i] != trends[i-1]:
            transition_count += 1
    
    # Dead code path (distractor - never executed under current logic)
    anomaly_score = 0
    if False and len(processed) > 1000:
        anomaly_score = sum(1 for x in processed if x > 95)
    
    # Critical computation path
    base_metric = sum(binned) * 0.7
    adjustment = transition_count * 1.3
    final_score = base_metric + adjustment
    
    # Unused intermediate variables (distractors)
    avg_bin = sum(binned) / len(binned) if binned else 0
    peak_magnitude = max(binned) - min(binned)
    stability_index = 100 - (transition_count * 5)
    
    # Final diagnostic derived from key logic
    final_diagnostic = int(round(final_score))
    return final_diagnostic

# Unused function (red herring)
def simulate_noise(level, seed=42):
    import random
    random.seed(seed)
    return [random.uniform(0, level) for _ in range(50)]

# Irrelevant data structure (distractor)
diagnostic_metadata = {
    "version": "2.1.5",
    "calibration": [0.1, 0.3, 0.2, 0.4],
    "thresholds": {"low": 20, "high": 80},
    "units": "arb"
}

# Core execution sequence
raw_sensor_data = [15, 88, 76, 23, 45, 52, 68, 31, 41, 59, 77, 12, 63, 39, 47]

cleaned_data = preprocess_readings(raw_sensor_data)

enhanced_signal = apply_temporal_mask(cleaned_data)

# Apply slicing transformation (every third element starting from index 1)
transformed_data = enhanced_signal[1::3]

# Key statement: compute final diagnostic
final_diagnostic = analyze_pattern(transformed_data)

print(f"Result: {final_diagnostic}")