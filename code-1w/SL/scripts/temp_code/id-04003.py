def calculate_final_score(results, multiplier):
    base_score = sum(results.values())
    adjusted_score = base_score * 0.85
    if base_score >= 250:
        adjusted_score += 15
    rank = 'A' if adjusted_score > 220 else 'B'
    final_score = adjusted_score + (multiplier if rank == 'A' else 0)
    return final_score

exam_results = {
    'math': 92,
    'physics': 87,
    'chemistry': 76,
    'biology': 81,
    'computer_science': 74
}
bonus_multiplier = 12

irrelevant_list = [x**2 for x in range(5)]
temp_value = len(irrelevant_list) * 2

final_score = calculate_final_score(exam_results, bonus_multiplier)
print(f"Result: {final_score}")