from collections import Counter

# Sensor data collection with noise filtering
raw_readings = [105, 107, 106, 105, 110, 108, 107, 130, 106, 105, 104, 120, 105]
reading_frequencies = Counter(raw_readings)

# Identify outlier readings (occurring only once and above normal range)
normal_range = range(104, 111)
outliers = [val for val in raw_readings if reading_frequencies[val] == 1 and val not in normal_range]

cleaned_readings = [val for val in raw_readings if val not in outliers]
filtered_measurements = [val for val in cleaned_readings if str(val).startswith('10')]
filtration_score = sum(filtered_measurements)

Result: filtration_score