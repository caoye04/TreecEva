def calculate_performance(entries, limit):
    total_chars = 0
    valid_count = 0
    temp_buffer = []
    cumulative_score = 0
    efficiency_ratio = 0.0

    for entry in entries:
        stripped = entry.strip()
        length = len(stripped)
        total_chars += length

        if length == 0:
            continue

        is_valid = length >= limit
        status_flag = 1 if is_valid else 0

        if is_valid:
            valid_count += 1
            cumulative_score += length ** 0.5

        temp_buffer.append(f'{stripped}:{length}')

    # Irrelevant transformation
    reversed_buffer = [s[::-1] for s in temp_buffer]
    discarded_sum = sum(len(item) for item in reversed_buffer if 'a' in item)

    # Distractor variable - not used in final result
    average_length = total_chars / len(entries) if entries else 0

    scaling_factor = 2.5 if valid_count > 3 else 1.8

    # Key computation
    if valid_count > 0 and cumulative_score > 0:
        efficiency_ratio = (cumulative_score * scaling_factor) / valid_count
    else:
        efficiency_ratio = 0.0

    final_output = efficiency_ratio

    # Print required at the end
    print(f'Result: {final_output}')
    
    return final_output

# Input data
log_data = [
    'system: INIT',
    'proc_1: OK',
    '',
    'error: null_ref',
    'data_load: SUCCESS',
    'retry: none',
    'status: READY'
]
threshold = 7

# Execute
result_var = calculate_performance(log_data, threshold)