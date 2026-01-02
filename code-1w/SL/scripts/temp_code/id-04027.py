def calculate_final_score(raw_data, limits):
    warnings = []
    adjustments = []
    total_penalty = 0
    base_score = 0
    
    # Process each entry with index tracking
    for idx, (value, flag) in enumerate(zip(raw_data, [x > limits[0] for x in raw_data])):
        if flag:
            warnings.append(f'High at {idx}')
            total_penalty += 1
        
        temp_adjust = abs(value - limits[1])
        adjustments.append(temp_adjust)
        
        # Irrelevant intermediate calculation (distractor)
        dummy_calc = (idx + 1) * value % 7
        
        if dummy_calc > 5:
            base_score += 2
        else:
            base_score += 3

    # Reset base score — this negates prior logic (misleading path)
    base_score = sum([x for x in raw_data if x < limits[2]])

    # Real scoring starts here: count how many adjusted values are above threshold
    valid_corrections = 0
    for adj in adjustments:
        if adj > limits[3]:
            valid_corrections += 1
        else:
            break  # Early termination on first invalid

    # Final logic: combine base and correction, penalize for warnings
    final_score = base_score + valid_corrections - total_penalty
    
    # Extra unused variables to increase cognitive load
    summary_stats = {'count': len(raw_data), 'warnings': len(warnings)}
    debug_trace = [f'Step {i}' for i in range(len(raw_data))]
    
    return final_score

# Input data
data = [12, 15, 8, 20, 7, 9]
thresholds = [10, 14, 18, 6]

# Execute
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")