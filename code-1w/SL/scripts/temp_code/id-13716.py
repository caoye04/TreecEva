def calculate_final_score(points, penalties):
    base_score = points * 10
    adjustment = len(str(penalties)) if penalties > 0 else 0
    bonus = 25 if 'A' in str(base_score)[0] else 10
    final_score = base_score - (penalties * 5) + bonus - adjustment
    return final_score

raw_points = 87
penalty_count = 3
temp_data = 'intermediate_result_cache'
final_score = calculate_final_score(raw_points, penalty_count)
print(f"Result: {final_score}")