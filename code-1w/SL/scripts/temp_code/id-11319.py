def process_temperatures(temps):
    temp_offsets = [t - 20 for t in temps]
    positive_indices = [i for i, t in enumerate(temp_offsets) if t > 0]
    scaled_values = [t * 1.5 for t in temp_offsets]
    filtered_values = [v for i, v in enumerate(scaled_values) if i in positive_indices]
    filtered_sum = sum(filtered_values)
    return filtered_sum

temperature_data = [22, 19, 25, 18, 30]
result = process_temperatures(temperature_data)
print(f"Result: {result}")