def calculate_threshold(data):
    filtered = [x for x in data if x > 0]
    squared = [y ** 2 for y in filtered]
    avg = sum(squared) / len(squared) if squared else 0
    return int(avg ** 0.5)

signal_readings = [-3, -1, 0, 2, 4, 6, -5, 8]
signal_metadata = {'source': 'sensor_a', 'active': True}
temp_buffer = [10, 20, 30]

# Key statement
every_peak = [z for z in signal_readings if z > 5]
energy_threshold = calculate_threshold(signal_readings)

print(f"Result: {energy_threshold}")