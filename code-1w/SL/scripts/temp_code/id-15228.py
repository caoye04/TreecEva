import itertools

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum(i ** 2 for i in x if i % 3 == 0)

# Decoy transformation chain
def decoy_transform(seq):
    a = [x * 2 + 1 for x in seq]
    b = [y for y in a if y < 50]
    c = sorted(b, reverse=True)
    return c[:10] if len(c) > 5 else c

# Real processing components
def filter_valid_packets(stream):
    return [p for p in stream if (p & 0b1100) >> 2 == 3]

def compute_checksum(chunk):
    chk = 0
    for val in chunk:
        chk ^= val  # Bitwise XOR accumulation
        chk = (chk + (chk << 1)) % 257  # Nonlinear mod step
    return chk

def extract_payload(header_masked_data):
    return [d & 0xFF for d in header_masked_data][1::2]  # Take odd indices, mask to byte

def rolling_window_avg(values, window_size=3):
    if len(values) < window_size:
        return [sum(values)/len(values)] if values else [0]
    avgs = []
    for i in range(len(values) - window_size + 1):
        avgs.append(sum(values[i:i+window_size]) / window_size)
    return avgs

# Complex conditional expression used in pipeline
def select_mode(flag_list):
    return 'aggressive' if sum(flag_list) > 5 else 'conservative' if any(f == 0 for f in flag_list) else 'balanced'

# Main data processing pipeline
def process_pipeline(raw_input):
    # Step 1: Filter valid packets based on bit pattern
    stage1 = filter_valid_packets(raw_input)
    
    # Distractor computation (not used later)
    temp_analysis = [x for x in stage1 if x % 7 == 0 and x > 10]
    magnitude_score = len(temp_analysis) * max(temp_analysis) if temp_analysis else -1
    
    # Step 2: Extract payload bytes
    stage2 = extract_payload(stage1)
    
    # Step 3: Compute checksum of original filtered data
    chksum = compute_checksum(stage1)
    
    # Step 4: Apply rolling average with conditional window logic
    window_mode = 'large' if chksum > 100 else 'small'
    window_size = 4 if window_mode == 'large' else 2
    
    # Conditional expression for smoothing
    smoothed = rolling_window_avg(stage2, window_size) if len(stage2) >= window_size else stage2
    
    # Step 5: Further filtering using logical operations
    flags = [(x > 15) and ((x & 1) == 0) for x in smoothed if isinstance(x, int)]
    flag_sum = sum(flags)
    
    # Another decoy structure
    decoy_matrix = [[i + j for j in range(5)] for i in range(3)]
    decoy_stats = list(itertools.chain.from_iterable(decoy_matrix))
    
    # Step 6: Final mode selection influences output
    operational_mode = select_mode(flags + [flag_sum])
    
    # Final computation branch
    if operational_mode == 'aggressive':
        result_base = sum(smoothed) * chksum
    elif operational_mode == 'balanced':
        result_base = int(max(smoothed or [0]) * 100)
    else:
        # conservative mode
        avg_val = sum(smoothed) / len(smoothed) if smoothed else 0
        result_base = int(avg_val * chksum // 2)
    
    # Critical red herring: this looks important but isn't final
    intermediate_result = (result_base ^ 0xFFFF) & 0xFFF
    
    # Actual final output calculation
    adjustment_factor = len([x for x in raw_input if x & 0b1])  # Count odd inputs
    final_output = result_base - adjustment_factor
    
    return final_output

# Simulated sensor data stream (deterministic input)
data_stream = [
    0b110101, 0b110010, 0b101001, 0b110111,
    0b110001, 0b111110, 0b100011, 0b110101,
    0b111100, 0b110011
]

# Execute main logic
final_output = process_pipeline(data_stream)
print(f"Target result: {final_output}")