def calculate_mood_score():
    # Simulate daily activity tracking with emotional impact
    activities = ['reading', 'jogging', 'meditation', 'cooking', 'gaming']
    scores = [8, 7, 9, 6, 5]
    weights = [0.3, 0.25, 0.35, 0.1, 0.05]
    
    # Auxiliary data (irrelevant to final result)
    durations = [30, 45, 20, 60, 120]
    calories_burned = [85, 250, 0, 120, 10]
    
    # Core computation
    weighted_impact = []
    for i, (score, weight) in enumerate(zip(scores, weights)):
        weighted_impact.append(score * weight)
    
    total_happiness = sum(map(lambda x: x[0] * x[1], zip(scores, weights)))
    
    # Extra unused variables (minor interference)
    avg_duration = sum(durations) / len(durations)
    max_calories = max(calories_burned)
    
    print(f"Result: {total_happiness}")

calculate_mood_score()