def preprocess_signal(data):
    # Irrelevant signal smoothing (dead code path)
    smoothed = [x * 0.9 for x in data]
    return [int(x) for x in data if x > 0]


def validate_chunk(chunk, key):
    # Misleading checksum that isn't actually used
    fake_sum = sum(chunk) * key % 256
    actual_bits = sum((x & 3) for x in chunk)  # Only lower 2 bits matter
    return actual_bits > key


def encode_frame(payload):
    # Unused encoding logic (distractor)
    encoded = []
    for x in payload:
        encoded.append((x << 2) | (x >> 6))
    return encoded

# Initialization of various buffers (some irrelevant)
raw_samples = [15, 23, 17, 45, 91, 67, 89, 22]
filter_threshold = 20
excluded_zones = {1, 3, 5}

# Simulated sensor stream with control flags
stream_buffer = []
for val in raw_samples:
    if val < filter_threshold:
        continue
    flag = (val & 8) >> 3  # Extract bit 3
    priority = (val & 4) >> 2  # Extract bit 2
    
    # Add transformed value and metadata
    stream_buffer.append(val & 0b111)  # Keep only lowest 3 bits
    
    # Dead code: this block never executes due to value ranges
    if val > 200:
        backup_queue = [val]

# Red herring: unused set operations
working_set = {x for x in stream_buffer if x % 2 == 0}
temp_set = {x+1 for x in working_set}
delta_set = temp_set - working_set

# Key control variable disguised among distractions
validation_key = len(raw_samples) ^ 0b1101  # XOR with magic number

# Unused intermediate processing
shifted_data = [x << 1 for x in stream_buffer]
masked_data = [x & 7 for x in shifted_data]  # Redundant masking

# Actual critical computation chain
active_flags = 0
for item in stream_buffer:
    active_flags ^= item  # Accumulate XOR state

checksum = 0
for i, item in enumerate(stream_buffer):
    if i % 2 == 0:
        checksum += item * (i + 1)

# Conditional logic with early exit red herring
if validation_key < 5:
    final_output = -1
    print("Target result: -1")
else:
    # Real computation: combine checksum with flag state
    final_output = (checksum & 0xFF) + (active_flags << 2)
    
    # Additional distraction: unused dictionary aggregation
    stats = {}
    for x in stream_buffer:
        tag = 'low' if x < 4 else 'high'
        if tag not in stats:
            stats[tag] = 0
        stats[tag] += 1
    
    # Another dead-end function call
    dummy = preprocess_signal([10, 5, 3])

print(f"Result: {final_output}")