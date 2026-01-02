import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw = [2.1, 3.5, 4.8, 5.2, 6.9, 7.0, 8.3, 9.6, 10.1]
    offset = 0.9
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant auxiliary function - dead code path
def legacy_calibrate(x):
    return (x * 1.05) - 0.2 if x > 5 else (x * 0.98) + 0.1

# Data transformation pipeline
def transform_signal(signal):
    filtered = [math.sin(x / 2) * math.cos(x / 3) for x in signal]
    amplified = [val * 1.75 for val in filtered]
    return amplified

# Outlier detection - used but contains red herring logic
def detect_spikes(data, limit=1.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    # Misleading: this count is never used
    spike_count = sum(1 for x in data if abs(x - mean_val) > limit * std_dev)
    return std_dev > 0.5

# Core pattern analyzer - relevant
def compute_entropy(values):
    total = sum(abs(v) for v in values)
    if total == 0:
        return 0.0
    probs = [abs(v) / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 4)

# Unused decoy function - looks important but irrelevant
def normalize_dataset(arr):
    min_val, max_val = min(arr), max(arr)
    if max_val == min_val:
        return [0.5] * len(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Primary analysis function
def analyze_pattern(data, cutoff):
    # Step 1: Filter based on threshold
    subset = [x for x in data if x > cutoff]
    
    # Step 2: Compute rolling differences (3-level nesting)
    diffs = []
    for i in range(len(subset)):
        inner_diffs = []
        for j in range(i+1, len(subset)):
            diff = subset[j] - subset[i]
            if diff > 0.25:
                inner_diffs.append(diff)
        if inner_diffs:
            avg_inner = sum(inner_diffs) / len(inner_diffs)
            diffs.append(avg_inner)
    
    # Step 3: Aggregate statistics
    if not diffs:
        base_score = 0
    else:
        base_score = int(sum(diffs) * 100)
    
    # Step 4: Conditional entropy adjustment (conditional expression)
    entropy = compute_entropy(data)
    adjustment = 1.5 if entropy > 2.0 else 0.8
    
    # Step 5: Apply non-linear scaling
    scaled_score = base_score * adjustment
    
    # Step 6: Apply fake correction factor (distractor - not actually used)
    correction_factor = 0.91
    temp_estimate = scaled_score * correction_factor  # Red herring
    final_estimate = scaled_score  # Actual path
    
    # Step 7: Final threshold gating
    result = final_estimate if detect_spikes(data) else final_estimate / 2
    
    # Step 8: Clamp to realistic diagnostic range
    clamped = max(100, min(int(result), 9999))
    
    return clamped

# Orchestration block
if __name__ == '__main__':
    # Irrelevant initialization
    system_status = {'active': True, 'mode': 'diagnostic', 'version': '3.7'}
    calibration_sequence = [legacy_calibrate(x) for x in range(5)]  # Dead computation
    
    # Real data flow
    readings = collect_readings()                    # Step 1
    transformed_data = transform_signal(readings)    # Step 2
    threshold = -1.0
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output required result
    print(f"Result: {final_diagnostic}")