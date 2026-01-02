def analyze_pattern(sequence, pivot):
    accumulator = 0
    temp_history = []
    for index in range(len(sequence)):
        if sequence[index] > pivot:
            accumulator += index * sequence[index]
        else:
            accumulator -= sequence[index]
        temp_history.append(accumulator)
    
    # Irrelevant transformation (distractor)
    normalized = [x / (max(temp_history) + 1e-5) for x in temp_history]
    scaled_sum = sum(normalized)

    return accumulator

# Misleading precomputation (semi-relevant)
def estimate_complexity(n):
    if n <= 1:
        return 1
    return estimate_complexity(n - 1) + estimate_complexity(n // 2)

# Core logic with conditional expression
def validate_state(buffer, limit):
    base_score = sum(x ** 2 for x in buffer if x % 2 == 1)  # Only odd values contribute
    penalty = 0 if len(buffer) < limit else len(buffer) * 2
    adjustment = 10 if any(buffer[i] == buffer[i+1] for i in range(len(buffer)-1)) else 5
    
    # Red herring: unused intermediate calculation
    entropy_proxy = 0.0
    for val in buffer:
        if val > 0:
            entropy_proxy += val * (val).bit_length()

    final_score = base_score - penalty + adjustment
    return int(final_score)

# Main execution flow
primary_data = [3, 7, 2, 8, 7, 4, 9]
dynamic_pivot = 5

result_a = analyze_pattern(primary_data, dynamic_pivot)

# Simulate side computation (dead-end)
size_estimate = estimate_complexity(6)  # Not used later

transient_buffer = [x - dynamic_pivot for x in primary_data]
threshold = 4

# Key statement
equilibrium_score = validate_state(transient_buffer, threshold)

print(f"Result: {equilibrium_score}")