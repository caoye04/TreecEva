from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'type': 'cpu', 'value': 78, 'active': True},
    {'type': 'mem', 'value': 85, 'active': True},
    {'type': 'disk', 'value': 45, 'active': False},
    {'type': 'net', 'value': 92, 'active': True}
]

# Irrelevant baseline thresholds (distractor)
baseline_thresholds = defaultdict(lambda: 50)
baseline_thresholds['cpu'] = 80
baseline_thresholds['mem'] = 85
baseline_thresholds['disk'] = 60
baseline_thresholds['gpu'] = 70

# Misleading auxiliary function (dead path)
def analyze_health_legacy(data):
    return sum([d['value'] * 0.1 for d in data if d['type'] in ['cpu', 'mem']])

# Decoy metrics (irrelevant computations)
stale_metric = sum((x['value'] + 10) for x in telemetry_stream if x['value'] > 50)
shadow_weight = math.log(stale_metric + 1) if stale_metric > 0 else 0
temporal_bias = [i * 0.5 for i in range(4)]

# Real processing begins here
metric_data = {item['type']: item['value'] for item in telemetry_stream if item['active']}

# Complex conditional transformation with list comprehension and filtering
transformed = [
    (k, v ** 0.5 if k == 'cpu' else v / 10) 
    for k, v in metric_data.items() 
    if v > 40 or k == 'disk'
]

# Secondary distraction: character counting in keys (seemingly meaningful but unused)
key_chars = sum(len(k) for k in metric_data.keys())

# Another red herring: bitwise manipulation on unrelated constants
dummy_flag = 0b1010 ^ 0b1100 & 0b1111
flag_shift = (dummy_flag << 3) | 0b0001

# Core logic disguised among distractions
def compute_normalization(values):
    total = sum(values)
    return [v / total for v in values] if total > 0 else [0] * len(values)

# Simulated weights (some are irrelevant)
weight_map = {'cpu': 0.4, 'mem': 0.35, 'net': 0.25, 'io': 0.1}

# Critical intermediate (misleading name)
effective_load = sum(
    weight_map.get(t, 0) * (metric_data[t] / 100) 
    for t in metric_data
)

# Real evaluation logic hidden in abstraction
def evaluate_performance(metrics):
    # Extract relevant components
    cpu_val = metrics.get('cpu', 0)
    mem_val = metrics.get('mem', 0)
    net_val = metrics.get('net', 0)
    
    # Logical conditions with short-circuiting (relevant)
    if cpu_val >= 75 and (mem_val >= 80 or net_val > 90):
        base_score = 95
    elif cpu_val < 75 and net_val > 90:
        base_score = 70
    else:
        base_score = 50
    
    # Bonus calculation using list comprehension and math
    bonuses = [
        10 if cpu_val > 80 else 5,
        8 if mem_val > 84 else 0,
        int(net_val / 10) if net_val > 90 else 0
    ]
    
    # Final adjustment using counter (collections module usage)
    bonus_counter = Counter(bonuses)
    total_bonus = sum(bonus_counter.values()) * 1.2  # artificial multiplier
    
    # Actual answer computation
    final_raw = base_score + total_bonus
    
    # Distractor: unused transformed data
    unused_result = [math.sin(x[1]) for x in transformed]
    
    return int(final_raw)

# Execution point of interest
final_score = evaluate_performance(metric_data)

# Print result as required
print(f"Result: {final_score}")