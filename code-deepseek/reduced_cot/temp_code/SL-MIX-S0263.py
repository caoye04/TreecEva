# Data processing pipeline for quality control metrics
raw_measurements = [12, 18, 7, 25, 14, 31, 9, 22]

# Filter and process valid measurements
threshold_check = lambda x: x % 2 == 0
filtered_data = [x for x in raw_measurements if threshold_check(x)]

# Apply transformation and calculate final metric
processed_data = [x * 1.5 for x in filtered_data]
final_metric = max(filter(lambda x: x > 15, processed_data))

print(f"Target result: {final_metric}")