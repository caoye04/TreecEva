def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant helper function (decoy)
def smooth_data(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        avg = (data[i-1] + data[i] + data[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(data[-1])
    return smoothed

# Unused transformation (dead code path)
def transform_signal(signal):
    return [x << 2 for x in signal if x % 2 == 0]

# Distractor: complex but unused bitwise routine
def encrypt_values(arr, key=7):
    return [((val ^ key) << 1) & 255 for val in arr]

# Real processing chain
base_sequence = [3, 7, 4, 8, 2, 9, 1, 6, 5]

# Irrelevant string-based metadata (distractor)
sensor_tag = "HXL-9G"
if sensor_tag.startswith("HX") and len(sensor_tag) == 6:
    calibration_code = sum([ord(c) for c in sensor_tag]) // 6
else:
    calibration_code = 0

# Fake preprocessing step that isn't used later
filtered_data = [x for x in base_sequence if x % 2 == 1]

# Actual relevant data path
processed = [x * 2 + 1 for x in base_sequence]
even_mask = [1 if x % 2 == 0 else 0 for x in processed]

# Another red herring: dictionary with misleading stats
diagnostic_log = {
    'peak_count': analyze_pattern(base_sequence),
    'avg_value': sum(base_sequence) / len(base_sequence),
    'max_shift': max(processed) - min(base_sequence),
    'status_flag': 'CALIBRATED' if calibration_code > 0 else 'UNKNOWN',
    'checksum': (sum(base_sequence) ^ 255) & 127
}

# Conditional expression with distractor logic
mode_override = 'FORCE' if diagnostic_log['peak_count'] > 2 else 'NORMAL'
override_factor = 3 if mode_override == 'FORCE' else 1

# Key computation buried in noise
intermediate_score = 0
for idx, val in enumerate(processed):
    if idx % 2 == 0:
        intermediate_score += val * even_mask[idx]
    else:
        # This branch does nothing due to mask being 0 on odd indices
        intermediate_score += val >> 1 if even_mask[idx] else 0

# Real dependency chain starts here
health_data = [abs(x - 5) for x in processed]
threshold = sum(even_mask) * override_factor

# Core logic hidden among distractions
def process_metrics(data, limit):
    if limit <= 0:
        return -1
    
    # Dictionary operations (required feature)
    stats = {
        'length': len(data),
        'min_val': min(data),
        'max_val': max(data),
        'range': max(data) - min(data)
    }
    
    # String method used as part of non-critical formatting (distractor)
    metric_id = f"DMX-{stats['length']}".replace('D', 'X')
    
    # Actual answer derivation
    clipped = [min(x, stats['range'] // 2) for x in data]
    adjustment = stats['min_val'] + (stats['max_val'] // 4)
    
    # Final computation
    total = sum(clipped) // (limit or 1)
    final_diagnostic = (total - adjustment) * (1 + (len(metric_id) % 2))
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold)

# Print required output
print(f"Target result: {final_diagnostic}")