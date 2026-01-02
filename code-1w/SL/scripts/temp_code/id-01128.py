def analyze_data(samples):
    # Irrelevant statistical analysis (dead-end function)
    mean = sum(samples) / len(samples)
    variance = sum((x - mean) ** 2 for x in samples) / len(samples)
    return [mean, variance]


def preprocess_tags(raw_tags):
    # Distractor: tag normalization with no impact on result
    cleaned = {tag.strip().lower() for tag in raw_tags}
    reserved = {'debug', 'test', 'temp'}
    return cleaned - reserved

# Misleading global variables
total_cycles = 0
baseline_offset = 3.14159
useless_buffer = [0] * 100

# Core logic disguised among noise
status_flags = [True, False, True, True]
metric_set = ['latency', 'throughput', 'error_rate', 'retries']

config_matrix = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]

# Decoy data structure
performance_map = {
    'latency': {'weight': 0.4, 'threshold': 200},
    'throughput': {'weight': 0.3, 'threshold': 1000},
    'error_rate': {'weight': 0.2, 'threshold': 0.5},
    'retries': {'weight': 0.1, 'threshold': 3}
}

# Unused but plausible-looking function
def compute_legacy_score(data):
    score = 0
    for k, v in data.items():
        if 'rate' in k:
            score -= v * 10
        else:
            score += v
    return score

# Simulated system states (some relevant, some not)
system_states = [
    {'mode': 'active', 'load': 75, 'errors': 2},
    {'mode': 'idle', 'load': 20, 'errors': 0},
    {'mode': 'active', 'load': 85, 'errors': 5},
    {'mode': 'maintenance', 'load': 5, 'errors': 1}
]

# Early filtering that looks important but only partially used
active_states = [s for s in system_states if s['mode'] == 'active']
high_load = [s for s in system_states if s['load'] > 70]

# Bit manipulation red herring
def scramble_value(x):
    x = (x ^ 42) << 1
    x = (x & 255) | (x >> 8)
    return x % 100

scrambled_metrics = [scramble_value(len(m)) for m in metric_set]

# Real computation buried in noise
def evaluate_performance(metrics):
    # Complex weight derivation using set operations and slicing
    weights = []
    for i, m in enumerate(metrics):
        if 'latency' in m:
            w = 0.4
        elif 'throughput' in m:
            w = 0.35  # Slight adjustment
        elif 'error' in m:
            w = 0.15 + 0.05 * (len(active_states) / len(system_states))
        else:
            w = 0.1
        weights.append(w)
    
    # Actual scoring logic
    base_scores = {
        'latency': 180,
        'throughput': 950,
        'error_rate': 0.7,
        'retries': 4
    }
    
    # Normalize scores using thresholds (real logic)
    normalized = []
    for m in metrics:
        raw = base_scores[m]
        threshold = performance_map[m]['threshold']
        if 'rate' in m or m == 'retries':
            norm = max(0, (threshold - raw) / threshold)  # Inverted scale
        else:
            norm = min(1, raw / threshold)
        normalized.append(norm)
    
    # Weighted combination
    composite = sum(normalized[i] * weights[i] for i in range(len(metrics)))
    
    # Final nonlinear transformation
    import math
    final = math.floor(composite * 1000) / 10
    
    # Dead code branch (never reached due to return)
    if final < 0:
        final = 0
    
    return final

# Secondary distraction: unused matrix reduction
reduced_config = [
    sum(row[i] for i in range(len(row))) 
    for row in config_matrix
]

# Critical execution point
final_score = evaluate_performance(metric_set)

# Print required output
print(f"Result: {final_score}")