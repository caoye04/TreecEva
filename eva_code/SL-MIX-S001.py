import math
import random

# Constants initialization
PI = 3.14159265359
MAX_SIZE = 1024
DEBUG_MODE = True
ERROR_CODE = -1
SUCCESS_CODE = 0

# Data structures initialization
numbers = [15, 42, 87, 23, 91, 56, 34, 78, 12, 65]
weights = [0.1, 0.2, 0.15, 0.25, 0.3]
config = {'threshold': 50, 'multiplier': 2.5, 'enabled': True}
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Variable assignments and arithmetic operations
total_sum = sum(numbers)
average = total_sum / len(numbers)
max_value = max(numbers)
min_value = min(numbers)
range_value = max_value - min_value

# Boolean operations and conditional logic
is_above_threshold = average > config['threshold']
is_enabled = config['enabled'] and DEBUG_MODE
has_valid_range = range_value > 0 and range_value < MAX_SIZE

# API/Function calls with complex parameters
squared_numbers = [x **2 for x in numbers if x > min_value]
filtered_sum = sum(squared_numbers)
sqrt_result = math.sqrt(filtered_sum)
log_result = math.log10(sqrt_result) if sqrt_result > 0 else 0

# Complex arithmetic with multiple operations
weighted_score = sum(w * n for w, n in zip(weights, numbers[:len(weights)]))
normalized_score = weighted_score / sum(weights)
bonus_multiplier = config['multiplier'] if is_above_threshold else 1.0
final_score = normalized_score * bonus_multiplier

# Bitwise operations
flags = 0b1010
position = 3
mask = flags | (1 << position)
check_bit = (mask & (1 << position)) != 0
toggled_flags = flags ^ (1 << position)

# String operations and API calls
status_message = "Processing" if is_enabled else "Disabled"
message_length = len(status_message)
uppercase_message = status_message.upper()
reversed_message = status_message[::-1]

# Multiple assignments and tuple unpacking
first, second, *rest = numbers
a, b = b if 'b' in locals() else 10, a if 'a' in locals() else 20
temp_x, temp_y, temp_z = 1, 2, 3
temp_x, temp_y = temp_y, temp_x  # Swap

# Complex expression evaluation
complex_expr = (final_score * 0.8 + log_result * 0.2)** 0.5
rounded_expr = round(complex_expr, 2)
int_expr = int(complex_expr * 100) % 1000

# Array operations and slicing
sliced_numbers = numbers[2:8:2]
reversed_slice = sliced_numbers[::-1]
sum_slice = sum(reversed_slice)

# Matrix operations
matrix_sum = sum(sum(row) for row in matrix)
diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
matrix_flatten = [item for row in matrix for item in row]

# Conditional assignments
status_code = SUCCESS_CODE if all([is_enabled, has_valid_range, check_bit]) else ERROR_CODE
error_count = 0 if status_code == SUCCESS_CODE else 1

# Final result calculation combining all elements
result = (
    int_expr + 
    sum_slice + 
    diagonal_sum + 
    (status_code * 100) + 
    error_count + 
    len(rest) + 
    message_length + 
    (toggles_flags if 'toggles_flags' in locals() else toggled_flags)
) % 10000

print(f"Final result: {result}")
    