import itertools

# Simulated sensor data preprocessing with red herrings
def fetch_raw_signals():
    return [18, 22, 19, 25, 21, 17, 23]

# Irrelevant transformation - decoy function
def amplify_signal(data):
    amplified = [x * 1.5 + 3 for x in data]
    offset = sum(amplified) / len(amplified)
    return [x - offset for x in amplified]

# Unused noise filter - dead code path
def denoise(data, strength=0.8):
    return [x * strength for x in data]

# Real transformation: map to parity and magnitude threshold
def transform_readings(raw):
    threshold = 20
    return [(1 if x >= threshold else 0, abs(x - threshold)) for x in raw]

# Auxiliary utility - looks important but not used in main flow
def rolling_average(data, window=3):
    if len(data) < window:
        return []
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

# Core processing with recursion and slicing
def extract_features(pairs):
    # Extract every second element from first half as a distraction
    mid = len(pairs) // 2
    decoy_slice = pairs[:mid][1::2]
    
    # Actual relevant logic: recursive count of high-magnitude events
    def count_significant_recursive(index):
        if index >= len(pairs):
            return 0
        current_flag, magnitude = pairs[index]
        # Only count if flag is set AND magnitude > 2
        contribution = 1 if (current_flag == 1 and magnitude > 2) else 0
        return contribution + count_significant_recursive(index + 1)
    
    feature_a = count_significant_recursive(0)
    feature_b = sum(pair[1] for pair in pairs) // 4  # Integer division
    
    # Decoy aggregation using itertools
    combinations = list(itertools.combinations([p[0] for p in pairs], 2))
    decoy_complexity = len(combinations) + (feature_b % 5)
    
    return (feature_a, feature_b, decoy_complexity)

# Final processing step
def process_sequence(features):
    f1, f2, f3 = features
    # Conditional expression with misleading weight
    adjustment = f3 * 0.1 if f1 > 2 else f3 * 0.05
    # Key deterministic calculation
    result = (f1 * 100) + (f2 * 10) + int(round(adjustment))
    return result

# Orchestration with irrelevant intermediate steps
raw_sensor_data = fetch_raw_signals()
noise_filtered = amplify_signal(raw_sensor_data)  # Unused
baseline_corrected = [x - 18 for x in raw_sensor_data]  # Partially used only for distraction

transformed_data = transform_readings(raw_sensor_data)
extracted = extract_features(transformed_data)
final_output = process_sequence(extracted)

# Print required output
print(f"Target result: {final_output}")