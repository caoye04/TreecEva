import itertools

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    raw_data = [78, 85, 92, 67, 88, 73, 90, 82]
    noise_floor = 5
    adjusted = [x - noise_floor for x in raw_data]
    return {
        'latency': sum(adjusted[::2]) / len(adjusted[::2]),
        'throughput': sum(adjusted[1::2]),
        'error_rate': len([x for x in adjusted if x < 70]),
        'peak_utilization': max(adjusted),
        'stability': adjusted[-1] - adjusted[0],
        'redundant_metric_a': sum(x * x for x in adjusted) % 100,
        'placeholder_b': 0,
        'dummy_flag': True
    }

# Legacy weight configuration (partially deprecated)
def get_weights_legacy():
    return {
        'latency': 0.3,
        'throughput': 0.25,
        'error_rate': -0.2,
        'peak_utilization': 0.15,
        'stability': 0.1,
        'redundant_metric_a': 0.0,
        'internal_only': 0.05  # Unused in current model
    }

# Active weight configuration
weights = {
    'latency': 0.25,
    'throughput': 0.3,
    'error_rate': -0.15,
    'peak_utilization': 0.2,
    'stability': 0.1,
    'redundant_metric_a': 0.05,  # Distractor: looks relevant but scaled down
    'placeholder_b': 0.0,
    'junk_factor': 0.01  # Decoy weight
}

# Secondary processing chain – appears important but feeds into unused path
def transform_metrics_secondary(m):
    m['throughput'] = m['throughput'] * 1.1
    m['latency'] = m['latency'] * 0.95
    m['derived_enhancement'] = (m['peak_utilization'] - m['error_rate'] * 10) * 0.5
    return m

# Unused recursive validator (dead code path)
def validate_structure(obj, depth=0):
    if depth > 3 or not isinstance(obj, dict):
        return False
    if 'error_rate' in obj and obj['error_rate'] > 10:
        return False
    return all(validate_structure(v, depth + 1) for v in obj.values())

# Redundant transformation using itertools (distractor)
def generate_combinations(data_dict):
    values = [v for k, v in data_dict.items() if isinstance(v, (int, float)) and k != 'dummy_flag']
    pairs = list(itertools.combinations(values, 2))
    return sum(abs(a - b) for a, b in pairs[:10])  # Computation done but not used

# Main evaluation logic
metrics = collect_metrics()

# Apply secondary transformation (modifies metrics but some fields ignored later)
transformed_metrics = transform_metrics_secondary(metrics.copy())

# Generate combination score (computed but not used – red herring)
combination_noise = generate_combinations(transformed_metrics)

# Validate structure (called but result unused – misleading call)
validation_result = validate_structure(transformed_metrics)

# Weighted scoring with selective field usage
def evaluate_performance(met, wts):
    score = 0.0
    used_fields = ['latency', 'throughput', 'error_rate', 'peak_utilization', 'stability']
    for field in used_fields:
        if field in met and field in wts:
            score += met[field] * wts[field]
    # Apply non-linear bonus if stability is positive (rarely triggered)
    if met['stability'] > 0:
        bonus = (met['stability'] ** 1.5) * 0.05
        score += bonus
    # Decoy conditional – looks like correction but never activates in this case
    if met.get('dummy_flag') and met.get('placeholder_b') > 5:
        score *= 0.9
    return score

# Final computation
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")