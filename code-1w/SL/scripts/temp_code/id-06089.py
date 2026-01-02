import math

# Simulated sensor data from a distributed environmental monitoring system
def fetch_sensor_readings():
    raw_readings = [
        23.4, 19.5, 25.1, 17.3, 20.8, 22.7, 18.9, 24.0, 26.5, 15.2,
        21.3, 16.8, 23.9, 14.7, 19.1, 27.0, 20.2, 18.4, 22.1, 13.9
    ]
    return raw_readings

# Outlier detection using interquartile range (distractor function - not used in final computation)
def detect_outliers_iqr(data):
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in data if x < lower_bound or x > upper_bound]

# Legacy normalization method (dead code path)
def normalize_legacy(readings):
    min_val = min(readings)
    max_val = max(readings)
    return [(x - min_val) / (max_val - min_val) for x in readings]

# Signal processing: apply moving average filter
def smooth_signal(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window = signal[start:end]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Transform raw sensor data into indexed metrics
def transform_readings(raw):
    indexed = {i: val * 1.8 + 32 for i, val in enumerate(raw)}  # Convert to Fahrenheit
    keys = list(indexed.keys())
    midpoint = len(keys) // 2
    first_half = [indexed[k] for k in keys[:midpoint]]
    second_half = [indexed[k] for k in keys[midpoint:]]
    
    # Irrelevant aggregation (distractor)
    avg_first = sum(first_half) / len(first_half) if first_half else 0
    avg_second = sum(second_half) / len(second_half) if second_half else 0
    
    # Slice and reverse second half (used later)
    processed_slice = second_half[::-1]
    
    # Bit manipulation on indices (red herring)
    bit_shifted_indices = [k << 1 for k in keys]
    _ = [bit_shifted_indices[i] ^ 3 for i in range(len(bit_shifted_indices))]  # Unused
    
    return {
        'data': indexed,
        'diagnostics': {
            'first_avg_f': avg_first,
            'second_avg_f': avg_second,
            'slice_rev': processed_slice
        }
    }

# Calculate adaptive thresholds based on time-of-day index
def generate_threshold_map(base_offset=10.0):
    hours = list(range(24))
    thresholds = {}
    for h in hours:
        if h < 6 or h > 18:
            factor = 0.8
        elif 10 <= h <= 14:
            factor = 1.2
        else:
            factor = 1.0
        thresholds[h] = base_offset * factor
    
    # Decoy structure (not fully used)
    decoy_weights = {h: math.cos(h * math.pi / 12) for h in hours}
    _ = sum(decoy_weights.values())  # Computed but irrelevant
    
    return thresholds

# Core diagnostic processor
def process_metrics(metrics_dict, thresholds):
    data = metrics_dict['data']
    diagnostics = metrics_dict['diagnostics']
    slice_data = diagnostics['slice_rev']
    
    # Extract every other element from reversed slice (actual usage)
    sampled = slice_data[::2]
    
    # Apply dynamic thresholding based on index modulo 24 (simulating hourly cycle)
    aggregated = 0.0
    for i, val in enumerate(sampled):
        hour = i % 24
        threshold = thresholds[hour]
        if val > threshold:
            deviation = val - threshold
            # Non-linear response
            score = math.log(1 + deviation) * (i + 1)
            aggregated += score
    
    # Secondary adjustment using unused diagnostic (distractor)
    phantom_influence = diagnostics.get('first_avg_f', 0) * 0.001  # Negligible effect
    result = aggregated - phantom_influence
    
    # Final transformation
    final_score = int(round(result * 100))
    return final_score

# Orchestration function
def main_pipeline():
    # Step 1: Fetch raw data
    readings = fetch_sensor_readings()
    
    # Step 2: Smooth signal (used)
    smoothed = smooth_signal(readings)
    
    # Step 3: Transform data structure
    transformed_data = transform_readings(smoothed)
    
    # Step 4: Generate threshold map
    threshold_map = generate_threshold_map(12.5)
    
    # Step 5: Compute final diagnostic
    final_diagnostic = process_metrics(transformed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")
    
    # Irrelevant secondary outputs (distractors)
    _ = sum(transformed_data['data'].values()) * 0.01
    _ = len(threshold_map.keys()) ** 2
    
    return final_diagnostic

# Execute
if __name__ == "__main__":
    main_pipeline()