def evaluate_performance(scores):
    max_score = max(scores)
    min_score = min(scores)
    adjusted_scores = [score - min_score for score in scores if score > min_score]
    normalization_factor = max_score - min_score if max_score != min_score else 1
    normalized_ratings = [round((score / normalization_factor) * 10, 2) for score in adjusted_scores]
    
    # Irrelevant tracking variables (low interference)
    entry_count = len(scores)
    valid_entries = len(adjusted_scores)
    
    total_score = sum(normalized_ratings)
    return total_score

# Main execution
data = [85, 90, 78, 92, 85, 76]
total_score = evaluate_performance(data)
print(f"Result: {total_score}")