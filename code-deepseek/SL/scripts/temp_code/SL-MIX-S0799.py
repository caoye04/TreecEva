from collections import defaultdict

def process_data_stream(data_points):
    # Distractor: initialize tracking variables that won't affect final count
    temp_buffer = []
    validation_flag = True
    
    # Core processing logic
    count_dict = defaultdict(int)
    processed_count = 0
    
    for point in data_points:
        # Distractor: validation check that always passes
        if validation_flag:
            # Distractor: intermediate calculation that's not used
            buffer_size = len(temp_buffer)
            temp_buffer.append(point)
            
            # Core counting logic
            if point % 2 == 0:
                count_dict['even'] += 1
                processed_count += 1
            else:
                count_dict['odd'] += 1
                processed_count += 1
                
    # Distractor: final validation that doesn't affect result
    final_validation = len(temp_buffer) == len(data_points)
    
    return processed_count

# Main execution
sample_data = [15, 8, 23, 42, 7, 56, 31, 64]
data_batch = sample_data[:]

# Distractor: additional processing that gets discarded
preliminary_scan = lambda x: [i for i in x if i > 20]
filtered_data = preliminary_scan(data_batch)

result = process_data_stream(data_batch)
print(f"Result: {result}")