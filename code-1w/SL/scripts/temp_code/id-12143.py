def process_sequence(data: str) -> int:
    # Simulate a data integrity check with distraction logic
    base_value = 17
    temp_accum = 0
    checksum = 0
    offset = len(data) % 8
    
    # Irrelevant statistical counters (distractors)
    vowel_count = 0
    digit_sum = 0
    symbol_weight = 0
    
    for i, char in enumerate(data):
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel_count += 1
            # Real logic branch
            ordinal = ord(char.lower()) - ord('a') + 1
            temp_accum += (ordinal * (i + 1))
        elif char.isdigit():
            digit_sum += int(char)
            temp_accum += digit_sum ** 2
        else:
            symbol_weight += ord(char) % 5

        # Core checksum update (only this affects final answer)
        checksum += ord(char) + i * offset
        if (i + 1) % 3 == 0:
            checksum = (checksum * 3) % 97  # Key statement

    # Dead code path (never executed under normal input)
    if len(data) > 1000:
        extra = ''.join(sorted(data, reverse=True))
        checksum += hash(extra) % 100

    # Final irrelevant transformation
    final_length = len(data.replace(' ', '').strip())
    scaling_factor = (final_length + 5) // 6
    dummy_result = (base_value + temp_accum) * scaling_factor

    return checksum

# Input string with mixed content
input_data = "B7!kPx$2qR"
result = process_sequence(input_data)
print(f"Result: {result}")