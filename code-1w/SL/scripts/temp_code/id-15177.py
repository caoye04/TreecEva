def calculate_final_score(results, weights):
    normalized = []
    base_offset = 10
    scaling_factor = 2.5
    temp_sum = 0

    for i, (key, score) in enumerate(zip(results.keys(), results.values())):
        if i % 2 == 0:
            normalized.append(score / 100)
        else:
            normalized.append((score + base_offset) / 110)

    for idx in range(len(normalized)):
        temp_sum += normalized[idx] * weights[idx]

    final_adjustment = temp_sum * scaling_factor
    return int(final_adjustment)

# Simulation data
results = {'round_1': 88, 'round_2': 94, 'round_3': 76, 'round_4': 85}
weights = [0.2, 0.3, 0.15, 0.35]

# Irrelevant auxiliary variable (minor distraction)
dummy_var = [x ** 2 for x in weights]

# Key computation
result_value = calculate_final_score(results, weights)
total_score = result_value

print(f"Result: {total_score}")