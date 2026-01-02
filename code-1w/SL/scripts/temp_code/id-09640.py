def find_equilibrium_index(sequence):
    total_sum = sum(sequence)
    left_sum = 0
    equilibrium_index = -1
    temp_placeholder = 0

    for i, value in enumerate(sequence):
        total_sum -= value
        
        # Check if left and right sums are balanced
        if left_sum == total_sum:
            equilibrium_index = i
            break
        
        left_sum += value
        temp_placeholder += i  # Irrelevant operation (minimal interference)

    return equilibrium_index

# Input sequence
data_stream = [2, 3, 4, -4, 3, 2]
equilibrium_index = find_equilibrium_index(data_stream)
print(f"Result: {equilibrium_index}")