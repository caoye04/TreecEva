def analyze_system_load(usage_data):
    peak = max(usage_data)
    avg = sum(usage_data) / len(usage_data)
    variance = sum((x - avg) ** 2 for x in usage_data) / len(usage_data)
    threshold_alert = True if peak > 90 else False
    normalized = [(x - avg) / (variance ** 0.5) for x in usage_data]
    return variance, threshold_alert, normalized


def transform_features(raw_inputs):
    processed = []
    for val in raw_inputs:
        if val < 0:
            processed.append(abs(val) ** 0.5)
        elif val == 0:
            processed.append(0.1)
        else:
            processed.append(val ** 0.3)
    reversed_scaled = processed[::-1]
    return [round(x * 1.07, 4) for x in reversed_scaled]


def compute_robustness_score(config_matrix):
    score = 0
    for row in config_matrix:
        for elem in row:
            if elem % 2 == 0:
                score += elem // 4
            else:
                score -= elem % 3
    return score + len(config_matrix) * len(config_matrix[0])

# Irrelevant utility function (dead code path)
def legacy_compat_check(data):
    if isinstance(data, dict):
        return sum(len(v) for v in data.values()) % 7 == 0
    return False

# Misleading intermediate variables
temp_log = [12, 45, 67, 89, 23, 56]
buffer_cache = {'a': 10, 'b': 20, 'c': 30}
shadow_weights = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

# Simulated sensor metrics (some relevant, some distractors)
sensor_readings = [88, 76, 92, 85, 79, 94]
adjusted_metrics = [x for x in sensor_readings if x > 75]
drift_compensation = sum(x > 90 for x in sensor_readings) * 1.5

# Apply transformation to metrics
filtered_metrics = transform_features(adjusted_metrics)

# Real-time system load analysis
variance, alert_flag, norm_usage = analyze_system_load(sensor_readings)

# Configuration robustness check (distractor)
config_grid = [[4, 6, 8], [5, 9, 2], [7, 3, 1]]
robustness_index = compute_robustness_score(config_grid)

# Weight vector with decoy elements
weights = {
    'base': 0.4,
    'drift': drift_compensation * 0.05,
    'stability': 0.3,
    'legacy': 0.0,
    'fallback': 0.1
}

# Core evaluation logic
metrics = {
    'base': sum(filtered_metrics[:3]),
    'peak_adjust': max(filtered_metrics) - min(filtered_metrics),
    'consistency': 1 / (variance + 1)
}

# Unused but plausible computation (red herring)
avg_filtered = sum(filtered_metrics) / len(filtered_metrics)
penalty_factor = 0.9 if alert_flag else 1.0

# Key statement: combines multiple sources, including distractors
final_score = 0
for key in ['base', 'peak_adjust', 'consistency']:
    if key in metrics and key in weights:
        final_score += metrics[key] * weights[key]

# Injecting a conditional expression distraction
final_score = final_score * (0.95 if robustness_index > 10 else 1.0) + (weights['fallback'] * 5 if 'fallback' in weights else 0)

# Distractor: slicing on unrelated data
dummy_slice = temp_log[2:5:1]

# Output target result
Result: {final_score}