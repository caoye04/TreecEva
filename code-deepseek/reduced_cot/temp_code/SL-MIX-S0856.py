def compute_avg_speed(readings):
    # Calculate average of valid readings (ignore negative values)
    valid_readings = [r for r in readings if r > 0]
    total = sum(valid_readings)
    count = len(valid_readings)
    
    # Distractor: calculate but don't use this value
    max_speed = max(readings) if readings else 0
    
    # Conditional expression to handle empty list
    avg_speed = total / count if count > 0 else 0
    
    # Apply speed adjustment based on conditions
    if avg_speed > 50:
        adjusted = avg_speed * 0.9  # Reduce by 10%
    else:
        adjusted = avg_speed * 1.1  # Increase by 10%
    
    # Final calculation with lambda function
    final_adjustment = (lambda x: round(x, 2))(adjusted)
    return final_adjustment

# Test data with mixed positive and negative values
data_points = [45.3, -12.8, 67.2, 0, 38.9, -5.6, 52.1]

# Distractor variables that don't affect final result
temp_sum = sum(data_points)
range_data = max(data_points) - min(data_points)

# Main calculation
final_speed = compute_avg_speed(data_points)

print(f"Target result: {final_speed}")