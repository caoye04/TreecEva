def calculate_final_score(results, weights):
    base_total = 0
    bonus_points = 0
    adjustment_factor = 1.0

    for subject, score in results.items():
        if len(subject) > 6:
            base_total += score * 0.8
        else:
            base_total += score * 0.9

        if 'math' in subject or 'sci' in subject:
            bonus_points += weights.get(subject, 0)

    if base_total > 200:
        adjustment_factor = 0.95

    temp_result = (base_total + bonus_points) * adjustment_factor
    final_score = int(temp_result)

    return final_score

# Irrelevant utility function (mild distraction)
def format_report(data):
    return '; '.join([f'{k}: {v}' for k, v in data.items()])

# Main data
class_data = {
    'math_core': 85,
    'science_exp': 90,
    'english': 78,
    'history': 82,
    'cs_honors': 88
}

bonus_distribution = {
    'math_core': 7,
    'science_exp': 10,
    'cs_honors': 5
}

# Execution
final_score = calculate_final_score(class_data, bonus_distribution)
print(f"Result: {final_score}")