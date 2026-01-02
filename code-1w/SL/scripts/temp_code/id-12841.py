def analyze_sequence(data):
    # Irrelevant transformation: character frequency map (dead path)
    char_freq = {}
    for item in data:
        if isinstance(item, str):
            for c in item.lower():
                char_freq[c] = char_freq.get(c, 0) + 1

    # Distractor: complex but unused bitwise cascade
    magic_offset = 0
    for i in range(len(data)):
        if isinstance(data[i], int):
            magic_offset ^= (data[i] << 2) | (i & 3)
            magic_offset -= (magic_offset >> 4) ^ 17

    # Real logic begins: extract and filter numeric values
    filtered = [x for x in data if isinstance(x, int) and x > 0]

    # Distractor: unused recursive reduction
    def deep_reduce(seq):
        if len(seq) <= 1:
            return seq[0] if seq else 1
        mid = len(seq) // 2
        left = deep_reduce(seq[:mid])
        right = deep_reduce(seq[mid:])
        return (left ^ right) + (left * right) % 97

    # Real computation: summation with conditional scaling
    base_sum = sum(filtered)
    scale = 2 if len(filtered) > 3 else 1
    adjusted = base_sum * scale

    # Conditional expression (required Python feature)
    mode_flag = 5 if any(x % 2 == 0 for x in filtered) else -3

    # Secondary distractor: tuple-based state that goes unused
    status_tuple = ('ANALYZED', len(filtered), mode_flag)
    shadow_state = (status_tuple[1] ^ mode_flag, len(char_freq) if char_freq else 0)

    # Bit manipulation chain (relevant)
    bits = adjusted
    for _ in range(3):
        bits = ((bits << 1) | (bits >> 31)) & 0xFFFFFFFF  # Rotate left 1 bit
    bits = bits ^ 0xAA55AA55

    # Flag construction (partially relevant)
    flags = set()
    if adjusted > 100:
        flags.add('HIGH')
    if mode_flag == 5:
        flags.add('EVEN_PRESENT')
    if len(filtered) % 2 == 0:
        flags.add('EVEN_COUNT')

    # Decoy function call with misleading name
    def validate_integrity(x):
        return (x ^ (x << 5)) & 0xFFFF
    
    # Unused validation
    integrity = validate_integrity(adjusted)

    # Critical path: summation and flags passed to finalize
    summation = adjusted + (mode_flag * 2)

    # Finalization function defined inside (abstraction layer)
    def finalize(value, flag_set):
        result = value
        if 'HIGH' in flag_set:
            result = (result ^ 0x5A5A) + 13
        if 'EVEN_PRESENT' in flag_set:
            result = (result * 2) + (result & 7)
        if 'EVEN_COUNT' in flag_set:
            result = (result >> 1) ^ 123
        return result + len(flag_set)

    checksum = finalize(summation, flags)
    return checksum

# Input data with mixed types (realistic scenario)
data_stream = [15, 'temp', 22, -5, 8, 'log', 44, 3.14, 9]

# Execute and print target result
target_result = analyze_sequence(data_stream)
print(f"Result: {target_result}")