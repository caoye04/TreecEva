def calculate_performance_score():
    base_scores = [85, 90, 78, 92, 88]
    thresholds = [80, 85, 90]
    bonuses = [1.1, 1.2, 1.5]
    
    # Irrelevant distraction: unused variable
    max_possible = sum([x * 2 for x in base_scores])
    
    total_score = 0
    for i, score in enumerate(base_scores):
        if score >= thresholds[2]:
            multiplier = bonuses[2]
        elif score >= thresholds[1]:
            multiplier = bonuses[1]
        elif score >= thresholds[0]:
            multiplier = bonuses[0]
        else:
            multiplier = 1.0
        
        # Apply multiplier and accumulate
        adjusted = score * multiplier
        total_score += adjusted
    
    # Additional computation: round to nearest integer
    total_score = round(total_score)
    
    return total_score

result = calculate_performance_score()
print(f"Result: {result}")