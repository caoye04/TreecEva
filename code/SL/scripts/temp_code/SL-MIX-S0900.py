def analyze_data_samples():
    sample_data = [15, 7, 22, 15, 8, 22, 30, 7, 15, 45]
    
    # Process data to find unique values within threshold
    threshold = 25
    filtered_samples = [x for x in sample_data if x < threshold]
    
    # Apply lambda transformation
    transformer = lambda x: x * 2 - 5
    transformed = list(map(transformer, filtered_samples))
    
    # Use set to eliminate duplicates
    result_set = set(transformed)
    final_count = len(result_set)
    
    print(f"Target result: {final_count}")

analyze_data_samples()