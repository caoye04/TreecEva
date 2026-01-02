import math

# Simulated system metrics for performance evaluation
def collect_metrics():
    raw_data = [
        {'cpu': 78.2, 'mem': 63.1, 'latency': 45, 'requests': 980},
        {'cpu': 82.5, 'mem': 70.3, 'latency': 52, 'requests': 1100},
        {'cpu': 65.0, 'mem': 55.0, 'latency': 38, 'requests': 890},
        {'cpu': 91.8, 'mem': 75.4, 'latency': 61, 'requests': 1200},
        {'cpu': 73.4, 'mem': 59.2, 'latency': 41, 'requests': 950}
    ]

    # Irrelevant transformation - red herring
    processed = [{
        'usage': (d['cpu'] + d['mem']) / 2,
        'efficiency': d['requests'] / (d['latency'] + 1)
    } for d in raw_data]

    # Decoy function embedded inside
    def analyze_trend(data):
        return sum(d['cpu'] for d in data) / len(data)

    trend = analyze_trend(raw_data)  # Unused result

    # Distractor: complex but unused data structure
    stats_tree = {
        'root': {
            'left': {'value': math.floor(raw_data[0]['cpu'])},
            'right': {
                'left': {'value': int(raw_data[1]['mem'])},
                'right': {'value': raw_data[2]['requests']}
            }
        }
    }

    # Actual relevant extraction
    extracted = []
    for entry in raw_data:
        if entry['cpu'] > 75:
            extracted.append(entry['latency'])
    
    return extracted

# Baseline configuration with decoy fields
baseline_config = {
    'thresholds': {
        'cpu_high': 75,
        'latency_critical': 55,
        'memory_warning': 70
    },
    'weights': [0.4, 0.3, 0.3],
    'version': '2.1.0',
    'calibration': lambda x: x * 1.05,  # Never invoked
    'deprecated_flag': True
}

# Core evaluation logic with nested reasoning
def evaluate_performance(log, config):
    # Extract values above CPU threshold
    high_cpu_latencies = log

    # Compute average latency for high-CPU periods
    avg_latency = sum(high_cpu_latencies) / len(high_cpu_latencies)

    # Determine penalty tiers
    penalty = 0
    if avg_latency > config['thresholds']['latency_critical']:
        penalty += 15
    elif avg_latency > 50:
        penalty += 8
    else:
        penalty += 3

    # Bonus calculation based on distribution
    sorted_latencies = sorted(high_cpu_latencies)
    median = sorted_latencies[len(sorted_latencies) // 2]
    if median <= 50:
        penalty -= 5  # Bonus for good median

    # Redundant dictionary operation - distractor
    metadata_map = {i: f"sample_{i}" for i in range(len(high_cpu_latencies))}
    reverse_lookup = {v: k for k, v in metadata_map.items()}
    total_keys = len(reverse_lookup)

    # Unused combinatorics distraction
    combinations = 0
    n = len(high_cpu_latencies)
    if n > 2:
        combinations = (n * (n - 1)) // 2  # C(n,2)

    # Final scoring with modular arithmetic twist
    base_score = 100
    adjusted = base_score - penalty
    
    # Apply cyclic correction based on number of observations
    cycle_factor = (len(high_cpu_latencies) ** 2) % 7
    final_adjustment = (adjusted + cycle_factor) * 0.97

    # Hidden rounding behavior
    final_score = math.floor(final_adjustment) if final_adjustment % 1 > 0.5 else round(final_adjustment)

    # Dead code path - never executed due to logic
    if False and total_keys > 100:
        fallback = 0
        for k in reverse_lookup:
            fallback += ord(k[0])
        final_score = fallback // 10

    # Return point
    return final_score

# Misleading pre-initialization
interim_result = None
debug_trace = []

# Primary execution flow
metrics_log = collect_metrics()
final_score = evaluate_performance(metrics_log, baseline_config)

# Output requirement
print(f"Result: {final_score}")