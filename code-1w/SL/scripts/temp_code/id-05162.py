import itertools

# Sensor simulation and diagnostic processing system
def generate_synthetic_readings():
    base_values = [1.2, 3.4, 2.5, 4.6, 5.1, 3.3, 2.9, 4.0]
    noise_pattern = [0.1 * (i % 3) for i in range(8)]
    return [base_values[i] + noise_pattern[i] for i in range(8)]

# Irrelevant transformation - decoy function
def transform_signal(data):
    return [round(x ** 0.5, 3) for x in data if x > 2]

# Data smoothing - red herring operation
def smooth_readings(signal):
    smoothed = []
    for i in range(len(signal)):
        neighbors = signal[max(0, i-1):min(len(signal), i+2)]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed

# Core filtering logic - relevant path
def filter_outliers(readings, factor=1.5):
    median_val = sorted(readings)[len(readings)//2]
    deviation = [abs(x - median_val) for x in readings]
    mad = sorted(deviation)[len(deviation)//2]  # Median absolute deviation
    threshold = factor * mad
    return [x for x in readings if abs(x - median_val) <= threshold], median_val, mad

# Unused diagnostic - dead code path
def legacy_diagnostic(seq):
    cumulative = 0
    for val in seq:
        if val > 3.0:
            cumulative += val * 0.1
    return cumulative

# Main processing pipeline
readings = generate_synthetic_readings()

# Apply smoothing (distractor - not used in final computation)
smoothed_signal = smooth_readings(readings)

# Extract key statistical features (some used, some not)
filtered_data, median_reading, dispersion = filter_outliers(readings, factor=1.8)

# Threshold configuration map - relevant for final step
threshold_map = {
    'critical': 4.5,
    'warning': 3.7,
    'normal': 2.8
}

# Decoy data structure with misleading values
diagnostic_cache = {
    'raw_stats': {k: len([x for x in readings if x > v]) 
                  for k, v in threshold_map.items()},
    'processed_hint': sum(smoothed_signal[:4]) / 4,
    'timestamp': 1712345678
}

# Auxiliary calculation - irrelevant but plausible
redundant_score = sum(itertools.chain(
    [int(x * 10) % 7 for x in filtered_data if x < 4.0],
    [0]
))

# Secondary validation check - never invoked
def validate_consistency(arr):
    return all(abs(arr[i] - arr[i-1]) < 1.0 for i in range(1, len(arr)))

# Key state variables with distractors
active_mode = 'diagnostic'
system_flag = (len(filtered_data) % 2 == 0)
override_enable = False

# Conditional override - unused due to flag
if system_flag and override_enable:
    threshold_map['warning'] = 3.5

# String-based identifier generation - distraction
mode_prefix = active_mode[:3].upper()
run_id = mode_prefix + '-' + ''.join([
    str(int(dispersion * 100)), 
    str(len(readings))
])

# Core processing function that determines final answer
def process_readings(data, limits):
    count_critical = len([x for x in data if x >= limits['critical']])
    count_warning = len([x for x in data if 
                        limits['warning'] <= x < limits['critical']])
    count_normal = len([x for x in data if x < limits['normal']])
    
    # Complex weighting scheme
    weights = {
        'critical': -10.5,
        'warning': -2.3,
        'normal': 4.7
    }
    
    score = (weights['critical'] * count_critical + 
             weights['warning'] * count_warning + 
             weights['normal'] * count_normal)
    
    # Additional adjustment based on data characteristics
    if len(data) > 5:
        avg_val = sum(data) / len(data)
        if avg_val >= 3.5:
            score -= 5.0
        else:
            score += 2.0
    
    return round(score, 4)

# Final computation - this determines the answer
final_diagnostic = process_readings(filtered_data, threshold_map)

# Redundant print statements - distractions
print(f"Run ID: {run_id}")
print(f"Data points retained: {len(filtered_data)}")
print(f"Median: {median_reading:.2f}, MAD: {dispersion:.3f}")

# Only this output matters
print(f"Target result: {final_diagnostic}")