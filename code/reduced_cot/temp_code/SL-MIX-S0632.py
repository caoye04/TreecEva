from collections import deque

def max_non_adjacent_sum(row):
    if not row:
        return 0
    if len(row) == 1:
        return row[0]
    
    prev_prev = row[0]
    prev = max(row[0], row[1])
    
    for i in range(2, len(row)):
        current = max(prev, prev_prev + row[i])
        prev_prev, prev = prev, current
    
    return prev

# Container value matrix
containers = [
    [2, 1, 4, 9],
    [3, 6, 2, 8],
    [1, 7, 5, 3]
]

correction_lambda = lambda x, factor=1.5: int(x * factor) if x % 2 == 0 else x

max_values_per_row = []
for row in containers:
    max_val = max_non_adjacent_sum(row)
    corrected_val = correction_lambda(max_val)
    max_values_per_row.append(corrected_val)

stack_operations = deque()
for val in max_values_per_row:
    stack_operations.append(val if val > 5 else val * 2)

final_sum = 0
while stack_operations:
    top_element = stack_operations.pop()
    final_sum = final_sum + top_element if top_element % 2 == 0 else final_sum - top_element

optimized_loading_score = final_sum
print(f"Result: {optimized_loading_score}")