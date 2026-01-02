def process_temperatures(temp_data):
    scaled_temps = [(t * 9/5) + 32 for t in temp_data]
    valid_range = lambda x: 32 <= x <= 212
    filtered_values = [temp for temp in scaled_temps if valid_range(temp)]
    outlier_count = len([t for t in scaled_temps if not valid_range(t)])
    filtered_sum = sum(filtered_values)
    return filtered_sum

# Simulated sensor readings in Celsius
temperatures_celsius = [0, 25, -10, 100, 150, -30, 50]
result = process_temperatures(temperatures_celsius)
print(f"Target result: {result}")