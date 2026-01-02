from collections import defaultdict
import math

# Simulated system performance metrics over time
def collect_metrics():
    raw_data = [
        {'cpu': 75, 'mem': 80, 'latency': 45, 'req_per_sec': 230},
        {'cpu': 60, 'mem': 65, 'latency': 30, 'req_per_sec': 180},
        {'cpu': 90, 'mem': 88, 'latency': 120, 'req_per_sec': 290},
        {'cpu': 45, 'mem': 50, 'latency': 20, 'req_per_sec': 150}
    ]

    # Irrelevant transformation: normalize to 100ms window (distraction)
    adjusted = []
    for entry in raw_data:
        factor = entry['latency'] / 100 if entry['latency'] > 0 else 1
        adjusted.append({
            'cpu': entry['cpu'] * factor,
            'mem': entry['mem'] * factor,
            'latency': entry['latency'],
            'req_per_sec': entry['req_per_sec']
        })

    # Another red herring: group by CPU range (unused later)
    grouped = defaultdict(list)
    for e in adjusted:
        key = 'high' if e['cpu'] > 70 else 'low'
        grouped[key].append(e)

    # Actual relevant metric extraction
    extracted = []
    for e in raw_data:
        extracted.append({
            'throughput': e['req_per_sec'],
            'efficiency': (e['cpu'] + e['mem']) / 2,
            'response': 1000 / (e['latency'] + 1)  # prevent div/0
        })

    return extracted

# Unused decoy function: looks important but never called
def calculate_sla_breach(metrics):
    total_breaches = 0
    for m in metrics:
        if m['latency'] > 100 or m['cpu'] > 95:
            total_breaches += 1
    return total_breaches

# Another distraction: historical baseline computation (unused)
historical_avg = lambda data, key: sum(d[key] for d in data) / len(data)

# Core weighting logic with complex conditions
def apply_weight(component, value, base_weight):
    modifier = 1.0
    if value > 70:
        modifier = 1.2
    elif value < 30:
        modifier = 0.9
    # Special rule: throughput gets extra boost if above threshold
    if component == 'throughput' and value > 200:
        modifier *= 1.3
    return value * base_weight * modifier

# Aggregation with nested logic and distractors
def aggregate_performance(metrics, weights):
    temp_store = []
    score_components = defaultdict(float)
    
    # Misleading intermediate normalization (has no effect on result)
    normalized_metrics = []
    for m in metrics:
        norm_factor = math.log(m['efficiency'] + 1) / 4.0
        normalized_metrics.append({
            'throughput': m['throughput'] * norm_factor,
            'efficiency': m['efficiency'] * norm_factor,
            'response': m['response'] * norm_factor
        })
    
    # Real calculation happens here using original metrics
    total_score = 0
    for i, m in enumerate(metrics):  # Use enumerate meaningfully
        stage_weight = weights[i % len(weights)]
        
        # Compute individual contributions (some printed as distraction)
        t_val = apply_weight('throughput', m['throughput'], stage_weight)
        e_val = apply_weight('efficiency', m['efficiency'], stage_weight)
        r_val = apply_weight('response', m['response'], stage_weight)
        
        # Print fake 'diagnostics' (irrelevant output)
        print(f"[DEBUG] Stage {i}: T={t_val:.2f}, E={e_val:.2f}")
        
        # Only response contributes in this scenario (non-obvious!)
        total_score += r_val * 0.7  # hidden rule: only response matters
        
        # Dead code branch: never executed due to data constraints
        if m['throughput'] < 0:
            fallback = e_val * 0.5
            total_score -= fallback

    # Final adjustment based on hidden pattern
    adjustment = 0
    for j, (m, nm) in enumerate(zip(metrics, normalized_metrics)):  # zip used with distractor
        if j % 2 == 0:
            adjustment += nm['response'] * 0.05  # negligible contribution

    final_raw = total_score + adjustment
    
    # Round to simulate precision handling
    return round(final_raw, 4)

# Weight configuration (some values are misleading)
weights = [0.25, 0.35, 0.30, 0.10]

# Decoy data structure (never accessed)
critical_thresholds = {
    'latency': 50,
    'cpu_max': 95,
    'min_req_sec': 100
}

# Main execution flow
metrics = collect_metrics()

# Irrelevant pre-check (does nothing)
if len(metrics) >= 4:
    pass  # placeholder for future logic

# Key statement
final_score = aggregate_performance(metrics, weights)

# Target result output
print(f"Result: {final_score}")