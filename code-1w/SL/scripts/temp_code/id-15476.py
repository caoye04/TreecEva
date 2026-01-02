import itertools

def analyze_risk_factors(data_points):
    # Irrelevant risk analysis with decoy logic
    threshold = 75
    high_risk = [x for x in data_points if x > threshold]
    return len(high_risk) > 3

def preprocess_signals(raw_inputs):
    # Distractor: signal filtering that isn't used later
    filtered = [x for x in raw_inputs if x % 2 == 1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized

def compute_entropy(values):
    # Dead function - looks important but unused
    from math import log
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * log(p) for p in probs if p > 0)

def extract_key_indicators(log_entries):
    # Processes logs but only one field matters
    critical_flags = []
    timestamps = []
    for entry in log_entries:
        parts = entry.split('|')
        level = parts[1].strip()
        message = parts[2].strip()
        if 'ERROR' in level or 'CRITICAL' in message:
            critical_flags.append(1)
        timestamps.append(parts[0])  # Unused
    return sum(critical_flags)

def validate_checksum(structured_data):
    # Complex-looking validation that doesn't affect final result
    checksum = 0
    for item in structured_data:
        if isinstance(item, dict):
            for k, v in item.items():
                checksum ^= hash(str(k)) ^ hash(str(v))
    return checksum % 100 == 0

def transform_metrics(raw_measures):
    # Actual relevant transformation
    adjusted = []
    for val in raw_measures:
        if val < 0:
            adjusted.append(abs(val) ** 0.5)
        elif val == 0:
            adjusted.append(0.5)
        else:
            adjusted.append(val * 0.9 + 0.1)
    return adjusted

def combine_via_policy(weights, metrics):
    # Weighted combination using tuple unpacking and comparisons
    total = 0.0
    for w, m in zip(weights, metrics):
        policy_cap = 85.0 if w > 0.5 else 95.0
        effective_metric = min(m, policy_cap)
        total += w * effective_metric
    return total

def evaluate_performance(weight_dict, outcome_list):
    # Main evaluation with distractors
    temp_results = []
    decoy_accum = 0
    
    # Real processing path
    processed = transform_metrics(outcome_list)
    
    # Irrelevant list comprehensions
    outliers = [x for x in processed if x > 90]
    suppression_factor = len(outliers) * 0.05 if outliers else 0.0
    
    # Multiple dictionary operations (only some matter)
    metric_names = ['latency', 'throughput', 'reliability', 'accuracy']
    weight_tuples = list(weight_dict.items())
    sorted_weights = sorted(weight_tuples, key=lambda x: x[1], reverse=True)
    
    # Extract weights in order
    extracted_weights = [w for _, w in sorted_weights]
    
    # Linear search for a condition that never triggers (red herring)
    fallback_applied = False
    for name, wt in sorted_weights:
        if name == 'bandwidth_emulation':
            fallback_applied = True
            break
    
    # Core calculation
    raw_score = combine_via_policy(extracted_weights, processed)
    
    # Decoy recursion - looks complex but unused
    def recursive_discount(n, base):
        if n <= 0:
            return base
        return 0.95 * recursive_discount(n-1, base)
    
    # String method distraction
    log_snapshot = "ERROR|WARNING|INFO|CRITICAL"
    alerts = log_snapshot.split('|')
    alert_count = len([a for a in alerts if len(a) > 4])
    
    # Final adjustment - this is where answer comes from
    final_adjustment = raw_score * (1 - suppression_factor)
    
    # Key variable assignment
    final_score = int(round(final_adjustment))
    
    # Unused itertools example
    permutations = list(itertools.permutations([1,2,3]))[:2]  # computed but not used
    
    return final_score

# Simulated input data
metric_weights = {
    'latency': 0.4,
    'throughput': 0.3,
    'reliability': 0.2,
    'accuracy': 0.1
}

raw_outcomes = [88, -49, 0, 92]

# Additional irrelevant variables
system_uptime = 99.97
maintenance_window = "2023-12-01T02:00:00Z"
emergency_override = False
audit_trail = set()

# Call the main function
final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Target result: {final_score}")