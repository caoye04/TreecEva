def validate_pattern(sequence):
    return len(sequence) > 3 and sequence[0] == sequence[-1]

def calculate_offset(values):
    temp_sum = sum(values) * 2
    offset_factor = temp_sum // len(values) if values else 0
    unused_var = offset_factor * 3.14
    return offset_factor

def process_sequence(data):
    if not data:
        return -1
    
    filtered_data = [x for x in data if x % 2 == 0]
    misleading_total = sum(filtered_data) * 10
    
    if validate_pattern(filtered_data):
        offset = calculate_offset(filtered_data)
        result = misleading_total - offset
        dead_branch = result * 2
    else:
        sorted_data = sorted(filtered_data)
        midpoint = len(sorted_data) // 2
        relevant_slice = sorted_data[midpoint-1:midpoint+2] if len(sorted_data) >= 3 else sorted_data
        
        offset = calculate_offset(relevant_slice)
        result = sum(relevant_slice) * 3 - offset
        misleading_intermediate = result + 1000
    
    unused_calc = (result * 1.5) // 2
    return result

data_stream = [8, 3, 12, 7, 8, 15, 4, 9, 8]
redundant_check = len(data_stream) * 2
distraction_var = sum(data_stream) // redundant_check

result = process_sequence(data_stream)
final_output = result + 5

print(f"Target result: {final_output}")