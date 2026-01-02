import math

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_array(raw_stream, calibration_factor=1.05):
    calibrated = [x * calibration_factor for x in raw_stream]
    filtered = [x for x in calibrated if x > 0.1]
    normalized = [x / max(filtered) for x in filtered] if filtered else [0]
    return normalized

# Irrelevant transformation chain (dead path)
def spectral_decompose(signal):
    result = []
    for i in range(len(signal)):
        component = sum(signal[j] * math.sin(i * j) for j in range(len(signal)))
        result.append(component)
    return result

# Core feature extraction (partially relevant)
def extract_features(dataset):
    lengths = list(map(len, dataset))
    averages = [sum(d) / len(d) for d in dataset if d]
    variances = []
    for seq in dataset:
        if len(seq) > 1:
            mean_val = sum(seq) / len(seq)
            variance = sum((x - mean_val) ** 2 for x in seq) / len(seq)
            variances.append(variance)
        elif seq:
            variances.append(0.0)
    return lengths, averages, variances

# Decoy function using lambda (misleading usage)
external_weight_fn = lambda w: (w ** 0.5) * 1.85  # Unused in actual logic

# Real transformation pipeline
def transform_sequence(seq, op=lambda x: x ** 2 + 0.1):
    processed = []
    for item in seq:
        if item < 0.3:
            processed.append(op(item))
        elif item < 0.6:
            processed.append(math.log(item + 0.1))
        else:
            processed.append(item * 0.8)
    return [p for p in processed if p > 0]

# Aggregation logic with conditional weighting
def aggregate_metrics(data_batches, weight_vector):
    totals = []n    for idx, batch in enumerate(data_batches):
        weighted_sum = 0
        for i, val in enumerate(batch):
            if i % 2 == 0:
                weighted_sum += val * weight_vector[0]
            else:
                weighted_sum += val * weight_vector[1]
        totals.append(weighted_sum)
    return int(sum(totals) * 1000)  # Final conversion to integer diagnostic code

# Auxiliary checksum (irrelevant)
def compute_legacy_checksum(arrays):
    total_chars = 0
    for a in arrays:
        total_chars += len(''.join(f'{x:.2f}' for x in a))
    return total_chars % 17

# Main execution flow with distractions
if __name__ == '__main__':
    # Simulated multi-channel input (real data source)
    primary_stream = [0.12, 0.34, 0.56, 0.78, 0.23, 0.45, 0.67]
    secondary_stream = [0.21, 0.43, 0.65, 0.87, 0.19, 0.38]
    
    # Process streams through valid and invalid paths
    processed_primary = preprocess_sensor_array(primary_stream)
    processed_secondary = preprocess_sensor_array(secondary_stream)
    
    # Apply correct transformation
    transformed_primary = transform_sequence(processed_primary)
    transformed_secondary = transform_sequence(processed_secondary)
    transformed_tertiary = transform_sequence([0.15, 0.25, 0.55])  # Hidden third component
    
    # Extract features (partially dead call)
    all_data = [transformed_primary, transformed_secondary, transformed_tertiary]
    lengths, means, _ = extract_features(all_data)
    
    # Dead code: spectral analysis not used
    frequency_components = spectral_decompose(means)
    legacy_hash = compute_legacy_checksum(all_data)
    
    # Weight vector appears arbitrary but is fixed
    weights = [1.7, 0.9]  # Critical for final calculation
    
    # Key statement
    final_diagnostic = aggregate_metrics(all_data, weights)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")