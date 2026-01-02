import math

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    return sum(-x * math.log2(x) for x in data if x > 0)

# Unused utility for red herring
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Simulated sensor drift compensation (dead code path)
def correct_drift(signal, rate=0.01):
    return [s * (1 - rate * i) for i, s in enumerate(signal)]

# Core logic: performance evaluation with multiple concepts

def analyze_efficiency(runs):
    avg = sum(runs) / len(runs)
    variance = sum((x - avg) ** 2 for x in runs) / len(runs)
    return avg, math.sqrt(variance)


def recursive_filter(items, threshold, depth=0):
    # Simple recursion with pruning
    if not items or depth > 5:
        return []
    pivot = items[0]
    rest = items[1:]
    included = [pivot] if pivot >= threshold * (0.95 ** depth) else []
    return included + recursive_filter(rest, threshold, depth + 1)

# Main evaluation logic
def process_metrics(raw_data):
    # Extract timing and resource usage
    timings = [d['time'] for d in raw_data]
    resources = [d['mem'] for d in raw_data]
    
    # Compute efficiency metrics
    time_avg, time_std = analyze_efficiency(timings)
    resource_avg, _ = analyze_efficiency(resources)
    
    # Apply recursive filtering to clean outliers
    filtered_timings = recursive_filter(sorted(timings), time_avg - time_std)
    
    # Distractor: unused transformation
    adjusted_resources = [r * (1.05 if r < resource_avg else 0.98) for r in resources]
    
    # Key metric derived from filtered data
    if filtered_timings:
        primary_metric = sum(filtered_timings) / len(filtered_timings)
    else:
        primary_metric = time_avg
    
    # Irrelevant signal processing
    sample_waveform = [math.sin(i * 0.5) for i in range(10)]
    corrected_waveform = correct_drift(sample_waveform, 0.02)
    
    return {
        'primary': primary_metric,
        'memory_avg': resource_avg,
        'count': len(filtered_timings),
        'waveform_rms': math.sqrt(sum(x**2 for x in corrected_waveform)/len(corrected_waveform))  # decoy
    }

# Set operations and conditional expressions
baseline_flags = {'optimized', 'cached', 'parallel'}
current_config = {'optimized', 'parallel', 'vectorized'}
feature_overlap = len(baseline_flags & current_config)
feature_gap = len(current_config - baseline_flags)

config_score = 100 if feature_overlap >= 2 else 70

# Benchmark data with noise and distractors
timing_data = [120, 115, 130, 118, 125, 132, 140, 119]
memory_data = [45, 48, 50, 44, 47, 52, 46, 49]

raw_dataset = [
    {'time': t, 'mem': m, 'id': f'trial_{i}'} 
    for i, (t, m) in enumerate(zip(timing_data, memory_data))
]

# Unused anomaly detection (red herring)
def detect_anomalies(seq, window=3):
    anomalies = []
    for i in range(len(seq)):
        window_slice = seq[max(0, i - window):i + window]
        local_avg = sum(window_slice) / len(window_slice)
        if abs(seq[i] - local_avg) > 0.5 * local_avg:
            anomalies.append(i)
    return anomalies

# Another decoy function using list comprehension and conditionals
def assess_stability(values):
    trends = ['up' if v > values[i-1] else 'down' for i, v in enumerate(values) if i > 0]
    return sum(1 for t in trends if t == 'up') / len(trends)

metrics = process_metrics(raw_dataset)

# Complex conditional expression with distractors
benchmark_data = {
    'base_time': 110,
    'tolerance': 15,
    'penalty_factor': 0.8 if metrics['memory_avg'] > 48 else 1.0,
    'bonus_applied': False
}

# Critical statement with mixed logic
final_score = (metrics['primary'] - benchmark_data['base_time'])

if final_score <= benchmark_data['tolerance']:
    bonus = 25 if config_score > 80 else 15
    final_score += bonus
else:
    penalty = 30 * benchmark_data['penalty_factor']
    final_score -= penalty

# Dead code: never executed but looks important
def generate_report(score, details):
    report_lines = []
    report_lines.append(f"Performance Score: {score}")
    for k, v in details.items():
        report_lines.append(f"{k}: {v}")
    return '\n'.join(report_lines)

# Noise variables to distract
entropy_test = [0.1, 0.3, 0.25, 0.35]
dummy_entropy = calculate_entropy(entropy_test)

stability_index = assess_stability(timing_data)
anomaly_list = detect_anomalies(timing_data)

# Print final result as required
Result: {final_score}