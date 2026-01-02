import itertools

# Simulated sensor data and calibration parameters
data_stream = [0.88, 0.91, 0.76, 0.94, 0.85, 0.79, 0.92, 0.87]
calibration_factors = [1.02, 0.99, 1.01, 1.03, 0.98, 1.00, 1.04, 0.97]

# Irrelevant baseline thresholds (distractor)
thresh_low = 0.75
thresh_high = 0.95
count_in_range = sum(1 for x in data_stream if thresh_low < x < thresh_high)

# Noise filter using set operations (partially relevant but overcomplicated)
valid_indices = set(range(0, len(data_stream), 2))
filtered_data = [data_stream[i] for i in range(len(data_stream)) if i in valid_indices]

# Weight generation with itertools cycle (red herring)
cycle_gen = itertools.cycle([0.5, 0.75, 1.0])
generated_weights = [next(cycle_gen) for _ in range(8)]

# Actual signal processing begins here
weighted_signal = [
    data_stream[i] * calibration_factors[i]
    for i in range(len(data_stream))
]

# Compute moving average over 3 points (distraction from core logic)
moving_avg = [
    sum(weighted_signal[i:i+3]) / 3
    for i in range(len(weighted_signal) - 2)
]

# Focus metric: variance of first half vs second half
first_half = weighted_signal[:4]
second_half = weighted_signal[4:]
mean_first = sum(first_half) / len(first_half)
mean_second = sum(second_half) / len(second_half)
var_first = sum((x - mean_first)**2 for x in first_half) / len(first_half)
var_second = sum((x - mean_second)**2 for x in second_half) / len(second_half)

# Optimization heuristic based on variance ratio (misleading intermediate)
if var_first > var_second:
    adjustment_factor = 1.1
else:
    adjustment_factor = 0.9

# Core weight optimization (critical path)
optimized_weights = [
    (weighted_signal[i] ** 2) / (calibration_factors[i] + 0.1)
    for i in range(len(weighted_signal))
]

# Secondary irrelevant transformation (dead path)
sorted_pairs = sorted(zip(data_stream, generated_weights), key=lambda x: x[0], reverse=True)
top_4_values = [p[1] for p in sorted_pairs[:4]]
sum_top_4 = sum(top_4_values)

# Auxiliary diagnostic log (decoy output)
diagnostic_checksum = 0
for i, val in enumerate(weighted_signal):
    diagnostic_checksum += int(val * 100) ^ (i + 1)

# Key function that computes final result
def process_metrics(weights):
    total = 0.0
    for w in weights:
        if w > 0.8:
            total += w * 1.2
        elif w > 0.6:
            total += w * 0.8
        else:
            total += w * 0.5
    # Apply adjustment factor from earlier (false dependency?)
    total *= adjustment_factor
    return total

# Final computation — this is the critical execution point
final_score = process_metrics(optimized_weights)

# Print result as required
print(f"Result: {final_score}")