def process_data(entries):
    total = 0
    temp_buffer = []
    outlier_count = 0  # distractor: not used in final logic

    for entry in entries:
        if isinstance(entry, str):
            continue  # skip non-numeric
        
        if entry < 0:
            outlier_count += 1
            continue
            
        adjusted = entry * 0.95
        if adjusted > 50:
            adjusted -= 10
        
        temp_buffer.append(adjusted)

    filtered = [x for x in temp_buffer if x >= 10]  # list comprehension

    base_sum = sum(filtered)
    count = len(filtered)
    
    avg = base_sum / count if count > 0 else 0

    # Secondary processing with lambda
    transform = lambda x: x ** 0.5 * 2
    transformed_vals = [transform(val) for val in filtered]

    temp_result = sum(transformed_vals) + avg

    # Flag system with conditional expressions
    flags = []
    for v in filtered:
        flag = 'A' if v > 40 else 'B' if v > 20 else 'C'
        flags.append(flag)
    
    high_priority = flags.count('A')
    medium_priority = flags.count('B')  # semi-relevant but not critical

    def calculate_final(value, f_list):
        multiplier = 1.5 if 'A' in f_list else 1.0
        penalty = 0.1 * f_list.count('C')
        return int((value * multiplier) - (penalty * 10))

    final_score = calculate_final(temp_result, flags)
    
    # Dead code path (distractor)
    if len(entries) > 1000:
        final_score *= 0.9  # unreachable in this context

    return final_score

# Input data
input_entries = [10, 25, 'skip', 60, 80, -5, 30, 70, 'bad', 45]

result = process_data(input_entries)
print(f"Result: {result}")