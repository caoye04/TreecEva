def calculate_performance(data):
    base_multiplier = 1.5
    adjustment_factor = 0.8
    temp_buffer = []
    cumulative_shift = 0
    
    for i, (name, values) in enumerate(data.items()):        
        if len(name) % 2 == 0:
            scale = base_multiplier
        else:
            scale = 1.2
            
        # Irrelevant string processing (distractor)
        processed_name = ''.join([c.upper() if i % 3 == 0 else c for i, c in enumerate(name)])
        padded_name = processed_name.ljust(10, '*')
        
        local_total = sum(v * scale for v in values)
        
        # Red herring: this is computed but not used
        average_offset = local_total / len(values) if values else 0
        
        if 'x' in padded_name or len(values) > 4:
            local_total *= adjustment_factor

        temp_buffer.append(local_total)
        
        # Extra logic that doesn't contribute to final result
        if i % 2 == 0:
            cumulative_shift += len(values)

    # Real computation path
    raw_sum = sum(temp_buffer)
    length_penalty = len(temp_buffer) * 0.1
    adjusted_sum = raw_sum - length_penalty
    
    # Misleading transformation (not actually impactful due to constants)
    for _ in range(2):
        adjusted_sum = round(adjusted_sum, 2)

    # Final score calculation - only this matters
    final_score = int(adjusted_sum // 1)
    
    return final_score

# Setup data
benchmark_data = {
    'alpha': [4, 7, 2],
    'beta': [5, 9, 1, 8],
    'gamma': [3, 6],
    'delta': [10, 1, 4, 2, 8]
}

# Additional distractor variables
auxiliary_matrix = [[i*j for j in range(3)] for i in range(3)]
dummy_counter = 0
for row in auxiliary_matrix:
    for elem in row:
        dummy_counter += elem ** 0.5

# Key execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")