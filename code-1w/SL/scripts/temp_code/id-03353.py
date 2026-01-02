def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return i
        left_sum += value
    return -1

# Simulate chemical concentration levels across a reaction chain
temp_readings = [23, 45, 12, 67, 34]  # Irrelevant sensor data (distractor)
concentration_levels = [1, 3, 2, 4, 3]
equilibrium_point = find_equilibrium_index(concentration_levels)

print(f"Result: {equilibrium_point}")