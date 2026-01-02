def analyze_signal(samples):
    filtered = []
    noise_floor = 0.04
    gain_boost = 1.87
    temp_accum = 0.0
    for s in samples:
        if abs(s) > noise_floor:
            boosted = s * gain_boost
            filtered.append(boosted)
    return filtered

samples_raw = [0.01, -0.03, 0.05, 0.12, -0.07, 0.002, 0.15]
downscaled_samples = [s * 0.5 for s in samples_raw]
processed_signal = analyze_signal(downscaled_samples)

# Irrelevant transformation chain (distractor)
scaling_map = {i: val * 2.1 for i, val in enumerate(processed_signal)}
index_offset = sum(1 for x in scaling_map.values() if x > 0.1)

# Decoy function with unused result
def compute_ghost_metric(data):
    return sum(d ** 2 for d in data) * 0.001

ghost_value = compute_ghost_metric(processed_signal)  # Dead end

# Real processing begins here — deeply nested logic
baseline_shift = 0.08
calibration_factor = len(processed_signal) * 0.3

sensor_data = []
for idx, val in enumerate(processed_signal):
    adjusted = val + baseline_shift
    if idx % 2 == 0:
        adjusted *= 0.9
    else:
        adjusted *= 1.1
    sensor_data.append(round(adjusted, 6))

# Secondary irrelevant computation (misleading intermediate)
redundant_aggregate = 0
for i, v in enumerate(sensor_data):
    redundant_aggregate += v * (i + 1) ** 0.5
aux_diagnostic = redundant_aggregate / (len(sensor_data) + 1)

# Core logic hidden among distractors
status_flags = [1 if x > 0.1 else 0 for x in sensor_data]
flag_transitions = 0
for i in range(1, len(status_flags)):
    if status_flags[i] != status_flags[i-1]:
        flag_transitions += 1

# Key red herring: complex but unused bitwise calculation
bit_entropy = 0
for v in [int(abs(x * 100)) for x in sensor_data]:
    while v:
        bit_entropy += v & 1
        v >>= 1
bit_entropy *= len(sensor_data)  # Looks important, not used

# Actual answer derivation via composite logic
def process_readings(readings, factor):
    total_energy = sum(r ** 2 for r in readings)
    peak_response = max(abs(r) for r in readings)
    stability_score = len(readings) - flag_transitions  # Uses outer-scope var
    normalized_index = (total_energy * factor) / (peak_response + 0.01)
    return int(normalized_index + stability_score)

final_diagnostic = process_readings(sensor_data, calibration_factor)
print(f"Result: {final_diagnostic}")