def analyze_temperature(readings):
    avg_temp = sum(readings) / len(readings)
    normalized = [(t - avg_temp) ** 2 for t in readings]
    variance = sum(normalized) / len(normalized)
    adjusted_scores = [abs(t - variance) for t in readings]
    return sum(adjusted_scores) // len(adjusted_scores)


def filter_outliers(values, threshold=5):
    mean_val = sum(values) / len(values)
    deviances = [abs(v - mean_val) for v in values]
    filtered = [v for v in values if abs(v - mean_val) < threshold]
    if len(filtered) == 0:
        return [mean_val]
    return filtered

experiment_data = [
    12, 15, 14, 13, 17, 22, 25, 11, 16, 19,
    30, 18, 14, 15, 16, 20, 23, 14, 17, 19
]

# Simulate preprocessing with distractors
raw_sum = sum(experiment_data)
duplicate_check = set(experiment_data)
duplicates_removed = list(duplicate_check)
sorted_data = sorted(duplicates_removed, reverse=True)

# Irrelevant string processing (distractor)
data_labels = [f'expt_{i}' for i in range(len(experiment_data))]
labeled_map = {lbl: val for lbl, val in zip(data_labels, experiment_data)}
label_lengths = [len(lbl.upper().strip()) for lbl in data_labels]

# Actual signal path begins
filtered_data = filter_outliers(experiment_data, threshold=6)
temp_analysis = analyze_temperature(filtered_data)

# Secondary analysis with combinatorics distraction
pair_count = 0
for i in range(len(filtered_data)):
    for j in range(i + 1, len(filtered_data)):
        if (filtered_data[i] + filtered_data[j]) % 2 == 0:
            pair_count += 1

# More distractions: set operations and unused calculations
unique_temps = set(filtered_data)
overlap_with_high = unique_temps & {20, 21, 22, 23, 24, 25}
high_temp_influence = len(overlap_with_high) * 1.5

# Core logic embedded within noise
baseline = 10
scaling_factor = 1.75
penalty = len(experiment_data) - len(filtered_data)
efficiency_ratio = (temp_analysis - penalty) * scaling_factor

# Final computation chain
interim_result = efficiency_ratio ** 2
normalized_interim = int(interim_result // 1.8)
final_yield = normalized_interim + (pair_count % 7)

# Red herring: unused conditional expression
status_flag = 'valid' if final_yield > 50 else 'review'

# Output the required result
Result: {final_yield}