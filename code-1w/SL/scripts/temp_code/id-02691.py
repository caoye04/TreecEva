from collections import defaultdict, Counter

# Simulated sensor signal processing with diagnostic logic
def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Irrelevant helper (distractor)
def smooth_data(data):
    if len(data) < 3:
        return data
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append(round((data[i-1] + data[i] + data[i+1]) / 3, 3))
    smoothed.append(data[-1])
    return smoothed

# Red herring function (unused)
def calculate_entropy(seq):
    count = Counter(seq)
    total = len(seq)
    entropy = 0
    for c in count.values():
        p = c / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, misleading
    return round(entropy, 4)

# Core logic disguised among distractions
def detect_anomalies(values, config):
    anomalies = []
    baseline = sum(values) / len(values)
    deviation = [abs(v - baseline) for v in values]
    
    # Nested conditional red herrings
    if len(deviation) > 5:
        cutoff = config.get('high', 0.5)
        for d in deviation:
            if d > cutoff * 1.2:
                anomalies.append(d)
    else:
        cutoff = config.get('low', 0.3)
        anomalies = [d for d in deviation if d > cutoff]
    
    # Decoy mutation
    temp_result = [a * 100 for a in anomalies if a != 0.45]  # Filter out artificial case
    return sorted(temp_result, reverse=True)

# Real target function — subtle and buried
def recursive_transform(seq, depth):
    if depth == 0 or len(seq) == 0:
        return [abs(int(s * 10)) % 7 for s in seq]
    transformed = [(s + 0.1) * 0.9 for s in seq]
    return recursive_transform(transformed, depth - 1)

# Another decoy: unused statistical check
def validate_coherence(data):
    if not data:
        return False
    diffs = [abs(data[i+1] - data[i]) for i in range(len(data)-1)]
    avg_diff = sum(diffs) / len(diffs)
    return avg_diff < 0.5

# Key analysis function with critical logic interwoven
def analyze_pattern(sequence, thresholds):
    # Step 1: Preprocess signal
    processed = preprocess_signal(sequence)
    
    # Distractor: unused smoothing
    smoothed = smooth_data(processed)
    
    # Step 2: Apply recursive transformation
    core_signature = recursive_transform(processed, 3)
    
    # Step 3: Count patterns
    freq_map = Counter(core_signature)
    
    # Step 4: Use threshold map to filter significant codes
    trigger_code = thresholds.get('code', 5)
    active_nodes = [k for k, v in freq_map.items() if v >= 2 and k % 2 == 1]
    
    # Step 5: Generate diagnostic score
    base_score = sum(active_nodes) * 1000
    
    # Misleading branch (never taken due to data)
    if len(active_nodes) == 0 and base_score == 0:
        backup_config = {"mode": "failover", "value": 999}
        base_score = backup_config["value"] * 10
    
    # Critical computation
    modifier = thresholds.get('mod', 1)
    final_score = base_score + modifier * 17
    
    # Dead code path (distractor)
    debug_trace = []
    for i in range(3):
        debug_trace.append({"step": i, "temp": final_score // (i+1) if i > 0 else 0})
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    signal_sequence = [1.2, -0.8, 0.5, 1.2, -0.3, 0.5, 0.9, -0.8, 1.2]
    
    # Threshold configuration (mixture of relevant and irrelevant keys)
    threshold_map = {
        'level': 'critical',
        'code': 3,
        'mod': 4,
        'debug': True,
        'version': '2.1'
    }
    
    # Unused intermediate computations (distractors)
    raw_stats = [x**2 for x in signal_sequence]
    peak_magnitude = max(raw_stats)
    moment = sum(x**3 for x in signal_sequence)  # Unused
    
    # Data structure cross-reference distraction
    node_registry = defaultdict(list)
    for idx, val in enumerate(signal_sequence):
        node_registry[f'node_{idx % 4}'].append(round(val, 1))
    
    # Another red herring: set operations with no impact
    unique_phases = set([int(abs(x * 10)) % 4 for x in signal_sequence])
    phase_lock = {1, 2} | unique_phases and {2, 3}  # Complex but unused
    
    # Key call
    final_diagnostic = analyze_pattern(signal_sequence, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")