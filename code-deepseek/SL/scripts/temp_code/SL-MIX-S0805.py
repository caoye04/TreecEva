def process_measurements(samples):
    base_value = 42
    measurement_transform = lambda x: (x * 2) - 5
    processed_samples = set()
    
    for sample in samples:
        transformed = measurement_transform(sample)
        processed_samples.add(transformed)
    
    cumulative_sum = sum(processed_samples)
    final_result = cumulative_sum - base_value
    print(f"Target result: {final_result}")
    return final_result

data_samples = [15, 20, 25, 30, 15]
final_result = process_measurements(data_samples)