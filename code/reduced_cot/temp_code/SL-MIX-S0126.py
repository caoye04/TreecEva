def analyze_dataset_quality(dataset):
    total_samples = len(dataset)
    valid_entries = []
    invalid_entries = []
    
    # Process each data point
    for data_point in dataset:
        if isinstance(data_point, str) and data_point.strip():
            clean_point = data_point.strip().lower()
            if clean_point.isalpha():
                valid_entries.append(clean_point)
            else:
                invalid_entries.append(data_point)
        else:
            invalid_entries.append(data_point)
    
    # Calculate statistics
    validation_count = len(valid_entries)
    rejection_count = len(invalid_entries)
    
    # Intermediate calculations (some are distractors)
    processing_efficiency = (validation_count / total_samples) * 85
    data_integrity_ratio = validation_count / (total_samples + 0.1)
    quality_threshold = 80.0
    
    # Final quality score calculation
    data_quality_score = (len(valid_entries) / total_samples) * 100
    
    # Additional operations that don't affect the result
    temp_metrics = [processing_efficiency, data_integrity_ratio]
    summary_stats = tuple(temp_metrics)
    
    print(f"Result: {data_quality_score}")
    return data_quality_score

# Test dataset
test_data = ["apple", "banana123", "cherry", "date", "", "elderberry", "FIG", "grape ", None, "kiwi"]
result = analyze_dataset_quality(test_data)