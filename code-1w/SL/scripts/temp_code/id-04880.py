from itertools import accumulate

# Simulate sensor readings along a beam
deflections = [4, 5, 1, 6, 3, 2, 8]

# Irrelevant baseline offset (minimal distraction)
baseline = 2
adjusted_deflections = [d - baseline for d in deflections]

# Compute prefix sums for efficient range queries
prefix_sums = list(accumulate(deflections, initial=0))

total_sum = sum(deflections)
equilibrium_index = -1

# Find first equilibrium point where left sum equals right sum
for i in range(1, len(deflections) + 1):
    left_sum = prefix_sums[i] - deflections[i-1]
    right_sum = total_sum - prefix_sums[i]
    
    if left_sum == right_sum:
        equilibrium_index = i - 1
        break

# Print result as required
print(f"Result: {equilibrium_index}")