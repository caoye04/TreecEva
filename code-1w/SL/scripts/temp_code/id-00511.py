import itertools

# Simulated sensor data processing with distractors
def analyze_readings(readings):
    filtered = [x for x in readings if x > 25]
    outliers = [x for x in readings if x > 100]  # distractor
    normalized = [x / max(readings) for x in filtered]  # relevant
    return sum(normalized)

# Legacy function – dead code path (decoy)
def legacy_calibrate(arr):
    return [int(x * 0.9) for x in arr if x > 10]

# Core transformation logic
def transform_sequence(seq):
    shifted = [(x << 1) + 1 for x in seq]  # bit manipulation
    masked = [x & 255 for x in shifted]  # keep within byte range
    return list(set(masked))  # remove duplicates

# Weighted aggregation using dictionary lookups
def apply_weights(values, config):
    base_weights = config.get('weights', {})
    fallback = config.get('default', 1.0)
    weighted = []
    for i, v in enumerate(values):
        w = base_weights.get(i, fallback)
        weighted.append(v * w)
    return round(sum(weighted), 4)

# Recursive reduction (simple recursion)
def recursive_reduce(arr):
    if len(arr) <= 1:
        return arr[0] if arr else 0
    return recursive_reduce([arr[i] + arr[i+1] for i in range(0, len(arr)-1, 2)])

# Main scoring logic
def calculate_final_score(dataset, weights):
    # Step 1: Transform raw data
    processed = transform_sequence(dataset)
    
    # Step 2: Analyze subset (irrelevant segment)
    _ = analyze_readings([x * 2 for x in dataset if x % 2 == 0])  # red herring call
    
    # Step 3: Aggregate using windowed sums
    windows = list(itertools.windowed(processed, n=3))  # using itertools
    reduced_windows = [sum(window) for window in windows if sum(window) > 100]
    
    # Step 4: Apply recursive reduction
    interim = recursive_reduce(reduced_windows) if reduced_windows else 0
    
    # Step 5: Use dictionary-based weighting
    config = {
        'weights': {0: 1.1, 1: 0.9, 2: 1.05},
        'default': 1.0
    }
    adjustment = apply_weights([interim % 10, interim // 10], config)
    
    # Step 6: Combine with phantom metric (distractor)
    phantom_metric = len([x for x in processed if x & (x-1) == 0])  # count powers of two
    dummy_offset = phantom_metric ** 2  # unused but computed
    
    # Final score computation (key statement)
    final_score = (interim * 1.5) + adjustment - 10
    return int(final_score)

# --- Execution ---
if __name__ == "__main__":
    # Input data
    raw_data = [23, 45, 67, 89, 12, 34, 56, 78]
    weights_config = {'weights': {0: 2.0, 1: 1.5}, 'default': 0.5}
    
    # Distractor variables
    temp_result = legacy_calibrate(raw_data)
    stats_summary = {"count": len(raw_data), "max": max(raw_data), "sum": sum(raw_data)}
    
    # Key execution point
    final_score = calculate_final_score(raw_data, weights_config)
    
    # Output result
    print(f"Result: {final_score}")