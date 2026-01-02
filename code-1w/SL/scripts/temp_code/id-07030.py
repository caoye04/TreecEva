from collections import defaultdict, Counter
import itertools

# Simulated sensor array diagnostics with noise filtering and data reconciliation

# Raw sensor inputs (simulated)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
raw_readings = [
    [102, 98, 105, 110, 95],
    [205, 198, 200, 210, 190],
    [301, 303, 299, 305, 297],
    [400, 410, 395, 405, 415]
]

# Irrelevant auxiliary mapping (distractor)
legacy_mapping = {s: f'OLD_{i}' for i, s in enumerate(sensor_ids)}

# Noise threshold parameters (some are red herrings)
noise_floor = 5
clipping_threshold = 1000
baseline_offset = 0.5

# Data structure initialization
calibrated = {}
outlier_flags = defaultdict(list)
consistency_log = []

# Calibration phase with conditional filtering
for idx, readings in enumerate(raw_readings):
    sensor = sensor_ids[idx]
    filtered = []
    flags = []

    # Mean and variance for adaptive thresholding
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    std_dev = variance ** 0.5

    # Adaptive threshold (used)
    adaptive_threshold = 2 * std_dev if std_dev > 3 else 6

    # Dead code path - never triggered due to fixed data (distractor)
    if mean_val < 0:
        scaled = [x * 1.1 for x in readings]
        consistency_log.append(f'{sensor}: inverted domain correction')
    elif any(x > clipping_threshold for x in readings):
        # This block is unreachable with current data (red herring)
        clipped = [min(x, clipping_threshold) for x in readings]
        consistency_log.append(f'{sensor}: clipping applied')
        calibrated[sensor] = sum(clipped) / len(clipped)
    else:
        # Actual processing path
        for x in readings:
            if abs(x - mean_val) > adaptive_threshold:
                flags.append(True)
                # Apply mild Winsorizing instead of removal
                adjusted = mean_val
                filtered.append(adjusted)
            else:
                flags.append(False)
                filtered.append(x)
        
        # Final calibration uses trimmed mean concept
        trimmed_mean = sum(filtered) / len(filtered)
        calibrated[sensor] = trimmed_mean + baseline_offset  # Small systematic bias added
    
    outlier_flags[sensor] = flags

# Cross-sensor consistency analysis (partially irrelevant)
flag_counts = {s: sum(outlier_flags[s]) for s in sensor_ids}
total_outliers = sum(flag_counts.values())

# Decoy diagnostic chain (not used in final result)
if total_outliers > 10:
    status_code = 0xACE1
elif total_outliers > 5:
    status_code = 0xDEF2
else:
    status_code = 0xBAD3  # Actually unused

# Real computation begins here: bitwise signature from sensor IDs
signature = 0
for s in sensor_ids:
    # XOR hash of first character ASCII values
    signature ^= ord(s[0])

# Combine with statistical moment
means = [calibrated[s] for s in sensor_ids]
mean_of_means = sum(means) / len(means)
second_moment = sum((m - mean_of_means) ** 2 for m in means)

# Use itertools to generate pairwise combinations (only count matters)
pairwise_combinations = list(itertools.combinations(sensor_ids, 2))
combination_count = len(pairwise_combinations)  # Used as scaling factor

# Composite score construction
aggregate_score = 0
for i, m in enumerate(means):
    # Weight by index parity and combination count
    weight = combination_count if i % 2 == 0 else 1
    aggregate_score += m * weight

# Spurious entropy calculation (distractor)
reading_chain = list(itertools.chain.from_iterable(raw_readings))
freq_counter = Counter(reading_chain)
entropy = 0
if freq_counter:
    total = sum(freq_counter.values())
    entropy = -sum((count / total) * (count / total) ** 0.5 for count in freq_counter.values())

# Correction factor based on signature and second moment
correction_factor = (signature ^ int(second_moment)) & 0xFF  # Bit masking to cap size

# Key statement: final diagnostic fusion
final_diagnostic = aggregate_score + correction_factor

# Additional decoy logic (never executed but looks important)
if __debug__:
    import sys
    debug_stack = sys._getframe().f_code.co_name
    # This runs only if optimized mode is off, but value not used

# Only this print matters
print(f"Target result: {final_diagnostic}")