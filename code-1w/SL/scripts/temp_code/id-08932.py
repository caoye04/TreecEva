from collections import defaultdict, Counter
import itertools

# Simulated sensor data stream (irrelevant for final result but adds distraction)
sensor_readings = [1024, 2048, 512, 768, 3072, 1536, 896, 4096]
noise_floor = sum([r % 128 for r in sensor_readings]) // len(sensor_readings)
adjusted_readings = [r >> 2 for r in sensor_readings if r > 1000]

# Decoy function: appears important but unused
def analyze_signal_strength(data):
    return sum(d & 0xFF for d in data) ^ len(data)

# Unused transformation pipeline
def transform_sequence(seq):
    result = []
    for i, val in enumerate(seq):
        if i % 3 == 0:
            result.append(val << 1)
        elif val > 2000:
            result.append(val // 4)
    return result

# Misleading statistical analysis (dead code path)
stats_summary = defaultdict(float)
for reading in sensor_readings:
    if reading > 2048:
        stats_summary['high'] += 1
    elif reading > 1024:
        stats_summary['medium'] += 1
    else:
        stats_summary['low'] += 1

# Phantom normalization factor (never used)
normalization_factor = max(sensor_readings) / (min(sensor_readings) + 1e-6)

# Actual problem context: performance metric evaluation
baseline = {'p': 0.85, 'r': 0.72, 'f1': 0.78}
raw_metrics = [
    {'p': 0.87, 'r': 0.70, 'f1': 0.77},
    {'p': 0.90, 'r': 0.68, 'f1': 0.78},
    {'p': 0.82, 'r': 0.75, 'f1': 0.78},
    {'p': 0.88, 'r': 0.71, 'f1': 0.78}
]

# Distractor: complex filtering that leads nowhere
efficiency_ratios = []
for m in raw_metrics:
    ratio = (m['p'] * m['r']) / (m['f1'] + 1e-8)
    efficiency_ratios.append(round(ratio, 4))

# Unused combinatorial generation
combinations = list(itertools.combinations(raw_metrics, 2))
consistency_scores = []
for c in combinations:
    diff = abs(c[0]['f1'] - c[1]['f1'])
    consistency_scores.append(1 - diff)

# Irrelevant slicing operation on string representation (distractor)
metric_names = ['precision', 'recall', 'f1_score']
abbreviations = [name[:2].upper() for name in metric_names]

# Real computation begins here — subtle and buried among distractions
def calculate_stability(metrics):
    f1_values = [m['f1'] for m in metrics]
    mean_f1 = sum(f1_values) / len(f1_values)
    variance = sum((x - mean_f1) ** 2 for x in f1_values) / len(f1_values)
    return 1 / (1 + variance)  # Higher stability = lower variance

# Secondary relevant calculation with red herring input
def adjust_for_bias(raw_value, control_factor=0.93):
    # This function is called but control_factor is ignored in logic
    adjustment_curve = [0.01 * i**2 for i in range(1, 11)]  # decoy list
    if raw_value > 0.8:
        return raw_value * 1.02
    else:
        return raw_value * 0.98

# Core evaluation logic — interwoven with noise
def evaluate_performance(metric_data, base):
    # Extract key performance indicator
    primary_metric = [m['f1'] for m in metric_data]
    
    # Compute aggregate score (this is critical)
    avg_precision = sum(m['p'] for m in metric_data) / len(metric_data)
    avg_recall = sum(m['r'] for m in metric_data) / len(metric_data)
    harmonic_mean = 2 * (avg_precision * avg_recall) / (avg_precision + avg_recall)
    
    # Stability bonus (relevant)
    stability_bonus = calculate_stability(metric_data)
    
    # Apply adjustment (only one matters)
    adjusted_harmonic = adjust_for_bias(harmonic_mean)
    
    # Final weighting — this determines the answer
    weighted_component_1 = adjusted_harmonic * 0.6
    weighted_component_2 = stability_bonus * 0.4
    
    # Red herring: unused intermediate
    phantom_score = (harmonic_mean + stability_bonus) / 2 * 100
    
    # The real final score
    final_computation = weighted_component_1 + weighted_component_2
    
    # More distraction: irrelevant bit manipulation
    binary_tag = 0b1010
    for val in primary_metric:
        binary_tag ^= int(val * 100)
        binary_tag &= 0xFFFF
    
    return round(final_computation * 1000)  # Scale up to integer

# Key execution point
final_score = evaluate_performance(raw_metrics, baseline)

# Print result as required
print(f"Result: {final_score}")