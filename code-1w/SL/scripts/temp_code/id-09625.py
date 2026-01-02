def analyze_string_data(input_str):
    # Irrelevant counters and transformations (distractors)
    temp_buffer = []
    redundant_sum = 0
    dummy_flag = False
    for char in input_str:
        if char.isdigit():
            redundant_sum += int(char) ** 2
        elif char.isalpha():
            temp_buffer.append(char.lower())
        if char == 'X':
            dummy_flag = True  # Dead logic, never used later

    # Misleading intermediate transformation
    reversed_temp = ''.join(temp_buffer[::-1])
    magic_offset = len(reversed_temp) % 7

    # Real computation begins: count valid alphabetic characters in specific pattern
    valid_count = 0
    search_pattern = 'pattern_to_find'
    fake_cache = {c: input_str.count(c) for c in 'xyz'}  # Useless cache

    # Core logic: find consecutive vowel-consonant pairs
    vowels = set('aeiou')
    i = 0
    while i < len(input_str) - 1:
        current, next_char = input_str[i].lower(), input_str[i+1].lower()
        if current.isalpha() and next_char.isalpha():
            if current in vowels and next_char not in vowels:
                valid_count += 1
                i += 2  # Skip next to avoid overlap
                continue
        i += 1

    # Another red herring: bit manipulation with no impact
    decoy_value = 0
    for v in fake_cache.values():
        decoy_value ^= (v << 2) | 3
        decoy_value &= 0xFF

    # Character frequency analysis (partially relevant)
    char_freq = {}
    for ch in input_str.lower():
        if ch.isalpha():
            char_freq[ch] = char_freq.get(ch, 0) + 1

    # Extract unique consonants (distraction from main path)
    seen = set()
    unique_consonants = []
    for k in char_freq.keys():
        if k not in vowels and k not in seen:
            unique_consonants.append(k)
            seen.add(k)

    # Prime offset based on length (actually used)
    base_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    prime_offset = base_primes[len(input_str) % 10]

    # Digit sum calculation (used in final result)
    digit_sum = sum(int(c) for c in input_str if c.isdigit())

    # Critical statement: combines valid_count, prime_offset, and digit_sum
    checksum = (valid_count * prime_offset) + digit_sum

    # Final unrelated operation (to confuse flow)
    if len(unique_consonants) > magic_offset:
        checksum -= decoy_value  # Never triggers due to constraints

    return checksum

# Main execution
data_stream = 'aE3kP9uRiO2xXzZ1eI4nMm8qA7'
result = analyze_string_data(data_stream)
print(f"Target result: {result}")