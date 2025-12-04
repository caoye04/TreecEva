def analyze_data_stream(data_chunks):
    # Initialize tracking variables
    raw_count = len(data_chunks)
    processed_count = 0
    discarded_count = 0
    quality_modifier = 17
    
    # Distractor: irrelevant buffer operations
    buffer_size = 1024
    buffer_utilization = buffer_size // 8
    compression_ratio = 3.2
    
    # Process data chunks with filtering
    valid_chunks = [chunk for chunk in data_chunks if len(chunk) > 5]
    processed_count = len(valid_chunks)
    
    # Misleading intermediate calculation
    temp_efficiency = (raw_count * buffer_utilization) // compression_ratio
    
    # Quality assessment with conditional expressions
    quality_scores = [8 if 'error' not in chunk else 2 for chunk in valid_chunks]
    high_quality_count = sum(1 for score in quality_scores if score > 5)
    discarded_count = processed_count - high_quality_count
    
    # Dead code path - never executed
    if compression_ratio > 10:
        optimization_factor = 2
        # This branch is never taken
        processed_count *= optimization_factor
    
    # Final throughput calculation (target statement)
    final_throughput = (processed_count * 2 - discarded_count) % quality_modifier
    
    # Print result
    print(f"Result: {final_throughput}")
    return final_throughput

# Test data
test_chunks = ['data_packet_1', 'error_data', 'valid_stream_3', 'corrupt_4', 'good_packet_5', 'data_6']
result = analyze_data_stream(test_chunks)