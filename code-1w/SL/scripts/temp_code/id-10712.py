import math

# Simulated sensor array diagnostics with noise filtering and pattern analysis

def collect_readings():
    raw_signals = [2.1, 3.5, -1.2, 8.8, 4.0, -3.3, 7.2, 0.1, 9.9, -5.0]
    noise_floor = 0.5
    filtered = [x for x in raw_signals if abs(x) > noise_floor]
    return filtered

def generate_baseline(count):
    # Irrelevant function - generates unused baseline data
    return [math.sin(i * 0.5) for i in range(count + 5)]

def extract_features(data):
    peaks = [x for x in data if x > 5.0]
    negatives = [x for x in data if x < 0]
    magnitude_sum = sum(abs(x) for x in data)
    avg = sum(data) / len(data)
    return peaks, negatives, magnitude_sum, avg

def transform_signal(signal):
    # Applies exponential scaling then truncates
    scaled = [math.exp(x / 10.0) for x in signal]
    truncated = [int(x * 100) / 100.0 for x in scaled]  # Round to 2 decimals
    shifted = [x + 0.1 for x in truncated]  # Small offset
    return shifted

def compute_entropy(data):
    # Dead-end computation - not used in final result
    total = sum(data)
    probs = [abs(x / total) for x in data if x != 0]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return round(entropy, 4)

def validate_consistency(arr):
    # Distractor function: checks symmetry but unused
    n = len(arr)
    return all(abs(arr[i] + arr[n-1-i]) < 1e-6 for i in range(n//2))

def analyze_patterns(data, config):
    feature_vector = []
    for chunk in data:
        if len(chunk) == 0:
            feature_vector.append(0)
            continue
        max_val = max(chunk)
        min_val = min(chunk)
        span = max_val - min_val
        mid = (max_val + min_val) / 2
        if span > config['threshold_high']:
            flag = 2
        elif span > config['threshold_low']:
            flag = 1
        else:
            flag = 0
        score = mid * flag
        feature_vector.append(score)
    
    # Final aggregation
    aggregate = sum(feature_vector)
    adjustment = config.get('adjustment', 0)
    final_score = aggregate + adjustment
    return int(round(final_score))

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect and filter sensor readings
    sensor_readings = collect_readings()  # [2.1, 3.5, 8.8, 4.0, 7.2, 9.9, -5.0]
    
    # Step 2: Extract key features (some will be ignored)
    peak_values, negative_values, total_magnitude, average_value = extract_features(sensor_readings)
    
    # Step 3: Transform signal using exponential scaling
    transformed_signal = transform_signal(sensor_readings)
    
    # Step 4: Compute irrelevant entropy metric
    entropy_metric = compute_entropy(sensor_readings)  # Unused
    
    # Step 5: Create data chunks for pattern analysis
    chunk_1 = transformed_signal[1:4]  # [3.5 -> ~1.42, 8.8 -> ~2.41, 4.0 -> ~1.49]
    chunk_2 = transformed_signal[4:7]  # [7.2 -> ~2.05, 9.9 -> ~2.69, -5.0 -> ~0.61]
    chunk_3 = transformed_signal[0:2]  # [2.1 -> ~1.23, 3.5 -> ~1.42]
    
    # Misleading assignment - looks important but unused
    baseline_reference = generate_baseline(len(sensor_readings))
    
    # Validate consistency (result unused)
    is_consistent = validate_consistency(transformed_signal)
    
    # Prepare data structure for analysis
    transformed_data = [chunk_1, chunk_2, chunk_3]
    
    # Define threshold configuration
    thresholds = {
        'threshold_low': 0.8,
        'threshold_high': 1.2,
        'adjustment': -3
    }
    
    # Critical statement: analyze patterns to produce diagnostic result
    final_diagnostic = analyze_patterns(transformed_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")