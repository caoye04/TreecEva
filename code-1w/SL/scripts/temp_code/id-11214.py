import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x) % 7

# Distractor transformation chain
def transform_a(val):
    temp = val ^ 255  # bitwise XOR with red herring
    temp = (temp + 17) * 3
    return temp  # never actually used in main logic

def transform_b(val):
    return val * 2 + 10

def transform_c(val):
    return int(math.sqrt(val)) if val > 0 else 0

def transform_d(val):
    return abs(val - 100) | 45  # irrelevant OR operation

# Core processing pipeline
pipeline_functions = [
    lambda x: x + 10,
    lambda x: x * 3,
    lambda x: x - 25,
    lambda x: x ** 2,
    lambda x: x // 10
]

def apply_filters(value, threshold=50):
    if value < 0:
        return 0
    elif value > 1000:
        return 1000
    return value  # clamping filter (used once)

# Misleading data history (unused)
historical_data = [12, 15, 22, 31, 40, 55]
accumulated = 0
for h in historical_data:
    accumulated += h * 2

# Main data flow
raw_input = 15
intermediate_1 = raw_input + 5

# Conditional bypass that looks important but isn't
if intermediate_1 % 2 == 0:
    backup_path = transform_b(intermediate_1)
    secondary_check = backup_path - 30
else:
    backup_path = 0

# Real computation begins here
working_value = intermediate_1

# Apply series of transformations
for func in pipeline_functions:
    working_value = func(working_value)
    # Early break that only triggers under other conditions (not this case)
    if working_value > 10000:
        break

# Filtering step
filtered_result = apply_filters(working_value)

# Decoy branching logic
if filtered_result < 50:
    final_output = transform_c(filtered_result)
elif filtered_result > 500:
    final_output = transform_d(filtered_result)
else:
    # This is the actual execution path
    adjustment_factor = (filtered_result + 5) % 17
    final_output = filtered_result + adjustment_factor

# Extraneous logging block (no effect)
counter = 0
log_entries = []
while counter < 3:
    log_entries.append(f"Log entry {counter}: system active")
    counter += 1

# Critical output statement
target_variable_name = "final_output"
Result = final_output
print(f"Target result: {Result}")