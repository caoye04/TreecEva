def analyze_pattern(seq):
    # Irrelevant analysis function (dead code path)
    count = 0
    for x in seq:
        if x % 3 == 0:
            count += 1
    return count


def validate_checksum(stream):
    # Distractor: looks important but unused in final logic
    checksum = 0
    for i, val in enumerate(stream):
        checksum ^= val * (i + 1)
    return checksum > 50


def transform_entry(val, index):
    # Bit manipulation with red herring operations
    temp_shift = (val << 2) & 0xFF
    masked = temp_shift | (index & 0x0F)
    fake_norm = (val + index) / max(1, sum([1 for _ in range(3)]))  # constant distraction
    return temp_shift ^ index


def generate_pairs(iterable):
    # Unused helper – creates illusion of complexity
    return list(zip(iterable, iterable[1:]))


def process_sequence(data):
    # Core logic hidden among noise
    temp_result = []
    for idx, item in enumerate(data):
        transformed = transform_entry(item, idx)
        temp_result.append(transformed)
    
    # Real computation begins here — obscured by prior distractions
    filtered = [x for x in temp_result if x % 4 == 2]
    offset = len(temp_result) - len(filtered)
    accumulator = 0
    
    # Actual arithmetic chain determining the answer
    for num in filtered:
        accumulator += num * 2
        if accumulator > 100:
            accumulator -= 85  # Resetting mechanic to obscure pattern
    
    # Final adjustment based on control flow history
    if offset > 3:
        accumulator *= 2
    else:
        accumulator += 17
    
    scaling_factor = 1.0  # Misleading float usage
    scaling_factor *= 3  # Looks like it matters
    scaling_factor = int(scaling_factor)  # Convert back, distracts type tracking
    
    # Critical line: this is where the answer is determined
    final_output = accumulator // scaling_factor
    
    # Dead code branch – appears reachable but isn't due to logic above
    if validate_checksum(data):
        alternate = sum(data) >> 3
        final_output = alternate  # Never executed under current inputs
    
    return final_output

# Main execution context
sequence_metadata = {"version": "2.1", "mode": "legacy"}  # Unused config
auxiliary_buffer = [x**2 for x in range(15) if x % 4 != 2]  # Irrelevant data structure

# Primary input stream – key to deterministic result
data_stream = [7, 12, 9, 14, 3, 18, 22, 27, 31]

# Trigger processing
final_output = process_sequence(data_stream)

# Output result as required
print(f"Target result: {final_output}")