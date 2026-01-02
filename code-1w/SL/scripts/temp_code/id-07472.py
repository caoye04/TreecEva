import math

# Simulated sensor array data (irrelevant but plausible)
sensor_ids = [f'SEN-{i:03d}' for i in range(1, 16)]
sensor_readings = [round(math.sin(i) + math.cos(i * 1.5), 4) for i in range(15)]

# Irrelevant signal processing (red herring)
def apply_filter(signal):
    return [round(s * 0.9 + 0.1, 4) for s in signal]

filtered_data = apply_filter(sensor_readings)

# Decoy diagnostic computation (unused path)
baseline_offset = sum(filtered_data[:5]) / 5
reference_checksum = int(sum(ord(c) for c in sensor_ids[0]) * 100)

# Real data path begins here — hidden among distractions
raw_signals = [3, 7, 2, 8, 4, 6, 5]
weight_vector = [1, -1, 2, -2, 1, 0, -1]

# Weighted combination with distraction via zip and enumerate
weighted_sum = 0
for i, (signal, weight) in enumerate(zip(raw_signals, weight_vector)):
    if i % 2 == 0:
        weighted_sum += signal * weight + (i // 2)
    else:
        weighted_sum -= signal

# Misleading normalization (not used in final result)
normalized_score = round(weighted_sum / len(weight_vector), 3)

# Actual relevant logic buried in dictionary operations
aggregate_metrics = {
    "raw_index": abs(weighted_sum),
    "derived_factor": 0,
    "auxiliary_flag": False,
    "threshold_check": 0
}

# Conditional updates with decoy branches
if weighted_sum > 0:
    aggregate_metrics["derived_factor"] = 2 * weighted_sum
else:
    aggregate_metrics["derived_factor"] = -weighted_sum // 2

if abs(weighted_sum) % 3 == 0:
    aggregate_metrics["auxiliary_flag"] = True

# Key assignment hidden in loop over dictionary items (distraction)
for key, value in aggregate_metrics.items():
    if 'factor' in key and isinstance(value, int):
        aggregate_metrics[key] += 3

# Another red herring: list comprehension with side-effect-free transformation
transformed = [x ** 2 - x for x in raw_signals if x > 4]
sum_transformed = sum(transformed)

# Critical real operation — obscured by context
aggregate_metrics["threshold_check"] = len([x for x in weight_vector if x != 0])

# System load factor computed from irrelevant formula (but actually used)
timestamp_millis = 123456789
system_load_factor = (timestamp_millis % 11) / 10.0  # Evaluates to 9/10 = 0.9

# Final diagnostic — this is the target statement
final_diagnostic = aggregate_metrics["threshold_check"] * system_load_factor

# Print result for verification
print(f"Result: {final_diagnostic}")