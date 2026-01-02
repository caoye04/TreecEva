from collections import defaultdict
import math

# Simulate a chemical reaction equilibrium computation with noise filtering

def preprocess_readings(sensor_log):
    # Irrelevant preprocessing: logs are filtered but not used in final result
    valid_readings = []
    for entry in sensor_log:
        if entry['status'] == 'ok':
            valid_readings.append(entry['value'])
    smoothed = [valid_readings[i] for i in range(len(valid_readings)) if i % 2 == 0]
    return smoothed  # Not actually used later


def build_concentration_map(elements):
    # Creates a frequency map of element occurrences
    counter = defaultdict(int)
    for elem in elements:
        counter[elem] += 1
    return counter

# Unused helper function (dead code path)
def deprecated_scale(x, factor=2):
    return x * factor ** 2

# Threshold function based on dynamic condition
threshold_fn = lambda x: x > 0.5 and math.sin(x) >= 0.1

# Simulated sensor data (irrelevant)
sensor_log = [
    {'value': 0.3, 'status': 'ok'},
    {'value': 0.7, 'status': 'ok'},
    {'value': 0.1, 'status': 'error'}
]

# Preprocess but do not use result (distractor)
filtered_data = preprocess_readings(sensor_log)

# Main grid of concentration values (core data)
concentration_grid = [
    [0.4, 0.6, 0.5],
    [0.7, 0.3, 0.8],
    [0.5, 0.5, 0.4]
]

# Element sequence to build map from
elements = ['H', 'O', 'H', 'N', 'O', 'H']
element_freq = build_concentration_map(elements)  # Used to derive weight_factor

# Derive weight factor from element frequency (H appears 3 times)
weight_factor = element_freq['H']  # = 3

# Secondary distractor variable (unused)
baseline_offset = sum([len(row) for row in concentration_grid])  # = 9

# Core calculation function
def calculate_equilibrium(grid, threshold_func):
    total_active = 0
    adjustment = 0
    
    # Nested traversal with conditional activation
    for i, row in enumerate(grid):
        row_sum = sum(row)
        if row_sum >= 1.5:  # Activate row
            for j, val in enumerate(row):
                if threshold_func(val + i * 0.1):  # Stateful condition
                    adjustment += math.cos(j * 0.5)
                    total_active += 1
    
    # Complex but deterministic score
    raw_score = total_active * weight_factor  # weight_factor captured from outer scope
    final_adjustment = adjustment if adjustment > 0 else 0.5
    
    # Red herring: unused intermediate
    temp_normalization = raw_score / (final_adjustment + 1e-8) if final_adjustment != 0 else 0
    
    return int(raw_score - 2)  # Final deterministic integer result

# Key execution point
equilibrium_score = calculate_equilibrium(concentration_grid, threshold_fn)
print(f"Result: {equilibrium_score}")