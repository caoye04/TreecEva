def analyze_sensor_data(values, min_val):
    # This function is a distractor - it processes but doesn't affect final result
    temp_sum = sum(values)
    filtered = [v for v in values if v > min_val]
    return len(filtered) * 2.5

def calculate_offset(base, modifier):
    # Another distractor function with misleading operations
    bit_shift = base << 2
    xor_result = bit_shift ^ modifier
    return xor_result // 4

def process_data(readings, limit):
    # Main processing function with complex logic chain
    from collections import Counter
    
    # Distractor calculations that don't affect the final result
    temp_counter = Counter(readings)
    most_common_val = temp_counter.most_common(1)[0][0]
    offset_distraction = calculate_offset(most_common_val, 15)
    
    # Core logic with multiple steps
    valid_readings = [r for r in readings if r >= limit]
    if not valid_readings:
        # Dead code path - never executed with given inputs
        return -999
    
    # Complex conditional chain
    first_valid = valid_readings[0]
    last_valid = valid_readings[-1]
    
    # Main computation with bitwise and arithmetic operations
    base_calc = (first_valid & 0x0F) | (last_valid & 0xF0)
    
    # Conditional expression with multiple checks
    adjustment = 25 if len(valid_readings) > 3 else 10
    
    # Final computation with misleading intermediate variable
    intermediate = base_calc * adjustment
    
    # Additional distractor that looks important but isn't
    sensor_analysis = analyze_sensor_data(readings, limit)
    
    # Actual result computation
    result = intermediate - (len(valid_readings) * 5)
    
    return result

# Main execution with realistic data
sensor_readings = [12, 8, 15, 6, 20, 9, 18, 5, 22, 7]
threshold = 10

# Execute the key statement
final_output = process_data(sensor_readings, threshold)

# Additional distractor operations that don't affect output
backup_calc = sum(sensor_readings) // len(sensor_readings)
validation_check = backup_calc & 0xFF

print(f"Result: {final_output}")