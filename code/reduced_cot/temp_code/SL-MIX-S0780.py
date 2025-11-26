def process_data_samples(samples):
    # Initial processing
    total_samples = len(samples)
    valid_samples = sum(1 for sample in samples if sample > 50)
    invalid_samples = total_samples - valid_samples
    
    # Distractor calculations (not used in final result)
    sample_variance = sum((s - 75) ** 2 for s in samples) / len(samples)
    average_sample = sum(samples) / len(samples)
    
    # Core processing
    processed_samples = [s * 2 if s > 50 else s + 10 for s in samples]
    processed_total = sum(processed_samples)
    
    # Error correction chain
    error_count = sum(1 for s in samples if s < 30)
    correction_factor = error_count * 15
    error_correction = correction_factor if error_count > 0 else 25
    
    # Final calculation
    data_quality_score = processed_total - error_correction
    
    # Additional unused metrics
    quality_ratio = valid_samples / total_samples
    efficiency_metric = processed_total / total_samples
    
    print(f"Target result: {data_quality_score}")
    return data_quality_score

# Test data
sample_data = [45, 67, 89, 23, 78, 92, 34, 56, 81, 29]
result = process_data_samples(sample_data)