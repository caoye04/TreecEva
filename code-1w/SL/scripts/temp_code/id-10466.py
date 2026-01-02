def process_sequence(data):
    # Irrelevant transformation: frequency analysis (dead-end)
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    
    # Distractor: unused complex list comprehension
    expanded = [x * 2 + (i % 3) for i, x in enumerate(data) if x % 2 == 0]
    expanded = [e for e in expanded if e in freq_map]  # Misleading filter

    # Real logic begins: extract every third element
    subset = data[::3]
    
    # Apply bitwise twist: XOR with index
    twisted = []
    for idx, val in enumerate(subset):
        twisted.append(val ^ idx)
    
    # Sum positive twisted values
    sum_twisted = sum(x for x in twisted if x > 0)

    # Secondary path: set operations on slices (partially relevant)
    left_half = set(data[:len(data)//2])
    right_half = set(data[len(data)//2:])
    symmetric_diff = left_half ^ right_half  # XOR of sets
    intersection = left_half & right_half

    # Distractor: unused transformations
    outliers = {x for x in symmetric_diff if x > sum_twisted // 4}
    adjusted = [x - 1 for x in intersection if x > 5]

    # Filtering based on bit count (real path)
    def has_odd_ones(n):
        return bin(n).count('1') % 2 == 1

    filtered = [x for x in twisted if has_odd_ones(x)]
    sum_filtered = sum(filtered)

    # Masking via bit operation
    mask = (1 << 7) - 1  # 127

    # Finalize function (obscured relevance)
    def finalize(x):
        temp = x >> 2
        temp = temp ^ 987  # arbitrary constant
        return temp & 0xFFFF  # clamp to 16 bits

    checksum = finalize(sum_filtered & mask)

    # Dead code path: never executed but looks important
    if len(outliers) > 100:
        backup = sum(adjusted) ^ sum(expanded)
        checksum ^= backup

    return checksum

# Main execution
sequence = list(range(89, 124)) + [x * 2 for x in range(15, 25)]
result = process_sequence(sequence)
print(f"Result: {result}")