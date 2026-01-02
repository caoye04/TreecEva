import itertools

# Simulated sensor array data processing with diagnostic evaluation
def preprocess_readings(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 6) for x in filtered]
    return normalized

# Irrelevant helper - distractor function (dead path)
def legacy_compatibility_mode(data):
    temp_buffer = []
    for i in range(len(data)):
        temp_buffer.append(data[i] * 0.95)  # outdated scaling
    return temp_buffer

# Signal compression using run-length encoding (relevant)
def compress_signal(sequence):
    compressed = []
    for key, group in itertools.groupby(sequence):
        count = len(list(group))
        compressed.append((key, count))
    return compressed

# Threshold-based anomaly detection map (relevant)
def generate_threshold_map(values):
    avg = sum(values) / len(values)
    std_dev = (sum((x - avg) ** 2 for x in values) / len(values)) ** 0.5
    return {
        'low': avg - 1.5 * std_dev,
        'normal': avg,
        'high': avg + 2.0 * std_dev
    }

# Diagnostic analyzer with complex logic chain (core function)
def analyze_signal(packed_data, limits):
    diagnostics = []
    cumulative_score = 0
    
    for val, count in packed_data:
        # Misleading intermediate calculation (distractor)
        buffer_check = (val * count) % 7
        if buffer_check > 5:
            cumulative_score -= 1  # red herring adjustment
        
        # Actual logic: classify based on thresholds
        if val < limits['low']:
            severity = 3
        elif val > limits['high']:
            severity = 2
        elif val > limits['normal']:
            severity = 1
        else:
            severity = 0
        
        impact = severity * count
        diagnostics.append(impact)
        
        # Nested conditional with bitwise decoy
        flag = (impact & 3) == 0
        if flag and count > 1:
            cumulative_score += impact | 4  # irrelevant bit op
        else:
            cumulative_score += impact
    
    # Final aggregation with tuple unpacking distraction
    temp_results = [(i, v) for i, v in enumerate(diagnostics)]
    index_sum, total_impact = zip(*temp_results) if temp_results else ((0,), (0,))
    final_impact = sum(total_impact)
    
    # Decoy transformation (never used)
    transformed = [x * 1.05 for x in total_impact if x > 2]
    
    # Key computation: weighted diagnostic score
    adjustment_factor = len(packed_data) / (final_impact + 1)
    base_score = final_impact * 10
    final_diagnostic = int(base_score - adjustment_factor * 17)
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Simulated input data
    sensor_readings = [0.0, 0.15, 0.15, -0.3, -0.3, -0.3, 0.8, 0.8, 0.8, 0.8, 0.2, -1.2, -1.2]
    
    # Step 1: Preprocess (filter and normalize)
    clean_data = preprocess_readings(sensor_readings)
    
    # Distractor: legacy mode call (unused result)
    obsolete_output = legacy_compatibility_mode(clean_data)
    
    # Step 2: Compress the signal
    compressed_data = compress_signal(clean_data)
    
    # Step 3: Generate dynamic thresholds
    threshold_map = generate_threshold_map(clean_data)
    
    # Step 4: Core analysis (contains key statement)
    final_diagnostic = analyze_signal(compressed_data, threshold_map)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")