from collections import defaultdict

# Simulate thermal regulation system for a microgrid node
temperature_readings = [23.5, 24.1, 22.9, 25.3, 23.8, 24.0, 23.2]
pressure_levels = {"node_a": 101.3, "node_b": 102.1, "node_c": 99.7}

# Irrelevant mapping (distractor)
material_codes = {'A1': 'copper', 'B2': 'aluminum', 'C3': 'steel'}
redundant_list = [x ** 2 for x in range(5) if x % 2 == 0]  # Unused computation

# State tracker for fault detection (partial use)
fault_counter = defaultdict(int)
for temp in temperature_readings:
    if temp > 24.0:
        fault_counter['high_temp'] += 1
    elif temp < 23.0:
        fault_counter['low_temp'] += 1

# Core calculation setup
base_capacity = sum([t for t in temperature_readings if t >= 23.0]) / len(temperature_readings)
median_pressure = sorted(pressure_levels.values())[len(pressure_levels)//2]

# Secondary derived values (some distraction)
pressure_variance = sum((p - median_pressure)**2 for p in pressure_levels.values()) / len(pressure_levels)
adjustment_factor = abs(pressure_variance - 1.5)  # Not directly used

# Efficiency logic with conditional override
if fault_counter['high_temp'] > 2:
    efficiency_factor = 0.85
else:
    efficiency_factor = 0.92

# Red herring: unused function
def calculate_stress_index(t, p):
    return (t * 1.8 + 32) / (p / 100)

# Key computational step
thermal_capacity = base_capacity * efficiency_factor

# Additional irrelevant state mutation
temporary_buffer = set()
for i, t in enumerate(temperature_readings):
    if i % 2 == 0:
        temporary_buffer.add(round(t * adjustment_factor))

# Final output
Result: thermal_capacity