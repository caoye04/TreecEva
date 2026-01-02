def analyze_system_load(inputs):
    # Irrelevant preprocessing: normalize inputs (not used in final calculation)
    normalized = [round((x - min(inputs)) / (max(inputs) - min(inputs)) * 100) for x in inputs]
    thresholds = { 'low': 30, 'medium': 70, 'high': 90 }
    load_categories = []
    for val in normalized:
        if val < thresholds['low']:
            load_categories.append('idle')
        elif val < thresholds['medium']:
            load_categories.append('moderate')
        else:
            load_categories.append('heavy')
    # Dead code path — never called
    def legacy_reweight(val):
        return val * 0.85 if val > 80 else val * 1.1
    # Unused transformation
    inverted = list(map(lambda x: 100 - x, normalized))
    return load_categories

# Simulate sensor readings (distractor data)
sensor_data = [23, 45, 67, 89, 12, 77, 95]
_ = analyze_system_load(sensor_data)

# Core evaluation logic — mixed arithmetic, dictionary ops, lambda, conditionals
baseline_metrics = {
    'response_time_ms': 142,
    'error_rate': 0.04,
    'throughput': 870,
    'availability': 0.997,
    'latency_jitter': 18
}

# Weight mapping using dictionary and lambdas (some weights are decoys)
raw_weights = {
    'response_time_ms': lambda w: w * 1.2,
    'error_rate': lambda w: w * 2.1,
    'throughput': lambda w: w * 0.9,
    'availability': lambda w: w * 1.5,
    'latency_jitter': lambda w: w * 1.3,
    'deprecated_metric': lambda w: w * 0.5  # unused key
}

# Actual weights applied (only some are relevant)
active_keys = ['response_time_ms', 'error_rate', 'throughput', 'availability']
weights = {k: raw_weights[k](1.0) for k in active_keys}

# Secondary distraction: hypothetical scenario scaling
hypothetical_scale = 1.17
projected_metrics = {}
for k, v in baseline_metrics.items():
    if k == 'error_rate' or k == 'availability':
        projected_metrics[k] = round(v * hypothetical_scale, 4)
    else:
        projected_metrics[k] = int(v * 1.05)

# Real metric adjustment with branching logic and bit manipulation
adjusted_metrics = {}
for key in baseline_metrics:
    val = baseline_metrics[key]
    if key == 'response_time_ms':
        # Apply decay factor and bit shift for 'optimization level'
        opt_level = 3
        adjusted = (val * 0.87) >> opt_level  # Right shift by 3 bits
        adjusted_metrics[key] = round(adjusted)
    elif key == 'error_rate':
        adjusted_metrics[key] = val ** 2  # Penalty via squaring
    elif key == 'throughput':
        # Conditional boost based on availability threshold
        base_avail = baseline_metrics['availability']
        boost_factor = 1.15 if base_avail >= 0.995 else 1.05
        adjusted_metrics[key] = int(val * boost_factor)
    elif key == 'availability':
        # Convert to minutes of downtime per month for complexity
        uptime_minutes = int(30 * 24 * 60 * val)
        total_minutes = 30 * 24 * 60
        adjusted_metrics[key] = total_minutes - uptime_minutes  # downtime
    elif key == 'latency_jitter':
        # XOR-based smoothing (bitwise red herring)
        smoothed = val ^ 7  # arbitrary XOR mask
        adjusted_metrics[key] = max(smoothed, 10)

# Combine only specific adjusted metrics using weighted sum
relevant_pairs = {
    'response_time_ms': 'time_penalty',
    'error_rate': 'error_penalty',
    'throughput': 'throughput_bonus',
    'availability': 'downtime_penalty'
}

mapped_values = {}
for orig, mapped in relevant_pairs.items():
    if orig == 'response_time_ms':
        mapped_values[mapped] = adjusted_metrics[orig] * weights[orig] * -1
    elif orig == 'error_rate':
        mapped_values[mapped] = adjusted_metrics[orig] * 100 * weights[orig] * 2
    elif orig == 'throughput':
        mapped_values[mapped] = adjusted_metrics[orig] / 10 * weights[orig]
    elif orig == 'availability':
        # Higher downtime = worse score
        mapped_values[mapped] = adjusted_metrics[orig] * -0.5 * weights[orig]

# Final aggregation with conditional bonus
base_total = sum(mapped_values.values())

# Bonus logic: if error penalty below threshold, add innovation credit
innovation_credit = 0
if mapped_values['error_penalty'] < 50:
    innovation_credit = 25
    extra_boost = lambda x: x * 1.5  # defined but not used

# Penalize high time penalty
overhead_deduction = 0
if mapped_values['time_penalty'] < -20:
    overhead_deduction = 15

final_score = base_total + innovation_credit - overhead_deduction

# Distractor: unused performance tiers
performance_tier = ''
tiers = ['basic', 'standard', 'premium', 'enterprise']
tier_thresholds = [0, 50, 100, 150]
for i in range(len(tier_thresholds)-1, -1, -1):
    if final_score >= tier_thresholds[i]:
        performance_tier = tiers[i]
        break

# Unused composite structure
summary_report = {
    'metrics': adjusted_metrics,
    'weights_applied': weights,
    'raw_contributions': mapped_values,
    'bonus_deductions': {
        'innovation': innovation_credit,
        'overhead': overhead_deduction
    },
    'final_numeric_score': final_score
}

# Key execution point
final_score = calculate_performance(baseline_metrics, weights)

# Define the real calculation function (this overrides previous logic)
def calculate_performance(metrics, weight_map):
    # Independent clean calculation to avoid confusion with prior steps
    rt = metrics['response_time_ms']
    er = metrics['error_rate']
    tp = metrics['throughput']
    av = metrics['availability']

    # Use lambda for dynamic weighting
    scale = lambda x, factor: round(x * factor)

    # Core formula: mix of arithmetic and logical decisions
    time_score = scale(100 - (rt / 10), 1.2)  # max 100, scaled
    error_score = scale((1 - er) * 100, 1.8)
    throughput_score = scale(tp / 10, 0.7)
    availability_score = scale(av * 100, 1.4)

    # Conditional adjustment: synergy bonus if all above median
    if time_score > 50 and error_score > 50 and throughput_score > 50 and availability_score > 50:
        synergy = 8
    else:
        synergy = 0

    # Weighted combination
    total = (
        time_score * 0.25 +
        error_score * 0.30 +
        throughput_score * 0.20 +
        availability_score * 0.15
    ) + synergy

    # Final nonlinear transformation
    if total > 75:
        total = total * 0.95 + 5
    elif total > 60:
        total = total * 1.02
    else:
        total = total * 0.98

    return round(total, 4)

# Recompute final_score using correct function
calculate_performance = calculate_performance  # redundant reassignment (distraction)
final_score = calculate_performance(baseline_metrics, weights)

print(f"Target result: {final_score}")