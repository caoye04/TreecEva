def calculate_final_score(results, weights):
    weighted_values = [results[key] * weights[key] for key in results if key in weights]
    adjusted_values = [val + 0.5 if val < 3 else val for val in weighted_values]
    raw_score = sum(adjusted_values)
    bonus = 2 if len(weighted_values) >= 3 else 0
    final_score = raw_score + bonus
    return final_score

# Evaluation results for student project components
evaluation_components = {'design': 4, 'implementation': 5, 'testing': 2, 'documentation': 3}
weights = {'design': 0.3, 'implementation': 0.4, 'testing': 0.2, 'documentation': 0.1}

# Irrelevant distraction variable (minimal interference)
temp_data = {'temp_key': 'temp_value'}

results = evaluation_components
final_score = calculate_final_score(results, weights)
print(f"Result: {final_score}")