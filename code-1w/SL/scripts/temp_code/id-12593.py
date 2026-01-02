import itertools

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return (x ** 2 + 3 * x + 1) % 17

def misleading_aggregator(values):
    # This function is called but its result is discarded
    temp_sum = 0
    for v in values:
        if v % 3 == 0:
            temp_sum += v * 2
        elif v % 5 == 0:
            temp_sum += v // 2
    return temp_sum

def compute_checksum(seq):
    # Used in final computation
    checksum = 0
    for i, val in enumerate(seq):
        checksum ^= (val + i) % 256
    return checksum

def recursive_filter(arr, depth):
    if depth == 0 or len(arr) == 0:
        return [x for x in arr if x % 4 == 2]
    filtered = [x for x in arr if x > (depth * 10)]
    return recursive_filter(filtered, depth - 1)

def generate_sequence(n):
    # Generates a deterministic sequence with modular arithmetic
    seq = [1]
    for i in range(1, n):
        next_val = (seq[-1] * 7 + 13) % 997
        seq.append(next_val)
    return seq

def process_pipeline(data):
    # Real pipeline logic
    stage1 = [x for x in data if x % 2 == 1]  # Keep odd numbers
    stage2 = [x * 2 for x in stage1 if x < 500]  # Double them if under 500
    
    # Apply bit manipulation: flip every other bit in lower byte
    stage3 = []
    for x in stage2:
        modified = x
        for bit_pos in [1, 3, 5, 7]:
            modified ^= (1 << bit_pos)  # Toggle specific bits
        stage3.append(modified)
    
    # Group using itertools and take max from each group
    grouped = [list(group) for k, group in itertools.groupby(stage3, key=lambda x: x // 50)]
    stage4 = [max(group) for group in grouped if len(group) >= 1]
    
    # Final transformation: use checksum as offset
    offset = compute_checksum(stage4) % 100
    final_values = [v - offset for v in stage4]
    
    # Decoy accumulation (not used)
    total_magnitude = sum(abs(v) for v in final_values)
    average_spread = sum(final_values) / len(final_values) if final_values else 0
    
    # The actual answer depends only on sum of final_values
    return sum(final_values)

# --- Main execution ---
data_stream = generate_sequence(80)

# Distraction: call irrelevant functions
_ = misleading_aggregator(data_stream)
decoy_result = [unused_transform(x) for x in data_stream[::10]]

# Key statement
final_output = process_pipeline(data_stream)

print(f"Target result: {final_output}")