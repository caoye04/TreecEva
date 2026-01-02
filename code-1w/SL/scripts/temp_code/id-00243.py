from collections import defaultdict

# Simulate signal processing pipeline
signal_readings = [12, 7, 15, 3, 9, 22, 11]
baseline = 10
signal_gain = 1.5

def calculate_energy_levels(readings):
    energy_map = defaultdict(float)
    for i, val in enumerate(readings):
        energy_map[i] = val ** 1.1
    return [energy_map[i] for i in range(len(readings))]

energy_levels = calculate_energy_levels(signal_readings)
energy_threshold = max(energy_levels, key=lambda x: x * signal_gain if x > baseline else 0)
print(f"Result: {energy_threshold}")