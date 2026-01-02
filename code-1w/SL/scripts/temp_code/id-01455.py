import itertools

# System calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.023
REFERENCE_VOLTAGE = 3.3
BASELINE_DRIFT = 0.0017

# Simulation parameters (some are decoys)
sample_rate = 128
decimation_factor = 4
oversampling_ratio = 8

# Core process stage data (relevant)
stage_temperatures = [23.5, 47.1, 68.9, 91.2, 110.8]
stage_durations = [15, 22, 31, 28, 19]
stage_efficiency = [0.88, 0.91, 0.85, 0.89, 0.92]

# Irrelevant sensor arrays (distractors)
sensor_readings_a = [[0.12, 0.15], [0.11, 0.14], [0.13, 0.16]]
sensor_readings_b = [0.21, 0.19, 0.23, 0.22]

# Fake transformation matrix (dead code path)
transform_matrix = [[1, 0], [0, 1]]
def apply_transform(vec):
    return [vec[0]*transform_matrix[0][0] + vec[1]*transform_matrix[0][1],
            vec[0]*transform_matrix[1][0] + vec[1]*transform_matrix[1][1]]

# Unused recursive function (red herring)
def binary_entropy(n):
    if n <= 1:
        return 0
    return n * (n-1) / binary_entropy(n-1) if n > 2 else 1

# Decoy statistical computation
mean_duration = sum(stage_durations) / len(stage_durations)
variance_estimate = sum((t - mean_duration)**2 for t in stage_durations) / len(stage_durations)

# Real processing logic begins here
weighted_temp_sequence = [
    temp * (duration / 10) * efficiency
    for temp, duration, efficiency in zip(stage_temperatures, stage_durations, stage_efficiency)
]

# Generate phase harmonics (partially relevant, but only last value matters)
phase_harmonics = []
for i in range(len(weighted_temp_sequence)):
    harmonic = weighted_temp_sequence[i]
    for j in range(i):
        harmonic *= 0.95  # decay factor
    phase_harmonics.append(round(harmonic, 4))

# Slice and shift operations (some relevant, some not)
history_window = phase_harmonics[-3:]
shifted_buffer = [0] + history_window[:-1]

delta_correction = [a - b for a, b in zip(history_window, shifted_buffer)]

# Simulate redundant checksum (irrelevant)
checksum = 0
for val in sensor_readings_b:
    checksum = (checksum + val) % 1.0

# Complex data transformation using itertools (only one part used)
combined_indices = list(itertools.combinations(range(len(stage_durations)), 2))
valid_pairs = [(i, j) for i, j in combined_indices if stage_durations[i] + stage_durations[j] > 40]

# Only this aggregated metric feeds into final calculation
aggregated_metric = sum(
    phase_harmonics[i] * 0.5 for i in range(len(phase_harmonics))
) + len(valid_pairs) * 0.7

# Redundant normalization (distraction)
normalized_metric = aggregated_metric / (max(phase_harmonics) + 1e-9)

# Critical function: computes thermal integral from process stages
def calculate_thermal_integral(stages):
    base_integral = 0
    for idx, stage in enumerate(stages):
        # Non-linear response curve
        if idx % 2 == 0:
            contribution = stage ** 0.95
        else:
            contribution = stage * 0.85
        base_integral += contribution
    
    # Apply artificial system loss (fixed)
    system_loss_factor = 0.93
    adjusted_integral = base_integral * system_loss_factor
    
    # Spurious bit manipulation (irrelevant)
    int_rep = int(adjusted_integral)
    masked = int_rep & 0xFFFF
    flipped = masked ^ 0xAAAA
    
    # Return unmodified adjusted_integral (bit ops are red herrings)
    return adjusted_integral

# Execute key statement
thermal_capacity = calculate_thermal_integral(phase_harmonics)

# Print final result as required
print(f"Target result: {thermal_capacity}")