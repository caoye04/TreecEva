from collections import Counter

# Simulate sensor readings with some noise
temperature_readings = [20, 22, 25, 22, 30, 25, 28, 30, 33, 22]
humidity_readings = [45, 50, 55, 50, 60, 55, 65, 70, 50, 55]

# Count frequency of temperature and humidity values
temp_freq = Counter(temperature_readings)
humid_freq = Counter(humidity_readings)

# Find values that appear more than once
duplicated_temps = {k for k, v in temp_freq.items() if v > 1}
duplicated_humid = {k for k, v in humid_freq.items() if v > 1}

# Generate multiples of 5 from duplicated temperatures
multiples_of_5 = {x for x in duplicated_temps if x % 5 == 0}
filtered_multiples = {x // 2 for x in multiples_of_5}  # Integer division

# Common elements in both duplicated sets (irrelevant but present for mild distraction)
common_elements = duplicated_temps & duplicated_humid

# Key computation step
current_mode = max(temp_freq, key=temp_freq.get)  # Most frequent temperature
result = len(common_elements.intersection(filtered_multiples))

print(f"Target result: {result}")