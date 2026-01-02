def calculate_load_index(sequence, threshold):
    index = 0
    temp_sum = 0
    for val in sequence:
        if val > threshold:
            temp_sum += val * 0.5
        else:
            temp_sum += val * 0.1
    index = int(temp_sum % 10)
    return index

sequences = [
    [3, 7, 2, 8, 5],
    [9, 1, 4, 6, 3],
    [2, 5, 8, 1, 9],
    [4, 4, 7, 3, 6]
]

summary_stats = []
for seq in sequences:
    avg = sum(seq) / len(seq)
    variance = sum((x - avg) ** 2 for x in seq) / len(seq)
    summary_stats.append({'avg': avg, 'variance': variance})

# Irrelevant transformation
transformed = [seq[::2] for seq in sequences]  # slicing operation used

baseline = 4
load_factors = []
for i in range(len(sequences)):
    factor = calculate_load_index(sequences[i], baseline)
    load_factors.append(factor)

grid = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

start_row = 1

# Misleading pre-computation with no impact
aggregate = 0
for row in grid:
    for elem in row:
        aggregate += elem ** 0.5

# Helper function using recursion
def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

# Dead code path (never called)
def unused_diagonal_check(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total == 50

# Real logic begins
offset = recursive_sum(3)  # returns 6

mask = [i % 2 for i in range(len(grid[start_row]))]

filtered_row = []
for i, val in enumerate(grid[start_row]):
    if mask[i] == 1:
        filtered_row.append(val)

# Slice-based extraction
segment = filtered_row[1:]

intermediate_total = 0
for num in segment:
    intermediate_total += num * load_factors[num % len(load_factors)]

scaling_factor = summary_stats[0]['avg']  # 5.0

adjusted_total = intermediate_total / scaling_factor

# Final peak capacity calculation
peak_capacity = calculate_peak(grid, start_row)

def calculate_peak(matrix, row_idx):
    base = sum(matrix[row_idx])
    correction = len(matrix[row_idx][2:])  # slicing
    bonus = 0
    if base > 30:
        bonus = 5
    return base + correction + bonus + offset

Result: {peak_capacity}