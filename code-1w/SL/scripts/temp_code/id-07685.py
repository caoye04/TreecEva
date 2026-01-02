import math

# Simulated sensor array diagnostics with noise filtering and anomaly detection
def process_sensors(raw_data, threshold=0.75):
    normalized = [x / max(raw_data) for x in raw_data]
    anomalies = []
    running_sum = 0
    temp_offset = 0.0

    # Irrelevant temperature compensation (distractor)
    ambient_temp = 23.5
    temp_compensation = [math.sin(x) * ambient_temp for x in normalized[:5]]

    for i, val in enumerate(normalized):
        if val > threshold:
            anomalies.append(i)
        running_sum += val * (i + 1)

    score = sum(math.sqrt(x) for x in normalized if x > 0.5)
    return anomalies, running_sum, score


def transform_sequence(seq):
    # Complex but ultimately unused transformation (dead path)
    shifted = seq[-3:] + seq[:-3]
    xor_key = 242
    masked = [x ^ xor_key for x in shifted]
    reversed_chunks = [masked[i:i+2][::-1] for i in range(0, len(masked), 2)]
    flattened = [item for chunk in reversed_chunks for item in chunk]
    return flattened


def filter_metrics(data_points):
    # Key preprocessing: extract every third reading and apply decay factor
    decaying_samples = []
    decay_factor = 0.92
    for idx in range(0, len(data_points), 3):
        adjusted = data_points[idx] * (decay_factor ** (idx // 3))
        decaying_samples.append(round(adjusted, 4))

    # Add dummy smoothing (irrelevant)
    smoothed = []
    for i in range(len(decaying_samples)):
        window = decaying_samples[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))

    # Real processing: keep only those above dynamic threshold
    dynamic_threshold = sum(decaying_samples) / len(decaying_samples) * 1.1
    filtered = [x for x in decaying_samples if x > dynamic_threshold]

    # Dummy modular arithmetic (red herring)
    checksum = 0
    for x in filtered:
        checksum = (checksum + int(x * 100)) % 97

    return filtered


def analyze_readings(metrics):
    if not metrics:
        return -1
    
    # Compute weighted index using bitwise weighting
    weights = [1 << i for i in range(len(metrics))]  # exponentially increasing weights
    weighted_sum = sum(metrics[i] * weights[i] for i in range(len(metrics)))
    total_weight = sum(weights)
    
    # Apply logarithmic compression
    compressed_index = math.log(weighted_sum + 1) / math.log(total_weight + 1)
    
    # Secondary metric: count of values above median (unused)
    sorted_vals = sorted(metrics)
    median_val = sorted_vals[len(sorted_vals)//2]
    above_median_count = len([x for x in metrics if x > median_val])
    
    # Final diagnostic derived from compressed index and length
    base_diagnostic = int(compressed_index * 10000)
    adjustment = (len(metrics) ** 2) * 17
    final_diagnostic = base_diagnostic + adjustment
    
    # Early return trap (never reached due to logic)
    if base_diagnostic < 0:
        return 0
        
    return final_diagnostic

# Main execution sequence
if __name__ == '__main__':
    # Simulated input: IoT sensor readings (vibration intensity)
    sensor_readings = [89, 102, 76, 134, 155, 67, 143, 112, 98, 130, 144, 72, 108]
    
    # Step 1: Detect high-intensity anomaly indices (used for distraction)
    detected_anomalies, activity_trace, heuristic_score = process_sensors(sensor_readings)
    
    # Step 2: Transform sequence (completely irrelevant)
    transformed = transform_sequence(sensor_readings)
    
    # Step 3: Filter metrics - this is critical path
    filtered_metrics = filter_metrics(sensor_readings)
    
    # Step 4: Analyze filtered metrics to produce result
    final_diagnostic = analyze_readings(filtered_metrics)
    
    # Output target result
    print(f"Result: {final_diagnostic}")