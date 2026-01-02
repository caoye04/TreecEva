import math

# Simulated sensor data processing pipeline for environmental monitoring system
def process_readings(raw_data):
    filtered = [x for x in raw_data if x > -50 and x < 1000]
    normalized = [round(math.log(abs(x) + 1), 3) for x in filtered]
    return normalized

# Irrelevant auxiliary function - decoy
def calculate_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return round(total, 4)

# System calibration constants (some are red herrings)
baseline_offset = 23.7
timing_drift = 0.008
phase_shift = 1.414
phase_offset = int(baseline_offset // 5)  # Evaluates to 4

# Simulated multi-sensor input (temperature readings in millidegrees)
sensor_bank_a = [1250, -450, 8900, 10203, 567, -999, 8765, 2345]
sensor_bank_b = [9876, 1100, 432, 7654, 3210, 6543, 2109]

# Process primary sensor stream
processed_a = process_readings(sensor_bank_a)
processed_b = process_readings(sensor_bank_b)

# Misleading intermediate fusion (unused later)
fused_stream = []
for i in range(min(len(processed_a), len(processed_b))):
    fused_stream.append((processed_a[i] + processed_b[i]) / 2)

# Real processing path begins here
primary_signal = processed_a[1:-1]  # Slice out first and last elements
smoothed = []
for i in range(1, len(primary_signal) - 1):
    smoothed.append(sum(primary_signal[i-1:i+2]) / 3)

# Secondary transformation with slicing
transformed = [math.sin(x / 10) for x in smoothed[::2]]

# Aggregate calculation chain
aggregation_weights = [0.8, 1.1, 0.9, 1.2]
aggregate_metrics = []
for i, val in enumerate(transformed):
    weighted = val * aggregation_weights[i % len(aggregation_weights)]
    adjusted = abs(weighted) * 100
    aggregate_metrics.append(round(adjusted, 2))

# Dead code path - never executed but looks important
if len(aggregate_metrics) > 10:
    backup_result = sum(aggregate_metrics) / len(aggregate_metrics)
    outlier_removed = [x for x in aggregate_metrics if x < backup_result]

# Critical execution point
final_diagnostic = aggregate_metrics[-1] + phase_offset

# Print target result
print(f"Target result: {final_diagnostic}")