import math

# Simulated system performance metrics (some are red herrings)
def generate_diagnostics():
    return {
        'latency_ms': 120,
        'throughput_ops': 450,
        'error_rate': 0.03,
        'cpu_util': 78.5,
        'mem_usage_mb': 2048,
        'queue_depth': 15,
        'retry_count': 4,
        'timeout_events': 2
    }

def transform_metrics(raw):
    # Relevant transformation: normalize latency to seconds and invert for scoring
    normalized = {
        'response_time': raw['latency_ms'] / 1000.0,
        'success_rate': 1 - raw['error_rate'],
        'efficiency': raw['throughput_ops'] / (raw['cpu_util'] + 1)
    }
    
    # Distractor computations (dead code path - not used later)
    if raw['mem_usage_mb'] > 1024:
        overhead = math.log(raw['mem_usage_mb'] / 512)
        penalty = 0.1 * overhead
    else:
        overhead = 0
        penalty = 0
    
    # More irrelevant transformations
    stability_score = (10 - raw['retry_count']) * (10 - raw['timeout_events'])
    queue_warning = True if raw['queue_depth'] > 10 else False
    
    # This is actually unused but looks important
    diagnostic_summary = [
        f"Load: {raw['cpu_util']}%",
        f"Errors: {raw['error_rate']:.2%}"
    ]
    
    return normalized

def calculate_risk_factors(data):
    # Completely irrelevant function — distractor
    risk = 0
    if data['response_time'] > 0.1:
        risk += 2
    if data['success_rate'] < 0.97:
        risk += 1
    if data['efficiency'] < 5:
        risk += 3
    return risk

# Weighting schema — only some weights are actually applied
default_weights = {
    'response_time': 0.4,
    'success_rate': 0.35,
    'efficiency': 0.25,
    'stability': 0.1  # Unused weight — misleading
}

# Core evaluation logic
def score_component(value, max_val=1.0, reverse=False):
    """Normalize a metric to 0-1 scale."""
    score = value / max_val
    return 1 - score if reverse else score

eval_hooks = [
    lambda x: score_component(x, 0.2, reverse=True),      # response_time max at 200ms -> 0.2s
    lambda x: score_component(x, 1.0),                   # success_rate already in [0,1]
    lambda x: score_component(x, 10.0)                  # efficiency capped at 10
]

def evaluate_performance(metrics, weight_schema):
    # Extract relevant values in order
    ordered_values = [
        metrics['response_time'],
        metrics['success_rate'],
        metrics['efficiency']
    ]
    
    # Apply scoring functions via list comprehension — core computation
    scaled_scores = [
        hook(val) for hook, val in zip(eval_hooks, ordered_values)
    ]
    
    # Weighted sum — actual answer determined here
    weights = [weight_schema['response_time'], weight_schema['success_rate'], weight_schema['efficiency']]
    weighted_total = sum(s * w for s, w in zip(scaled_scores, weights))
    
    # Distractor: complex but unused calculation
    geo_mean = math.exp(sum(math.log(max(s, 1e-9)) for s in scaled_scores) / len(scaled_scores))
    adjusted = weighted_total * (0.95 if geo_mean < 0.8 else 1.0)
    
    # Irrelevant tuple unpacking — looks significant
    backup_levels = ('low', 'medium', 'high')
    primary, _, _ = backup_levels
    
    # Final aggregation
    final_raw = weighted_total * 100  # Scale to percentage-like score
    
    # Additional decoy logic
    if final_raw > 90:
        category = 'excellent'
    elif final_raw > 75:
        category = 'good'
    else:
        category = 'needs_improvement'
    
    return int(round(final_raw))  # Deterministic integer result

# Auxiliary function that appears important but isn't used
def audit_trail(entries):
    count = 0
    for k, v in entries.items():
        if isinstance(v, (int, float)) and v > 0:
            count += 1
    return [(k, v) for k, v in entries.items() if v == max(entries.values())]

# Main execution flow
if __name__ == '__main__':
    raw_metrics = generate_diagnostics()
    processed = transform_metrics(raw_metrics)
    
    # This call looks like it affects something but doesn’t change outcome
    risk_level = calculate_risk_factors(processed)
    
    # Critical statement
    final_score = evaluate_performance(processed, default_weights)
    
    # Print result as required
    print(f"Result: {final_score}")
