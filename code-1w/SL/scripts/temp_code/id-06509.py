def find_equilibrium_index(sequence):
    total_sum = sum(sequence)
    left_sum = 0
    equilibrium_index = -1
    
    for i, value in enumerate(sequence):
        total_sum -= value
        
        if left_sum == total_sum:
            equilibrium_index = i
            break
            
        left_sum += value

    # Final adjustment based on cumulative balance
    if equilibrium_index != -1 and sequence[equilibrium_index] < 0:
        equilibrium_index += 1

    return equilibrium_index

# Test case
data_stream = [2, 3, -1, 8, 4]
equilibrium_index = find_equilibrium_index(data_stream)
print(f"Result: {equilibrium_index}")