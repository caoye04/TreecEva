def analyze_component_health(health_flags):
    return sum(1 for h in health_flags if h == 'CRITICAL')

# Irrelevant helper function (dead code path)
def deprecated_normalization(data):
    return [x / max(data) for x in data]

# Misleading preprocessing block (distractor)
temp_weights = [0.1, 0.2, 0.3, 0.4]
adjusted_weights = []
for w in temp_weights:
    if w > 0.25:
        adjusted_weights.append(w * 1.5)
    else:
        adjusted_weights.append(w * 0.8)

# Unused transformation map (red herring)
transform_map = {
    'A': lambda x: x ** 2,
    'B': lambda x: x + 10,
    'C': lambda x: x * 0.5
}

# Real data pipeline starts here
raw_metrics = [85, 90, 78, 92, 88]

# Bitwise encoding of metric categories (relevant but obfuscated)
category_mask = 0
for i, val in enumerate(raw_metrics):
    if val > 80:
        category_mask |= (1 << i)

# Simulate sensor drift correction (irrelevant computation)
sensor_drift = 0.037
compensated_metrics = [round(m - sensor_drift * i, 3) for i, m in enumerate(raw_metrics)]

# Destructuring assignment with mixed relevance
primary_metric, *secondary_set = raw_metrics

# Dictionary-based threshold mapping (core concept)
thresholds = {
    'optimal': 85,
    'warning': 70,
    'failure': 50
}

# Conditional aggregation with early exit (relevant logic)
def aggregate_stability(metrics, config=None):
    if not config:
        config = {'window': 3, 'tolerance': 5}
    
    stability_log = []
    for i in range(len(metrics) - config['window'] + 1):
        window = metrics[i:i+config['window']]
        if max(window) - min(window) <= config['tolerance']:
            stability_log.append(True)
        else:
            return len(stability_log)  # early return
    return len(stability_log)

# Recursive depth calculation on binary representation (key logic)
def recursive_bit_depth(n, depth=0):
    if n <= 1:
        return depth
    return recursive_bit_depth(n // 2, depth + 1)

# Complex data transformation with dictionary lookups
metric_data = {
    'values': raw_metrics,
    'mask': category_mask,
    'baseline': sum(raw_metrics) / len(raw_metrics),
    'flags': ['NORMAL'] * len(raw_metrics)
}

# Update flags based on thresholds (relevant update)
for i, v in enumerate(metric_data['values']):
    if v < thresholds['warning']:
        metric_data['flags'][i] = 'WARNING'
    if v < thresholds['failure']:
        metric_data['flags'][i] = 'FAILURE'

# Decoy combinatorics block (heavy distractor)
def count_combinations(n, r):
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator

# Unused combination analysis
combination_grid = {}
for size in range(2, 5):
    combination_grid[size] = count_combinations(len(raw_metrics), size)

# Core evaluation function (contains answer path)
def evaluate_performance(data, refs):
    base = data['baseline']
    critical_count = data['flags'].count('FAILURE')
    
    # Apply bitwise mask analysis
    active_high = bin(data['mask']).count('1')
    
    # Recursive depth of total mask
    depth_score = recursive_bit_depth(data['mask'])
    
    # Dictionary lookup chain
    level = 'optimal'
    if base < refs[level]:
        level = 'warning'
    if base < refs[level]:
        level = 'failure'
    
    # Primary computation
    adjustment = 0
    if level == 'optimal':
        adjustment = 10
    elif level == 'warning':
        adjustment = 0
    else:
        adjustment = -15
    
    # Final formula (answer derivation)
    raw_score = base * active_high
    penalty = critical_count * 25
    final = int(raw_score - penalty + adjustment + depth_score)
    
    return final

# Benchmark reference values
benchmarks = dict(thresholds)  # copy
benchmarks['optimal'] = 82  # override for tolerance

# Execution point of interest
final_score = evaluate_performance(metric_data, benchmarks)

# Dead code: post-processing that doesn't affect result
if final_score > 100:
    final_score = 100 + (final_score % 10)

# Additional red herring: unused tuple unpacking
eval_summary = (final_score, category_mask, len(adjusted_weights))
dummy_a, dummy_b, _ = eval_summary

# Print target result
print(f"Result: {final_score}")