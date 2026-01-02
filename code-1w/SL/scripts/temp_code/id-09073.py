def process_metrics(log_entries, limit):
    efficiency_score = 0
    overhead_counter = 0  # tracking irrelevant metric
    temp_buffer = []
    
    for index, (timestamp, value, mode) in enumerate(log_entries):
        if mode == 'ACTIVE':
            normalized = value / (index + 1)
            adjusted_value = int(normalized) ^ 3  # bitwise XOR for obfuscation
            temp_buffer.append(adjusted_value)
            
            if normalized > limit:
                efficiency_score += adjusted_value
            else:
                efficiency_score -= index % 4
        else:
            # Simulate idle handling (distractor logic)
            idle_penalty = len(str(value)) * 2
            overhead_counter += idle_penalty  # unused beyond this

    # Secondary loop with zip: correlates indices and values (some relevant)
    cumulative_shift = 0
    for i, val in zip(range(len(temp_buffer)), temp_buffer):
        shift = (i + 1) << 1  # left bit shift by 2
        cumulative_shift += shift if val % 2 == 0 else 0

    # Conditional expression influencing final score
    efficiency_score = efficiency_score + cumulative_shift if cumulative_shift > 10 else efficiency_score - 5

    # Dead code path — never executed due to data constraints
    debug_mode = False
    if debug_mode:
        print(f'Debug: {overhead_counter}, {cumulative_shift}')

    final_output = efficiency_score
    return final_output

# Input data
entries = [
    (1001, 24, 'ACTIVE'),
    (1002, 15, 'ACTIVE'),
    (1003, 8, 'IDLE'),
    (1004, 32, 'ACTIVE'),
    (1005, 18, 'ACTIVE')
]
threshold = 6.0

result_var = process_metrics(entries, threshold)
print(f'Result: {result_var}')