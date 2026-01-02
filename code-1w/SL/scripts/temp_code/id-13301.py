import math

# Irrelevant helper function (dead code path)
def unused_checksum(data):
    return sum(d ^ 0xFF for d in data) % 256

# Distractor variables
temp_cache = [0] * 100
debug_trace = []
rolling_hash = 1
offset_table = {i: (i * 17) % 23 for i in range(20)}

# Real processing components
def decode_signal(x):
    return (x >> 2) & ~(1 << 3)

def evaluate_entropy(chunk):
    total = 0
    for val in chunk:
        if val > 0:
            total += int(math.log(val + 1, 2))
    return total

def filter_anomalies(logs):
    return [x for x in logs if x % 4 != 3]

# Core logic with distractors
stream_buffer = [
    12, 8, 15, 3, 9, 11, 6, 4, 13, 7, 10, 5, 14, 2, 1, 0
]

scaling_factor = 1.5
base_shift = 3
mask_pattern = 0x0F

# Misleading intermediate computation (unused)
candidate_keys = []
for i in range(8):
    candidate_keys.append((i * 13 + 7) % 97)

# Another red herring: complex but irrelevant structure
lookup_matrix = [[(i*j + 1) % 11 for j in range(5)] for i in range(5)]

# Conditional expression and enumerate usage
event_flags = [
    idx * 2 if val % 2 == 0 else val + 1
    for idx, val in enumerate(stream_buffer)
]

# Lambda for obfuscation (not actually needed)
transform = lambda x: x ^ base_shift

data_weights = list(map(lambda w: (w + 1) * scaling_factor, event_flags[:8]))

# Real function that contributes to final result
def process_data(data):
    # Level 1 nesting
    cleaned = filter_anomalies(data)
    accumulator = 0
    
    # Level 2 nesting
    for index, item in enumerate(cleaned):
        # Level 3 nesting
        if index % 3 == 0:
            decoded = decode_signal(item)
            
            # Level 4 nesting
            if decoded > 2:
                # Key transformation
                accumulator += int(math.sqrt(decoded * 4))
        elif index == 4:
            # Red herring branch: modifies rolling_hash but never used
            global rolling_hash
            rolling_hash = (rolling_hash * 31 + item) % 10007
            debug_trace.append('triggered')
    
    # Use of zip and conditional expression
    pairs = list(zip(cleaned[::2], cleaned[1::2]))
    entropy_chunk = [max(a, b) if a != b else a + 1 for a, b in pairs]
    
    # Actual contribution to answer
    entropy_score = evaluate_entropy(entropy_chunk)
    
    # Final calculation
    temp_result = accumulator * 2 + (entropy_score % 7)
    
    # Decoy operation (looks important but unused)
    _ = [temp_cache.__setitem__(i % 100, (temp_result ^ i) % 1000) for i in range(5)]
    
    return temp_result

# Execution point of interest
final_output = process_data(stream_buffer)

# Output requirement
print(f"Target result: {final_output}")