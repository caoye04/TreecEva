from itertools import compress

def calculate_threshold(data, base):
    filtered = [x for x in data if x > base]
    avg = sum(filtered) / len(filtered) if filtered else 0
    return int(avg // 1.5)

# Simulate sensor signal processing
time_points = list(range(10))
signal_strength = [85, 90, 70, 60, 95, 100, 65, 50, 80, 75]
binary_mask = [t % 2 == 0 for t in time_points]
signal_data = list(compress(signal_strength, binary_mask))  # Only even-indexed signals
base_level = 60
energy_threshold = calculate_threshold(signal_data, base_level)

# Additional computation to simulate side calculation (minimal interference)
calibration_factor = 1.1
temp_result = sum(signal_data) * calibration_factor

print(f"Target result: {energy_threshold}")