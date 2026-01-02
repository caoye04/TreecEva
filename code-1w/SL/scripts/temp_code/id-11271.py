def analyze_trend(data, threshold=0.5):
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    trend_ratio = len(above_threshold) / len(below_threshold) if below_threshold else float('inf')
    return trend_ratio

# Simulated sensor readings over time (normalized)
sensor_readings = [0.6, 0.4, 0.7, 0.3, 0.8, 0.2, 0.9]

# Irrelevant transformation: reverse slicing without assignment impact
temp_slice = sensor_readings[::-1]
ignored_value = sum([x**2 for x in temp_slice[:3]])  # Dead-end calc

# Data windowing for stability analysis
stable_window = sensor_readings[1:6]
drift_detected = any(stable_window[i] > stable_window[i+1] for i in range(len(stable_window)-1))

def evaluate_consistency(measurements):
    diffs = [abs(measurements[i] - measurements[i-1]) for i in range(1, len(measurements))]
    avg_diff = sum(diffs) / len(diffs)
    consistency_flag = 'stable' if avg_diff < 0.25 else 'unstable'
    return avg_diff, consistency_flag

# Compute auxiliary metrics with partial reuse
average_deviation, status = evaluate_consistency(sensor_readings)

# Secondary analysis: outlier detection using conditional expression
outlier_count = sum(1 for x in sensor_readings if x < 0.35 or x > 0.85)
severity_level = 'high' if outlier_count >= 3 else 'moderate' if outlier_count >= 1 else 'low'

# Dummy state tracker (distractor)
current_state = {'phase': 'analysis', 'version': 1.2, 'debug_mode': False}
current_state['last_updated'] = 'N/A'

# Core logic disguised among side computations
def calculate_baseline_adjustment():
    base = sum(sensor_readings) / len(sensor_readings)
    adjustment_factor = 1.0 + (0.1 * (len([x for x in sensor_readings if x > 0.7]) - len([x for x in sensor_readings if x < 0.3])))
    return base * adjustment_factor

baseline = calculate_baseline_adjustment()

# Final performance metric integrates multiple concepts
impact_weights = [1.2, 0.8, 1.5, 0.6, 1.1, 0.7, 1.3]
weighted_impact = sum(val * weight for val, weight in zip(sensor_readings, impact_weights))

# Misleading complex expression that doesn't affect final result
phantom_metric = (lambda x: x ** 2 + 2 * x + 1)(len(sensor_readings)) if len(sensor_readings) > 5 else 0

# Key statement — target of question
def calculate_performance_metric():
    trend = analyze_trend(sensor_readings, threshold=0.5)
    normalized_trend = trend if trend != float('inf') else 10.0
    consistency_bonus = 1.1 if status == 'stable' else 0.9
    raw_score = baseline * normalized_trend * consistency_bonus
    final_correction = 0.95 if severity_level == 'moderate' else 1.0
    return int(raw_score * weighted_impact * final_correction)

final_score = calculate_performance_metric()
print(f"Result: {final_score}")