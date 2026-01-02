def analyze_system_load(usage_logs):
    peak_load = max(usage_logs)
    avg_load = sum(usage_logs) / len(usage_logs)
    normalized = [u / peak_load for u in usage_logs]
    variance = sum((x - avg_load) ** 2 for x in usage_logs) / len(usage_logs)
    efficiency = (1 - variance / (avg_load + 1)) if avg_load > 0 else 0
    return efficiency


def validate_checksum(data_sequence):
    checksum = 0
    for val in data_sequence:
        checksum ^= val
        checksum = (checksum << 1) % 256
    return checksum == 128


def transform_coordinates(coords):
    transformed = []
    for x, y in coords:
        radius = (x**2 + y**2)**0.5
        angle = (x + y) % (2 * 3.14159)
        transformed.append((radius * angle, radius))
    return transformed

# Irrelevant utility function (distractor)
def predictive_anomaly_detection(signal):
    moving_avg = [sum(signal[i:i+3]) / 3 for i in range(len(signal) - 2)]
    anomalies = [i for i, v in enumerate(moving_avg) if v > 0.8]
    return len(anomalies) > 5

# Key computation with distractors
usage_data = [120, 150, 130, 180, 160, 200, 140]
raw_metrics = {
    'latency': [0.45, 0.52, 0.48, 0.61, 0.55],
    'throughput': [88, 92, 85, 95, 90],
    'error_rate': [0.02, 0.01, 0.03, 0.015, 0.025],
    'memory_usage': [75, 78, 72, 80, 77]
}

# Distractor variables
signal_data = [0.1, 0.9, 0.85, 0.2, 0.78, 0.88, 0.15]
anomaly_flag = predictive_anomaly_detection(signal_data)

# Simulated sensor coordinates (irrelevant to final result)
sensor_grid = [(1, 2), (3, 4), (-1, 5), (2, -3)]
processed_coords = transform_coordinates(sensor_grid)

# Checksum validation on dummy sequence
data_packet = [10, 20, 30, 40, 50]
valid_packet = validate_checksum(data_packet)

# Core performance metrics influencing final score
system_efficiency = analyze_system_load(usage_data)
latency_score = 100 * (1 - sum(raw_metrics['latency']) / 5)
throughput_score = sum(raw_metrics['throughput']) / 5
stability_ratio = (min(raw_metrics['throughput']) + 1) / (max(raw_metrics['throughput']) + 1)

# Weighted aggregation inputs
metrics = [
    system_efficiency * 100,
    latency_score,
    throughput_score,
    stability_ratio * 50,
    len(processed_coords) * 10  # red herring: unrelated coordinate count
]

weights = [0.3, 0.25, 0.25, 0.15, 0.05]  # last weight de-emphasizes decoy

# Conditional adjustment based on irrelevant packet status
if valid_packet:
    weights[-1] *= 0.1  # further reduces impact of decoy

# Actual target computation
final_score = 0
for i in range(len(metrics)):
    final_score += metrics[i] * weights[i]

# Additional distraction: set operation with no effect
reported_alarms = {1, 3, 5, 7}
critical_alarms = {2, 4, 6}
pending_actions = reported_alarms - critical_alarms if len(critical_alarms) > 3 else reported_alarms | {9}

# Spurious rounding and integer division
temp_result = int(final_score // 1) + round((final_score % 1) * 100) / 100

# Final output
Result: {final_score}