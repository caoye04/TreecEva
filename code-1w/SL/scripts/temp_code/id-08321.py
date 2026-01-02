def calculate_performance_rating():
    base_scores = [85, 90, 78, 92, 88]
    weightings = [0.2, 0.25, 0.15, 0.3, 0.1]
    
    # Normalize scores to percentage of max
    max_base = max(base_scores)
    normalized = [round(score / max_base * 100) for score in base_scores]
    
    # Apply weighted sum using list comprehension and zip
    weighted_sum = sum([w * s for w, s in zip(weightings, normalized)])
    
    # Bonus logic based on consistency (range between min and max)
    score_range = max(normalized) - min(normalized)
    bonus = 5 if score_range <= 10 else 2
    
    # Final adjustment using string-based condition (simulates config)
    mode = 'standard'
    adjustment = 1.0
    if mode.startswith('premium'):
        adjustment = 1.1
    
    final_score = round(weighted_sum * adjustment + bonus)
    return final_score

# Irrelevant utility variable (minimal distraction)
utility_buffer = "temp_data_placeholder"

result = calculate_performance_rating()
print(f"Result: {result}")