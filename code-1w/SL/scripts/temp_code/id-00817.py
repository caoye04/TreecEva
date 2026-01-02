from collections import Counter

def calculate_final_score(raw_scores, deductions):
    # Normalize scores using mean adjustment
    mean_score = sum(raw_scores) / len(raw_scores)
    adjusted = [score - mean_score for score in raw_scores]
    
    # Apply penalty scaling based on frequency of violation type
    penalty_counter = Counter(deductions)
    total_penalty = 0
    for penalty_type, count in penalty_counter.items():
        if penalty_type == 'minor':
            total_penalty += count * 2
        elif penalty_type == 'major':
            total_penalty += count * 5
    
    # Compute final result using bitwise weighting of top performance
    top_adjusted = max(adjusted)
    weighted_contribution = int(top_adjusted) & 7  # Keep lower 3 bits
    base_result = sum(adjusted) + weighted_contribution
    
    # Final adjustment with penalty
    result = base_result - total_penalty
    
    # Irrelevant distraction: unused calculation (minimal interference)
    avg_penalty = total_penalty / len(deductions) if deductions else 0
    
    return result

# Input data
scores = [85, 90, 78, 92, 88]
penalties = ['minor', 'major', 'minor', 'minor']

result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")