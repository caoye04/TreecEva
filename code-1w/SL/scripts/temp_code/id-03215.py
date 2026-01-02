def calculate_final_score(results, weights):
    weighted_scores = {}
    normalized = [score / 100 for score in results]  # Normalize scores to 0-1
    adjusted = [round(n * w, 2) for n, w in zip(normalized, weights)]
    
    for i, val in enumerate(adjusted):
        if val > 0.7:
            weighted_scores[f'bonus_{i}'] = val * 1.2
        else:
            weighted_scores[f'standard_{i}'] = val
    
    # Extract only numeric values and sum those above threshold
    all_vals = list(weighted_scores.values())
    filtered = [v for v in all_vals if v > 0.5]
    base_total = sum(filtered)
    
    # Apply experience multiplier (irrelevant for now but part of domain logic)
    years_experience = 5
    exp_multiplier = 1 + (years_experience * 0.02)  # Up to 1.1 for 5 years
    
    final_bonus = 0.0
    if len(filtered) >= 3:
        final_bonus = 0.8
    
    return int((base_total * exp_multiplier) + final_bonus)

# Main execution
exam_results = [88, 92, 76, 81]
bonus_weights = [1.1, 0.9, 1.2, 1.0]

# Preprocessing step (slicing for recent exams)
recent_exams = exam_results[-3:]  # Ignore oldest exam

# Recompute weights accordingly
adjusted_weights = bonus_weights[:len(recent_exams)]

# Core computation
normalized_recent = [r / 100 for r in recent_exams]
dynamic_adjustment = [round(nr * aw, 2) for nr, aw in zip(normalized_recent, adjusted_weights)]

# Decision logic based on performance streak
streak_count = 0
for s in dynamic_adjustment:
    if s >= 0.85:
        streak_count += 1
    else:
        break

extra_credit = 1.5 if streak_count == 3 else 0

# Final score calculation
total_score = calculate_final_score(exam_results, bonus_weights)

# Add extra credit only if condition met (not applied in function to avoid interference)
if extra_credit > 0:
    total_score += int(extra_credit)

print(f"Result: {total_score}")