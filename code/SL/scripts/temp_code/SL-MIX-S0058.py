def validate_data_points(data_points):
    valid_count = 0
    invalid_count = 0
    temp_sum = 0
    adjustment_factor = 0
    
    for point in data_points:
        if point % 3 == 0 and point > 15:
            valid_count += 1
            temp_sum += point
        elif point % 5 == 0:
            invalid_count += 1
            temp_sum -= point * 2
        else:
            temp_sum += point // 2
    
    # Distractor calculations
    average_temp = temp_sum // len(data_points) if data_points else 0
    quality_ratio = valid_count / (invalid_count + 1) if invalid_count > 0 else valid_count
    
    # Misleading intermediate results
    preliminary_score = (valid_count * 3) + (invalid_count // 2)
    offset_value = preliminary_score % 7
    
    # Irrelevant bit operations (dead code path)
    if offset_value > 10:
        bit_shift_result = offset_value << 3
        adjustment_factor = bit_shift_result - 5
    else:
        adjustment_factor = offset_value * 2 + 1
    
    # Main calculation
    composite_score = (valid_count << 2) - (invalid_count >> 1) + adjustment_factor
    
    # Final output
    print(f"Result: {composite_score}")

# Test data
data_points = [18, 25, 21, 30, 12, 20, 24, 35, 15, 28]
validate_data_points(data_points)