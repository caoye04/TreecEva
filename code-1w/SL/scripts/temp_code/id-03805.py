def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    return [x ** 2 for x in filtered if x % 2 == 1]


def transform_sequence(seq):
    # Irrelevant transformation (dead path)
    shifted = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    smoothed = [sum(seq[i:i+3]) / 3 for i in range(len(seq)-2)]
    return smoothed  # Unused return


def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    return -sum(p * log2(p) for p in probs if p > 0)


def extract_features(raw_log):
    # Distractor: complex parsing with unused components
    lines = raw_log.strip().split('\n')
    timestamps = []
    events = []
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 3:
            timestamps.append(float(parts[0]))
            events.append(parts[2].strip())
    
    # Real feature extraction
    event_counts = {}
    for e in events:
        event_counts[e] = event_counts.get(e, 0) + 1
    
    # Return only what's needed later
    return [event_counts.get('CRITICAL', 0), event_counts.get('WARN', 0), event_counts.get('INFO', 0)]


def evaluate_performance(metrics, weights):
    # Core logic: weighted harmonic mean (only this matters)
    filtered = [m for m in metrics if m > 0]
    if not filtered:
        return 0.0
    weighted_inv_sum = sum(weights[i] / metrics[i] for i in range(len(filtered)))
    return len(filtered) / weighted_inv_sum if weighted_inv_sum != 0 else 0.0

# Main execution
raw_data = [-1.2, 0.3, 2.5, -3.7, 4.1, 0.0, -2.2]
signal_analysis = analyze_signal(raw_data)
sequence_trend = transform_sequence([1, 2, 4, 7, 11])  # Dead assignment

log_input = '''
1623456789.12,USER1,INFO
1623456790.23,USER2,CRITICAL
1623456791.45,USER1,WARN
1623456792.67,USER3,CRITICAL
1623456793.89,USER2,INFO
'''

event_metrics = extract_features(log_input)

# Injecting decoy calculations
entropy_value = compute_entropy([4, 2, 2, 1])  # Computed but unused
shifted_data = [x - 1.5 for x in raw_data if x > 0]  # Partially used, mostly noise
sliced_view = shifted_data[1:4:2]  # Another distraction

# Actual relevant metrics and weights
base_scores = [85, 70, 90]  # Performance metrics
weight_map = {0: 0.5, 1: 0.3, 2: 0.2}
weights = [weight_map[i] for i in range(3)]

# Augment with one event-derived metric
augmented_metrics = base_scores + [event_metrics[0] * 10]  # Only CRITICAL count matters

# Key statement
final_score = evaluate_performance(augmented_metrics, weights)

# Print result as required
Target result: {final_score}