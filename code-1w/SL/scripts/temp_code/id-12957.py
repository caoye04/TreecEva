import math

# Simulated sensor array data (irrelevant initial setup)
base_frequency = 50.0
harmonic_noise = [0.1, 0.3, 0.4, 0.2, 0.5]
dummy_weights = [0.9, 0.8, 0.7, 0.6, 0.5]

# Core signal processing chain
raw_readings = [12, 15, 10, 8, 20, 14, 16, 11]
scaling_factor = 1.75
calibration_offset = 3

# Irrelevant transformation path (dead code - never used)
def legacy_transform(x):
    return [val * 0.8 + 2 for val in x if val > 10]

legacy_data = legacy_transform(raw_readings)

# Real processing begins here
filtered_readings = [val for val in raw_readings if val >= 10]
scaled_readings = [(val * scaling_factor) - calibration_offset for val in filtered_readings]

# Decoy statistical analysis (misleading intermediate)
mean_value = sum(scaled_readings) / len(scaled_readings)
variance_proxy = sum([(x - mean_value) ** 2 for x in scaled_readings]) / len(scaled_readings)
adjusted_variance = math.sqrt(variance_proxy) if variance_proxy > 10 else 0

# Bit manipulation red herring (unrelated to final result)
bit_flags = 0
for val in raw_readings[:4]:
    bit_flags ^= int(val) << 2
    bit_flags |= 1

# Conditional data routing based on arbitrary threshold (distractor)
if mean_value > 20:
    signal_priority = 'HIGH'
    boost_factor = 1.5
else:
    signal_priority = 'MEDIUM'
    boost_factor = 1.1  # Not actually used later

# Tuple unpacking distraction
config_settings = ('NORMAL', 42, 0.95)
mode_flag, entity_id, tolerance_ratio = config_settings

# Actual computation chain (non-obvious due to noise)
intermediate_signal = []
for i, val in enumerate(scaled_readings):
    if i % 2 == 0:
        transformed = val * (1.1 + 0.05 * i)
    else:
        transformed = val * 0.9
    intermediate_signal.append(transformed)

# Secondary irrelevant list comprehension
shadow_copy = [x for x in intermediate_signal if x > 25]

# Key function with conditional expression and nested logic
threshold_reference = 18.5
def evaluate_stability(x):
    return 1 if x > threshold_reference else -1

stability_marks = [evaluate_stability(x) for x in intermediate_signal]

# Data structure cross-reference decoy
lookup_table = {i: val for i, val in enumerate(raw_readings)}
for idx in range(len(intermediate_signal)):
    if idx in lookup_table and lookup_table[idx] % 2 == 0:
        intermediate_signal[idx] += 1.0  # Minor mutation, but not impactful

# Critical processing step (hidden among distractions)
aggregated_power = sum(intermediate_signal)
penalty_rate = 0.02 * len([x for x in raw_readings if x < 12])
effective_yield = aggregated_power * (1 - penalty_rate)

# Final diagnostic calculation
status_codes = {'OK': 100, 'CALIBRATE': 200, 'REVIEW': 300}
status_key = 'OK' if effective_yield > 100 else 'REVIEW'

# Key statement
final_diagnostic = analyze_readings(processed_signals)

# Supporting functions (one is decoy)
def normalize_signal(signal_list):
    max_val = max(signal_list)
    return [x / max_val for x in signal_list]

def analyze_readings(data):
    base_score = sum(data)
    adjustment = 0
    if len(data) >= 5:
        adjustment += 10
    if base_score > 150:
        adjustment += 25
    return int(base_score + adjustment)

# Data flow reconstitution (correct path)
processed_signals = intermediate_signal
final_diagnostic = analyze_readings(processed_signals)

print(f"Result: {final_diagnostic}")