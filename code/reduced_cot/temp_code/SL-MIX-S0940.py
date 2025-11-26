def calculate_total(metrics):
    total = 0
    temp_sum = 0
    intermediate = []
    
    # Process each metric point
    for metric in metrics:
        processed = metric * 2  # Double each metric
        intermediate.append(processed)
        temp_sum += processed
    
    # Calculate average (distractor - not used in final result)
    average = temp_sum / len(metrics) if metrics else 0
    
    # Extract relevant portion using slicing
    core_data = intermediate[1:-1]
    
    # Apply string method-like filtering (simulated)
    filtered_data = [x for x in core_data if x > 5]
    
    # Final calculation
    for value in filtered_data:
        total += value
    
    # Additional unused computation
    alternate_total = sum(intermediate) * 0.8
    
    return total

data_points = [3, 7, 2, 9, 4, 6]
final_score = calculate_total(data_points)
print(f"Result: {final_score}")