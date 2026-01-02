import itertools

# System calibration module for quantum sensor array
sensor_ids = [101, 102, 103, 104]
calibration_phases = ['alpha', 'beta', 'gamma']
baseline_readings = {sid: (sid * 17) % 97 for sid in sensor_ids}

# Irrelevant auxiliary data — red herring
maintenance_logs = {
    'scheduled': ['2023-08-01', '2023-09-05'],
    'status': 'completed'
}

# Decoy function — never called
def legacy_recalibrate(data):
    return sum(x ** 2 for x in data if x > 50)

# Simulated noise profile — partially used but misleading
noise_profile = [0.1, -0.3, 0.2, 0.0, -0.1]

# Threshold configuration map (used later)
default_thresholds = {'alpha': 15, 'beta': 25, 'gamma': 40}
adjustment_factor = 0.8

# Distractor: complex-looking but unused transformation
transformed_noise = [round((n + 0.5) ** 3 - 0.1, 2) for n in noise_profile if n != 0]

# Real processing begins here
active_phase = 'gamma'
reference_key = sensor_ids[2]  # sensor 103

# Generate calibration sequence using itertools — actually used
calibration_sequence = list(itertools.chain(
    [baseline_readings[sid] for sid in sensor_ids[:2]],
    [baseline_readings[reference_key] + 5],
    [baseline_readings[sid] - 3 for sid in sensor_ids[3:]]
))

# Build threshold map with conditional expression — critical
threshold_map = {
    phase: default_thresholds[phase] * (adjustment_factor if phase != active_phase else 1.0)
    for phase in calibration_phases
}

# Misleading intermediate calculation — dead code path
aggregate_bias = sum(transformed_noise) * len(calibration_sequence)

# Another decoy: unused recursive function
def compute_depth_score(seq, depth=0):
    if depth >= 3 or not seq:
        return depth
    return compute_depth_score(seq[1:], depth + 1)

# Primary metric processor — used once
max_reading = max(calibration_sequence)
avg_reading = sum(calibration_sequence) / len(calibration_sequence)

# Conditional expression to determine correction mode — relevant
correction_mode = 'aggressive' if avg_reading < 20 else 'standard'

# Core logic hidden among distractions
flagged_count = 0
temp_adjustments = []
for val in calibration_sequence:
    # Simulate per-value diagnostics
    deviation = abs(val - avg_reading)
    temp_adjustments.append(deviation * 0.1)
    if deviation > 10:
        flagged_count += 1

# Secondary filter based on threshold map
phase_limit = threshold_map[active_phase]
effective_limit = phase_limit * (0.9 if correction_mode == 'aggressive' else 1.0)

# Final diagnostic computation — depends on multiple prior steps
exceedance_count = sum(1 for v in calibration_sequence if v > effective_limit)

# Key statement: this combines all previous logic
final_diagnostic = (flagged_count * 1000) + (exceedance_count * 100) + (len(temp_adjustments) // 2)

# Output result as required
print(f"Result: {final_diagnostic}")