def normalize_sensor_data(data_slice):
    offset = sum(data_slice[:3]) / 3
    normalized = [val - offset for val in data_slice]
    scale_factor = max(normalized, default=1)
    return [val / scale_factor for val in normalized]


def calculate_entropy(sequence):
    from math import log2
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)

# Sensor array readings (simulated)
raw_readings = [23.5, 24.1, 23.8, 25.3, 26.0, 25.7, 24.9, 25.1, 26.2, 26.5]

# Misleading preprocessing: irrelevant transformation
shifted_readings = [x + 273.15 for x in raw_readings]  # Kelvin conversion - unused

# Extract critical window and normalize
window_start = 2
window_end = 8
extracted_window = raw_readings[window_start:window_end]
processed_readings = normalize_sensor_data(extracted_window)

# Dummy sorting - looks important but not used in final path
sorted_normalized = sorted(processed_readings, reverse=True)

# Auxiliary calculation - distractor
signal_strength = sum(x ** 2 for x in processed_readings) / len(processed_readings)
noise_floor = 0.1 * signal_strength

# Entropy check - appears diagnostic, not directly contributing
data_entropy = calculate_entropy([round(x, 1) for x in processed_readings])

# Key control flow with red herring branch
if data_entropy > 2.0:
    adjustment_factor = 0.85
else:
    adjustment_factor = 1.0  # This branch actually taken

# Critical function that computes final answer
def calculate_thermal_output(norm_vals):
    base_energy = sum(val ** 3 for val in norm_vals)
    length_factor = len(norm_vals)
    efficiency = 0.92
    # Complex but irrelevant intermediate
    temp_storage = [base_energy / (i + 1) for i in range(length_factor)]
    stored_sum = sum(temp_storage[::2])  # Partial use - misleading
    return int((base_energy * efficiency * adjustment_factor) + 0.5)

# Final computation
thermal_capacity = calculate_thermal_output(processed_readings)

print(f"Result: {thermal_capacity}")