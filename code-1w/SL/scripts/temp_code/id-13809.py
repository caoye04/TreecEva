from collections import defaultdict

def preprocess_signals(raw_readings):
    normalized = [x % 7 for x in raw_readings if x > 0]
    frequency_map = defaultdict(int)
    for val in normalized:
        frequency_map[val] += 1
    return frequency_map

def calculate_residual(freq_data):
    total = 0
    for key in freq_data:
        if key % 2 == 1:
            total += freq_data[key] * key
    return total % 11

# Main execution
raw_sensor_data = [15, -3, 22, 8, 0, 4, 9, -1, 16]
processed_data = preprocess_signals(raw_sensor_data)
residual = calculate_residual(processed_data)
print(f"Result: {residual}")