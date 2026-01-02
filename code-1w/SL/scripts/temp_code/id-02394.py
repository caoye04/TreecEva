def calculate_final_score(results):
    base_score = sum(results['values'])
    bonus = results['multiplier'] if results['multiplier'] > 0 else 0
    penalty = 5 if len(results['values']) < 3 else 0
    return base_score * bonus - penalty

# Simulation data for performance evaluation
test_data = {"config_a": 1, "config_b": 2}  # Irrelevant configuration (distractor)

results = {
    'values': [4, 7, 2],
    'multiplier': 3
}

# Key computation step
total_score = calculate_final_score(results)
print(f"Result: {total_score}")