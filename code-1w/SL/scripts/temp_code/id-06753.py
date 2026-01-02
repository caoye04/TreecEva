from collections import defaultdict, Counter

# Simulate sensor data processing with noise filtering and performance scoring
def preprocess_signals(raw_readings):
    filtered = []
    noise_floor = 0.05
    for val in raw_readings:
        if abs(val) > noise_floor:
            filtered.append(round(val * 100) / 100)
    return filtered

# Misleading auxiliary function (dead path - never called)
def legacy_normalization(x):
    return max(0, min(1, (x + 1) / 2))

# Unused transformation map (distractor)
transform_map = {
    'A': lambda x: x ** 2,
    'B': lambda x: x + 10,
    'C': lambda x: x * 0.5
}

# Real processing pipeline
metric_data = [-0.34, 0.67, -1.22, 0.0, 0.89, -0.45, 1.11]
processed = preprocess_signals(metric_data)

# Irrelevant statistical artifacts (distractors)
mean_proxy = sum(processed) / len(processed) if processed else 0
variance_estimate = sum((x - mean_proxy) ** 2 for x in processed) / len(processed) if processed else 0
deviation_flag = variance_estimate > 0.5

# Dummy counters (red herring)
event_counter = defaultdict(int)
for val in processed:
    category = 'positive' if val > 0 else 'negative'
    event_counter[category] += 1

# Decoy data structure with unused calculations
analysis_log = []
analysis_log.append(f"Raw count: {len(metric_data)}")
analysis_log.append(f"Filtered count: {len(processed)}")
analysis_log.append(f"Extremes: {sum(1 for x in processed if abs(x) > 1.0)}")

# Bit manipulation distraction (irrelevant to final result)
bit_flags = 0
for val in processed:
    truncated = int(abs(val))
    bit_flags |= (1 << truncated) if truncated < 32 else 0

# Core logic hidden among noise
def count_sign_switches(data):
    if len(data) < 2:
        return 0
    switches = 0
    for i in range(1, len(data)):
        if (data[i-1] >= 0) != (data[i] >= 0):
            switches += 1
    return switches

# Secondary metric (unused but plausible)
peak_count = sum(1 for x in processed if abs(x) > 0.8)

# Recursive smoothing function (not used - misleading)
def smooth_recursive(arr, factor=0.3, depth=0):
    if depth >= 3 or len(arr) == 0:
        return arr
    smoothed = [arr[0]]
    for i in range(1, len(arr)):
        smoothed.append(factor * arr[i] + (1 - factor) * smoothed[i-1])
    return smooth_recursive(smoothed, factor, depth + 1)

# Main evaluation logic (the actual relevant path)
def evaluate_performance(data):
    # Step 1: Count sign switches
    switch_penalty = count_sign_switches(data) * 10
    
    # Step 2: Sum absolute values (performance base)
    base_score = sum(abs(x) for x in data)
    
    # Step 3: Apply penalty
    adjusted = base_score - switch_penalty
    
    # Step 4: Amplify by number of positive values
    positive_multiplier = sum(1 for x in data if x > 0) or 1
    return adjusted * positive_multiplier

# Critical execution point
final_score = evaluate_performance(processed)

# Output requirement
print(f"Result: {final_score}")