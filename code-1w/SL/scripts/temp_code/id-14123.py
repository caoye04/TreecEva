def calculate_final_score(records, importance):
    base_score = 0
    bonus = 0
    penalty = 0
    temp_result = []

    # Irrelevant string processing (distractor)
    status_labels = ['valid', 'active', 'verified']
    label_summary = ''.join([label[0] for label in status_labels])

    # Real logic begins: compute base score from records
    for key, value in records.items():
        if len(key) > 3:
            base_score += value * importance.get(key, 1)

        # Misleading conditional that never triggers due to data
        if key == "deprecated":
            penalty += 100  # dead code path

    # Simulate intermediate transformation (semi-relevant)
    transformed = [x * 1.5 for x in records.values() if x > 10]
    adjustment_factor = sum(transformed) / len(transformed) if transformed else 1.0

    # Bonus logic based on dictionary structure
    if len(records) >= 4 and 'alpha' in records:
        bonus += 15

    # Another distraction: unused list comprehension
    squared_values = [v**2 for v in importance.values() if v > 0.5]

    # Final computation with adjustment
    final_score = int((base_score + bonus) * adjustment_factor - penalty)

    return final_score

# Data setup
raw_data = {
    'alpha': 12,
    'beta': 8,
    'gamma': 15,
    'delta': 20,
    'z': 5
}

weights_map = {
    'alpha': 1.2,
    'beta': 0.8,
    'gamma': 1.5,
    'delta': 1.1
}

# Execute main logic
target_variable = 'final_score'
final_score = calculate_final_score(raw_data, weights_map)

print(f"Result: {final_score}")