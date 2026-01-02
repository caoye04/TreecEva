import math

# Irrelevant helper function (decoy)
def useless_transform(x):
    return (x ** 2 + 3 * x + 1) % 17

# Another red herring: complex-looking but unused transformation
class ObfuscationLayer:
    def __init__(self, shift):
        self.shift = shift
        self.key = [useless_transform(i + shift) for i in range(5)]

    def scramble(self, val):
        return val ^ self.key[0]

# Misleading data structure with unused computations
redundant_cache = {
    'temp_metrics': [],
    'debug_flags': [False] * 10,
    'aux_data': [i * i - 2 * i + 1 for i in range(15)]  # Unused polynomial sequence
}

# Core logic disguised among distractions
data_stream = [
    5, 3, 8, 1, 9, 4, 2, 7, 6
]

# Distractor: irrelevant slicing and lambda combinations
shadow_copy = data_stream[2:7][::-1]
filter_func = lambda x: x > 4
filtered_junk = list(filter(filter_func, shadow_copy))

# Real processing begins — subtle and buried
transformation_chain = [
    lambda x: x * 2,
    lambda x: x + 3 if x % 4 == 0 else x,
    lambda x: x ^ 5  # Bitwise XOR as part of actual logic
]

def apply_transforms(val, chain):
    result = val
    for func in chain:
        result = func(result)  # Each step modifies the value
    return result

# Secondary distraction: recursive dead-end function
def bad_recursion(n):
    if n <= 1:
        return 1
    return bad_recursion(n - 2) + bad_recursion(n - 1)  # Exponential waste

# Unused but plausible-looking accumulator
decoys = []
for i in range(len(data_stream)):
    if i % 3 == 0:
        decoys.append(useless_transform(data_stream[i]))

# Actual critical computation path
intermediate_values = []
for num in data_stream:
    processed = num
    if processed % 2 == 0:  # Only even numbers go through full transform
        processed = apply_transforms(processed, transformation_chain)
    intermediate_values.append(processed)

# More misdirection: slice manipulation that isn't used later
temp_slice = intermediate_values[1:6:2]

# Real aggregation
aggregated = 0
for val in intermediate_values:
    aggregated += val % 11  # Modulo arithmetic is key

# Additional noise: unused early exit pattern
def check_early(val):
    if val > 100:
        return True
    return False

# Final processing buried in a larger context
def process_pipeline(stream):
    base_sum = sum(stream)  # Used only in decoy way
    main_result = 0
    for v in stream:
        if v in {1, 3, 5, 7}:  # Specific odd values trigger action
            main_result += v * 4
        elif v % 2 == 0:  # Even values follow transformed path
            temp = apply_transforms(v, transformation_chain)
            main_result += temp % 7
    # Final twist: combine with earlier modulo sum
    final_adjustment = (aggregated * 3) // 4
    return main_result - final_adjustment

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output required format
print(f"Target result: {final_output}")