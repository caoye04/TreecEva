import math

# Irrelevant helper function (dead code path)
def unused_calculate_entropy(data):
    return sum(-x * math.log2(x) for x in data if x > 0)

# Misleading auxiliary computation
temp_weights = [0.1, 0.3, 0.4, 0.2]
weighted_sum = sum(w * (i + 1) for i, w in enumerate(temp_weights))

# Real configuration dictionary
benchmark_config = {
    'threshold': 0.75,
    'penalty_factor': 0.9,
    'bonus_multiplier': 1.2,
    'decay_rate': 0.95,
    'stages': 3
}

# Simulated performance metrics from system logs
raw_data = [0.81, 0.72, 0.88, 0.64, 0.91]

# Distractor transformation (not used in final calculation)
normalized = [(x - min(raw_data)) / (max(raw_data) - min(raw_data)) for x in raw_data]

# Actual relevant metrics processing
metrics = {
    'avg_accuracy': sum(raw_data) / len(raw_data),
    'peak_count': len([x for x in raw_data if x >= 0.8]),
    'consistency_ratio': len([x for x in raw_data if x >= benchmark_config['threshold']]) / len(raw_data),
    'variance': sum((x - sum(raw_data)/len(raw_data))**2 for x in raw_data) / len(raw_data)
}

# Unused lambda (red herring)
decoy_transform = lambda x: x ** 2 + 1

# Complex conditional expression with embedded logic
initial_base = metrics['avg_accuracy'] * 100 if metrics['consistency_ratio'] > 0.6 else 50

# Bit manipulation distraction (irrelevant)
flag_mask = 0b101010
activation_flag = flag_mask & 0b111100

# Multiple assignments that look important but only some matter
total_stages, bonus_awarded, penalty_applied = benchmark_config['stages'], False, False

# Dictionary-based dynamic adjustment rules
adjustment_rules = {
    'high_peak': lambda m: m['peak_count'] >= 3,
    'stable_perf': lambda m: m['variance'] < 0.01,
    'exceed_threshold': lambda m: m['avg_accuracy'] > 0.75
}

# Evaluate conditions using dictionary lookup and logical operations
conditions_met = [
    adjustment_rules['high_peak'](metrics),
    adjustment_rules['stable_perf'](metrics),
    adjustment_rules['exceed_threshold'](metrics)
]

# Another decoy variable (misleading intermediate)
theoretical_max = 100 * benchmark_config['bonus_multiplier']

# Conditional bonus assignment (actual logic branch)
if all(conditions_met[:2]):
    bonus_awarded = True
elif conditions_met[2] and metrics['consistency_ratio'] > 0.8:
    bonus_awarded = True
else:
    penalty_applied = True

# Core calculation chain with nested logic
running_score = initial_base

for stage in range(total_stages):
    if bonus_awarded:
        running_score *= benchmark_config['bonus_multiplier']
    elif penalty_applied:
        running_score *= benchmark_config['penalty_factor']
    else:
        running_score *= benchmark_config['decay_rate']

    # Early termination red herring (never triggers due to data)
    if running_score < 40:
        break

# Final adjustment using lambda and dictionary get method
final_modifier = (lambda c: c.get('bonus_multiplier') if bonus_awarded else c.get('penalty_factor'))(benchmark_config)

# Critical execution point
final_score = round(running_score * final_modifier, 4)

# Irrelevant set operation (distractor)
unique_caps = set(str(int(final_score)) + str(int(benchmark_config['threshold'] * 100)))

count_of_digits = len(unique_caps)

# Output the target result
print(f"Result: {final_score}")