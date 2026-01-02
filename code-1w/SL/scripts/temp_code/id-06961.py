import itertools

# Irrelevant helper function (decoy)
def normalize_signal(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Misleading precomputed constants (distractors)
BASE_FREQ = 3.2
core_multiplier = 4.8
voltage_offset = 0.075
target_tdp = 125.0  # Thermal Design Power (watts)

# Unused intermediate calculations (dead code path)
efficiency_ratio = 0.87
overhead_penalty = 1.05
legacy_mode = False
fallback_threshold = 9876

# Simulated sensor readings (irrelevant data structure)
sensor_data = {
    'core_0': [45.2, 46.1, 44.9],
    'core_1': [47.0, 48.3, 46.8],
    'core_2': [50.1, 51.5, 49.7],
    'core_3': [55.2, 54.8, 56.0]
}

# Process load history (red herring)
load_history = list(itertools.accumulate([0.15, -0.03, 0.22, -0.07, 0.11]))
smoothed_load = sum(load_history) / len(load_history) if load_history else 0

# Decoy algorithm using irrelevant math
def predict_fan_speed(temp, age_factor=1.0):
    decay = 0.95 ** age_factor
    speed = 2000 * (temp / 80) ** 1.5 * decay
    return int(speed)

# Unused recursive function (misdirection)
def compute_latency_depth(level):
    if level <= 1:
        return 1
    return level * compute_latency_depth(level - 1)

# Core calculation function (only this matters)
def calculate_thermal_output(load):
    # Nested logic with conditional expressions and comparisons
    base_heat = 32.0
    if load < 0.3:
        heat_factor = 1.1
    elif load < 0.6:
        heat_factor = 1.4
    elif load < 0.8:
        heat_factor = 1.8
    else:
        heat_factor = 2.3  # High load multiplier
    
    # Secondary adjustment using bitwise manipulation (relevant)
    intensity_flag = int(load * 100) & 0b1111  # Lower 4 bits
    adjustment = (intensity_flag >> 2) * 0.05
    
    # Combine factors with composite arithmetic
    final_multiplier = heat_factor + adjustment
    capacity = (base_heat * final_multiplier) + target_tdp * 0.1
    
    # Early return simulation (logical break)
    if capacity > 100.0:
        return round(capacity, 4)
    
    return round(base_heat * load, 4)

# Critical execution point variables
processor_frequency = BASE_FREQ * core_multiplier
processor_load = min(0.85, (sum(sensor_data['core_3']) / len(sensor_data['core_3'])) / 60.0)

# Key assignment statement — answer depends on this
thermal_capacity = calculate_thermal_output(processor_load)

# Print result as required
print(f"Result: {thermal_capacity}")