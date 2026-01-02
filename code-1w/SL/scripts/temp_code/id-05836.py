import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(x):
    return [i ** 2 for i in x if i % 3 == 0]

# Misleading transformation chain
def corrupt_signal(signal):
    shifted = [(s << 1) ^ 0x5 for s in signal]
    filtered = [s for s in shifted if s & 1]
    return [s * 1.5 for s in filtered]  # Not used in main logic

# Core processing function with distractors
def encode_frame(frame):
    base_shift = 7
    temp_result = []
    for val in frame:
        if val > 10:  # Red herring condition (never true in input)
            temp_result.append(val ** 2)
        else:
            temp_result.append((val + base_shift) ^ 5)
    return temp_result

# Data masking with decoy operations
def mask_data(chunk, key=3):
    masked = {}
    for i, v in enumerate(chunk):
        masked[f'idx_{i}'] = (v ^ key) + (i * 2)  # Some distraction
    # Relevant part: returns XOR-sum
    xor_sum = 0
    for k, v in masked.items():
        if 'idx_' in k and int(k[4:]) % 2 == 0:
            xor_sum ^= int(v)
    return xor_sum

# Main pipeline with list comprehension and multiple concepts
def process_pipeline(stream):
    # Step 1: Decode using encode_frame (only this matters)
    decoded = encode_frame(stream)
    
    # Distractor: Attempt to corrupt (not actually used)
    corrupted = corrupt_signal(stream)
    
    # Distractor dictionary with fake diagnostics
    diagnostics = {
        'raw_sum': sum(stream),
        'shifted_max': max(corrupted) if corrupted else 0,
        'frame_size': len(decoded),
        'useless_flag': False
    }
    
    # Step 2: Transform via list comprehension (relevant)
    transformed = [math.floor(x * 0.5) for x in decoded]
    
    # Step 3: Masking stage — only mask_data matters here
    intermediate_key = mask_data(transformed)
    
    # Fake branch that doesn't alter outcome
    if diagnostics['useless_flag']:
        intermediate_key -= 100
    
    # Final computation with bitwise and arithmetic mix
    accumulator = 0
    for t in transformed:
        accumulator += (t ^ intermediate_key) & 0xF
    
    # Final output depends on correct tracing through encode_frame → transformed → mask_data → accumulator
    final_output = accumulator + intermediate_key
    
    # Print required result
    print(f"Result: {final_output}")
    return final_output

# Simulated sensor data (input)
data_stream = [2, 4, 6, 1, 8]

# Execution entry point
final_output = process_pipeline(data_stream)