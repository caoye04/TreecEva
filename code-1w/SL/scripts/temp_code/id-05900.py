import math

# Irrelevant helper function (dead code path)
def unused_network_check(hosts):
    return len([h for h in hosts if h.startswith('192.')])

# Misleading metric accumulator with decoy logic
def accumulate_signals(values):
    temp_result = 0
    for v in values:
        if v % 3 == 0:
            temp_result += v ** 0.5
        elif v % 2 == 0:
            temp_result -= v // 4
    return temp_result  # Never used in final calculation

# Red herring data structure
decoys = {
    'outlier_1': 999,
    'outlier_2': -888,
    'flagged': True,
    'aux_data': [10, 20, 30, 40]
}

# Core transformation pipeline
transformation_map = {
    'factor_a': lambda x: x * 1.5,
    'factor_b': lambda x: x + math.log(x) if x > 1 else 0,
    'factor_c': lambda x: x ** 0.75
}

# Simulated sensor readings (irrelevant to final result but looks important)
sensor_readings = {
    'temp': [23.5, 24.1, 22.9],
    'pressure': [101.3, 100.7, 102.1],
    'humidity': [45, 47, 44]
}

# Actual input data for evaluation
metric_data = [8, 12, 16, 20]

# Benchmark thresholds (used in filtering)
benchmarks = {
    'threshold_low': 10,
    'threshold_high': 18,
    'weighting': { 'w1': 0.4, 'w2': 0.6 }
}

# Distractor: complex-looking but unused bitwise computation
def bit_analysis(x):
    shifted = (x << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return bin(toggled).count('1')

# Auxiliary transformation with side appearance of relevance
def preprocess_entry(val, cfg):
    if val < cfg['threshold_low']:
        return transformation_map['factor_a'](val)
    elif val > cfg['threshold_high']:
        return transformation_map['factor_c'](val)
    else:
        return transformation_map['factor_b'](val)

# Secondary processing chain (partially used)
def filter_and_weight(items, config):
    weighted_parts = []
    for item in items:
        processed = preprocess_entry(item, config)
        # Only items in middle range contribute to final score
        if config['threshold_low'] <= item <= config['threshold_high']:
            weighted_parts.append(processed * config['weighting']['w2'])
        else:
            # These are computed but not used
            _ = processed * config['weighting']['w1']
    return weighted_parts

# Main evaluation logic
variance_table = set()
for d in metric_data:
    variance_table.add(d % 7)

# Conditional override based on set size
adjustment_factor = 1.2 if len(variance_table) >= 3 else 0.8

# Real work happens here
intermediate_results = filter_and_weight(metric_data, benchmarks)

# Final aggregation using dictionary lookup and adjustment
correction_map = {4: 5.5, 5: 6.0, 6: 7.2}
base_sum = sum(intermediate_results)

# Key statement
final_score = base_sum * adjustment_factor + correction_map.get(len(variance_table), 0)

# Output target result
print(f"Target result: {final_score}")