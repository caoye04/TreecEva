def calculate_adjusted_harmonic(elements):
    weights = [max(1, e // 2) for e in elements]
    inverse_weights = []
    
    for idx, val in enumerate(weights):
        if idx % 2 == 0:
            inverse_weights.append(1 / val)
        else:
            inverse_weights.append(val / (val + 1))
    
    total_harmonic = sum(inverse_weights)
    adjustment_factor = 0.5
    final_score = total_harmonic * adjustment_factor
    
    return final_score

# Input data
data_stream = [8, 5, 12, 3, 10]
result = calculate_adjusted_harmonic(data_stream)

temp_var = 999  # irrelevant distraction

weights = [max(1, e // 2) for e in data_stream]
inverse_weights = []
for idx, val in enumerate(weights):
    if idx % 2 == 0:
        inverse_weights.append(1 / val)
    else:
        inverse_weights.append(val / (val + 1))

total_harmonic = sum(inverse_weights)

print(f"Target result: {total_harmonic}")