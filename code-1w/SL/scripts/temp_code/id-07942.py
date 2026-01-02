import math

# Simulated sensor data from multiple sources
def fetch_sensor_readings():
    raw_stream = [23.1, 19.5, 20.3, 25.7, 18.9, 22.4, 21.0, 19.8, 24.2]
    scaling_factor = 1.05
    adjusted = [round(x * scaling_factor, 2) for x in raw_stream]  # Minor calibration
    return adjusted

# Legacy function – unused but looks relevant
def legacy_calibrate(data):
    return [x * 0.98 for x in data if x > 20]

# Signal processing pipeline
def clean_noise(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        window_vals = signal[start:end]
        smoothed.append(sum(window_vals) / len(window_vals))
    return [round(x, 2) for x in smoothed]

def extract_features(data):
    # Compute statistical features
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    peak = max(data)
    
    # Distractor: irrelevant feature computations
    entropy_proxy = -sum(math.log(abs(x) + 1e-5) for x in data)
    dummy_transform = ''.join([chr(int(abs(x)) % 26 + 97) for x in data[:5]])
    
    # Actual used features
    return {
        'avg': round(mean_val, 2),
        'variance': round(variance, 3),
        'peak': peak,
        'count_above_20': len([x for x in data if x > 20.0])
    }

# Threshold configuration from external profile (simulated)
def load_threshold_profile(mode='diagnostic'):
    profile = {
        'diagnostic': {'base': 20.5, 'sensitivity': 0.8, 'window': 3},
        'monitoring': {'base': 19.0, 'sensitivity': 1.1, 'window': 5}
    }
    return profile.get(mode, profile['diagnostic'])

# Data slicing and filtering based on dynamic criteria
def filter_segments(data, flags, mode='keep_valid'):
    # Simulate segmented analysis
    n = len(data)
    mid = n // 2
    left_half = data[:mid]
    right_half = data[mid:]
    
    if mode == 'keep_valid':
        # Only use right half in this context
        return right_half  # Red herring: left_half computed but unused
    else:
        return left_half[::-1]

# Core analysis function
def analyze_signal(features, thresholds):
    base = thresholds['base']
    sensitivity = thresholds['sensitivity']
    
    # Weighted diagnostic score
    deviation_score = (features['avg'] - base) * sensitivity
    stability_penalty = features['variance'] * 0.5
    peak_bonus = 2.0 if features['peak'] > base + 2.0 else 0.0
    
    # Misleading intermediate calculation (not used in final result)
    hypothetical = (features['avg'] + features['peak']) / 2 * sensitivity - stability_penalty
    
    # Final diagnostic logic
    raw_diagnostic = deviation_score - stability_penalty + peak_bonus
    
    # Clamp to meaningful range and round
    return int(round(max(-100, min(100, raw_diagnostic)), 0))

# Unused utility – distractor
def generate_report_snapshot(data):
    timestamp_slice = "2024-Q3"
    summary_hash = sum([ord(c) for c in timestamp_slice]) + len(data)
    return f"Report_{summary_hash}"

# Main execution flow
if __name__ == "__main__":
    # Step 1: Fetch and preprocess raw sensor input
    raw_data = fetch_sensor_readings()
    
    # Step 2: Apply noise reduction filter
    filtered_signal = clean_noise(raw_data)
    
    # Step 3: Extract analytical features
    extracted_features = extract_features(filtered_signal)
    
    # Step 4: Load threshold configuration
    threshold_config = load_threshold_profile(mode='diagnostic')
    
    # Step 5: Segment filtering (simulate selective processing)
    segments = filter_segments(filtered_signal, None, mode='keep_valid')
    processed_data = extract_features(segments)  # Re-extract on filtered subset
    
    # Step 6: Perform final diagnostic analysis
    final_diagnostic = analyze_signal(processed_data, threshold_config)
    
    # Print result for evaluation
    print(f"Result: {final_diagnostic}")