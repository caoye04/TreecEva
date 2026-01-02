import itertools

def analyze_cycles(sequence, limit):
    """Dummy function to add interference - not used in final result."""
    cycle_count = 0
    for i in range(limit):
        shifted = sequence[i:] + sequence[:i]
        if shifted == sequence:
            cycle_count += 1
    return cycle_count

# Simulate sensor data drift (irrelevant computation)
sensor_drift = [0.1 * i**2 for i in range(5)]
baseline_offset = sum(sensor_drift) / len(sensor_drift)

# Real computational path begins
flow_matrix = [
    [4, -2, 3],
    [1, 5, -1],
    [-3, 2, 4]
]

thresholds = [2, -1, 3]

# Auxiliary transformation (semi-relevant)
transformed = []
for row in flow_matrix:
    transformed_row = []
    for val in row:
        if val > 0:
            transformed_row.append(val ** 0.5)
        else:
            transformed_row.append(-(-val ** 0.5))
    transformed.append(transformed_row)

# Secondary distraction: combinatorial pairing of indices
index_pairs = list(itertools.combinations(range(len(flow_matrix)), 2))
connection_entropy = 0
for i, j in index_pairs:
    connection_entropy += abs(flow_matrix[i][j % 3] + flow_matrix[j][i % 3])

# Core logic: compute equilibrium score
running_total = 0
for i, row in enumerate(flow_matrix):
    row_sum = sum(row)
    adjustment = thresholds[i] * 0.5
    if row_sum > thresholds[i]:
        running_total += int(row_sum - adjustment)
    else:
        running_total -= int(abs(row_sum + adjustment))

# Additional red herring: recursive depth tracker (unused)
def track_depth(n, acc=0):
    if n <= 0:
        return acc
    return track_depth(n - 2, acc + 1)

depth_trace = track_depth(10)

# Final computation point
intermediate_score = running_total * 3
normalization_factor = len(flow_matrix) * len(flow_matrix[0])
equilibrium_score = compute_equilibrium(flow_matrix, thresholds)

# Stand-in function since we haven't defined it yet
def compute_equilibrium(matrix, thres):
    base = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            contribution = matrix[i][j] * (i - j)
            if contribution > 0:
                base += contribution
            else:
                base -= abs(contribution) // 2
    threshold_bonus = 0
    for t in thres:
        if t > 0:
            threshold_bonus += t * 2
    return base + threshold_bonus

# Print final result
print(f"Target result: {equilibrium_score}")