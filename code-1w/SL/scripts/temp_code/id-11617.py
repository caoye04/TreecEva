import itertools

# Simulated sensor array data with noise and calibration offsets
data_stream = [105, -30, 220, 180, -1, 95, 250, -20, 170, 88, 205, -50]
calibration_factor = 0.92
noise_threshold = 90
baseline_offset = 15

# Irrelevant auxiliary variables (distractors)
heartbeat_monitor = [1, 0, 1, 1, 0]
packet_sequence = list(itertools.permutations([1, 2, 3]))[:3]
system_uptime = 14200
maintenance_flag = False

# Signal processing pipeline
adjusted_readings = []
for val in data_stream:
    adjusted = (val + baseline_offset) * calibration_factor
    adjusted_readings.append(int(adjusted))

# Secondary transformation (partially irrelevant)
normalized_readings = [x / max(adjusted_readings) for x in adjusted_readings]
discrete_states = [1 if x > 0.5 else 0 for x in normalized_readings]

# Filtering logic with red herring conditionals
outlier_buffer = []
valid_indices = []
aggregated_diagnostics = 0

for i, raw in enumerate(data_stream):
    if raw < 0:
        outlier_buffer.append(raw)
        continue
    if raw == 0:
        aggregated_diagnostics += 10
        break  # Dead path: no zero in data
    valid_indices.append(i)

# Decoy statistical computation (never used later)
if len(outlier_buffer) > 3:
    anomaly_score = sum(outlier_buffer) ** 2
else:
    anomaly_score = abs(sum(outlier_buffer)) * 100  # This executes but is unused

# Core signal extraction with conditional expression and filtering
reference_peaks = [x for x in adjusted_readings if x > 100]
background_noise = [x for x in adjusted_readings if x <= 100]

# Critical branching with misleading early exit (never triggered)
critical_failure_mode = False
if sum(background_noise) < 50:
    critical_failure_mode = True
    shutdown_procedure = True
    # System halt simulation - not reached

# Main filter using itertools.chain and conditional filtering
filtered_measurements = []
chain_source = itertools.chain([0], reference_peaks)
for x in chain_source:
    # Artificial delay logic (distractor)
    smoothing_factor = 1.0
    for _ in range(1):
        smoothed = int(x * smoothing_factor)
        if smoothed > noise_threshold and smoothed % 2 == 1:
            filtered_measurements.append(smoothed)

# Spurious reassignment (looks important but isn't)
temporal_weighting = [1, 1, 2, 3] if len(filtered_measurements) > 4 else [1, 2]
compression_ratio = len(data_stream) / (len(filtered_measurements) or 1)

# Key statement: final yield calculation
filtration_yield = sum(filtered_measurements)

# Output required result
print(f"Result: {filtration_yield}")