def find_equilibrium_index(values):
    total_sum = sum(values)
    left_sum = 0
    for i in range(len(values)):
        total_sum -= values[i]
        if left_sum == total_sum:
            return i
        left_sum += values[i]
    return -1

# Simulate material stress testing across 7 segments
stress_levels = [12, 5, 7, 15, 3, 9, 6]
baseline = sum(stress_levels) // len(stress_levels)

# Normalize values above baseline to simulate compensation effect
normalized_stress = [x - baseline for x in stress_levels]

# Identify equilibrium point where left and right cumulative stresses balance
equilibrium_point = find_equilibrium_index(normalized_stress)

# Irrelevant tracking variable (minor distraction)
count_nonzero = sum(1 for x in normalized_stress if x != 0)

Result: equilibrium_point