import math

# Simulated sensor data processing with noise filtering and threshold analysis
data_stream = [3.2, 5.8, 6.1, 4.3, 7.9, 8.0, 2.5, 6.6, 9.1, 5.4, 4.8, 7.2, 6.3, 8.7, 3.9]
noise_floor = 2.0
smoothing_factor = 0.8

# Irrelevant transformation (distractor)
transformed_data = list(map(lambda x: round((x + 1.5) ** 1.1, 2), data_stream))

# Relevant preprocessing: filter out low-amplitude noise
cleaned_data = [x for x in data_stream if x > noise_floor]

# Misleading intermediate calculation (dead computation)
avg_transformed = sum(transformed_data) / len(transformed_data)

# Extract central segment using slicing (relevant)
data_slice = cleaned_data[2:-2]  # Focus on stable operating period

# Define dynamic thresholds based on statistical properties (relevant)
mean_clean = sum(cleaned_data) / len(cleaned_data)
std_dev = (sum((x - mean_clean) ** 2 for x in cleaned_data) / len(cleaned_data)) ** 0.5
thresholds = {
    'low': mean_clean - 0.5 * std_dev,
    'high': mean_clean + 0.7 * std_dev,
    'critical': 2 * std_dev
}

# Auxiliary function to compute weighted score (relevant)
def calculate_final_score(segment, limits):
    base_score = 0
    penalty = 0
    bonus = 0

    # Nested logic with multiple reasoning steps
    for val in segment:
        if val < limits['low']:
            base_score += 10
            penalty += 2
        elif val >= limits['high']:
            base_score += 15
            if val > limits['critical']:
                bonus += 3
        else:
            base_score += 12

        # Extra distraction inside loop (semi-relevant but not used)
        normalized = (val - mean_clean) / std_dev if std_dev != 0 else 0

    # Final adjustment using min/max logic
    adjusted = max(5, min(base_score - penalty + bonus, 100))
    return round(adjusted, 4)

# Secondary distractor: unused recursive helper
def recursive_sum(arr, n=None):
    if n is None or n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Unused statistical measure (dead code path)
total_variance = sum((x - mean_clean)**2 for x in cleaned_data) / (len(cleaned_data) - 1)

# Key execution point
final_score = calculate_final_score(data_slice, thresholds)

# Print result as required
print(f"Target result: {final_score}")