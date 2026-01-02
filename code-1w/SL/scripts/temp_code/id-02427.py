import itertools

# Sensor array diagnostics with noise filtering and calibration
sensor_ids = [101, 102, 103, 104, 105]
raw_readings = [85, 92, 78, 150, 88, 73, 95, 160]
noise_floor = 60
calibration_factor = 0.92
threshold_limit = 80

# Irrelevant auxiliary data (distractor)
legacy_mappings = {1: 'A', 2: 'B', 3: 'C'}
temp_offsets = [0.1, -0.3, 0.4, 0.0, -0.2]

# Simulate derived metrics from hardware layer (mostly unused)
def compute_health_score(readings):
    return sum(r > noise_floor for r in readings) / len(readings) * 100

# Unused transformation function (dead code path)
def legacy_transform(x):
    return [val * 1.05 - 2 for val in x if val % 2 == 0]

# Real processing begins here
readings_with_id = list(itertools.product(sensor_ids, raw_readings))

# Filter out sensor anomalies above arbitrary saturation point (red herring: not used later)
saturated_mask = [r > 140 for _, r in readings_with_id]
filtered_pairs = [(sid, r) for sid, r in readings_with_id if r <= 140]  # Remove saturated

# Extract values and apply conditional offset based on id divisibility (irrelevant branch)
processed_values = []
for sid, r in filtered_pairs:
    if sid % 3 == 0:
        processed_values.append(r + 5)
    elif sid % 5 == 0:
        processed_values.append(r + 2)
    else:
        processed_values.append(r)  # Only this branch is actually relevant

# Distractor: complex set operation with no impact
unique_sids = set(sid for sid, _ in filtered_pairs)
high_noise_sensors = {102, 104}
overlap_check = unique_sids & high_noise_sensors

# Actual signal extraction: count how many exceed dynamic threshold
exceedance_count = sum(1 for v in processed_values if v > threshold_limit)

# Secondary metric: sum of even-positioned elements (misleading intermediate)
even_sum = sum(processed_values[i] for i in range(0, len(processed_values), 2))

# Core logic hidden among distractions
adjusted_count = exceedance_count * 2 if even_sum > 300 else exceedance_count

# Decoy computation using itertools that does nothing
_ = list(itertools.combinations([1, 2, 3], 2))

# Critical section: filter only clean, valid readings below noise floor proxy
baseline_reference = [v for v in processed_values if v >= noise_floor]

# Final processing function
def process_readings(data, calib):
    base_metric = sum(data) // len(data)
    correction = len(data) % 4
    return int((base_metric - correction) * calib)

# Key assignment statement
final_diagnostic = process_readings(baseline_reference, calibration_factor)

# Output result as required
print(f"Result: {final_diagnostic}")