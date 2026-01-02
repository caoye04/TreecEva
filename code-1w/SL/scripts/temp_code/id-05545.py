def calculate_final_score(entries):
    total_score = 0
    weights = [0.2, 0.3, 0.5]
    
    for i, (key, values) in enumerate(entries.items()):
        raw_average = sum(values) / len(values)
        adjusted = raw_average * weights[i % len(weights)]
        total_score += adjusted
    
    bonus = 5 if all(len(v) >= 3 for v in entries.values()) else 0
    total_score += bonus
    
    return total_score

# Irrelevant auxiliary variable (minimal distraction)
dummy_data = {'temp': [1, 2], 'meta': [99]}

results = {
    'math': [85, 90, 78],
    'science': [88, 85],
    'english': [92, 87, 85, 90]
}

final_result = None
intermediate = []
for k, v in results.items():
    intermediate.append((k, len(v)))

# Key computation step
total_score = calculate_final_score(results)

print(f"Result: {total_score}")