import itertools

# Simulated telemetry data from sensor array (distractor: not all fields are used)
def generate_telemetry():
    return [
        {'timestamp': t, 'value': (t * 3) % 7, 'quality': q, 'flag': (t + q) % 2}
        for t, q in itertools.product(range(3), [1, 0])
    ]

# Legacy function - appears important but unused in critical path
def deprecated_normalization(data):
    factor = sum(d['value'] for d in data) or 1
    return [d['value'] / factor for d in data]

# Red herring transformation - operates on real data but irrelevant result
def compute_entropy(seq):
    counts = {}
    for x in seq:
        counts[x] = counts.get(x, 0) + 1
    entropy = 0
    total = len(seq)
    for count in counts.values():
        p = count / total
        entropy -= p * (p).log() if p > 0 else 0
    return round(entropy, 6)

# Misleading intermediate processing chain
def preprocess_stream(events):
    filtered = []
    temp_sum = 0
    for e in events:
        if e['quality'] == 1:
            adjusted = (e['value'] + 5) % 8
            temp_sum += adjusted
            if adjusted > 3:
                filtered.append({'seq': adjusted, 'meta': e['timestamp']})
    # Dead code branch - never reached due to logic above
    if len(filtered) > 100:
        return [{'seq': 999, 'meta': -1}]
    return filtered

# Core calculation disguised among distractors
def extract_features(dataset, offset):
    values = [d['value'] for d in dataset]
    shifted = [(v + offset) % 9 for v in values]
    grouped = []
    for k, g in itertools.groupby(shifted, lambda x: x % 3):
        grouped.append(sum(list(g)[:2]))  # Take at most first two per group
    return grouped

# Main aggregation with early termination red herring
def aggregate_performance(records, base):
    if not records:
        return -1
    
    # Real computation begins here
    features = extract_features(records, base)
    
    # Distractor: complex-looking but unused control flow
    accumulated = 0
    for i, f in enumerate(features):
        if f == 0:
            continue
        elif f % 4 == 0:
            accumulated += f // 2
        else:
            accumulated += f * 2
        if accumulated > 1000:  # Unreachable condition (red herring)
            return 9999
    
    # Critical path: this is where the actual answer is formed
    modifier = len([r for r in records if r['flag'] == 1])
    final_score = accumulated * 3 - modifier + base
    
    # Decoy output that looks important
    debug_trace = {"steps": 5, "peak": max(features, default=0), "score_x": final_score + 100}
    
    return final_score

# Irrelevant utility - included to suggest broader context
def format_report(data):
    return '\n'.join(f"{k}: {v}" for k, v in data.items())

# Unused constant arrays - visual noise
calibration_matrix = [[i*j for j in range(4)] for i in range(4)]
reference_weights = [0.1, 0.3, 0.5, 0.7, 0.9]

# Execution entry point
if __name__ == "__main__":
    logged_events = generate_telemetry()
    baseline_offset = 6
    
    # These calls look important but only some contribute to final answer
    processed = preprocess_stream(logged_events)
    legacy_norm = deprecated_normalization(logged_events)
    feature_vector = extract_features(logged_events, baseline_offset)
    
    # The key statement - contains the actual answer derivation
    final_score = aggregate_performance(logged_events, baseline_offset)
    
    # Additional misleading computations
    dummy_analysis = compute_entropy([e['value'] for e in logged_events])
    
    print(f"Result: {final_score}")