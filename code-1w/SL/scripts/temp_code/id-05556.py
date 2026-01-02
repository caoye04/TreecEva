import math

# System configuration and sensor simulation (mostly irrelevant)
sensor_offsets = [0.1, -0.2, 0.3, -0.15]
baseline_readings = [12, 15, 10, 8, 20]
calibration_matrix = [[1, 0], [0, 1]]

# Irrelevant helper function (dead code path)
def validate_sensor(id):
    if id < 0:
        return False
    return True

# Unused transformation (distractor)
def legacy_transform(x):
    return [val ** 0.5 for val in x if val > 5]

# Core signal processing chain
raw_signal = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_signal = [x for x in raw_signal if x % 2 == 0]  # Keep evens

# Simulate noise injection (irrelevant to final result)
noise_profile = []
for i in range(len(filtered_signal)):
    noise_value = math.sin(i * 0.5)
    noise_profile.append(noise_value)

# Key data transformation (actually used)
decay_factor = 0.9
weighted_values = []
for i, val in enumerate(filtered_signal):
    weighted_values.append(val * (decay_factor ** i))

# Bit manipulation layer (mixed relevance)
binary_flags = 0b1010
activation_mask = 0b1100
masked_flags = binary_flags & activation_mask  # Used later

# Data reshaping with list comprehension (critical)
reshaped_data = [[v, v * 2] for v in weighted_values]
flattened = [item for sublist in reshaped_data for item in sublist]

# Accumulation with conditional logic
accumulated = 0
threshold_met = False
for idx, num in enumerate(flattened):
    if idx % 3 == 0 and num > 1.0:
        accumulated += int(num)
    if accumulated > 15 and not threshold_met:
        accumulated -= masked_flags  # Uses masked_flags from earlier
        threshold_met = True

# Intermediate diagnostic (misleading value)
current_diagnostic = sum(flattened) / len(flattened)

# Configuration object (partial use)
config = {
    'version': '2.1',
    'mode': 'diagnostic',
    'debug': True,
    'threshold': 0.5
}

# Transform function that looks important but only uses part of input
def preprocess_input(data, cfg):
    if cfg['mode'] == 'normal':
        return [x * 0.9 for x in data]
    else:
        return [x for x in data if x > 0.5]  # Applied

# Another red herring: recursive checksum (never called)
def recursive_checksum(seq, n):
    if n <= 0:
        return 0
    return seq[n-1] + recursive_checksum(seq, n-1)

# Actual preprocessing step
transformed_data = preprocess_input(flattened, config)

# Final analysis function combining multiple concepts
def analyze_pattern(data, settings):
    total = 0
    multiplier = 1.0
    
    # Use of list comprehension with filtering and math
    squares = [x**2 for x in data if x > 2]
    
    # Summation with rounding logic
    raw_sum = sum(squares)
    
    # Integer division and truncation
    truncated = raw_sum // 1  # Remove decimals
    
    # Conditional bit influence
    if len(data) % 2 == 0:
        truncated ^= 0b101  # XOR with binary 5
    
    # Final accumulation with decay effect
    for i in range(3):
        multiplier *= 0.95
        
    result = truncated * multiplier
    
    # Rounding to nearest integer
    return int(round(result))

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, config)

# Output requirement
print(f"Target result: {final_diagnostic}")