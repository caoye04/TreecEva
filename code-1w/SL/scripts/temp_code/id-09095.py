from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_feed(raw_input, filter_strength=0.75):
    normalized = [x * filter_strength for x in raw_input if x > -50]
    outlier_buffer = [x for x in raw_input if x < -50]  # Dead path: never used later
    shifted = [(x + 10) ** 0.5 for x in normalized if x >= 0]
    return shifted

# Irrelevant transformation chain (distractor)
def deprecated_analysis(seq):
    temp = [math.sin(x) for x in seq]
    stats = defaultdict(float)
    for val in temp:
        stats['total'] += val
        stats['count'] += 1
    return dict(stats)

# Core signal processing pipeline
def transform_frequency_bands(data):
    result = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            result.append(val * 2.1)
        elif i % 5 == 0:
            result.append(val * 0.9)
        else:
            result.append(val * 1.1)
    return result

# Legacy checksum (decoy function - not used in final calculation)
def compute_checksum(arr):
    checksum = 0
    for idx, num in enumerate(arr):
        checksum += (num * idx) % 7
    return checksum

# Main analysis logic
def aggregate_metrics(signal):
    metrics = {}
    metrics['peak'] = max(signal)
    metrics['base'] = sum(1 for x in signal if x < 15)
    metrics['growth'] = len([x for x in signal if x > metrics['peak'] * 0.7])
    return metrics

# Higher-order analyzer using lambda and complex logic
def evaluate_stability(metrics_dict):
    assess = lambda p, b, g: (p * 0.3) + (b * 0.2) - (g * 0.1)
    score = assess(metrics_dict['peak'], metrics_dict['base'], metrics_dict['growth'])
    return round(score, 4)

# Final diagnostic engine
def analyze_signal(clean_data):
    freq_data = transform_frequency_bands(clean_data)
    interim_values = [math.log(x + 1) for x in freq_data if x > 0]
    
    # Key computation branch
    counter = Counter(interim_values)
    modal_group = counter.most_common(1)[0][1] if counter else 0
    
    adjustment_factor = 0.8 if modal_group > 2 else 1.2
    
    raw_sum = sum(freq_data)
    sample_count = len(freq_data)
    
    # Critical assignment point
    base_diagnostic = raw_sum / sample_count if sample_count > 0 else 0
    adjusted_diagnostic = base_diagnostic * adjustment_factor
    
    # Secondary correction based on distribution
    high_freq_ratio = sum(1 for x in freq_data if x > 20) / sample_count
    final_correction = 1.05 if high_freq_ratio > 0.3 else 0.95
    
    # Answer-determining assignment
    final_diagnostic = adjusted_diagnostic * final_correction
    
    # Unused variables (distractors)
    diagnostic_metadata = {
        'version': 'legacy_v2',
        'calibration_offset': -7.3,
        'redundant_flag': False
    }
    
    return final_diagnostic

# Simulated input (real data flow)
sensor_readings = [23, 45, 12, -55, 67, 34, 29, 88, 16, 54, 33, 71, 22]

# Processing steps with mixed relevance
filtered = preprocess_sensor_feed(sensor_readings)
analysis_snapshot = deprecated_analysis(filtered)  # Computed but unused
processed_data = transform_frequency_bands(filtered)
metrics_summary = aggregate_metrics(processed_data)
stability_score = evaluate_stability(metrics_summary)

# Key execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")