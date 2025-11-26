def calculate_metric(data, weights):
    temp_data = [x.upper() for x in data if len(x) > 2]
    processed = [ord(ch) - 64 for s in temp_data for ch in s]
    
    # Distractor calculations that don't affect final result
    intermediate_sum = sum(processed) * 2
    normalized = [x / max(processed) for x in processed]
    
    # Actual relevant computation
    weighted_values = []
    for i, val in enumerate(processed):
        if i < len(weights):
            weighted_values.append(val * weights[i])
    
    final_score = sum(weighted_values[-5:])
    return final_score

data = ['cat', 'dog', 'fish', 'bird']
weights = [1.5, 2.0, 0.5, 1.0, 0.8, 1.2]

# Unused distractor variable
unused_calc = len(data) * sum(weights)

result = calculate_metric(data, weights)
print(f"Result: {result}")