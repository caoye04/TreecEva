def calculate_equilibrium(sequence):
    processed = [x * 2 + 1 for x in sequence]
    filtered = [x for x in processed if x % 3 == 0]
    
    # Apply modular arithmetic to wrap values into range [0, 100)
    adjusted_values = [x % 100 for x in filtered]
    
    # Check balance condition using slicing and length check
    left_half = adjusted_values[:len(adjusted_values)//2]
    right_half = adjusted_values[-len(left_half):] if len(adjusted_values) >= 2 else []
    is_balanced = len(left_half) > 0 and sum(left_half) == sum(right_half)
    
    # Determine mid index and extract central value if available
    mid_index = len(adjusted_values) // 2
    equilibrium_point = adjusted_values[mid_index] if is_balanced else sum(adjusted_values) // len(adjusted_values)
    
    # Irrelevant tracking variable (minimal interference)
    total_iterations = 0
    for _ in adjusted_values:
        total_iterations += 1
    
    print(f"Result: {equilibrium_point}")

# Input sequence
data_stream = [4, 7, 13, 16, 22]
calculate_equilibrium(data_stream)