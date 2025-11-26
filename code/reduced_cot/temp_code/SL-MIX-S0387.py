data_samples = [12.5, 8.3, 15.7, 9.1, 11.4]
threshold_check = 10.0

# Primary processing path
base_value = sum(data_samples) / len(data_samples)
scaling_factor = 1.25 if base_value > 10 else 0.8
processed_mean = base_value * scaling_factor

# Secondary processing path (distractor)
max_sample = max(data_samples)
min_sample = min(data_samples)
range_calc = max_sample - min_sample
normalized_range = range_calc / 2.0

# Validation logic
validation_flag = processed_mean > 12.0
primary_score = int(processed_mean * 100)
secondary_score = int(normalized_range * 50)

# Temporary calculations (unused)
temp_product = base_value * max_sample
temp_difference = max_sample - base_value

# Final decision point
final_metric = primary_score if validation_flag else secondary_score

print(f"Result: {final_metric}")