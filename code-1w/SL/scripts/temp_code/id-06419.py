import math

# Simulated sensor data from a distributed environmental monitoring system
def generate_sensor_readings():
    return {
        'temperature': [23.5, 24.1, 22.8, 25.0, 23.9],
        'humidity': [45, 47, 50, 44, 46],
        'pressure': [1013, 1012, 1015, 1010, 1014],
        'co2_ppm': [420, 435, 450, 425, 430]
    }

# Irrelevant helper: unused in final computation
def calculate_average(data):
    return sum(data) / len(data)

# Misleading transformation with side effects (never called)
def legacy_normalization(x):
    if x < 0:
        return 0
    return int(math.sqrt(x * 2))

# Decoy function that looks important but does nothing
unused_flags = []
def flag_anomaly(value, threshold=100):
    if value > threshold:
        unused_flags.append(True)
    return False

# Real processing begins here
raw_data = generate_sensor_readings()

# Extract key metrics (only temperature and co2_ppm are actually used later)
primary_metrics = {
    'temp_baseline': raw_data['temperature'][0],
    'co2_peak': max(raw_data['co2_ppm']),
    'humidity_stable': all(h > 40 for h in raw_data['humidity'])
}

# Bit manipulation red herring
bitmask = 0b101010
encoded_shift = (bitmask << 3) & 0xFF
obfuscated_key = encoded_shift ^ 0b11110000

# Distractor: complex dictionary comprehension with no effect
_ = {f"sensor_{i}": {'raw': val, 'status': 'ok'} 
     for i, val in enumerate(raw_data['pressure'])}

# Unused lambda that looks like it's part of the pipeline
sensor_validator = lambda x: x > 0 and isinstance(x, (int, float))

# Actual signal extraction using only specific elements
signal_strength = 0
for t in raw_data['temperature']:
    signal_strength += int(t)  # Sum of integer parts

# Hidden dependency: count how many CO2 readings exceed 425
emission_cycles = len([c for c in raw_data['co2_ppm'] if c > 425])

# Fake aggregation path (dead code)
temp_aggregation = []
for reading in raw_data['temperature']:
    normalized = reading * 1.01
    adjusted = math.floor(normalized)
    temp_aggregation.append(adjusted)

# Core logic disguised among noise
scaling_factor = primary_metrics['temp_baseline'] / primary_metrics['co2_peak']
interim = math.log(scaling_factor * 1000)

# Conditional trap: this block never executes due to data constraints
if primary_metrics['co2_peak'] < 400:
    interim *= 0.1  # Never reached

# Real calculation path
baseline_offset = primary_metrics['temp_baseline'] - min(raw_data['temperature'])

# Lambda used meaningfully (required feature)
compress = lambda x, y: (x * 2 + y) // 3
compressed_signal = compress(int(interim), signal_strength)

# Dictionary operation central to result (required feature)
diagnostic_map = {
    'level1': compressed_signal,
    'level2': emission_cycles * 1000,
    'level3': int(baseline_offset * 100)
}

# Final combination obscured by irrelevant keys
final_weights = {
        'w1': diagnostic_map['level1'],
        'w2': diagnostic_map['level2'],
        'w3': diagnostic_map['level3'],
        'debug_only': obfuscated_key,  # Red herring
        'legacy_mode': None           # Dead weight
    }

# Critical execution point
final_diagnostic = sensor_array_processor(diagnostic_map) if 'sensor_array_processor' in globals() else (
    final_weights['w1'] + final_weights['w2'] + final_weights['w3']
)

# Simulate processor function that was missing
def sensor_array_processor(diagnostics):
    # Only uses level1 and level3; level2 is distraction
    return int(diagnostics['level1'] * 2.5) + diagnostics['level3']

# Recompute final_diagnostic with actual function now defined
final_diagnostic = sensor_array_processor(diagnostic_map)

print(f"Result: {final_diagnostic}")