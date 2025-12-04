def validate_data_points(data_stream):
    valid_counts = []
    threshold = 15
    
    # Process data batches
    for batch in data_stream:
        valid_batch = [point for point in batch if point >= threshold]
        valid_counts.append(len(valid_batch))
    
    # Temporary debug variable (distractor)
    debug_total = len(valid_counts)
    
    # Calculate final result
    total_valid = sum(valid_counts)
    
    print(f"Result: {total_valid}")

# Sample data stream
sample_data = [[10, 20, 30], [5, 25, 15], [12, 18, 22]]
validate_data_points(sample_data)