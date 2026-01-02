from itertools import accumulate

def find_equilibrium_index(sequence):
    total_sum = sum(sequence)
    left_sum = 0
    for i, value in enumerate(sequence):
        # Right sum is total minus left sum and current element
        right_sum = total_sum - left_sum - value
        if left_sum == right_sum:
            return i
        left_sum += value
    return -1

# Simulate stress level readings across a structural beam
turbine_stress = (12, 4, 8, 2, 10, 6, 14)
stress_levels = list(accumulate(turbine_stress))  # Cumulative stress propagation
baseline_offset = 3
adjusted_stress = [s - baseline_offset for s in stress_levels]

# Identify equilibrium point where forces balance
equilibrium_point = find_equilibrium_index(stress_levels)

# Irrelevant auxiliary calculation (minor distraction)
max_gradient = max(stress_levels[i+1] - stress_levels[i] for i in range(len(stress_levels)-1))

print(f"Result: {equilibrium_point}")