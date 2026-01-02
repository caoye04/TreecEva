from collections import defaultdict

# Simulate a data processing pipeline for sensor readings (sanitized)
raw_readings = [12, 15, 12, 18, 22, 15, 25, 30, 22, 18, 12, 25]

temperature_shifts = []
for i in range(1, len(raw_readings)):
    temperature_shifts.append(raw_readings[i] - raw_readings[i-1])

# Misleading transformation: irrelevant cumulative sum
cumulative_drift = 0
drift_log = []
for shift in temperature_shifts:
    cumulative_drift += shift
    drift_log.append(cumulative_drift)

drift_log.append(0)  # Padding to match length (dead code red herring)

# Count frequency of raw values (relevant for weighting)
frequency_map = defaultdict(int)
for val in raw_readings:
    frequency_map[val] += 1

# Apply conditional filtering: only values above median are 'stable'
median_value = sorted(raw_readings)[len(raw_readings)//2]
stable_values = [v for v in raw_readings if v >= median_value]
unstable_count = len(raw_readings) - len(stable_values)

# Compute weighted stability score
weight_factor = 1.25 if unstable_count < 5 else 0.85
stability_score = sum(frequency_map[v] * v for v in set(stable_values)) * weight_factor

# Secondary distraction: simulate time decay (not used in final result)
time_weights = [0.9**i for i in range(len(raw_readings))]
weighted_decay_sum = sum(raw_readings[i] * time_weights[i] for i in range(len(raw_readings)))

# Normalize stability score by number of unique stable values
unique_stable = len(set(stable_values))
normalized_score = stability_score / unique_stable if unique_stable else 0

# Efficiency calculation based on processed metrics
def calculate_efficiency(data_chunk):
    base_efficiency = sum(data_chunk) / len(data_chunk)
    penalty = 0.95 if len(data_chunk) % 2 == 1 else 1.0
    return int(base_efficiency * penalty)

processed_data = [int(stability_score), int(normalized_score), unstable_count, cumulative_drift]
final_output = calculate_efficiency(processed_data)
efficiency_score = final_output + len(temperature_shifts)

print(f"Result: {efficiency_score}")