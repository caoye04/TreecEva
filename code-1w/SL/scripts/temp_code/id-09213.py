from itertools import compress, cycle

# Sensor simulation and diagnostic system
raw_readings = [107, 214, 153, 88, 199, 134, 176, 167, 95, 108, 143, 152]
threshold = 95
calibration_factor = 0.93
noise_floor = 12
sample_size = len(raw_readings)

# Irrelevant baseline metrics (distractor)
baseline_avg = sum(range(1, 11)) / 10
offset_correction = [x % 7 for x in range(sample_size)]

# Misleading intermediate transformation (dead path)
decoy_signal = [(x ** 0.5) * 1.5 for x in raw_readings if x > 100]
deoy_mask = [x > 120 for x in raw_readings]  # Note: typo in variable name - red herring

# Actual filtering logic
validity_flags = [x >= threshold for x in raw_readings]
quality_weights = [0.8 if x % 2 == 0 else 1.2 for x in raw_readings]

# Data stream mixing (relevant but obscured)
modulated_indices = [(i * 2 + 1) % sample_size for i in range(sample_size)]
mixed_readings = [raw_readings[i] for i in modulated_indices]

# Real signal extraction
filtered_data = list(compress(mixed_readings, validity_flags))

# Fake data reconstruction path (decoy function)
def reconstruct_signal(data, factor):
    return [round(x * factor * 1.1, 2) for x in data][::2]

# Actual processing function
def process_readings(signal, calib):
    # Nested corrections and transformations
    adjusted = [x * calib for x in signal]
    
    # Secondary quality pass
    windowed = [adjusted[i:i+3] for i in range(len(adjusted)-2)]
    smooth_vals = []
    for window in windowed:
        if len(window) == 3:
            smoothed = sum(window) / 3
            smooth_vals.append(smoothed)
    
    # Final aggregation with redundancy check
    primary_sum = sum(smooth_vals)
    backup_check = sum([x for x in adjusted if x > 100])
    
    # Critical computation
    if primary_sum > backup_check:
        result = primary_sum * 0.87
    else:
        result = backup_check * 0.87
    
    return round(result, 4)

# Phantom diagnostic chain (unused)
cyclic_pattern = cycle([1, -1, 0])
phantom_score = 0
for i, p in enumerate(cyclic_pattern):
    phantom_score += raw_readings[i % sample_size] * p
    if i > 10:
        break

# Hidden character analysis (irrelevant string distraction)
sensor_id = "SNSR-ALPHA-7G"
id_chars = set(sensor_id)
char_count = {c: sensor_id.count(c) for c in id_chars}
vowel_count = sum(1 for c in sensor_id if c.lower() in 'aeiou')

# Trigger actual computation
diagnostic_interim = sum(filtered_data) + noise_floor  # Red herring usage
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Spurious output validation (misleading)
consistency_check = all([len(str(round(x))) == 3 for x in filtered_data if x > 100])

# Output the target result
print(f"Result: {final_diagnostic}")