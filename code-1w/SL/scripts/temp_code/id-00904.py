def calculate_final_score(ranks, importance):
    sorted_items = sorted(ranks.items(), key=lambda x: x[1])
    adjusted_values = {}
    for idx, (key, rank) in enumerate(sorted_items):
        adjusted_values[key] = (idx + 1) * importance.get(key, 1.0)
    
    total = 0
    for val in adjusted_values.values():
        total += val
        
    temp_result = total / len(adjusted_values)
    final_score = int(round(temp_result * 2))
    return final_score

# Input data
department_ranks = {
    'marketing': 3,
    'engineering': 1,
    'sales': 4,
    'hr': 2
}

weights = {
    'engineering': 1.5,
    'sales': 1.2,
    'marketing': 1.0,
    'hr': 0.8
}

# Irrelevant variable (minor distraction)
placeholder_value = None

result = calculate_final_score(department_ranks, weights)
final_score = result
print(f"Result: {final_score}")