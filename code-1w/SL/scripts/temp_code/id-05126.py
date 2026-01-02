def compute_filtered_average():
    data_stream = [18, 23, 45, 12, 77, 64, 39, 52, 81, 27, 34]
    threshold = 25
    
    # Extract subset above threshold
    filtered_data = [x for x in data_stream if x > threshold]
    
    # Use slicing to take only middle portion of sorted data
    sorted_filtered = sorted(filtered_data)
    mid_slice = sorted_filtered[1:-1]  # Exclude min and max from analysis
    
    # Calculate average using integer division
    total = sum(mid_slice)
    count = len(mid_slice)
    avg_slice = total // count if count > 0 else 0
    
    # Irrelevant tracking variable (minor distraction)
    sample_size_log = len(data_stream)
    
    return avg_slice

result = compute_filtered_average()
print(f"Target result: {result}")