import math

# Simulated sensor array data with calibration offsets
data_points = [127, 89, 255, 64, 191, 33, 142, 77, 203, 51]

calibration_factor = 0.88
offset_adjustment = -3.5

# Irrelevant transformation: frequency analysis (dead end)
frequency_spectrum = []
for x in data_points:
    freq = math.sin(x * 0.05) * math.cos(x * 0.02)
    frequency_spectrum.append(freq)

# Decoy list comprehension: normalized but unused
normalized_data = [round((x / 255.0) * 100, 2) for x in data_points]

# Simulated noise threshold filter (misleading intermediate)
noise_floor = 70
raw_above_threshold = [x for x in data_points if x > noise_floor]

# Critical path begins: apply physical response curve
adjusted_measurements = []
for val in data_points:
    adjusted = val * calibration_factor + offset_adjustment
    if adjusted < 0:
        adjusted = 0
    adjusted_measurements.append(int(adjusted))

# Secondary adjustment: dampen high-frequency components (partially relevant)
damped_values = []
for i, v in enumerate(adjusted_measurements):
    if i > 0 and abs(v - adjusted_measurements[i-1]) > 40:
        damped_values.append(int(v * 0.75))
    else:
        damped_values.append(v)

# Tertiary processing: simulate environmental interference (distractor)
environment_factor = [1.0, 0.98, 1.02, 0.95, 0.99, 1.01, 0.97, 0.94, 1.03, 0.96]
interference_impact = []
for i in range(len(damped_values)):
    impact = damped_values[i] * environment_factor[i]
    interference_impact.append(math.floor(impact))

# Red herring function: computes something plausible but unused
def compute_signal_strength(signal_list):
    peak = max(signal_list)
    avg = sum(signal_list) / len(signal_list)
    return (peak * 0.3) + (avg * 0.7)

unused_strength = compute_signal_strength(interference_impact)

# Actual signal path: isolate measurements above biochemical activation threshold
activation_threshold = 65
high_affinity = [v for v in adjusted_measurements if v > activation_threshold]

# Apply binding efficiency correction based on position parity
binding_efficiency = []
for idx, reading in enumerate(high_affinity):
    if idx % 2 == 0:
        binding_efficiency.append(reading * 1.1)
    else:
        binding_efficiency.append(reading * 0.9)

# Final filtering: exclude unstable transient readings
stability_mask = [True, False, True, True, False, True, True, False]
filtered_measurements = []
for i, val in enumerate(binding_efficiency):
    if i >= len(stability_mask) or not stability_mask[i % len(stability_mask)]:
        continue
    filtered_measurements.append(int(round(val)))

# KEY STATEMENT: compute final filtration yield
filtration_yield = sum(filtered_measurements)

# Output target result
print(f"Target result: {filtration_yield}")