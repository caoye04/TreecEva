import itertools
import math

def calculate_modulation_index(freq_vals):
    return sum(math.log(x + 1) for x in freq_vals if x > 0)

# Sensor readings simulation
raw_sensor_data = [2, 5, -1, 8, 0, 3]
sensor_labels = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta']

# Data preprocessing with dictionary comprehension and string transformation
preprocessed_readings = {label: val**2 if val >= 0 else -val for label, val in zip(sensor_labels, raw_sensor_data)}
transformed_keys = {k.upper(): v for k, v in preprocessed_readings.items()}

# Combinatorial signal enhancement
enhancement_pairs = list(itertools.combinations([v for v in preprocessed_readings.values() if v > 4], 2))
total_enhancement = sum(a * b for a, b in enhancement_pairs)

# Conditional modulation calculation
mod_index = calculate_modulation_index(raw_sensor_data)
adjusted_mod_index = mod_index if mod_index > 5 else mod_index * 2

# Final signal strength computation
base_signal = len(preprocessed_readings) * 10
processed_signal_strength = base_signal + total_enhancement + (adjusted_mod_index * 3)

print(f"Result: {int(processed_signal_strength)}")