from collections import defaultdict, Counter

# Simulated sensor network data processing with red herrings
def process_sensor_readings(raw_data):
    readings_count = len(raw_data)
    valid_readings = []
    anomalies = []
    temp_accumulator = 0
    spike_count = 0

    # Irrelevant transformation - distractor
    transformed = [x * 1.05 for x in raw_data if x > 0]
    backup_copy = transformed[:]

    for i, val in enumerate(raw_data):
        if val < -100 or val > 100:
            anomalies.append(i)
            continue
        if val > 85:
            spike_count += 1
        temp_accumulator += val * 0.9
        valid_readings.append(val)

    # Decoy calculation - never used later
    decoy_metric = sum(backup_copy) / len(backup_copy) if backup_copy else 0

    # Real processing path begins here
    filtered = [x for x in valid_readings if x != 0]
    avg_filtered = sum(filtered) / len(filtered) if filtered else 0

    # Bit manipulation red herring
    binary_flags = 0
    for v in filtered[:5]:
        binary_flags ^= int(v) & 0xF

    # Conditional expression distraction
    status_flag = 'high' if spike_count > 3 else 'normal' if spike_count > 0 else 'low'
    
    # Meaningless nested structure
    stats = defaultdict(lambda: 'N/A')
    stats['count'] = readings_count
    stats['spikes'] = spike_count
    stats['anomalies'] = len(anomalies)

    # Another decoy function inside scope
    def calculate_entropy(data):
        freqs = Counter(data)
        total = len(data)
        from math import log2
        return -sum((freq / total) * log2(freq / total) for freq in freqs.values())

    entropy_proxy = len(set(valid_readings))  # Not real entropy but looks related

    # Core logic buried in distractions
    base_score = 0
    for idx, value in enumerate(filtered):
        if idx % 2 == 0:
            base_score += value * 1.1
        else:
            base_score -= value * 0.2

    # Secondary irrelevant aggregation
    cumulative_trend = 0
    for j in range(1, len(filtered)):
        cumulative_trend += filtered[j] - filtered[j-1]

    # Key intermediate variables
    aggregate_score = abs(base_score) + len(valid_readings)

    # Complex conditional expression - looks important but simplified
    adjustment_factor = 0.1 if avg_filtered > 20 else 0.05
    adjustment_factor += 0.05 if len(anomalies) < 5 else -0.02
    adjustment_factor = max(0.01, adjustment_factor)

    # Dead code path - unreachable due to logic
    if status_flag == 'critical':
        adjustment_factor *= 2
    elif status_flag == 'emergency':
        adjustment_factor *= 3

    # Critical statement where target variable is computed
    final_diagnostic = aggregate_score * (1 + adjustment_factor)

    # Unused tuple unpacking - syntactic noise
    _, _, _ = (1, 2, 3) if binary_flags else (0, 0, 0)

    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Generate deterministic input
import math
input_data = []
for k in range(15):
    angle = k * math.pi / 6
    reading = int(50 * math.sin(angle) + 20 * math.cos(angle * 1.5))
    input_data.append(reading)

# Add known anomaly
input_data[7] = 150  # outlier

# Execute
process_sensor_readings(input_data)