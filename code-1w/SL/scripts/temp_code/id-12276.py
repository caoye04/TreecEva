def calculate_final_score(records, importance_weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result_cache = {}

    for idx, (key, value) in enumerate(records.items()):
        if idx % 2 == 0:
            transformed = (value ** 2) + importance_weights.get(key, 1)
            base_score += transformed * 0.1
        else:
            shifted = value << 1
            if shifted > 10:
                penalty_adjustment -= 1.5
            bonus_tracker.append(shifted % 7)

    # Irrelevant aggregation (distractor)
    for i, b in enumerate(bonus_tracker):
        temp_result_cache[f'bonus_{i}'] = b * 1.5 + 2.5

    # Dummy bitwise manipulation with no impact
    dummy_flag = 0
    for val in records.values():
        dummy_flag ^= (val & 3)

    # Actual score calculation using only base_score and fixed adjustment
    intermediate = base_score + penalty_adjustment
    scaling_factor = len(importance_weights) * 0.5
    final_score = int(intermediate * scaling_factor) + 5

    return final_score

# Input data
data = {'alpha': 3, 'beta': 4, 'gamma': 2, 'delta': 5}
weights = {'alpha': 2, 'gamma': 3}

# Execution
result = calculate_final_score(data, weights)
final_score = result
print(f"Result: {final_score}")