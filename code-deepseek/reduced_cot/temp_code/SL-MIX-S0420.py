def calculate_quality_scores(samples):
    base_scores = {}
    for i, sample in enumerate(samples):
        base_scores[f'sample_{i}'] = (sample * 2 + 5) % 15
    
    # Calculate adjustments (distractor operations)
    adjustment_factor = len(base_scores) * 0.75
    temp_sum = sum(base_scores.values()) * 1.2
    
    adjusted_scores = {}
    for key, value in base_scores.items():
        adjusted_value = value + (len(key) // 2)
        if adjusted_value > 10:
            adjusted_scores[key] = adjusted_value - 3
        else:
            adjusted_scores[key] = adjusted_value + 2
    
    # Find maximum scoring sample
    max_key = max(adjusted_scores, key=adjusted_scores.get)
    
    # Calculate bonus points (relevant but computed separately)
    bonus_calc = sum([v for v in base_scores.values() if v < 8])
    bonus_points = bonus_calc // 2
    
    # Final rating calculation
    final_rating = adjusted_scores.get(max_key, 0) + bonus_points
    
    # Distractor print statements
    print(f"Base scores: {base_scores}")
    print(f"Adjusted scores: {adjusted_scores}")
    print(f"Target result: {final_rating}")

# Sample data
quality_samples = [4, 7, 12, 3, 9, 6]
calculate_quality_scores(quality_samples)