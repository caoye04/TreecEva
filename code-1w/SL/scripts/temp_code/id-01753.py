from itertools import compress

# Sensor data validation and processing
data_points = [105, 210, 98, 315, 412, 198, 205, 512]
threshold = 100

# Determine valid readings based on dynamic criteria
is_high = [x > 200 for x in data_points]
is_round = [x % 5 == 0 for x in data_points]
valid_mask = [a and b for a, b in zip(is_high, is_round)]

# Extract qualifying data using boolean mask
filtered_data = list(compress(data_points, valid_mask))

# Secondary filter: exclude values over 500 (calibration limit)
filtered_data = [x for x in filtered_data if x <= 500]

result = sum(filtered_data)
print(f"Result: {result}")