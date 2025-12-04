def calculate_final(data, weight):
    base_score = sum(data) / len(data)
    adjustment = lambda x: x * 0.85 if x > 80 else x * 1.15
    weighted_base = base_score * weight
    final_result = adjustment(weighted_base)
    return round(final_result, 2)

survey_data = [85, 92, 78, 88, 95]
weight_factor = 1.2
result_data = survey_data
final_score = calculate_final(result_data, weight_factor)
print(f"Result: {final_score}")