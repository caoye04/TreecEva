def calculate_final_score(scores, weight_map):
    normalized = [score / 100.0 for score in scores]
    weighted = [n * weight_map[i] for i, n in enumerate(normalized)]
    adjusted = sum(weighted) * 100
    
    # Irrelevant distraction: string processing for logging (minimal interference)
    log_tag = "Processing".lower()
    status = f"{log_tag}_complete".replace('_', ' ')
    status_words = status.split(' ')
    
    # Key computation
    bonus = 5 if adjusted >= 85 else 2
    return int(adjusted + bonus)

# Main execution
course_names = ['Math', 'Physics', 'Chemistry', 'Biology']
raw_scores = [92, 87, 90, 85]
weights = {0: 0.3, 1: 0.25, 2: 0.25, 3: 0.2}

final_score = calculate_final_score(raw_scores, weights)
print(f"Result: {final_score}")