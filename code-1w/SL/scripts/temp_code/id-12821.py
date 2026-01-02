def calculate_final_score(scores, bonuses):
    base_total = sum(scores)
    bonus_multiplier = 1.5 if len(bonuses) >= 3 else 1.0
    applied_bonuses = [b for b in bonuses if b > 0]
    extra_credit = max(applied_bonuses) if applied_bonuses else 0
    temp_adjustment = {i: val * 0.1 for i, val in enumerate(scores)}
    adjustment_sum = sum(temp_adjustment.values())
    final_score = base_total + (sum(applied_bonuses) * bonus_multiplier) + adjustment_sum
    result = int(final_score)
    return result

scores = [85, 90, 78, 92]
bonuses = [5, 10, 0, 8]
result = calculate_final_score(scores, bonuses)
print(f"Result: {result}")