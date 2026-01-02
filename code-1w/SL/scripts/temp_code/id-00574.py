import math

# Irrelevant helper function (dead code path)
def unused_checksum(arr):
    return sum(x ^ 2 for x in arr) % 17

# Distractor transformation chain
def transform_signal(x):
    if x < 0:
        return abs(x) * 3 + 1
    else:
        return x * 2 - (x % 4)

# Unused recursive red herring
def bad_recursion(n):
    if n <= 1:
        return 1
    return bad_recursion(n-2) + bad_recursion(n-1)

# Misleading accumulator with decoy logic
def decoy_aggregator(values):
    acc = 0
    for v in values:
        acc += v ** 0.5 if v > 10 else v // 3
    return acc * 1.5

# Core processing pipeline (relevant)
data_mask = [i * i for i in range(15) if i % 3 != 0]
offset_lookup = {i: (i*5) % 13 for i in range(10)}

scaling_factor = 2.5
adjustment_bias = -0.7

# Simulated sensor data stream (input source)
data_stream = [transform_signal(x) for x in [-3, 7, 2, 8, -1, 4, 6]]

# Secondary irrelevant data structure
temporal_cache = [[i+j for j in range(4)] for i in [10, 20, 30]]

# Bit manipulation decoy
def bit_scramble(n):
    return ((n << 2) & 0xff) ^ 0xaa

# Main data processor (key function)
def process_pipeline(signal):
    # Step 1: Filter and scale valid signals
    filtered = [x for x in signal if x > 5]
    
    # Step 2: Apply scaling and bias
    adjusted = [(x * scaling_factor + adjustment_bias) for x in filtered]
    
    # Step 3: Map through offset lookup (only keys 0-9 used)
    mapped = []
    for val in adjusted:
        key = int(val) % 10
        if key in offset_lookup:
            mapped.append(val + offset_lookup[key])
    
    # Step 4: Logical filter using boolean conditions
    cleaned = [m for m in mapped if (m > 10) and (m % 2 != 0 or m < 20)]
    
    # Step 5: Accumulate using conditional summation
    total = 0
    for c in cleaned:
        if c.is_integer():
            total += int(c)
        else:
            total += int(round(c - 0.5))
    
    # Step 6: Final transformation via lambda-based reducer
    reducer = lambda a, x: a + x * 0.9 if x > 15 else a + x * 1.1
    intermediate = 0
    for val in cleaned:
        intermediate = reducer(intermediate, val)
    
    # Step 7: Apply fixed correction based on data_mask side-channel
    mask_correction = sum(data_mask[i] for i in range(5, 8)) // 10  # static indices
    
    # Step 8: Compute final output
    final = intermediate - mask_correction + len(cleaned)
    
    # Red herring: unused bitwise combination
    _unused_final = final ^ int(math.sin(final) * 100)
    
    return final

# Execution point of interest
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")