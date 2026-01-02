def analyze_sensor_data(raw_readings):
    filtered = [x for x in raw_readings if x > 0.1]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    normalized = [(x - baseline) * 1.5 for x in filtered]
    return normalized

modulus_map = {
    'A': 230.4,
    'B': 198.7,
    'C': 215.6,
    'D': 204.3
}

stress_profile = [-0.2, 0.5, 0.7, -0.1, 0.9, 0.3, 0.6]

def compute_deformation_index(values):
    index = 0
    for i, v in enumerate(values):
        if i % 2 == 0:
            index += v ** 2
        else:
            index -= v * 0.5
    return abs(index)

def derive_calibration_factor(mode):
    factors = {'safe': 1.05, 'high': 0.92, 'debug': 1.2}
    return factors.get(mode, 1.0)

calibration_mode = 'unknown'
reference_offset = 0.05 * derive_calibration_factor(calibration_mode) if calibration_mode in ['safe', 'high'] else 0.08

# Irrelevant preprocessing path (dead code - never used)
if reference_offset > 0.07:
    temp_buffer = [0] * 10
    for k in range(len(temp_buffer)):
        temp_buffer[k] = k * reference_offset

strain_accumulator = []
sensor_input = [0.15, 0.25, 0.08, 0.33, 0.41, 0.19]
processed_data = analyze_sensor_data(sensor_input)

for val in processed_data:
    if val > 0:
        strain_accumulator.append(val * 0.75)
    else:
        strain_accumulator.append(val * 1.1)

intermediate_score = compute_deformation_index(processed_data)
decoy_metric = intermediate_score * 1000  # Red herring value

# Simulate material phase adjustment (unused)
phase_shift = 0
for code in [65, 66, 67]:
    phase_shift += ord(chr(code)) % 3

# Core calculation chain
material_phases = ['A', 'C', 'B']
phase_weights = {
    'A': 0.4,
    'B': 0.3,
    'C': 0.3
}

weighted_modulus = sum(modulus_map[phase] * phase_weights[phase] for phase in material_phases)

adjusted_stress = [s * 1.2 if s > 0.4 else s * 0.85 for s in stress_profile]

active_segments = [s for s in adjusted_stress if s > 0.2]

# Misleading summation (looks important but unused in final result)
total_load = 0
for seg in active_segments:
    total_load += seg ** 2

mean_stress = sum(active_segments) / len(active_segments) if active_segments else 0

# Key transformation using conditional expression
stress_ratio = mean_stress / weighted_modulus if weighted_modulus != 0 else 0

efficiency_factor = 1.15 if stress_ratio > 0.005 else 0.88

# Final yield calculation
final_yield = 0
for i, s in enumerate(active_segments):
    contribution = s * efficiency_factor * (i + 1)
    final_yield += contribution

# Decoy output (distractor)
print(f'Debug: decoy_metric={decoy_metric}')
print(f'Phase shift total: {phase_shift}')

# Critical output
Target result: {final_yield}