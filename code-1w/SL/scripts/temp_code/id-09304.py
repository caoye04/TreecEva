import itertools
from functools import reduce

def analyze_sequence(seq):
    # Irrelevant analysis function (dead code path)
    return sum(a * b for a, b in zip(seq, seq[1:]))

def compute_entropy(data):
    # Distractor: computes something unused later
    from math import log2
    total = sum(data)
    if total == 0:
        return 0
    probabilities = [x / total for x in data if x > 0]
    return -sum(p * log2(p) for p in probabilities)

def transform_features(raw_inputs):
    # Real transformation used later
    shifted = [(x ** 2 + 1) % 101 for x in raw_inputs]
    filtered = [x for x in shifted if x % 3 != 0]
    return list(set(filtered))  # Remove duplicates using set

def aggregate_metrics(values, weights):
    # Core calculation buried in noise
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    norm_factor = sum(weights)
    return weighted_sum / norm_factor if norm_factor else 0

def simulate_feedback_loop(initial_state, iterations):
    # Misleading complex recursion (never called)
    if iterations <= 0:
        return initial_state
    updated = [x ^ (i % 7) for i, x in enumerate(initial_state)]
    return simulate_feedback_loop(updated, iterations - 1)

def detect_patterns(signal):
    # Unused signal processing (red herring)
    patterns = []
    for size in range(2, 5):
        windows = list(itertools.sliding_window(signal, size))
        patterns.extend(windows)
    return len(patterns)

def normalize_dataset(entries):
    max_val = max(entries)
    return [round(x / max_val, 6) for x in entries]

def evaluate_performance(weight_map, data_series):
    keys = sorted(weight_map.keys())
    metrics = []
    for k in keys:
        if k == 'precision':
            val = sum(data_series[i] * (i + 1) for i in range(len(data_series)))
        elif k == 'stability':
            diffs = [abs(data_series[i] - data_series[i-1]) for i in range(1, len(data_series))]
            val = 1 / (1 + sum(diffs))
        elif k == 'complexity':
            bit_analysis = [bin(int(x * 100))[2:] for x in data_series]
            ones_count = sum(b.count('1') for b in bit_analysis)
            val = ones_count / 100.0
        metrics.append(val)
    
    # Apply weights
    weighted_result = aggregate_metrics(metrics, [weight_map[k] for k in keys])
    return int(weighted_result * 1000)  # Scale to integer

# Main execution with distractions
if __name__ == '__main__':
    # Input data
    sensor_readings = [12, 45, 23, 67, 34, 89, 23, 56]
    
    # Dead variables and irrelevant computations
    entropy_value = compute_entropy(sensor_readings)  # Unused
    temporal_pattern_count = detect_patterns(sensor_readings)  # Unused
    base_transformation = analyze_sequence(sensor_readings)  # Unused
    
    # Relevant data path begins here
    processed_features = transform_features(sensor_readings)
    
    # More distraction: unused recursive simulation
    fake_state = [10, 20, 30]
    simulated_outcome = simulate_feedback_loop(fake_state, 5)  # Never used
    
    # Normalization step (used)
    normalized_data = normalize_dataset(processed_features)
    
    # Weight configuration (critical)
    metric_weights = {
        'stability': 0.35,
        'precision': 0.5,
        'complexity': 0.15
    }
    
    # Decoy dictionary operation (looks important but isn't used in final calc)
    decoy_aggregation = {k: v * 1.5 for k, v in metric_weights.items()}
    decoy_aggregation['adjusted'] = sum(decoy_aggregation.values())
    
    # Key statement
    final_score = evaluate_performance(metric_weights, normalized_data)
    
    # Output required result
    print(f"Target result: {final_score}")