import math

# Simulated sensor data processing with red herrings and complex flow
def preprocess_signal(raw):    
    offset = 107
    scale = 0.93
    filtered = [(x - offset) * scale for x in raw if x > 50]
    return filtered

# Irrelevant transformation - distractor
compute_factor = lambda a, b: (a ** 0.5 + b ** 0.5) * 0.1

# Core pattern analyzer - actually used
analyze_pattern = lambda seq: sum([seq[i] * (-1)**i for i in range(0, len(seq), 2)])

# Unused recursive function - dead code path
def recursive_denoise(data, depth=0):
    if depth > 3 or len(data) < 2:
        return data
    mid = len(data) // 2
    return recursive_denoise(data[:mid], depth+1) + recursive_denoise(data[mid:], depth+1)

# Misleading statistical functions - decoy metrics
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

def get_peak_width(signal):
    if not signal:
        return 0
    peak = max(signal)
    occurrences = [i for i, x in enumerate(signal) if x == peak]
    return occurrences[-1] - occurrences[0] if occurrences else 0

# Data masking operation - irrelevant slicing
mask_noise = lambda arr: arr[1:-1] if len(arr) > 2 else arr

# Real data pipeline starts here
raw_sensor_data = [88, 105, 63, 110, 92, 67, 119, 54, 124, 71, 89, 101, 58, 113, 66]

# Step 1: Apply preprocessing filter
filtered_readings = preprocess_signal(raw_sensor_data)

# Step 2: Spurious entropy calculation - distraction
entropy_metric = compute_entropy(filtered_readings)

# Step 3: Masking that isn't used later - red herring
masked_signal = mask_noise(filtered_readings)

# Step 4: Transform via slicing and scaling - relevant
transformed_data = [x * 0.1 for i, x in enumerate(filtered_readings) if i % 3 == 0]

# Step 5: Additional fake feature extraction
peak_width = get_peak_width(filtered_readings)

# Step 6: Decoy dictionary operations with unused results
stats_summary = {
    'count': len(filtered_readings),
    'base_entropy': entropy_metric,
    'temp_offset': 23.5,
    'readings_slice': filtered_readings[::2],
    'useless_flag': True
}

# Step 7: Add spurious dictionary computation
aux_data = {
    'factor_x': compute_factor(100, 200),
    'diagnostics': {k: v for k, v in stats_summary.items() if 'slice' not in k},
    'timestamp': 1678800000
}

# Step 8: Actual critical computation
final_diagnostic = analyze_pattern(transformed_data)

# Print result as required
print(f"Result: {final_diagnostic}")