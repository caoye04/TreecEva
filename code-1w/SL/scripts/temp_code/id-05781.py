from collections import defaultdict, Counter
import math

# Simulated sensor readings (irrelevant data structure)
sensor_readings = [127, 255, 64, 192, 31, 156, 89, 223]
reading_counter = Counter(sensor_readings)

# Irrelevant transformation path
def decoy_transform(x):
    if x < 100:
        return (x ** 2) + 7
    else:
        return (x // 3) * 2 - 1

# Unused recursive function (dead code)
def recursive_noise(n):
    if n <= 1:
        return 1
    return recursive_noise(n-1) + recursive_noise(n-2)

# Real computation begins here
raw_sequence = [3, 7, 15, 31, 63]
processed = []

for val in raw_sequence:
    temp = (val + 1) // 2
    processed.append(temp)

# Misleading intermediate aggregation
sum_decoy = sum(decoy_transform(x) for x in processed[:3])

# Bit manipulation red herring
bit_fiddling = 0
for i in range(5):
    bit_fiddling ^= (i << (i % 3))

# Actual relevant logic buried within
base_anchor = 4
shift_registry = defaultdict(int)

for idx, p_val in enumerate(processed):
    shift_registry[f'level_{idx}'] = p_val % base_anchor

# Conditional branch with early escape (partially relevant)
if len(processed) > 4:
    magnitude = sum(math.floor(p * 0.5) for p in processed)
    offset = 11
    # Key computational step disguised among distractions
    core_elements = [processed[i] for i in range(len(processed)) if i % 2 == 0]
    pivot_value = core_elements[-1] * 2

    # Decoy list slicing
    slice_trap = processed[1:4:2]
    
    # Critical operation hidden in modular arithmetic
    accumulator = 0
    for j in range(pivot_value):
        accumulator += (j * base_anchor) % 13
        if accumulator > 100:
            break  # Early termination

    # Real answer derivation
    adjustment = sum(shift_registry.values())
    final_flux = (accumulator + adjustment) * 3 - offset
else:
    final_flux = -999  # Dead path

# Unused set operations (distractor)
unique_processed = set(processed)
duplicate_check = unique_processed & {1, 2, 7, 15}

# Redundant print statements (noise)
# print(f'Debug: {sum_decoy}, {bit_fiddling}')
# print(f'Shifts: {dict(shift_registry)}')

# Only this output matters
print(f"Result: {final_flux}")