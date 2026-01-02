from itertools import accumulate

def find_equilibrium(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, value in enumerate(arr):
        # Right sum is total minus left sum and current element
        right_sum = total_sum - left_sum - value
        if left_sum == right_sum:
            return i  # Return index as equilibrium point
        left_sum += value
    return -1  # No equilibrium found

# Simulate sensor weight readings on a beam
top_weights = [4, 7, 3, 8, 5, 2]
equilibrium_point = find_equilibrium(top_weights)

# Irrelevant auxiliary calculation (minor interference)
double_accum = list(accumulate([x * 2 for x in top_weights]))

print(f"Target result: {equilibrium_point}")