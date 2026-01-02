import itertools

# System calibration constants (irrelevant to final result)
CALIBRATION_FACTOR = 0.987
TEMPORAL_OFFSET = 42
BASELINE_DRIFT = -1.3e-4

# Real-time sensor data stream simulation (some values relevant, others not)
sensor_readings = [15, -7, 22, 0, 31, -15, 8, 44, -3, 12]
timestamp_flags = [t % 7 for t in range(10)]

# Derived metrics - some used, most ignored
delta_rates = [abs(sensor_readings[i] - sensor_readings[i-1]) for i in range(1, len(sensor_readings))]
spike_indicators = [1 if x > 20 else 0 for x in sensor_readings]
accumulated_drift = sum(delta_rates) * BASELINE_DRIFT

# Core logic: signal conditioning and ranking
adjusted_readings = [x + CALIBRATION_FACTOR for x in sensor_readings]
ranked_values = [i for i, x in enumerate(adjusted_readings) if x > 10]

# Red herring: temporal alignment using unused sequence
temporal_pairs = list(itertools.combinations(timestamp_flags, 2))
weight_matrix = [[a * b for b in range(5)] for a in range(5)]

# Simulated fault detection (dead code path - never executed)
def detect_anomaly(sequence):
    return any(s < -10 for s in sequence)

# Decoy transformation chain
transformed_signal = []
for val in adjusted_readings:
    if val < 0:
        transformed_signal.append(val ** 2)
    elif val > 30:
        transformed_signal.append(val // 3)
    else:
        transformed_signal.append(val + 5)

# Actual critical computation path
binary_flags = [1 if x >= 0 else 0 for x in sensor_readings]
polarity_sequence = list(itertools.accumulate(binary_flags))
indexed_ranks = [r * polarity_sequence[i] for i, r in enumerate(ranked_values)]

# Misleading intermediate aggregation (looks important, unused)
aggregated_profile = max(indexed_ranks, default=0) + min(indexed_ranks, default=0)

# Signal filtration based on dynamic thresholds
threshold_map = {i: v * 0.75 for i, v in enumerate(adjusted_readings)}
filtered_ranks = [r for r in ranked_values if adjusted_readings[r] > threshold_map[r]]

# Key assignment statement
filtration_score = sum(filtered_ranks)

# Dead code - visual distraction
redundant_check = [x for x in filtered_ranks if x in temp_combinations := list(itertools.permutations([1,2], 2))]

# Output the target result
print(f"Result: {filtration_score}")