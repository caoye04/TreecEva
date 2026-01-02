from collections import defaultdict

# Simulate sensor readings with timestamps
timestamped_readings = [
    (1, 23.5), (2, 24.1), (3, 22.9), (4, 25.0), (5, 24.5),
    (6, 23.8), (7, 26.2), (8, 25.8), (9, 27.0), (10, 26.5)
]

# Irrelevant metadata (distractor)
device_info = defaultdict(str, {
    'model': 'SNSR-X1',
    'location': 'Room B',
    'calibration': '2023-10-05'
})

# Extract temperature values using lambda
get_temp = lambda record: record[1]
temperatures = list(map(get_temp, timestamped_readings))

# Apply filtering condition: temperatures above 25.0
high_temp_filter = lambda x: x > 25.0
filtered_data = [temp for temp in temperatures if high_temp_filter(temp)]

# Compute sum of filtered data
filtered_sum = sum(filtered_data)

Result: filtered_sum