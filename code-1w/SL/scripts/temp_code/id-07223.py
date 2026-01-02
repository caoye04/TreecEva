from itertools import compress

# Simulated environmental sensor array (irrelevant for final result but adds context)
sensor_ids = [101, 102, 103, 104, 105]
installation_year = 2020

data_readings = [12, -5, 8, 0, 15, -3, 9]
valid_flags = [x > 0 for x in data_readings]

# Apply filtering using itertools.compress to get only positive readings
filtered_data = list(compress(data_readings, valid_flags))

# Outlier detection: remove values above threshold using lambda
threshold_filter = lambda x: x < 10
refined_data = list(filter(threshold_filter, filtered_data))

# Final computation step
filtration_score = sum(refined_data)

Result: filtration_score