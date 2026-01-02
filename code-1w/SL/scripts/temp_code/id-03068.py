def process_data(sequence):
    # Irrelevant transformation: case conversion and string manipulation
    str_repr = ''.join([chr((ord('a') + x) % 26 + 97) for x in sequence])
    temp_str = str_repr.upper()[::-1]
    decoy_value = sum([ord(c) for c in temp_str if c in 'AEIOU'])

    # Distractor: unused recursive function
    def dummy_rec(n):
        if n <= 1:
            return 1
        return n * dummy_rec(n - 2)

    # Distractor: dead code path with bitwise red herring
    flag = False
    if len(temp_str) > 100:
        mask = 0xFF
        obfuscated = [b ^ mask for b in sequence]
    else:
        # This block runs, but most computations are irrelevant
        shifted = [(x << 2) & 0xFF for x in sequence]  # Unused
        filtered = list(filter(lambda x: x % 3 == 0, sequence))  # Partially used

    # Relevant data transformation chain
    base_shift = 7
    transformed = [(x ** 2 + base_shift) & 0xFFFF for x in filtered]  # Only `filtered` matters here

    # Another decoy: complex dictionary operation with no impact
    stats = {
        'max': max(transformed, default=0),
        'min': min(transformed, default=0),
        'range': lambda: stats['max'] - stats['min'],
        'entropy': sum([x * x for x in transformed]) / (len(transformed) + 1)
    }

    # Critical computation path begins here
    multiplier = len(filtered) or 1
    adjusted = [t * multiplier for t in transformed]

    # Finalization logic
    def finalize(values):
        if not values:
            return 0
        rolling = 0
        for v in values:
            rolling = (rolling * 31 + v) % 982451653
        return rolling % 1000000

    checksum = finalize(adjusted)
    return checksum

# Main execution
input_seq = list(range(1, 18))  # [1, 2, ..., 17]
result = process_data(input_seq)
print(f"Target result: {result}")