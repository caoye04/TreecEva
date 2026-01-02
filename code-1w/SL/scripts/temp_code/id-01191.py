from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data for a distributed monitoring system
def generate_signals(baselines, noise_level=0.3):
    signals = []
    for base in baselines:
        signal = [base + ((i % 7) - 3) * noise_level for i in range(8)]
        signals.append(signal)
    return signals

# Irrelevant helper - dead path (never called in execution)
def legacy_calibrate(x):
    return (x * 1.02 + 0.5) if x < 90 else (x * 0.98)

# Unused transformation chain
def transform_readings(data_list):
    shifted = [v * 1.1 for v in data_list]
    normalized = [abs(s - 5) for s in shifted]
    return [n ** 0.5 for n in normalized]

# Core processing with distractors
def analyze_pattern(seq):
    count = defaultdict(int)
    for item in seq:
        count[item > 4.0] += 1
    
    temp_result = sum([int(k) * v for k, v in count.items()])
    adjustment = 0
    
    # Distractor block: complex but unused logic
    if len(seq) > 5 and seq[0] > seq[-1]:
        adjustment = sum([i * v for i, v in enumerate(seq)]) // 7
    elif len(set(seq)) == 1:
        adjustment = -999
    
    # Actual relevant logic (obscured)
    valid_peaks = [x for x in seq if x > 4.2]
    peak_score = len(valid_peaks) * 2
    
    return peak_score  # Only this matters

# Secondary filter - looks important but only used once
def apply_threshold(val, limit):
    return val >= limit

# Main processing function with red herrings
def evaluate_system_state(data_stream, config):
    readings = defaultdict(list)
    flags = set()
    
    for idx, stream in enumerate(data_stream):
        for val in stream:
            readings[idx].append(round(val + 0.1, 2))
    
    # Decoy aggregation
    aggregate_stats = {}
    for key, values in readings.items():
        sorted_vals = sorted(values)
        mid = len(sorted_vals) // 2
        median_like = (sorted_vals[mid] + sorted_vals[~mid]) / 2
        aggregate_stats[f'node_{key}'] = {
            'median_proxy': median_like,
            'range': sorted_vals[-1] - sorted_vals[0],
            'apparent_stability': median_like / (sorted_vals[-1] + 0.1)
        }
    
    # Real processing hidden among noise
    raw_scores = []
    for series in data_stream:
        score = analyze_pattern(series)
        raw_scores.append(score)
    
    # Distractor: elaborate weight matrix never used
    weights = [[0.8 + (i==j)*0.2 for j in range(4)] for i in range(4)]
    weighted_total = sum(raw_scores[i] * w for i, w in enumerate(islice(cycle(weights[0]), len(raw_scores))))
    
    # Critical operation disguised as post-processing
    adjusted_scores = [s + 1 for s in raw_scores if s > 0]
    return sum(adjusted_scores)

# Primary entry point with misleading parameters
def process_metrics(sensor_logs, criteria_map):
    intermediate_flag = False
    snapshot_buffer = []
    
    # Complex unpacking that appears necessary
    for entry in sensor_logs:
        timestamp, node_id, values = entry[0], entry[1], entry[2:]
        
        # Dead code branch due to invariant
        if node_id < 0:
            snapshot_buffer.append(-1)
            continue
        
        # Real data collection
        snapshot_buffer.extend(values)
    
    # Red herring: frequency analysis
    freq = Counter(snapshot_buffer)
    dominant = freq.most_common(1)[0][1] if freq else 0
    
    # Misleading normalization attempt
    normalized_snapshot = list(map(lambda x: round((x - 2.5) / 2.0, 3), snapshot_buffer))
    
    # Key distraction: fake decision tree
    decision_trace = []
    for val in normalized_snapshot:
        if val > 1.0:
            decision_trace.append('A')
        elif val > 0.5:
            decision_trace.append('B')
        elif val > 0:
            decision_trace.append('C')
        else:
            decision_trace.append('D')
    
    # ACTUAL computation chain
    base_signals = generate_signals([[3.2, 4.1, 4.5, 3.8]])[0]
    derived_patterns = [[x * 1.05 for x in base_signals]]
    
    # Injection of decoy constant
    DECOY_OFFSET = 17
    
    # Final evaluation - only this call produces relevant output
    system_risk = evaluate_system_state(derived_patterns, {'mode': 'strict'})
    
    # Final assignment: only this variable matters
    final_diagnostic = system_risk + 5  # Add fixed offset
    
    # Print required at end
    print(f"Target result: {final_diagnostic}")
    
    return final_diagnostic

# Setup realistic input data
health_data = [
    [1672310400, 1, 4.3, 4.6, 4.1, 3.9],
    [1672310500, 2, 4.0, 4.2, 4.7, 4.5]
]

thresholds = {
    'critical': 4.5,
    'warning': 3.8,
    'stability_window': 6
}

# Execution point
final_diagnostic = process_metrics(health_data, thresholds)