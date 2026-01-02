def calculate_network_capacity():
    base_rates = [12, 15, 8, 20, 17, 9, 25]
    peak_multiplier = 1.4
    adjusted_rates = [rate * peak_multiplier for rate in base_rates]
    
    # Simulate segment optimization: take every other segment after threshold
    threshold = 16
    filtered_segments = [value for value in adjusted_rates if value >= threshold]
    optimized_segments = filtered_segments[::2]  # Use slicing to select alternate segments
    
    total_capacity = sum(optimized_segments)
    return int(total_capacity)

result = calculate_network_capacity()
print(f"Result: {result}")