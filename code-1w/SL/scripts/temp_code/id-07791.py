from collections import defaultdict

# Simulate sensor data processing with noise filtering and performance evaluation
def collect_sensor_metrics(raw_readings):
    processed = []
    noise_floor = 0.05
    for val in raw_readings:
        adjusted = abs(val - 0.1) * 1.2
        if adjusted > noise_floor:
            processed.append(round(adjusted, 3))
    return processed

def compute_entropy(values):
    freq = defaultdict(int)
    total = 0
    for v in values:
        freq[int(v * 10)] += 1
        total += 1
    entropy = 0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # simplified pseudo-entropy
    return round(entropy, 4)

def evaluate_performance(metrics, threshold):
    cumulative = 0
    peak_count = 0
    temp_buffer = []
    
    for m in metrics:
        if m > threshold * 1.1:
            peak_count += 1
            cumulative += m * 0.8
        elif m > threshold:
            cumulative += m * 0.5
        else:
            temp_buffer.append(m)
    
    # Secondary adjustment based on distribution shape
    high_peaks = peak_count > len(metrics) * 0.3
    size_penalty = len(temp_buffer) * 0.01
    
    final_score = int(cumulative * 100) - len(temp_buffer)
    
    # Irrelevant debug computation (distractor)
    debug_checksum = 0
    for i, m in enumerate(metrics):
        debug_checksum += (i + 1) * int(m * 100)
    
    # Early return not taken (dead logic path - distractor)
    if high_peaks and size_penalty < 0.5:
        return 999  # unreachable under this input
    
    return final_score

# Main execution
raw_input = [0.08, 0.12, 0.15, 0.09, 0.11, 0.13, 0.14, 0.07, 0.10, 0.16]
filtered_data = collect_sensor_metrics(raw_input)
metric_data = [x for x in filtered_data if x > 0.06]  # minor filter
base_threshold = 0.095

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

# Output result
print(f"Result: {final_score}")