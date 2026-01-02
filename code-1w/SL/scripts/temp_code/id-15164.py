import itertools

def analyze_signal(samples, baseline):
    filtered = [x for x in samples if abs(x - baseline) > 1.5]
    squared_devs = [(x - baseline) ** 2 for x in samples]
    avg_sq = sum(squared_devs) / len(squared_devs)
    normalized = [x / (avg_sq + 1e-5) for x in filtered]
    return [round(x, 3) for x in normalized]

def generate_lookup(keys, offset):
    # Distractor: complex but unused mapping
    lookup = {}
    for i, k in enumerate(keys):
        lookup[k] = (i * offset) % 97
    return {k: (v ** 2) % 100 for k, v in lookup.items()}

def compute_invariants(sequence):
    # Distractor: computes unused invariants
    a, b, c = sequence[:3]
    inv1 = (a * b + c) % 1000
    inv2 = (a + b * c) % 1000
    inv3 = ((a ^ b) | c) % 1000
    return inv1, inv2, inv3

def evaluate_stability(readings):
    if len(readings) < 5:
        return 0
    diffs = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    trend = sum(1 for d in diffs if d > 2)
    noise = sum(diffs) / len(diffs)
    stability_score = len(readings) - trend - int(noise)
    return max(stability_score, 0)

def aggregate_metrics(data, config):
    # Core logic begins here
    flat = list(itertools.chain.from_iterable(data))
    valid = [x for x in flat if x > config['min_signal']]
    
    # Real computation path
    chunked = [valid[i:i+4] for i in range(0, len(valid), 4)]
    processed = []
    for chunk in chunked:
        if len(chunk) == 4:
            # Apply transformation: (a + b) * (c - d)
            val = (chunk[0] + chunk[1]) * (chunk[2] - chunk[3])
            processed.append(abs(val))
    
    if not processed:
        return 0
    
    average_val = sum(processed) / len(processed)
    ceiling_val = int(round(average_val))
    
    # Final step with slicing and dictionary op
    history_log = {'values': processed[-10:], 'size': len(processed)}
    recent_sum = sum(history_log['values'])
    final_metric = ceiling_val + (recent_sum % 17)
    
    return final_metric

# Irrelevant setup data (distractors)
baseline_samples = [0.1, -0.3, 0.5, -0.2, 0.7, 0.9, -0.1, 0.0]
signal_keys = ['A1', 'B2', 'C3', 'D4', 'E5']
raw_invariants = compute_invariants([7, 11, 13])

# Unused complex structure
decoy_matrix = [
    [i * j + 2 for j in range(8)] for i in range(6)
]

# Real input data
sensor_streams = [
    [3.2, 1.8, 4.5, 2.1],
    [2.9, 2.0, 4.7, 1.9],
    [3.0, 1.7, 4.6, 2.2],
    [3.1, 1.9, 4.4, 2.0]
]

# Another distractor: unused lookup
table_offset = 73
symbol_map = generate_lookup(signal_keys, table_offset)

# Signal analysis (partially relevant)
baseline_ref = 2.5
diagnostic_peaks = analyze_signal([2.8, 1.9, 4.6, 2.0, 3.1], baseline_ref)

# Stability evaluation (red herring)
stability_flag = evaluate_stability([5, 5, 6, 5, 7, 5, 5])

# Threshold configuration (used in final function)
threshold_map = {
    'min_signal': 1.5,
    'sensitivity': 0.85,
    'window': 4
}

# Trend data — actual core input
trend_data = [
    [2.8, 1.9, 4.6, 2.0],
    [3.1, 2.1, 4.4, 1.8],
    [2.9, 1.7, 4.5, 2.1],
    [3.0, 2.0, 4.3, 1.9]
]

# Key execution point
final_diagnostic = aggregate_metrics(trend_data, threshold_map)

print(f"Result: {final_diagnostic}")