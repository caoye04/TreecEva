from itertools import compress

def calculate_final_score(scores, penalties):
    # Apply modular arithmetic to normalize scores
    normalized = [score % 100 for score in scores]
    
    # Use boolean logic to filter out penalized entries
    valid_entries = [p == 0 for p in penalties]
    filtered_scores = list(compress(normalized, valid_entries))
    
    # Compute mean and apply final adjustment
    if filtered_scores:
        mean_score = sum(filtered_scores) / len(filtered_scores)
        adjustment = len(filtered_scores) * 0.5
        result = mean_score + adjustment
    else:
        result = 0
    
    return result

# Input data
scores = [85, 92, 78, 103, 96]
penalties = [0, 1, 0, 0, 1]  # 1 indicates penalty applied

result = calculate_final_score(scores, penalties)
print(f'Result: {result}')