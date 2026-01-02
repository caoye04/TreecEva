import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [i * 0.5 + (i % 7) for i in range(15)]
    offset = 2.3
    calibrated = [round(x - offset, 3) for x in raw_samples]
    return calibrated

# Irrelevant helper - dead code path
def deprecated_filter(data):
    return [x for x in data if x > 1.0]

# Signal conditioning with distractor logic
def preprocess(signal):
    noise_floor = 0.15
    filtered = []
    for x in signal:
        if abs(x) > noise_floor:
            filtered.append(x * 1.08)
        else:
            filtered.append(0)
    # Distractor transformation
    inverted = [1.0 / (1 + math.exp(-x)) for x in filtered[:5]]
    enhanced = [round(f * 1.2, 3) for f in filtered]
    return enhanced

# Character frequency analysis - misleading side computation
def char_frequency(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    return freq

# Hidden pattern detector (actually unused)
detect_anomaly = lambda seq: sum(1 for x in seq if x > 5) > 3

# Core recursive energy summation over threshold segments
def recursive_energy(data, threshold, index=0):
    if index >= len(data):
        return 0
    current = abs(data[index]) if data[index] > threshold else 0
    rest = recursive_energy(data, threshold * 0.95, index + 1)
    return current + rest

# Data classification map (distractor structure)
class_map = {
    'low': lambda x: x < 2,
    'medium': lambda x: 2 <= x < 5,
    'high': lambda x: x >= 5
}

def classify_segments(data):
    counts = {k: 0 for k in class_map}
    for x in data:
        for cls, cond in class_map.items():
            if cond(abs(x)):
                counts[cls] += 1
                break
    return counts

# Main analysis pipeline
processed_data = {}
sensor_log = collect_readings()
filtered_signal = preprocess(sensor_log)

# Side computation with decoy result
symbol_text = "abcabdbca"
frequency_profile = char_frequency(symbol_text)
peak_count = sum(1 for x in filtered_signal if x > 4)

# Real processing branch
energy_total = recursive_energy(filtered_signal, 1.0)
segment_classes = classify_segments(filtered_signal)

# Red herring dictionary update
processed_data['readings'] = sensor_log
processed_data['status'] = 'stable'
processed_data['diagnostics'] = {'peaks': peak_count, 'classes': segment_classes}
processed_data['energy_snapshot'] = energy_total

# Decoy assignment
baseline_ref = {'calibration': 2.3, 'version': '1.0a'}

# Actual key processing function
def analyze_signal(signal_data):
    # Compute weighted harmonic mean of non-zero values
    nonzero = [x for x in signal_data if x != 0]
    weights = [i + 1 for i in range(len(nonzero))]
    
    # Misleading intermediate calculation
    avg_position = sum(i * w for i, w in enumerate(weights)) / sum(weights) if weights else 0
    
    # True computation path
    weighted_inv_sum = sum(weights[i] / x for i, x in enumerate(nonzero))
    total_weight = sum(weights)
    harmonic_baseline = total_weight / weighted_inv_sum if weighted_inv_sum != 0 else 0
    
    # Apply correction based on recursive energy (cross-concept linkage)
    correction_factor = 1 + (processed_data['energy_snapshot'] / 1000)
    adjusted_diagnostic = harmonic_baseline * correction_factor
    
    # Final adjustment using lambda (required feature)
    finalize = lambda x: round(x, 3)
    return finalize(adjusted_diagnostic)

# Critical execution point
final_diagnostic = analyze_signal(processed_data['readings'])
print(f"Result: {final_diagnostic}")