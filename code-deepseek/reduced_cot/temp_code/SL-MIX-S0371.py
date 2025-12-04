def calculate_final_score(data_records, cutoff_point):
    # Initialize tracking variables with misleading names
    temp_buffer = [x * 2 for x in range(5, 12)]  # [10, 12, 14, 16, 18, 20, 22]
    accumulator_total = sum(temp_buffer)  # 112 (distractor)
    
    # Actual data processing with enumerate and zip
    participants_data = [(15, 8), (22, 12), (18, 9), (25, 15), (30, 18)]
    performance_scores = []
    
    for idx, (score_a, score_b) in enumerate(participants_data):
        # Red herring calculation that looks important
        weighted_adjustment = score_a * 0.3 + score_b * 0.7  # Never used
        
        # Actual relevant calculation with lambda
        score_calculator = lambda x, y: (x // 2) + (y * 3) - (idx * 2)
        current_score = score_calculator(score_a, score_b)
        performance_scores.append(current_score)
    
    # Distractor set operations that don't affect result
    processed_set = set([x % 7 for x in temp_buffer])  # {3, 5, 0, 2, 4}
    filtered_scores = {x for x in performance_scores if x > 15}  # {19, 22, 28}
    
    # Main logic with linear search and accumulation
    threshold_value = 20
    qualified_scores = []
    
    for score in performance_scores:
        # Misleading condition check (dead code path)
        if score > accumulator_total:  # Never true
            print("Score exceeds maximum")
        
        # Actual filtering condition
        if score >= threshold_value:
            qualified_scores.append(score)
    
    # Multiple irrelevant calculations
    running_total = sum(temp_buffer) + len(processed_set)  # 117
    adjustment_factor = running_total // 10  # 11
    
    # Final result calculation
    if qualified_scores:
        final_output = sum(qualified_scores) - adjustment_factor
    else:
        final_output = 0
    
    # Dead code block that never executes
    if accumulator_total > 200:
        final_output += 50
    
    print(f"Result: {final_output}")
    return final_output

# Main execution
participants_data = [(15, 8), (22, 12), (18, 9), (25, 15), (30, 18)]
threshold_value = 20
result = calculate_final_score(participants_data, threshold_value)