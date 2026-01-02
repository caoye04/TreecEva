import math

# Irrelevant helper function (dead code path)
def deprecated_normalize(x):
    return x / sum(x)

# Misleading transformation chain
def transform_signal(values):
    shifted = [v * 1.5 for v in values]
    filtered = [s for s in shifted if s > 5]
    return [math.log(f + 1) for f in filtered]

# Decoy metric calculation with unused result
def compute_legacy_metric(records):
    base = sum(records) / len(records)
    penalty = 0.85 if base < 10 else 0.95
    return base * penalty ** 2

# Core processing with distractors
data_snapshot = [
    12, 15, 9, 20, 7, 14, 18, 11, 16, 13,
    25, 6, 19, 10, 17, 8, 21, 12, 14, 9
]

# Unused intermediate aggregations (distractors)
max_value = max(data_snapshot)
min_value = min(data_snapshot)
avg_value = sum(data_snapshot) / len(data_snapshot)
median_approx = sorted(data_snapshot)[len(data_snapshot)//2]

# Red herring: bit manipulation on irrelevant subset
subset_for_bits = data_snapshot[::3]
bit_encoded = 0
for val in subset_for_bits:
    bit_encoded ^= (val << 2) | (val >> 1)

# Simulated time decay weights (not actually used in final logic)
time_weights = [math.exp(-i * 0.1) for i in range(len(data_snapshot))]
weighted_sum = sum(v * w for v, w in zip(data_snapshot, time_weights))

# Key lambda abstraction for dynamic filtering
effective_filter = lambda threshold: list(filter(lambda x: x > threshold, data_snapshot))

# Conditional expression chain with early exit pattern
def evaluate_stability(measurements):
    if len(measurements) < 5:
        return 0.0
    
    # First-level analysis
    high_freq = effective_filter(14)
    low_freq = [x for x in measurements if x <= 14]
    
    if not high_freq:
        return 1.0
    
    # Second-level derived metrics
    ratio = len(high_freq) / len(low_freq) if low_freq else float('inf')
    variance = sum((x - avg_value) ** 2 for x in measurements) / len(measurements)
    
    # Complex conditional logic with nesting depth 3
    if ratio > 1.2:
        if variance < 20:
            adjustment_factor = 0.8
        else:
            adjustment_factor = 1.1
    elif ratio < 0.8:
        if max_value - min_value > 15:
            adjustment_factor = 1.3
        else:
            adjustment_factor = 0.9
    else:
        adjustment_factor = 1.0
    
    # Composite score computation (core relevant logic)
    base_score = sum(high_freq) * adjustment_factor
    penalty_rate = 0.05 * len([x for x in data_snapshot if x < 10])
    adjusted_score = base_score * (1 - penalty_rate)
    
    # Final thresholding using multiple concepts
    normalized_impact = adjusted_score / (len(high_freq) or 1)
    return round(normalized_impact, 3)

# Secondary transformation with decoy output
def generate_diagnostics(trace):
    stats = {}
    stats['peak'] = max(trace)
    stats['range'] = stats['peak'] - min(trace)
    stats['entropy'] = -sum((t / sum(trace)) * math.log(t / sum(trace)) for t in trace if t > 0)
    return stats

# Main processing function combining multiple paradigms
def process_metrics(log_data):
    # Level 1: Filtering and grouping
    critical_band = effective_filter(15)
    support_band = [x for x in log_data if 10 <= x < 15]
    outlier_count = len([x for x in log_data if x > 22])
    
    # Level 2: Counting and averaging with lambda
    average_critical = sum(critical_band) / len(critical_band) if critical_band else 0
    growth_rate = (lambda x: sum(i > j for i, j in zip(x[1:], x[:-1])) / len(x))(log_data)
    
    # Level 3: Boolean logic and control flow
    is_expanding = growth_rate > 0.5
    has_outliers = outlier_count > 2
    meets_threshold = len(critical_band) >= 6
    
    # Deeply nested decision structure (nesting level 4)
    if meets_threshold:
        if is_expanding:
            if has_outliers:
                base_multiplier = 1.75
            else:
                base_multiplier = 1.45
        else:
            if sum(support_band) > 50:
                base_multiplier = 1.25
            else:
                base_multiplier = 0.95
    else:
        if avg_value > 12:
            base_multiplier = 1.1
        else:
            base_multiplier = 0.8
    
    # Final computation chain
    raw_composite = average_critical * base_multiplier
    volatility_adjustment = 1 - (outlier_count * 0.05)
    final_composite = raw_composite * volatility_adjustment
    
    # Key assignment: this is the target variable
    threshold_score = int(round(final_composite * 2.1))
    
    # Dead code: unreachable branch
    if False:
        fallback = evaluate_stability(log_data)
        threshold_score = int(fallback * 100)
    
    return locals()  # Ensures all variables remain in scope

# Execute main logic
result_dict = process_metrics(data_snapshot)
threshold_score = result_dict['threshold_score']

# Print result as required
print(f"Target result: {threshold_score}")