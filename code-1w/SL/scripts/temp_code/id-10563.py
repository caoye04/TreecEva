import itertools
from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic analysis
def analyze_fluctuations(readings, threshold=0.15):
    moving_avg = [sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)]
    deviations = [(r - moving_avg[i]) / moving_avg[i] for i, r in enumerate(readings[2:])]
    spike_count = sum(1 for d in deviations if abs(d) > threshold)
    return spike_count

# Irrelevant auxiliary function – dead code path (distractor)
def calculate_entropy(sequence):
    freqs = Counter(sequence)
    total = len(sequence)
    entropy = -sum((count / total) * (count / total).__log__() for count in freqs.values())
    return entropy

# Data transformation pipeline with red herrings
def transform_stream(raw_points, mode='delta'):
    filtered = [x for x in raw_points if x > 0.5]  # Arbitrary filter
    shifted = [x * 1.07 for x in filtered]
    
    # Distractor: unused intermediate
    inverted_map = {i: 1.0 / (x + 1e-8) for i, x in enumerate(shifted)}
    stats_summary = {
        'max_val': max(shifted),
        'min_val': min(shifted),
        'range': max(shifted) - min(shifted)
    }
    
    if mode == 'delta':
        return [shifted[i+1] - shifted[i] for i in range(len(shifted)-1)]
    else:
        return [abs(shifted[i]) for i in range(len(shifted))]

# Core logic buried among distractions
def evaluate_stability(indices, reference_level):
    cumulative_drift = 0
    adjustment_log = []
    
    for idx, val in enumerate(indices):
        if idx % 3 == 0 and val < reference_level:
            cumulative_drift += val * 0.33
            adjustment_log.append(cumulative_drift)
        elif idx % 4 == 0:
            cumulative_drift -= 0.08
        else:
            pass  # Dead branch (misleading)
    
    # Real computation hidden in loop
    temp_factor = sum(itertools.islice(adjustment_log, None))
    return round(temp_factor * 100, 2)

# Main aggregation function – target execution point
def aggregate_metrics(metrics_list, offset):
    base_frame = defaultdict(float)
    for i, val in enumerate(metrics_list):
        base_frame[i] = val ** 0.5 + offset
    
    # Real contribution to answer
    signal_peaks = [k for k, v in base_frame.items() if v > offset + 0.5]
    enhancement = sum(base_frame[k] for k in signal_peaks)
    
    # Distractor variables
    phantom_weights = [base_frame[k] * 0.01 for k in base_frame if k % 5 == 0]
    shadow_accum = sum(phantom_weights)
    
    final_score = enhancement * 1.75 - shadow_accum
    return int(final_score)

# Simulated dataset generation (deterministic)
def main():
    seed_data = [0.21, 0.45, 0.68, 0.71, 0.59, 0.83, 0.92, 0.67, 0.54, 0.33]
    
    # Unused but plausible transformation (red herring)
    perturbed = [x + 0.02 * i for i, x in enumerate(seed_data)]
    
    trend_data = transform_stream(seed_data, mode='delta')
    
    # Misleading diagnostic call
    anomaly_count = analyze_fluctuations(seed_data, threshold=0.15)
    
    # Another distractor
    history_trace = list(itertools.accumulate(trend_data))
    snapshot = history_trace[::2]
    
    # Actual critical path
    baseline_offset = evaluate_stability(trend_data, reference_level=0.15)
    
    # Key statement
    final_diagnostic = aggregate_metrics(trend_data, baseline_offset)
    
    # Print result for evaluation
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()