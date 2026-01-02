def analyze_trend(data, threshold=0.5):
    above_threshold = list(filter(lambda x: x > threshold, data))
    below_threshold = [x for x in data if x <= threshold]
    trend_value = len(above_threshold) - len(below_threshold)
    dummy_calc_1 = sum(x ** 0.5 for x in above_threshold) if above_threshold else 0
    return trend_value


def compute_bias(sequence):
    positive_count = sum(1 for x in sequence if x > 0)
    negative_count = sum(1 for x in sequence if x < 0)
    total = len(sequence)
    if total == 0:
        return 0.0
    bias_ratio = (positive_count - negative_count) / total
    temp_debug = [bias_ratio * i for i in range(3)]  # Dead computation
    return bias_ratio

# Simulated sensor drift correction metrics
data_stream = [0.1, 0.7, 0.3, 0.9, 0.4, 0.6, 0.2]

# Irrelevant transformations
transformed = [round(x * 2 + 0.1, 2) for x in data_stream]
sorted_data = sorted(transformed)
mid_vals = sorted_data[1:-1]  # Middle values, not used later

# Core metrics
raw_trend = analyze_trend(data_stream)
bias_metric = compute_bias([0.1, -0.3, 0.2, -0.1])

# Weighting scheme with red herring
weights = {
    'trend': 3,
    'bias': 2,
    'dummy_factor': 0  # Unused weight
}

# Additional irrelevant state tracking
status_flags = set()
if raw_trend > 0:
    status_flags.add('positive_trend')
if abs(bias_metric) > 0.1:
    status_flags.add('significant_bias')

# Distractor variables
baseline_adjustment = 0.05 * len(data_stream)
adjusted_trend = raw_trend + int(baseline_adjustment)
dummy_aggregation = sum(mid_vals) / len(mid_vals) if mid_vals else 0

metrics = {
    'trend_strength': adjusted_trend,
    'bias_score': abs(bias_metric),
    'volume': len(data_stream)
}

# Final evaluation using lambda in calculation
penalty_func = lambda b: 2 if b > 0.25 else 0
penalty = penalty_func(metrics['bias_score'])

final_score = evaluate_performance(metrics, weights)

# Redefine function to ensure clarity and correctness
def evaluate_performance(met, w):
    base = met['trend_strength'] * w['trend']
    adjustment = met['bias_score'] * w['bias']
    # Ignore dummy_factor since it's zero
    temp_log = {'base': base, 'adjustment': adjustment}  # Debug structure
    result = base - adjustment - penalty  # Final logic step
    return int(result)

Result: final_score