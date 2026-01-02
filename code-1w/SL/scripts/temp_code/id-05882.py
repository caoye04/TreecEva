temperatures = [22, 19, 24, 27, 30]
humidity_levels = [60, 55, 65, 70, 80]

# Initialize indices and tracking variables
current_index = 0
total_humidity_index = 0
offset_correction = 3

# Iterate through temperatures with index
for i, temp in enumerate(temperatures):
    if temp > 23:
        total_humidity_index += humidity_levels[i] // 2
    else:
        total_humidity_index += humidity_levels[i] // 4

Result: {total_humidity_index}