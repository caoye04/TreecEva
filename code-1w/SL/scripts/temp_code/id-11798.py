import math

# Simulated sensor array diagnostics with interference
sensor_ids = ['S101', 'S102', 'S103', 'S104']
time_stamps = [162345, 162346, 162347, 162348]

# Irrelevant historical data (distractor)
historical_offsets = {sid: (idx * 1.07) for idx, sid in enumerate(reversed(sensor_ids))}
baseline_shifts = [0.1, -0.2, 0.3, -0.4]

current_readings = [85.3, 92.1, 76.5, 88.9]
reference_temps = [80.0, 90.0, 75.0, 85.0]

def compute_deviation(index):
    raw_dev = current_readings[index] - reference_temps[index]
    adjusted = raw_dev * (1 + 0.05 * index)
    return round(adjusted, 2)

def evaluate_anomaly(devs):
    if len(devs) == 0:
        return 0.0
    peak = max(devs)
    avg = sum(devs) / len(devs)
    return (peak * 0.7) + (avg * 0.3)

# Secondary unused function (dead code path - distractor)
def legacy_diagnostic(seq):
    total = 0
    for x in seq:
        total += x ** 0.5 if x > 0 else 0
    return total // len(seq) if seq else 0

# Bitwise masking for non-critical status flags (red herring)
system_status_word = 0b11010110
error_mask = 0b00101001
masked_diagnostics = system_status_word & ~error_mask

# Real computation begins here — deviations
individual_deviations = [compute_deviation(i) for i in range(len(current_readings))]

# Spurious transformation (irrelevant list comprehension)
normalized_logs = [round(math.log(x + 10), 3) for x in current_readings if x > 80]

# Control flow with misleading branch
threshold_met = False
if sum(baseline_shifts) < 0.5:
    threshold_met = True
    temp_buffer = [t * 1.1 for t in current_readings]
else:
    temp_buffer = [t for t in current_readings]  # Dead assignment due to scope

# Actual aggregation logic (critical path)
aggregate_threshold = 0
for i, dev in enumerate(individual_deviations):
    weight = 0.25
    if dev > 3:
        weight += 0.1
    contribution = dev * weight
    aggregate_threshold += contribution

# Simulate calibration offset (unused)
calibration_data = [0.05, -0.03, 0.07]
rolling_correction = sum([abs(c) for c in calibration_data])  # Computed but not used

# Anomaly scoring using modular arithmetic and max
mod_scores = [(int(d * 10) % 7) for d in individual_deviations]
anomaly_score = max(mod_scores) * 1.5

# Decoy calculation with tuple unpacking (distractor)
dummy_analysis = [(i, d) for i, d in enumerate(individual_deviations) if d > 5]
if dummy_analysis:
    idx_first, val_first = dummy_analysis[0]
    shadow_factor = idx_first * val_first  # Never used

# Key statement: final diagnostic score
final_diagnostic = aggregate_threshold + anomaly_score

# Output result as required
print(f"Result: {final_diagnostic}")