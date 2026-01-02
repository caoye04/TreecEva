def evaluate_performance(metrics):
    base_score = metrics['accuracy'] * 100 + metrics['speed']
    adjustment = lambda x: x * 1.1 if x < 5 else x * 0.95
    
    adjusted_score = adjustment(base_score)
    
    # Irrelevant metric (minimal distraction)
    theoretical_max = 100 * 100 + 10
    
    performance_rating = adjusted_score / 100
    apply_bonus = True if performance_rating > 8 else False
    
    bonus = 15 if apply_bonus else 0
    final_score = adjusted_score + bonus
    
    return final_score

# Input data
evaluation_data = {
    'accuracy': 0.85,
    'speed': 7.2
}

result = evaluate_performance(evaluation_data)
print(f"Result: {result}")