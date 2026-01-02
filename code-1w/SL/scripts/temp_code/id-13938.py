from itertools import combinations

# Simulate sensor fusion system with noise filtering and metric weighting
def preprocess_readings(raw_sensors):
    filtered = [x for x in raw_sensors if 10 <= x <= 90]
    baseline = sum(filtered) / len(filtered)
    normalized = [(x - baseline) for x in filtered]
    return normalized, baseline

def generate_derived_metrics(values):
    quad_moment = sum(v ** 4 for v in values) / len(values)
    pair_interactions = 0
    for a, b in combinations(values, 2):
        pair_interactions += abs(a - b)
    avg_deviation = sum(abs(v) for v in values) / len(values)
    return quad_moment, pair_interactions, avg_deviation

def calculate_reliability_score(raw_sensors):
    if len(raw_sensors) < 5:
        return 0
    processed, base = preprocess_readings(raw_sensors)
    if len(processed) == 0:
        return 0
    qm, pi, dev = generate_derived_metrics(processed)
    # Irrelevant transformation (distractor)
    entropy_proxy = 0
    for i in range(1, min(len(processed), 5)):
        entropy_proxy += abs(processed[i] - processed[i-1])
    # Another red herring: simulate unused diagnostic mode
    diagnostics = []
    for idx, val in enumerate(processed):
        if idx % 3 == 0:
            diagnostics.append(val * 0.1)
    reliability = (qm * 0.3) + (pi * 0.05) + (dev * 0.2)
    return reliability

def bitwise_diagnostic(code_sequence):
    # Simulate low-level health check using bitwise logic
    checksum = 0
    for code in code_sequence:
        checksum ^= (code & 255)
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF
    parity = bin(checksum).count('1') % 2
    return checksum if parity == 0 else checksum + 1

def evaluate_performance(weights, results):
    # Core logic starts here
    raw_sensors = results['readings']
    config_flags = results['flags']
    
    # Primary computation chain
    reliability = calculate_reliability_score(raw_sensors)
    
    # Bitwise diagnostic on configuration (semi-relevant but overcomplicated)
    health_code = bitwise_diagnostic(config_flags)
    adjustment_factor = (health_code % 20) / 100.0
    
    # Actual key computation
    base_score = reliability * (1 - adjustment_factor)
    
    # Weighted aggregation (only some weights are used)
    w1, w2, w3, w4 = weights
    
    # Distractor: complex-looking but unused weighted combination
    phantom_score = w1 * base_score
    if w2 > 0.1:
        for i in range(2):
            phantom_score -= w3 * 0.05  # Dead-end adjustment
    
    # Final score depends only on base_score and w4
    final_component = base_score * w4
    
    # Red herring: debug trace that doesn't affect output
    debug_snapshot = []
    for v in raw_sensors[:3]:
        debug_snapshot.append((v, v * adjustment_factor))
    
    # Critical assignment - this is the answer point
    final_score = int(final_component + 0.5)  # Round to nearest integer
    
    # Additional irrelevant state tracking
    audit_log = [{'stage': 'init', 'value': base_score}, {'stage': 'final', 'value': final_score}]
    
    return final_score

# Input data setup
metric_weights = [0.7, 0.2, 0.05, 0.8]  # w4 is the only one that matters
raw_results = {
    'readings': [15, 88, 12, 45, 67, 23, 76, 11, 54, 32],
    'flags': [0x1A, 0x2C, 0x0F, 0x88, 0x3E]
}

# Execution entry point
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Result: {final_score}")