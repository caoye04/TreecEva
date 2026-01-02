def analyze_efficiency(values):
    weighted_sum = sum([v * (i + 1) for i, v in enumerate(values)])
    normalization_factor = max(values) if values else 1
    return weighted_sum / normalization_factor if normalization_factor != 0 else 0


def calculate_entropy(data):
    from math import log2
    total = sum(data)
    if total == 0:
        return 0
    probabilities = [d / total for d in data]
    entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)


def track_progress(items):
    status_log = {}
    for idx, item in enumerate(items):
        key = f'item_{idx}'
        status_log[key] = 'completed' if item > 0 else 'pending'
    return len([v for v in status_log.values() if v == 'completed'])


# Simulate system diagnostics
metrics = [8, 5, 12, 7, 3, 9]
diagnostic_codes = [-1, 0, 1, 0, -1]
activity_flags = [True, False, True, True, False, True]

# Irrelevant preprocessing
shifted_metrics = [m + 2 for m in metrics if m % 2 == 0]
skewed_values = [abs(c) * 3 for c in diagnostic_codes]
active_count = len([f for f in activity_flags if f])

# Core computation chain
base_efficiency = analyze_efficiency(metrics)
entropy_level = calculate_entropy(metrics)
completion_rate = track_progress(metrics)

# Dummy state tracking
system_state = {"efficiency": base_efficiency, "entropy": entropy_level}
state_keys = list(system_state.keys())
key_count = len(state_keys)

# Secondary derived measures
temp_adjustment = sum(skewed_values) / (len(skewed_values) + 1)
baseline = base_efficiency * 0.8

# Conditional adjustment based on multiple factors
if completion_rate > 4 and entropy_level < 2.5:
    adjustment_factor = 1.25
else:
    adjustment_factor = 0.9

productivity = (base_efficiency + completion_rate) * adjustment_factor
risk_factor = entropy_level * temp_adjustment * 0.5

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Placeholder function to resolve final score
def evaluate_performance(perf, risk):
    if perf <= 0:
        return 0
    score = (perf * 2.0) - (risk * 3.5)
    return int(score) if score >= 0 else abs(int(score))

# Print result
Target result: {final_score}