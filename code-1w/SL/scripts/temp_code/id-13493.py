def analyze_pattern(sequence):
    # Irrelevant transformation: counts vowels in string representation
    str_seq = ''.join(map(str, sequence))
    vowel_count = sum(1 for c in str_seq.lower() if c in 'aeiou')

    # Distractor: complex but unused calculation involving bitwise and exponentiation
    decoy_value = (vowel_count ** 2) ^ (len(str_seq) << 3)
    temp_result = [x * 2 + 1 for x in sequence if x % 2 == 0]

    # Dead code path: never executed due to condition
    if False:
        decoy_value -= sum(temp_result) // (vowel_count or 1)
        return decoy_value

    # Relevant logic begins here
    filtered = [x for x in sequence if x > 0]
    shifted = [x >> 1 for x in filtered]  # Integer division by 2 via bit shift

    # Conditional expression with slicing distraction
    midpoint = len(shifted) // 2
    left_half = shifted[:midpoint]
    right_half = shifted[midpoint:]
    adjusted = [x + (1 if i % 2 == 0 else -1) for i, x in enumerate(right_half)]

    # Summation with conditional offset
    base_sum = sum(adjusted)
    length_factor = len(adjusted) if adjusted else 1

    # Another red herring: string method on numeric cast
    str_sum = str(base_sum)
    mirrored_str = str_sum[::-1]  # String slicing reverse
    if mirrored_str == str_sum and base_sum != 0:
        base_sum += 100  # Trigger avoided unless palindrome

    # Key recursive helper function — actually used
    def recursive_transform(n):
        if n <= 1:
            return 1
        return n + recursive_transform(n // 3)

    # Critical dependency on recursive result
    bonus = recursive_transform(length_factor)

    # Final aggregation logic
    final_score = base_sum * 2 + bonus - len(left_half)

    # Output required format
    print(f"Result: {final_score}")
    return final_score

# Misleading initialization block
raw_data = [3, -2, 7, 8, 0, 12, 5]
data_checksum = sum(x ^ 2 for x in raw_data)  # Unused
normalization_factor = max(raw_data) / (min(raw_data[1:]) or 1)  # Irrelevant

# Actual execution point
result = analyze_pattern([6, 10, 15, 21, 28])