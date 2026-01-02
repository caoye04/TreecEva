def calculate_final_score(results, weights):
    base_score = 0
    bonus = 10
    for key in results:
        if key in weights:
            base_score += results[key] * weights[key]
    adjustment = 5 if base_score > 70 else -2
    final_score = base_score + adjustment + bonus
    return final_score

# Simulation data
test_results = {'math': 8, 'physics': 9, 'chemistry': 7}
subject_weights = {'math': 5, 'physics': 6, 'chemistry': 4}

# Irrelevant distractor variables
dummy_value = 999
placeholder_list = [1, 2, 3]

final_score = calculate_final_score(test_results, subject_weights)
print(f'Result: {final_score}')