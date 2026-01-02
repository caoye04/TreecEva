def analyze_efficiency(values, threshold):
    """Irrelevant analysis function that computes efficiency but is not used in final result."""
    count = 0
    efficiency_ratio = 0.0
    for v in values:
        if v > threshold:
            count += 1
            efficiency_ratio += v / (threshold + 1)
    return efficiency_ratio * count


def normalize_data(data):
    """Misleading normalization function that appears important but is never called."""
    mean_val = sum(data) / len(data)
    return [round((x - mean_val) / mean_val * 100, 2) for x in data]


def filter_outliers(dataset, limit=3):
    """Dead code path - looks useful but unused."""
    return [x for x in dataset if abs(x) < limit]

# Core system parameters (some are red herrings)
baseline = {
    'tolerance': 5,
    'weight_a': 0.3,
    'weight_b': 0.7,
    'offset': -10,
    'scaling_factor': 2.5
}

# Distractor configuration block
config = {
    'max_iterations': 1000,
    'debug_mode': True,
    'cache_enabled': False,
    'timeout_ms': 500,
    'retries': 3
}

# Input metrics with mixed relevance
metrics = [
    {'type': 'latency', 'value': 120, 'critical': False},
    {'type': 'throughput', 'value': 85, 'critical': True},
    {'type': 'error_rate', 'value': 4, 'critical': True},
    {'type': 'jitter', 'value': 18, 'critical': False}
]

# Irrelevant dataset that seems related but isn't used
historical_data = [78, 82, 85, 76, 90, 88, 84]

# Decoy variables that look like they might contribute to final score
temp_correction = 0.95
adjustment_factor = -5
penalty_buffer = set()

# Simulated subsystem statuses (only one field matters)
subsystem_status = {
    'cpu': 'optimal',
    'memory': 'degraded',  # This triggers a penalty
    'disk': 'optimal',
    'network': 'unknown'
}

# Auxiliary lookup table for case conversion logic (partial distractor)
case_map = {'optimal': 'OPT', 'degraded': 'DEG', 'critical': 'CRT'}
status_codes = {key: case_map.get(value, 'UNK') for key, value in subsystem_status.items()}

# Bit manipulation red herring
critical_flag = 0b1001
mask = 0b0110
tamper_check = critical_flag ^ mask  # Computed but unused

# Set operations - actual relevant component
critical_types = {'throughput', 'error_rate'}
provided_types = {m['type'] for m in metrics}
missing_critical = critical_types - provided_types  # Empty set - all present

# Main evaluation logic buried among distractions
def evaluate_performance(met, base):
    score = 0
    
    # Relevance filtering via set intersection
    relevant_metrics = [m for m in met if m['type'] in critical_types]
    
    for m in relevant_metrics:
        val = m['value']
        if m['type'] == 'throughput':
            # Direct scoring
            score += val * base['weight_a']
        elif m['type'] == 'error_rate':
            # Inverse scoring
            score -= val * base['weight_b']
    
    # Apply offset from baseline
    score += base['offset']
    
    # Check memory status using string operation (case conversion)
    mem_status = subsystem_status['memory'].upper()
    if 'DEG' in mem_status:
        score -= 15  # Penalty applied
    
    # Early return red herring (never triggered due to data)
    if len(missing_critical) > 0:
        return -999
    
    # Linear search for debug flag (not active)
    for k, v in config.items():
        if k == 'debug_mode' and v:
            break  # Breaks but doesn't alter logic
    
    # Final scaling (this line is crucial)
    score *= base['scaling_factor']
    
    return int(score)

# Key execution point
final_score = evaluate_performance(metrics, baseline)

# Output the result as required
print(f"Result: {final_score}")