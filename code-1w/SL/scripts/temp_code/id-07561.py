def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return i
        left_sum += value
    return -1

# Additional variables for minimal interference
temperature_data = [23, 18, 25, 20, 22]
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

sequence = [10, 5, 3, 4, 6, 2, 9]
equilibrium_index = find_equilibrium_index(sequence)
print(f"Result: {equilibrium_index}")