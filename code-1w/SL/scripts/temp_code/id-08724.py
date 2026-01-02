def average(lst):
    return sum(lst) / len(lst)

# Sensor data with some initial processing
raw_data = [23.5, 19.0, 27.3, 31.2, 18.8, 24.1, 29.5, 35.0, 17.6, 22.3]
valid_range = (18.0, 30.0)

cleaned_data = [round(x, 1) for x in raw_data if isinstance(x, float)]
filtered_temperatures = [temp for temp in cleaned_data if valid_range[0] <= temp <= valid_range[1]]

# Minor irrelevant variable (distractor at intervention level 4)
dummy_flag = len(raw_data) > 5

filtered_avg = average(filtered_temperatures)
print(f"Result: {filtered_avg}")