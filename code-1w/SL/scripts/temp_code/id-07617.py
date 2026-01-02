def analyze_data_stream(raw_input):
    # Real processing variables
    checksum = 0
    mask = 0xFFFF
    data_segments = raw_input[::2]  # Slice: every second byte for actual processing
    temp_buffer = [x ^ 0xAA for x in raw_input]  # Distractor: unused transformation
    
    # Irrelevant statistical counters (red herrings)
    entropy_count = 0
    peak_magnitude = 0
    shadow_accumulator = 0
    
    for x in temp_buffer:
        if x > 128:
            entropy_count += 1
        if x > peak_magnitude:
            peak_magnitude = x  # Dead path: never used
    
    # Secondary distractor: complex but unused structure
    lookup_table = {i: (i * 2654435761 % 2**32) for i in range(16)}
    decoy_state = sum(lookup_table.get(i, 0) for i in range(0, len(raw_input), 3)) % 256
    
    # Actual logic buried in noise
    processed_values = []
    for idx, val in enumerate(data_segments):
        if idx % 3 == 0:
            shifted = val >> (idx % 5)
            processed_value = (shifted + idx) % 256
            processed_values.append(processed_value)
            
            # Core update hidden in conditional
            if len(processed_values) == 3:  # Only first three are relevant
                for p_val in processed_values:
                    checksum = (checksum << 1) ^ p_val & mask
        else:
            # More irrelevant computation
            shadow_accumulator += val * (val % 17)
    
    # Fake finalization step
    dummy_hash = ''.join([hex(checksum ^ i)[-1] for i in range(8)])  # Unused string op
    
    # Critical statement embedded in final logic
    # At this point, checksum has been fully updated
    return checksum

# Input data constructed to yield deterministic result
input_stream = [187, 42, 115, 88, 203, 73, 91, 102, 67, 55, 144, 39]
result = analyze_data_stream(input_stream)
print(f"Result: {result}")