def calculate_final_score():
    scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    
    # Irrelevant distraction: unused variable
    max_score = max(scores)
    
    weighted_pairs = zip(scores, weights)
    
    # Using lambda to compute weighted contribution
    apply_weight = lambda pair: pair[0] * pair[1]
    
    weighted_scores = [apply_weight(pair) for pair in weighted_pairs]
    
    total = sum(weighted_scores)
    
    # Additional logic step: bonus condition
    if total > 85:
        total += 2.5  # performance bonus
    
    # Another distraction: unused calculation
    count_above_80 = len([s for s in scores if s > 80])
    
    result = round(total, 3)
    return result

# Execute and print result
target_result = calculate_final_score()
print(f"Result: {target_result}")