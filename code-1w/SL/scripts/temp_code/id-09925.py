def apply_factor(value, flag):
    return value * 1.5 if flag else value * 0.8

# Simulate a multi-stage system equilibrium with noise filtering
input_stream = [3, 7, -2, 4, 6]
filter_threshold = 5
noise_count = 0
smoothed_values = []

for x in input_stream:
    if abs(x) < filter_threshold:
        smoothed_values.append(x + 0.5)
    else:
        noise_count += 1
        smoothed_values.append(x * 0.9)

# Secondary transformation with conditional scaling
transformed = list(map(lambda v: v ** 2 if v > 0 else abs(v), smoothed_values))

# Accumulate energy and baseline metrics (some are distractions)
energy_sum = sum(transformed)
baseline_offset = len(input_stream) * 0.3
adjustment_factor = 2 if energy_sum > 30 else 1

# Core state computation with distractor variables
state_log = {}
duplicate_tracker = set()
equilibrium_score = 0

for idx, val in enumerate(transformed):
    if idx % 2 == 0:
        equilibrium_score += val / (idx + 1)
    else:
        equilibrium_score -= val * 0.1

    # Distractor computations
    running_avg = (energy_sum + baseline_offset) / (idx + 1)
    state_log[idx] = {'value': val, 'avg': running_avg}
    duplicate_tracker.add(val)

# Irrelevant dictionary aggregation
summary_stats = {
    'count': len(transformed),
    'max_val': max(transformed),
    'flags': [True, False, True],
    'meta': {k: v['avg'] for k, v in state_log.items()}
}

# Final adjustment depends on bias condition (determined heuristically)
bias_flag = noise_count > 2
intermediate_result = equilibrium_score + summary_stats['count'] * 0.1  # semi-relevant
final_adjustment = apply_factor(equilibrium_score, bias_flag)
print(f"Result: {equilibrium_score}")