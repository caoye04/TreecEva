def process_data(data_list):
    # Distractor: misleading counter that doesn't affect result
    counter = 0
    
    # Distractor: irrelevant transformation
    temp_values = [x * 2 if x % 2 == 0 else x - 1 for x in data_list]
    
    # Relevant processing with enumerate
    processed = []
    for idx, val in enumerate(data_list):
        # Distractor: unused conditional path
        if idx > len(data_list) // 2:
            counter += val  # Dead code path
        
        # Actual processing logic
        if val % 3 == 0:
            processed.append(val * 2)
        elif val % 5 == 0:
            processed.append(val // 2)
        else:
            processed.append(val + 1)
    
    # Distractor: misleading intermediate calculation
    intermediate_sum = sum(temp_values) + counter
    
    # Relevant: zip operation with conditional expressions
    result = 0
    pairs = list(zip(data_list, processed))
    for orig, proc in pairs:
        # Conditional expression for compact logic
        multiplier = 3 if orig > proc else 2
        result += (orig + proc) * multiplier
    
    # Distractor: unused bitwise operation
    bit_check = result & 0xFF
    
    return result

# Main execution
values = [12, 8, 15, 7, 20, 9, 11]

# Distractor: irrelevant variable tracking
phase_tracker = [0] * len(values)

# Distractor: misleading state updates
for i in range(len(values)):
    phase_tracker[i] = values[i] % 4  # Unused

final_output = process_data(values)
print(f"Result: {final_output}")