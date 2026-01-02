def calculate_harmonic_aggregate(data):
    harmonic_values = []
    for i, (x, y) in enumerate(zip(data['inputs'], data['weights'])):
        if y == 0:
            continue
        contribution = (2 * x * y) / (x + y) if x + y != 0 else 0
        adjustment = 1.5 if i % 2 == 0 else 0.8
        harmonic_values.append(contribution * adjustment)
    
    filtered = [val for val in harmonic_values if val > 1.0]
    base_score = sum(filtered)
    
    multiplier = 1.2 if len(filtered) > 3 else 0.9
    final_score = base_score * multiplier
    
    temp_offset = 0.5  # Irrelevant distraction
    unused_flag = True  # Distractor variable
    
    return final_score

# Input data structure
data_set = {
    'inputs': [4, 6, 8, 10, 12],
    'weights': [2, 3, 0, 5, 6]
}

# Computation flow
total_harmonic_score = calculate_harmonic_aggregate(data_set)
print(f"Result: {total_harmonic_score}")