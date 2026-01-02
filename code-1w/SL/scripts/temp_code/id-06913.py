import math

# Irrelevant utility function (dead code path)
def unused_helper(x):
    return sum(i ** 2 for i in range(x))

# Misleading precomputed constant (distractor)
PRECOMPUTED_WEIGHT = 4.783

# Another decoy function with complex logic but no invocation
def decoy_transform(sequence):
    temp = [s ^ 3 for s in sequence]
    return [t * 1.5 if t % 2 else t // 2 for t in temp]

# Real processing begins here
initial_seed = 17
offset_mask = [i * 2 + 1 for i in range(10)]  # Unused red herring

# Core data
raw_values = [3, 7, 12, 15, 21, 33]
data_sequence = [x + 5 for x in raw_values]  # [8, 12, 17, 20, 26, 38]

# Control flags with misleading structure
control_flags = {
    'enable_x': True,
    'enable_y': False,
    'mode': 'aggressive',
    'threshold': 15
}

# Decoy list comprehension with side effects (never used)
_ = [math.log(z) for z in data_sequence if z > 20 and control_flags['enable_y']]

# Conditional expression chain (Python-specific feature)
intermediate = 10 if len(data_sequence) > 5 else 0
intermediate += sum(1 for d in data_sequence if d % 3 == 0)  # counts: 12, 21 → count=2 → intermediate=12

# Bit manipulation distraction (irrelevant computation)
bit_fiddle = initial_seed << 3
bit_fiddle ^= 7

# Real transformation pipeline
mask = [int(math.sin(i) * 100) % 7 for i in range(len(data_sequence))]
adjusted = [
    (data_sequence[i] + mask[i]) if i % 2 == 0 else (data_sequence[i] - mask[i])
    for i in range(len(data_sequence))
]

# Set-based filtering to remove duplicates (even though none exist)
filtered_set = set(adjusted)
filtered_sorted = sorted(list(filtered_set))

# Simulate conditional override using ternary-like behavior
override_flag = control_flags['enable_x'] and control_flags['threshold'] < 25
scaling_factor = 1.5 if override_flag else 0.8

# Apply scaling only to values above threshold
scaled = [
    val * scaling_factor if val > control_flags['threshold'] else val
    for val in filtered_sorted
]

# Final aggregation via recursive reduction (not strictly necessary but adds depth)
def recursive_sum(arr, idx=0):
    if idx >= len(arr):
        return 0
    return arr[idx] + recursive_sum(arr, idx + 1)

# Secondary distractor: unused recursion variant
def recursive_product(arr, acc=1):
    if not arr:
        return acc
    return recursive_product(arr[1:], acc * arr[0])

# Actual key computation
aggregated = recursive_sum(scaled)  # Sum of scaled values

# Apply conditional correction based on flag state (conditional expression)
correction = -5 if not control_flags['enable_y'] else +5
aggregated += correction

# Final output influenced by multiple concepts: sequences, sets, conditionals, bit ops (distractor), recursion
final_output = int(aggregated)  # Deterministic integer result

# Print required output
print(f"Target result: {final_output}")