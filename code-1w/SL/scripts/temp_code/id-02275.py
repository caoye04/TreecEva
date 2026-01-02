import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 100

# Unused utility for string scoring (distractor)
def compute_string_score(s):
    return sum(ord(c) - 96 for c in s.lower() if c.isalpha())

# Decoy data structure with misleading values
decoy_buffer = [17, 23, 45, 67, 89, 101]
buffer_sum = sum(decoy_buffer)  # Irrelevant computation

# Real processing begins here
initial_seed = 507
shift_factor = 7
mask_value = 23

# Simulated data stream (real input)
data_stream = [i * 3 + 2 for i in range(15) if i % 2 == 0]

# Bit manipulation red herring
bit_noises = [(x ^ mask_value) << 1 for x in data_stream]
truncated_noise = [x & 0xFF for x in bit_noises]  # Unused

# Core transformation chain
transform_A = list(map(lambda x: (x + shift_factor) // 3, data_stream))
transform_B = [math.floor(math.sqrt(x)) for x in transform_A if x > 10]

# Conditional filtering with short-circuit logic
filtered_vals = []
for val in transform_B:
    if val > 0 and (val % 2 == 0 or (val % 3 == 0 and val < 50)):
        filtered_vals.append(val * 2)

# Secondary transformation with integer division
aggregated = 0
for i, v in enumerate(filtered_vals):
    if i % 2 == 0:
        aggregated += v // (i + 1)
    else:
        aggregated -= v // 2

# String distraction: count characters in a fixed phrase
status_msg = "Processing final computation phase"
count_p = len([c for c in status_msg if c.lower() == 'p'])  # Irrelevant

# Key computational step disguised among noise
temp_offset = (initial_seed // 9) * 4
scaling_base = len(transform_A) + len(filtered_vals)
interim_result = aggregated + temp_offset - scaling_base

# Final pipeline function combining multiple concepts
def process_pipeline(stream):
    base = sum(stream) // len(stream)
    exponents = [2 ** (i % 4) for i in range(len(stream))]
    weighted = sum(s * e for s, e in zip(stream, exponents))
    # Actual answer derivation
    core_signal = weighted // base
    adjustment = math.floor(math.log(core_signal, 2)) if core_signal > 1 else 0
    return core_signal - adjustment

# Execution point of interest
final_output = process_pipeline(data_stream)

# Output result as required
print(f"Target result: {final_output}")