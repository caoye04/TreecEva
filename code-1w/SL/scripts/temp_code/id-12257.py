from collections import defaultdict

# Simulate a physical equilibrium problem: find index where left and right weighted sums are equal
def find_equilibrium_index(weights):
    total_weight = sum(weights)
    left_sum = 0
    for i, w in enumerate(weights):
        # Right sum is total - left_sum - current weight
        right_sum = total_weight - left_sum - w
        if left_sum == right_sum:
            return i  # Found equilibrium
        left_sum += w
    return -1  # No equilibrium found

# Irrelevant helper: counts frequency of weights (distractor)
weight_counter = defaultdict(int)
sequence = [4, 7, 3, 6, 8, 5, 3]
for w in sequence:
    weight_counter[w] += 1

# Main computation: find equilibrium index
equilibrium_index = find_equilibrium_index(sequence)

# Additional irrelevant operation (minor distraction)
total_moment = sum(i * w for i, w in enumerate(sequence))

Result: equilibrium_index