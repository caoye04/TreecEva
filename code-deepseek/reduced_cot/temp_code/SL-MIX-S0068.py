import itertools

def analyze_data(data_points):
    # Initialize tracking variables
    primary_sum = 0
    secondary_buffer = []
    temp_storage = {}
    
    # Process each data point
    for i, point in enumerate(data_points):
        # Main computation path
        if i % 3 == 0:
            primary_sum += point * 2
        elif i % 3 == 1:
            primary_sum -= point
        else:
            # This path is misleading - not used in final result
            secondary_buffer.append(point * 3)
        
        # Store intermediate (mostly irrelevant) values
        temp_storage[f"key_{i}"] = primary_sum + len(secondary_buffer)
    
    # Compute checksum (distractor)
    checksum = sum(secondary_buffer) * 2
    
    # Actual relevant processing
    processed_data = []
    for pair in itertools.combinations(data_points, 2):
        if abs(pair[0] - pair[1]) <= 5:
            processed_data.append(sum(pair))
    
    # Final computation - this is what matters
    if len(processed_data) > 0:
        final_value = sum(processed_data) // len(processed_data)
    else:
        final_value = primary_sum
    
    return final_value

# Sample data processing
sample_data = [12, 8, 15, 7, 20, 3, 18, 11, 25]

# Misleading intermediate computations
backup_calc = sum(sample_data) * 2 - 50
validation_flag = backup_calc > 100
auxiliary_sum = 0

for num in sample_data:
    if num % 2 == 0:
        auxiliary_sum += num
    else:
        auxiliary_sum -= num // 2

# This is the key execution
result = analyze_data(sample_data)

# Final variable assignment
final_analysis = result + (auxiliary_sum % 10)

# Dead code path (never executed)
if validation_flag and backup_calc < 200:
    final_analysis += 5
elif not validation_flag:
    final_analysis -= 3

print(f"Result: {final_analysis}")