import itertools

# Simulated sensor data stream with calibration offsets
def get_raw_readings():
    return [18, 22, 19, 25, 21, 17, 23, 20, 24, 16]

# Irrelevant helper function (decoy)
def analyze_trend(data):
    return sum(1 for i in range(1, len(data)) if data[i] > data[i-1])

# Red herring: unused transformation
def deprecated_filter(x):
    return x if x % 3 == 0 else 0

# Core processing pipeline
readings = get_raw_readings()
baseline = sum(readings) // len(readings)

# Apply moving average filter (slicing window)
smoothed = [(readings[i-1] + readings[i] + readings[i+1]) // 3 
           for i in range(1, len(readings)-1)]
smoothed.insert(0, readings[0])  # Preserve start
smoothed.append(readings[-1])   # Preserve end

# Mask outliers using modular threshold
mod_threshold = baseline % 7
masked = [x if abs(x - baseline) <= mod_threshold else baseline for x in smoothed]

# Bit manipulation for error correction (XOR-based checksum simulation)
checksum = 0
for val in masked:
    checksum ^= (val & 15)  # Use only lower 4 bits

corrected = [(val ^ (checksum >> 1)) for val in masked]

# Segment into chunks (using itertools)
chunked = list(itertools.batched(corrected, 4))  # Split into groups of 4

target_chunk = chunked[1]  # Second chunk is primary focus

# Transform via cyclic shift and scaling
shift_amount = checksum % 3
transformed_chunk = target_chunk[shift_amount:] + target_chunk[:shift_amount]
transformed_chunk = [x * 2 + (x % 4) for x in transformed_chunk]

# Spurious unrelated calculation (distractor)
aggregate_stats = {
    'peak': max(corrected),
    'variance': sum((x - baseline) ** 2 for x in corrected) // len(corrected),
    'transient_count': sum(1 for x in masked if x == baseline)
}

# Conditional logic with short-circuiting (red herring path)
if len(chunked) > 3 and not (aggregate_stats['peak'] < 20 or checksum < 5):
    alternate_route = [x - 5 for x in chunked[2]]
else:
    alternate_route = None  # Dead code branch

# Real computation path
intermediate_scale = sum(transformed_chunk[i] * (i+1) for i in range(len(transformed_chunk)))

# Final non-linear transformation
def process_data(seq):
    total = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            total += val ** 2
        else:
            total -= (val * checksum)
    return total // (baseline % 5 or 1)  # Avoid div-by-zero

# Critical execution point
final_output = process_data(transformed_chunk)

# Print result for verification
print(f"Result: {final_output}")