import itertools

# Simulated sensor array data with noise and calibration offsets
data_stream = [18, 22, 15, 30, 12, 27, 20, 25, 10, 13]
calibration_map = {'offset_A': 3, 'offset_B': -2, 'gain': 1.5}
noise_floor = 9
activation_threshold = 17

# Irrelevant auxiliary variables (distractors)
system_uptime = 14200
packet_loss_count = 5
redundant_cache = {x: x ** 2 for x in range(15)}
legacy_mode_flag = True
debug_snapshot = []

# Preprocessing stage: apply gain and offset correction
corrected_readings = []
for val in data_stream:
    adjusted = (val + calibration_map['offset_A']) * calibration_map['gain']
    corrected_readings.append(int(adjusted))

# Secondary noise filtering (only values above noise floor are valid)
filtered_readings = [x for x in corrected_readings if x > noise_floor]

# Misleading intermediate analysis (dead-end computation)
anomaly_score = 0
for i in range(1, len(filtered_readings)):
    if filtered_readings[i] - filtered_readings[i-1] > 10:
        anomaly_score += 1
# This score is never used again

# Data augmentation via cyclic permutations (relevant only if pattern exists)
window_size = 3
sliding_windows = list(itertools.sliding_window(filtered_readings, window_size))

# Define transformation function using lambda (Python idiom)
transform_fn = lambda win: (win[0] + win[2]) // 2  # average of first and last

# Apply transformation only to symmetric patterns
transformed_data = []
for window in sliding_windows:
    if window[0] != window[2]:  # non-symmetric
        continue
    transformed_value = transform_fn(window)
    if transformed_value % 2 == 0:  # even values only
        transformed_data.append(transformed_value)

# Decoy recursive function (never called)
def recursive_integrity_check(seq, idx=0):
    if idx >= len(seq):
        return True
    if seq[idx] < 0:
        return False
    return recursive_integrity_check(seq, idx + 1)

# Another red herring: set-based uniqueness check on irrelevant data
temp_set = set(corrected_readings)
duplicate_count = len(corrected_readings) - len(temp_set)  # unused

# Control flow obfuscation: nested conditionals with misleading branches
baseline_reference = 19
adjustment_factor = 0
if len(transformed_data) > 2:
    adjustment_factor += 2
    if sum(transformed_data) / len(transformed_data) > baseline_reference:
        adjustment_factor += 1
        for x in transformed_data:
            if x > baseline_reference * 1.1:
                adjustment_factor += 0.5  # float creep
    else:
        adjustment_factor -= 1  # dead branch due to data
else:
    adjustment_factor = -5  # not taken

threshold = activation_threshold + adjustment_factor

# Core diagnostic logic (recursive helper)
def analyze_pattern(data_list, limit):
    if not data_list:
        return -1
    
    # Filter values above dynamic threshold
    qualified = [x for x in data_list if x > limit]
    if len(qualified) == 0:
        return min(data_list) - 3
    
    # Compute weighted centroid of qualified signals
    total_weight = 0
    weighted_sum = 0
    for i, val in enumerate(qualified):
        weight = 1 / (i + 1)  # decaying weight
        weighted_sum += val * weight
        total_weight += weight
    
    raw_centroid = weighted_sum / total_weight
    
    # Final adjustment based on parity and size
    if len(qualified) % 2 == 0:
        result = int(raw_centroid) + 2
    else:
        result = int(raw_centroid) - 1
    
    return result

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print required output
print(f"Target result: {final_diagnostic}")