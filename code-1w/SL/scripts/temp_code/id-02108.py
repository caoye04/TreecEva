def evaluate_performance(raw_points, threshold=50):
    bonus = 0
    adjustment = 1.0
    
    # Irrelevant computation - distractor
    temp_data = [x ** 0.5 for x in range(1, 6)]
    avg_temp = sum(temp_data) / len(temp_data)
    
    if raw_points > threshold:
        status = "high"
        multiplier = 1.2
        # Nested logic with red herring
        corrections = list(map(lambda x: x * 0.9 + 2, temp_data))
        derived_offset = int(sum(corrections[:3])) % 4
        bonus = derived_offset if derived_offset > 2 else 0
    else:
        status = "low"
        multiplier = 0.8
        fallback_check = (raw_points + 5) // 3
        adjustment = 0.95

    base_score = int(raw_points * multiplier + bonus)
    
    # Dead code path - misleading control flow
    if status == "medium":
        base_score += 10

    def adjust_score(score, factor):
        # Conditional expression and modular arithmetic
        reduced = score % 97
        penalty = factor * 10 if factor > 0.5 else 5
        intermediate = reduced - int(penalty)
        
        # More irrelevant processing
        history = ['A', 'B', 'C']
        history.append('X')  # Unused mutation
        label = history[0].lower() if history else 'z'
        
        return intermediate * (1.1 if label == 'a' else 1.0)

    # Semi-relevant precomputation
    outlier_flag = False
    samples = [base_score - 5, base_score, base_score + 3]
    for s in samples:
        if s < 0 or s > 1000:
            outlier_flag = True
            break

    # Key statement
    penalty_factor = 0.75
    final_score = adjust_score(base_score, penalty_factor)

    # Extra output for distraction
    debug_info = f"Status: {status}, Adjustment: {adjustment}"
    metadata_log = {"version": "1.2", "score_origin": "adjusted"}

    print(f"Result: {final_score}")

# Execute scenario
evaluate_performance(68)