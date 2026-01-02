from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_readings(raw_data):
    processed = []
    for item in raw_data:
        if 'voltage' in item and item['voltage'] > 0:
            normalized = math.log(item['voltage']) * item.get('gain', 1.0)
            processed.append({'id': item['id'], 'level': normalized})
    return processed

# Irrelevant helper - looks important but not used in final calculation
def deprecated_filter(seq, threshold):
    return [x for x in seq if sum(x) > threshold]

# Core transformation function
def transform_levels(readings):
    result_map = defaultdict(float)
    magnitude_total = 0.0
    
    for entry in readings:
        key = entry['id'] % 10
        signal = abs(entry['level']) ** 0.5
        result_map[key] += signal
        magnitude_total += signal

    # Dead code path - never executed due to logic above
    if False and len(result_map) > 100:
        fallback = {k: v * 0.1 for k, v in result_map.items()}
        return fallback

    return dict(result_map), magnitude_total

# Secondary analysis with red herring variables
def compute_entropy(values):
    counts = Counter(values)
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 6)

# Unused complexity - simulates calibration drift (decoy)
calibration_history = [
    {'cycle': i, 'drift': math.sin(i * 0.5) * 0.1} for i in range(10)
]

def analyze_pattern(metrics, base):
    score = 0
    keys = sorted(metrics.keys())
    
    # Relevant computation
    for i, k in enumerate(keys):
        if k in base:
            diff = metrics[k] - base[k]
            if diff > 0.5:
                score += int(diff * 2)
    
    # Distractor: complex-looking but unused expression
    auxiliary_score = sum(
        math.tanh(v * 0.1) * (i + 1)
        for i, v in enumerate(sorted(metrics.values(), reverse=True))
    )
    
    return int(score * 1.75)

# Setup: synthetic input
data_stream = [
    {'id': 103, 'voltage': 25.0, 'gain': 1.2},
    {'id': 217, 'voltage': 49.0, 'gain': 0.8},
    {'id': 303, 'voltage': 81.0, 'gain': 1.1},
    {'id': 417, 'voltage': 16.0, 'gain': 1.5},
    {'id': 503, 'voltage': 64.0, 'gain': 0.9}
]

baseline = {3: 4.0, 7: 3.5}  # id % 10 -> expected level root

# Main execution flow
filtered = preprocess_readings(data_stream)
transformed_metrics, total_power = transform_levels(filtered)

# Diagnostic entropy (unused in final result - distraction)
signal_levels = [int(v * 10) for v in transformed_metrics.values()]
entropy_diagnostic = compute_entropy(signal_levels)

# Red herring: historical trend analysis (dead end)
trend_bias = sum(c['drift'] for c in calibration_history if c['cycle'] % 3 == 0)

# Key statement
final_diagnostic = analyze_pattern(transformed_metrics, baseline) + int(total_power)

print(f"Result: {final_diagnostic}")