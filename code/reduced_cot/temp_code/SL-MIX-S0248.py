def transform_value(x):
    # Irrelevant bitwise operation that doesn't affect main logic
    bit_shift = (x << 2) & 0xFF
    
    # Main transformation - conditional expression with arithmetic
    return x * 3 if x % 2 == 0 else x + 7

def calculate_bonus(scores):
    # Dead code path - never called
    unused_computation = sum(scores) * 2
    return max(scores) - min(scores)

# Primary data structure - 3x3 matrix
matrix = [[2, 5, 8], [3, 7, 1], [4, 6, 9]]

# Distractor calculations
row_sums = [sum(row) for row in matrix]
total_sum = sum(row_sums)
mean_value = total_sum / len(matrix) ** 2

# Misleading intermediate result
intermediate = [x for row in matrix for x in row]
filtered_values = [x for x in intermediate if x > 4]

# Irrelevant tuple operations
coordinate_pairs = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
distance_calc = sum(abs(a - b) for a, b in coordinate_pairs)

# Critical execution point - list comprehension with helper function
result_matrix = [[transform_value(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]

# Final computation with slicing
flattened = [item for sublist in result_matrix for item in sublist]
selected = flattened[2:7]  # Slice from index 2 to 6
final_output = sum(selected)

# Red herring - never used
bonus_calc = calculate_bonus([x for row in matrix for x in row])

print(f"Result: {final_output}")