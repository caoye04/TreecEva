from collections import defaultdict, Counter
import math

# Simulated sensor readings and diagnostic flags
temperature_readings = [23.4, 24.1, 22.9, 25.5, 26.0, 24.8, 23.9]
humidity_readings = [55, 57, 53, 60, 62, 58, 56]
pressure_readings = [1013, 1015, 1012, 1018, 1020, 1016, 1014]

# Irrelevant signal processing (distractor)
def apply_filter(data):
    smoothed = []
    for i in range(len(data)):
        window = data[max(0, i-1):min(i+2, len(data))]
        smoothed.append(sum(window) / len(window))
    return [round(x, 2) for x in smoothed]

filtered_temp = apply_filter(temperature_readings)
filtered_humid = apply_filter(humidity_readings)

# Diagnostic codes from hardware (some relevant, some red herrings)
diag_codes = ['OK_200', 'WARN_512', 'INFO_101', 'ERR_999', 'OK_200', 'WARN_512']
code_counter = Counter(diag_codes)

# System status mapping (partially used)
status_severity = {
    'OK_200': 0,
    'INFO_101': 1,
    'WARN_512': 2,
    'ERR_999': 3
}

total_severity = sum(status_severity[code] * count for code, count in code_counter.items())

# Environmental risk assessment (mostly irrelevant)
risk_matrix = defaultdict(int)
for t in temperature_readings:
    for h in humidity_readings:
        if t > 25 and h > 60:
            risk_matrix['high_risk'] += 1
        elif t > 24 and h > 55:
            risk_matrix['moderate_risk'] += 1

# Core algorithm: performance metric calculation (hidden among noise)
base_metrics = []
for i in range(len(temperature_readings)):
    temp_norm = (temperature_readings[i] - 20) / 5
    humid_norm = (humidity_readings[i] - 40) / 20
    press_norm = abs(pressure_readings[i] - 1015) / 10
    score = temp_norm * 0.4 + humid_norm * 0.3 - press_norm * 0.3
    base_metrics.append(round(score, 3))

# Bit manipulation layer for 'data integrity check' (misleading)
checksum = 0
for val in pressure_readings:
    checksum ^= int(val)
    checksum = (checksum << 1) % 1024

# Decoy function that looks important but isn't used
def calculate_system_health(logs, weights):
    total = 0
    for log in logs:
        for w in weights:
            total += math.sqrt(abs(log - w * 10))
    return total / (len(logs) * len(weights) + 1)

# Real processing begins: extract quality indicators
validity_flags = [1 if 22 <= t <= 26 and 50 <= h <= 65 else 0 
                  for t, h in zip(temperature_readings, humidity_readings)]

# Construct composite metric set
metric_set = {
    'mean_base': sum(base_metrics) / len(base_metrics),
    'stability': sum(1 for b in base_metrics if abs(b) < 0.5),
    'consistency_ratio': len([v for v in validity_flags if v]) / len(validity_flags),
    'outlier_count': sum(1 for b in base_metrics if abs(b) > 0.8),
    'temp_variance': sum((x - sum(temperature_readings)/len(temperature_readings))**2 
                        for x in temperature_readings) / len(temperature_readings)
}

# Evaluation function with conditional logic and nested checks
def evaluate_performance(metrics):
    # Hidden intermediate transformation
    adjusted_stability = metrics['stability'] - metrics['outlier_count']
    if adjusted_stability < 0:
        adjusted_stability = 0
    
    # Complex weighting scheme (key to answer)
    safety_component = metrics['consistency_ratio'] * 400
    precision_component = (3 - metrics['temp_variance']) * 50
    reliability_component = min(adjusted_stability, 4) * 75
    
    # Red herring: unused component
    fake_component = math.log(1 + metrics['mean_base'] ** 2) * 100
    
    # Critical calculation
    raw_score = safety_component + precision_component + reliability_component
    
    # Normalization with ceiling
    if raw_score > 500:
        raw_score = 500 + (raw_score - 500) / 2
    
    # Final adjustment based on diagnostic severity (minor influence)
    if total_severity > 5:
        penalty = (total_severity - 5) * 15
        raw_score -= penalty
    
    return int(round(raw_score))

# Execute main evaluation
temp_debug = [x for x in base_metrics if x > 0]  # Dead code path
final_score = evaluate_performance(metric_set)
print(f"Result: {final_score}")