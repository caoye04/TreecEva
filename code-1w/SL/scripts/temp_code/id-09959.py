def compute_neural_response(input_signal, weights):
    weighted_sum = sum([a * b for a, b in zip(input_signal, weights)])
    activation_level = max(0, weighted_sum)
    response_vector = [activation_level >> i for i in range(3)]
    
    # Irrelevant intermediate variable (minimal distraction)
    temp_normalization = sum(response_vector) + 1e-8
    
    normalized_response = [val / temp_normalization for val in response_vector]
    activation_score = int(sum(normalized_response) * 100)
    
    # Key computation with slicing and boolean logic
    threshold_flag = (activation_score > 75) and (response_vector[::2] != [])
    
    return threshold_flag

# Inputs
input_signal = [1, 2, 3, 4]
weights = [2, 3, 1, 2]

result = compute_neural_response(input_signal, weights)
print(f"Target result: {result}")