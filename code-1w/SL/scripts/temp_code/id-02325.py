import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [i * 1.5 + math.sin(i) for i in range(30)]
    offset_correction = sum([math.cos(j) for j in range(10)])
    corrected = [x + offset_correction * 0.1 for x in raw_readings]
    return corrected

def extract_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append((i, round(signal[i], 3)))
    return peaks

def generate_reference_template():
    template = {i: round(math.exp(-i * 0.1), 3) for i in range(15)}
    return template

def filter_anomalies(data_points):
    baseline = sum(data_points) / len(data_points)
    variance = sum((x - baseline) ** 2 for x in data_points) / len(data_points)
    std_dev = math.sqrt(variance)
    filtered = [x for x in data_points if abs(x - baseline) < 2 * std_dev]
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(filtered)) / (max(filtered) - min(filtered)), 3) for x in filtered]
    return filtered

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def build_correlation_matrix(data):
    # Dummy function - not used in final result (dead code path)
    n = len(data)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = round(math.sin(i - j) * 0.5 + 0.5, 2)
    return matrix

def slice_temporal_window(series, start=5, end=20):
    # Extracts central segment of time-series
    return series[start:end]

def identify_unique_signatures(peaks_list):
    indices = set(p[0] for p in peaks_list)
    values = set(int(p[1] * 1000) for p in peaks_list)
    combined = indices.symmetric_difference(values)
    return sorted(list(combined)[:10])

def analyze_pattern(dataset, reference):
    # Core logic: bit manipulation on aggregated metrics
    avg_val = sum(dataset) / len(dataset)
    squared_sum = sum(x * x for x in dataset)
    metric_a = int(avg_val * 10) & 255  # Lower byte of scaled average
    metric_b = int(squared_sum / 100) % 256  # Modulo energy measure
    xor_key = metric_a ^ metric_b
    
    # Bit rotation (simulated via shifting)
    rotated = ((xor_key << 3) & 255) | (xor_key >> 5)
    
    # Use of set operations (required feature)
    ref_set = set(reference.values())
    data_set = set(round(x) for x in dataset)
    overlap = data_set.intersection(ref_set)
    intersection_size = len(overlap)
    
    # Final computation combining bitwise and set results
    result = (rotated * 3) + (intersection_size * 7)
    
    # Decoy calculation (irrelevant)
    secondary_score = sum(math.tanh(x) for x in dataset) * intersection_size
    
    return result

# Main execution flow
if __name__ == '__main__':
    # Step 1: Collect raw data
    readings = collect_sensor_readings()
    
    # Step 2: Apply slicing (required feature)
    windowed_data = slice_temporal_window(readings)
    
    # Step 3: Filter anomalies
    filtered_data = filter_anomalies(windowed_data)
    
    # Step 4: Extract peak features (distractor)
    detected_peaks = extract_peaks(filtered_data)
    signature_codes = identify_unique_signatures(detected_peaks)
    
    # Step 5: Generate unused reference structures (red herring)
    template_map = generate_reference_template()
    correlation_grid = build_correlation_matrix(filtered_data)  # Dead assignment
    
    # Step 6: Create key reference series from template
    key_series = [template_map[k] for k in range(5, 12)]
    
    # Step 7: Perform final diagnostic analysis
    final_diagnostic = analyze_pattern(filtered_data, key_series)
    
    # Output target result
    print(f"Result: {final_diagnostic}")