def process_sequence(sequence):
    base_offset = 7
    temp_buffer = []
    checksum = 0
    multiplier = 3
    offset_map = {i: (i * base_offset) % 26 for i in range(10)}

    # Initialize transformed sequence with case-aware shifts
    for i, char in enumerate(sequence):
        if char.isalpha():
            shift = offset_map.get(i % 10, 0)
            new_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            if char.isupper():
                new_char = new_char.upper()
            temp_buffer.append(new_char)
        else:
            temp_buffer.append(char)

    # Apply scrambling using slicing and reversal heuristics
    mid = len(temp_buffer) // 2
    left_half = temp_buffer[:mid][::-1]  # reversed left half
    right_half = temp_buffer[mid:]       # original right half
    scrambled = left_half + right_half

    # Spurious accumulation - looks important but unused
    dummy_accumulator = 0
    for idx, item in enumerate(scrambled):
        if idx % 2 == 0 and item.isalpha():
            dummy_accumulator += ord(item) * (idx + 1)

    # Actual checksum computation happens here - key logic
    raw_string = ''.join(scrambled)
    for c in raw_string:
        if c.isalnum():
            checksum = (checksum + ord(c)) % 97  # critical statement

    # Red herring: another unused calculation
    verification_code = 0
    for i in range(len(raw_string)):
        if raw_string[i].isdigit():
            verification_code = (verification_code * 11 + int(raw_string[i])) % 10007

    return checksum

# Entry point
data_stream = "B3ndMy_8rR0w5!"
result = process_sequence(data_stream)
print(f"Result: {result}")