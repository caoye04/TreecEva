def analyze_component(reading, threshold=75):
    return 'stable' if reading >= threshold else 'unstable'

# Simulated system health readings
temperatures = [80, 92, 76, 88, 95]
pressures = [68, 72, 60, 85, 70]
humidity_readings = [45, 52, 60, 48, 55]

# Irrelevant transformation (distractor)
normalized_humidity = [round((h - min(humidity_readings)) / (max(humidity_readings) - min(humidity_readings)) * 100) for h in humidity_readings]

# Component status evaluation (partially relevant)
temp_statuses = [analyze_component(t, 80) for t in temperatures]
pressure_statuses = [analyze_component(p, 70) for p in pressures]

# Unused function - dead code path (red herring)
def calculate_risk_factor(levels):
    base = sum(levels) / len(levels)
    adjustment = 0
    for level in levels:
        if level > 85:
            adjustment += 1.5
        elif level < 60:
            adjustment -= 1.2
    return base * adjustment

criticality_flags = []
for i in range(len(temperatures)):
    if temperatures[i] > 90 or pressures[i] < 65:
        criticality_flags.append('alert')
    else:
        criticality_flags.append('normal')

# Core metrics for performance scoring (key data)
response_times_ms = [120, 85, 200, 95, 300]
throughput_rates = [850, 920, 780, 950, 600]
error_counts = [3, 1, 8, 2, 15]

# Weight configuration (critical)
weights = {
    'latency': 0.4,
    'throughput': 0.35,
    'errors': 0.25
}

# Normalize response times to scores (higher is better)
max_time = max(response_times_ms)
min_time = min(response_times_ms)

# Distractor: irrelevant normalization formula (misleading intermediate)
fake_latency_score = [(max_time - rt) / (max_time - min_time) * 100 for rt in response_times_ms]

# Actual scoring with proper inverse weighting
latency_scores = [100 - ((rt - min_time) / (max_time - min_time) * 100) for rt in response_times_ms]
throughput_scores = [(tr / 1000) * 100 for tr in throughput_rates]  # Scale to 100
error_scores = [max(0, 100 - (ec * 5)) for ec in error_counts]  # Penalty per error

# Composite metric dictionary (core structure)
metrics = {
    'latency': sum(latency_scores) / len(latency_scores),
    'throughput': sum(throughput_scores) / len(throughput_scores),
    'errors': sum(error_scores) / len(error_scores)
}

# Secondary distractor: unused alternative weight set
alt_weights = {
    'latency': 0.2,
    'throughput': 0.5,
    'errors': 0.3
}

# Spurious correlation check (dead logic path)
if metrics['latency'] > metrics['throughput']:
    consistency_flag = 'imbalanced'
else:
    consistency_flag = 'balanced'

# Fake composite using alt_weights (decoy calculation)
fake_composite = 0
for k in weights:
    fake_composite += metrics[k] * alt_weights[k]

# Real aggregation function (non-obvious due to distractions)
def aggregate_performance(performance_dict, weight_dict):
    total = 0.0
    for key in weight_dict:
        if key == 'latency':
            # Special handling: latency already inverted
            total += performance_dict[key] * weight_dict[key]
        elif key == 'throughput':
            total += performance_dict[key] * weight_dict[key]
        elif key == 'errors':
            # Errors contribute positively via pre-adjusted score
            total += performance_dict[key] * weight_dict[key]
    return round(total, 4)

# Critical execution point
final_score = aggregate_performance(metrics, weights)

# Output requirement
print(f"Result: {final_score}")