import itertools

# Simulated system performance metrics (some relevant, some red herrings)
metrics = {
    'throughput': 847.5,
    'latency': 12.3,
    'cache_hit_ratio': 0.88,
    'power_draw_watts': 145.7,
    'core_temperature_c': 67.4,
    'instructions_per_cycle': 2.15,
    'memory_bandwidth_gbps': 98.2,
    'context_switches': 4321,
    'page_faults': 234,
    'disk_iops': 1876
}

# Benchmark weight mapping (only some keys are actually used)
benchmark_weights = {
    'throughput': 0.35,
    'latency': -0.25,
    'instructions_per_cycle': 0.30,
    'memory_bandwidth_gbps': 0.10,
    # Deliberately unused weights (distractors)
    'power_draw_watts': 0.05,
    'core_temperature_c': -0.02,
    'context_switches': -0.03,
    'page_faults': -0.04
}

# Irrelevant auxiliary data structures (red herrings)
def generate_placeholder_data(size):
    return [dict(id=i, flag=(i % 3 == 0), meta=f"X{i % 7}") for i in range(size)]

device_inventory = generate_placeholder_data(128)

# Unused transformation functions (dead code paths)
def normalize(value, min_val=0, max_val=100):
    return max(0, min(1, (value - min_val) / (max_val - min_val)))

def calculate_efficiency_rating(data):
    # This function is defined but never called
    total = sum(v * 0.1 for v in data.values() if isinstance(v, (int, float)))
    return round(total ** 0.5, 4)

# Decoy scoring using irrelevant metrics
temp_bias_score = 0
tier = ''
if metrics['core_temperature_c'] < 60:
    temp_bias_score = 10
    tier = 'A'
elif metrics['core_temperature_c'] < 70:
    temp_bias_score = 5
    tier = 'B'
else:
    temp_bias_score = -5
    tier = 'C'

# Simulated historical averages (unused but plausible)
historical_avg = {
    'throughput': 750.0,
    'latency': 15.0,
    'instructions_per_cycle': 1.9
}

# Complex nested helper that looks important but only a part is relevant
def adjust_for_architecture(metric_name, value):
    arch_scaling = {
        'throughput': [1.0, 1.05, 1.02],
        'latency': [1.0, 0.98, 1.01],
        'instructions_per_cycle': [1.0, 1.03]
    }
    base_factor = 1.0
    if metric_name in arch_scaling:
        for factor in arch_scaling[metric_name]:
            base_factor *= factor
    return value * base_factor

# Red herring: complex grouping with itertools (looks computational, not impactful)
expanded_metrics = []
for key, val in metrics.items():
    if isinstance(val, (int, float)):
        expanded_metrics.extend([(key, val * (i+1)) for i in range(2)])
pair_groups = itertools.groupby(expanded_metrics, key=lambda x: x[0])
grouped_stats = {}
for key, group in pair_groups:
    entries = list(group)
    grouped_stats[key] = {
        'count': len(entries),
        'sum': sum(x[1] for x in entries)
    }

# Actual relevant logic buried within distractions
def preprocess_metric(name, value):
    if name == 'latency':
        return 100 / value  # Inverse relationship: lower latency → higher score
    return value

def evaluate_component(name, value, weights):
    if name not in weights:
        return 0
    adjusted = adjust_for_architecture(name, preprocess_metric(name, value))
    return adjusted * weights[name]

def evaluate_performance(metrix, weights):
    # Note: typo in arg name to simulate noise; actual logic uses correct keys
    score = 0.0
    components_used = []
    
    # Only these three keys are actually contributing
    critical_keys = ['throughput', 'latency', 'instructions_per_cycle']
    
    for key in critical_keys:
        if key in metrix:
            contribution = evaluate_component(key, metrix[key], weights)
            score += contribution
            components_used.append(contribution)
    
    # Additional minor adjustment based on memory bandwidth (fourth concept)
    if 'memory_bandwidth_gbps' in metrix and metrix['memory_bandwidth_gbps'] > 90:
        score += metrix['memory_bandwidth_gbps'] * 0.05  # Bonus for high bandwidth
    
    return round(score, 6)

# Misleading intermediate computation (never used)
raw_sum = sum(v for v in metrics.values() if isinstance(v, (int, float)))
adjusted_sum = raw_sum * 0.87

# Key execution point
final_score = evaluate_performance(metrics, benchmark_weights)

# Output result as required
print(f"Result: {final_score}")