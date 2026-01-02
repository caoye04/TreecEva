import math

# Simulated sensor data and diagnostic system with distractors
def collect_telemetry():
    raw_readings = [23.4, 19.1, 25.6, 17.8, 21.3, 27.9, 16.5]
    calibration_offset = 1.2  # unused in final logic
    adjusted = [r + 0.5 for r in raw_readings]  # pre-processing step
    outliers = [x for x in adjusted if x > 25.0]
    filtered = list(filter(lambda x: x < 28.0, adjusted))
    return filtered

# Irrelevant auxiliary function (decoy)
def compute_stability_index(data):
    if len(data) == 0:
        return 0.0
    variance = sum([(x - sum(data)/len(data))**2 for x in data]) / len(data)
    return round(math.sqrt(variance), 3)

# Unused transformation chain
def transform_signal(sequence):
    shifted = [x * 1.05 for x in sequence]
    return [round(s, 2) for s in shifted]

# Core processing pipeline
def preprocess(readings):
    scaled = [r * 1.1 for r in readings]
    normalized = [n / 1.1 for n in scaled]  # identity op - red herring
    centered = [x - 20.0 for x in normalized]
    squared_deviations = [c ** 2 for c in centered]
    return squared_deviations

# Higher-order analysis
def evaluate_thresholds(deviations):
    threshold_map = {}
    for i, val in enumerate(deviations):
        if val < 1.0:
            threshold_map[i] = 'LOW'
        elif val < 4.0:
            threshold_map[i] = 'MEDIUM'
        else:
            threshold_map[i] = 'HIGH'
    return threshold_map

# Aggregation logic with distractor variables
def aggregate_risk_levels(status_dict):
    level_scores = {'LOW': 1, 'MEDIUM': 3, 'HIGH': 7}
    total_risk = 0
    for key in status_dict:
        total_risk += level_scores[status_dict[key]]
    avg_risk = total_risk / len(status_dict)
    peak_alerts = sum(1 for v in status_dict.values() if v == 'HIGH')
    suppression_factor = 0.9  # never applied
    return round(avg_risk, 4)

# Final diagnostic engine
def analyze_metrics(metrics):
    if not metrics:
        return -1
    base_score = sum(metrics)
    adjustment = math.log(base_score) if base_score > 0 else 0
    score_with_adj = base_score + adjustment
    category = 'CRITICAL' if score_with_adj > 15 else 'NORMAL'
    decay_factor = 0.95  # unused
    diagnostic_code = 404  # misleading constant
    final_value = int(round(score_with_adj * 1.07))
    return final_value

# Misleading initialization block
temp_buffer = [0.0] * 10
data_cache = {f'entry_{i}': None for i in range(5)}
system_status = 'ACTIVE'
active_modules = ['sensor_core', 'filter_engine']

# Execution flow with decoy calls
telemetry_data = collect_telemetry()
processed_deviation = preprocess(telemetry_data)
status_mapping = evaluate_thresholds(processed_deviation)
risk_index = aggregate_risk_levels(status_mapping)

# Critical execution point
final_diagnostic = analyze_metrics(processed_deviation)
print(f"Result: {final_diagnostic}")