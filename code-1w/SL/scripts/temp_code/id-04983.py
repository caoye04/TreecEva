from itertools import combinations

# System load parameters
core_nodes = [3, 7, 4, 8, 2]
dummy_var_1 = [x ** 2 for x in core_nodes]  # Irrelevant computation

# Generate overlapping usage windows of size 3
usage_windows = []
for i in range(len(core_nodes) - 2):
    window_sum = sum(core_nodes[i:i+3])
    usage_windows.append(window_sum)

dummy_var_2 = list(combinations(core_nodes, 2))  # Slight distraction using itertools

# Identify peak capacity across all sliding windows
peak_capacity = max(usage_windows)

# Early termination if peak exceeds threshold
if peak_capacity > 15:
    peak_capacity -= 1  # Adjustment based on safety margin

print(f"Result: {peak_capacity}")