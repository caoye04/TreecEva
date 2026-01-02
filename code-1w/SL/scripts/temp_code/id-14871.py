def calculate_final_score(scores, penalty):
    normalized = [score / max(scores) for score in scores]
    adjusted = [round(s * (1 - penalty), 4) for s in normalized]
    return sum(adjusted) if sum(adjusted) > 0 else 0

# Simulation of performance metrics
raw_scores = [85, 92, 78, 96, 88]
penalty_factor = 0.1
initial_total = sum(raw_scores)
scaling_ratio = initial_total / 100

# Final computation with conditional expression
evaluation_status = 'valid' if scaling_ratio > 4 else 'invalid'
final_score = calculate_final_score(raw_scores, penalty_factor) if evaluation_status == 'valid' else 0

# Output result
print(f"Result: {final_score}")