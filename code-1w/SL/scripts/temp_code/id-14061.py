def calculate_net_flux(readings_a, readings_b):
    differences = [a - b for a, b in zip(readings_a, readings_b)]
    positive_only = [val for val in differences if val > 0]
    negative_only = [val for val in differences if val < 0]
    filtered_differences = [d for d in differences if abs(d) > 1]
    total_magnitude = sum(abs(x) for x in differences)
    net_flux = sum(filtered_differences)
    return net_flux

sensor_a = [12, 15, 10, 8, 20]
sensor_b = [10, 16, 12, 9, 18]
result = calculate_net_flux(sensor_a, sensor_b)
print(f"Result: {result}")