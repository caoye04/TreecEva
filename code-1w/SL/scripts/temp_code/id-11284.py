import math

# Simulated sensor array diagnostics with noise filtering and health scoring
def analyze_sensor_health(raw_readings, baseline):
    adjusted = [x - baseline for x in raw_readings]
    squared_errors = [val ** 2 for val in adjusted if val > 0.5]  # Only penalize positive deviations
    avg_sq_error = sum(squared_errors) / len(squared_errors) if squared_errors else 0.0

    # Irrelevant diagnostic path (dead code)
    temp_score = 0
    if len(raw_readings) > 100:
        temp_score = sum(1 for x in raw_readings if x > 50) * 0.1

    health_index = 100 / (1 + avg_sq_error) if avg_sq_error > 0 else 100
    return int(health_index)


def extract_critical_indices(signal, sensitivity):
    # Find peaks above sensitivity threshold
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1] and signal[i] > sensitivity:
            peaks.append(i)
    
    # Distractor: irrelevant valley detection
    valleys = []
    for i in range(1, len(signal) - 1):
        if signal[i] < signal[i-1] and signal[i] < signal[i+1]:
            valleys.append(i)  # Not used later

    return peaks[:5]  # Limit to top 5 peak indices


def filter_anomalies(dataset, limit):
    # Outlier removal using IQR method (simplified)
    sorted_vals = sorted(dataset)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    filtered = [x for x in dataset if lower_bound <= x <= upper_bound]
    
    # Decoy transformation
    shifted = [x * 1.05 for x in dataset if x < 0]  # Unused
    
    return filtered


def compute_entropy(data):
    # Simple entropy approximation based on value frequency
    if not data:
        return 0.0
    freq_map = {}
    for val in data:
        freq_map[val] = freq_map.get(val, 0) + 1
    total = len(data)
    entropy = -sum((count/total) * math.log2(count/total) for count in freq_map.values())
    return round(entropy, 4)


def process_readings(data, min_threshold):
    # Core processing chain
    valid_inputs = [x for x in data if x >= min_threshold]
    
    # Bit manipulation red herring
    bit_encoded = 0
    for x in valid_inputs[:8]:
        bit_encoded |= (1 << (int(x) % 32))  # Complex but unused
    
    # Conditional expression with slicing
    subset = valid_inputs[::2] if len(valid_inputs) > 10 else valid_inputs[::-1]
    
    # Real computation path
    magnitude_factor = sum(abs(x) for x in subset)
    sign_contributions = sum(-1 if x < 0 else 1 for x in subset)
    
    # Final transformation
    score = magnitude_factor * sign_contributions + len(subset)
    
    # Secondary distractor: combinatorics calculation (unused)
    combinations = 0
    n = len(valid_inputs)
    if n > 1:
        combinations = (n * (n - 1)) // 2
    
    return score

# Main execution block
if __name__ == "__main__":
    # Simulated input data from sensor grid
    raw_sensor_data = [
        10.2, 9.8, 11.5, 8.7, 12.1, 7.3, 13.0, 6.9, 14.2, 5.8,
        15.1, 4.7, 16.3, 3.9, 17.0, 5.2, 18.1, 4.3, 19.2, 3.8,
        20.0, 105.5, -5.2, 110.3, -3.8, 12.5, 11.7, 10.9, 13.2, 14.1
    ]

    # Irrelevant preprocessing step
    normalized = [round((x - min(raw_sensor_data)) / (max(raw_sensor_data) - min(raw_sensor_data)), 3) for x in raw_sensor_data]
    
    # Health assessment (used only for distraction)
    health_status = analyze_sensor_health(raw_sensor_data, baseline=10.0)
    
    # Extract critical event indices
    critical_positions = extract_critical_indices(raw_sensor_data, sensitivity=15.0)
    
    # Filter anomalies
    cleaned_data = filter_anomalies(raw_sensor_data, limit=2)
    
    # Compute data entropy (distractor metric)
    signal_entropy = compute_entropy([int(x) for x in cleaned_data])
    
    # Key threshold for processing
    threshold = 5.0
    
    # Filtered data used in final step
    filtered_data = [x for x in cleaned_data if x != 105.5 and x != 110.3]  # Remove known spikes
    
    # Final diagnostic computation
    final_diagnostic = process_readings(filtered_data, threshold)
    
    # Output result
    print(f"Result: {final_diagnostic}")