import itertools

def calculate_data_quality(data_points, threshold=75):
    # Irrelevant function - dead code path
    valid_count = sum(1 for x in data_points if x > threshold)
    return valid_count * 2.5  # Misleading calculation

def process_sensor_readings(readings):
    # Distractor function with misleading operations
    filtered = [r for r in readings if r % 3 == 0]  # Irrelevant filtering
    processed = list(itertools.chain.from_iterable([[x, x*2] for x in filtered]))  # Unused operation
    return sum(filtered) * 1.25  # Misleading intermediate result

def calculate_final_score(data_values, quality_factors):
    # Main logic with complex reasoning chain
    base_score = sum(data_values) // len(data_values)
    
    # Irrelevant bitwise operations
    bit_mask = 0b10101010
    processed_bits = base_score & bit_mask | 0b01010101
    
    # Lambda function for quality adjustment
    adjust_quality = lambda x, y: (x * y) % 100 + min(x, y)
    
    # Complex mixed operations
    quality_adjustment = adjust_quality(quality_factors['precision'], quality_factors['accuracy'])
    
    # Slicing operations with accumulation
    data_slice = data_values[2:7]  # Fixed slice
    slice_sum = sum(data_slice) * quality_adjustment // 10
    
    # Final calculation with bitwise XOR
    final_result = (base_score ^ processed_bits) + slice_sum - quality_adjustment
    
    # Unused variable (distraction)
    unused_calc = final_result * 3.14159  # Dead code path
    
    return final_result

# Main execution
sensor_data = [45, 78, 92, 33, 67, 84, 29, 51, 76, 88]
quality_metrics = {'precision': 85, 'accuracy': 92, 'reliability': 78}  # reliability unused

# Irrelevant calculations
processed_data = process_sensor_readings(sensor_data)  # Result unused
quality_check = calculate_data_quality(sensor_data)  # Result unused

# Critical execution point
final_score = calculate_final_score(sensor_data, quality_metrics)

print(f"Result: {final_score}")