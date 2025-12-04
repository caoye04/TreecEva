def evaluate_classifier(scores):
    # Calculate base metrics
    total = sum(scores)
    count = len(scores)
    base_accuracy = total / count if count > 0 else 0
    
    # Distractor calculations that don't affect final result
    max_score = max(scores) if scores else 0
    min_score = min(scores) if scores else 0
    score_range = max_score - min_score
    
    # Main processing with list comprehension
    adjusted_scores = [score * 1.05 if score > 80 else score * 0.95 for score in scores]
    
    # More irrelevant intermediate steps
    score_variance = sum((score - base_accuracy) ** 2 for score in scores) / count if count > 0 else 0
    normalized_scores = [score / 100 for score in adjusted_scores]
    
    # Key processing that determines final result
    processed_values = [round(score * 100, 2) for score in normalized_scores]
    
    # Final assignment
    final_accuracy = processed_values[-1]
    
    print(f"Target result: {final_accuracy}")
    return final_accuracy

# Test data
classification_scores = [85, 92, 78, 88, 95, 82, 91]
result = evaluate_classifier(classification_scores)