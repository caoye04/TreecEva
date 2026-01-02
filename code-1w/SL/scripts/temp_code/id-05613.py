import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(math.sqrt(i) > 1 for i in x if i > 0)

# Decoy transformation chain
def decoy_transform(seq):
    temp = [x ** 2 for x in seq if x % 2 == 0]
    temp = [t - 1 for t in temp]
    return sorted(temp, reverse=True)

# Unused accumulator (misleading intermediate)
cumulative_shift = 0
for i in range(12):
    cumulative_shift += (i * 2) % 7

# Real data preprocessor with distractors
dummy_cache = {}
for key in ['a', 'b', 'c']:
    dummy_cache[key] = sum([ord(key) * j for j in range(3)])

# Actual core logic disguised among noise
data_stream = [8, 3, 16, 5, 2, 9, 4, 7]

scaling_factor = 1.5
offset_correction = lambda x: x + 2 if x < 5 else x  # Used later

# Misdirection: complex-looking but unused bit manipulation
bit_flags = 0
for val in data_stream:
    bit_flags ^= val
    bit_flags = (bit_flags << 1) | (bit_flags >> 7)

# Fake statistical summary (distractor)
mean_proxy = sum(data_stream) / len(data_stream)
variance_proxy = sum((x - mean_proxy) ** 2 for x in data_stream) / len(data_stream)

# Real processing begins here — deeply nested and mixed with red herrings
def apply_filter(chunk, threshold=4):
    filtered = []
    for item in chunk:
        if item > threshold:
            # Simulate conditional transform
            transformed = item // 2
            if transformed % 2 == 0:
                transformed = int(math.log2(transformed)) if transformed > 0 else 0
            filtered.append(transformed)
    return filtered

# Chained functional transformations (core relevant logic)
intermediate = list(map(lambda x: x * 3, data_stream))
intermediate = [x - 1 for x in intermediate if x % 3 == 0]

# Conditional branching with hidden relevance
if len(intermediate) > 4:
    intermediate = apply_filter(intermediate, threshold=5)
else:
    # Dead branch — never executed but looks important
    intermediate = [x + 100 for x in intermediate]

# Key pipeline function combining multiple concepts
def process_pipeline(signal):
    # Step 1: unpack and shift
    shifted = [offset_correction(x) for x in signal]
    
    # Step 2: tuple-based transformation
    paired = list(zip(shifted[::2], shifted[1::2]))
    aggregated = [a + b for a, b in paired]
    
    # Step 3: dictionary accumulation with filtering
    hist = {}
    for val in aggregated:
        hist[val] = hist.get(val, 0) + 1
    
    # Step 4: sort and transform via lambda
    sorted_vals = sorted(hist.keys(), reverse=True)
    processed = list(map(lambda x: x * scaling_factor, sorted_vals))
    
    # Step 5: final reduction
    result = 0
    for idx, p in enumerate(processed):
        if idx % 2 == 0:
            result += p
        else:
            result -= p
    return int(result)

# Execution point of interest
final_output = process_pipeline(data_stream)

# Red herring: unused final validation
checksum = sum(final_output.to_bytes(4, 'little')) if final_output > 0 else 0

# Correct output print
print(f"Result: {final_output}")