def calculate_final_score(raw_data):
    # Preprocessing: clean and normalize input
    cleaned = [x.strip().lower() for x in raw_data if len(x.strip()) > 0]
    
    # Irrelevant transformation (distractor)
    reversed_strings = [s[::-1] for s in cleaned]
    upper_version = [s.upper() for s in cleaned]

    # Count specific character patterns (semi-relevant)
    vowel_count = 0
    total_chars = 0
    for entry in cleaned:
        total_chars += len(entry)
        for char in entry:
            if char in 'aeiou':
                vowel_count += 1

    # Compute entropy-like metric (not used, distractor)
    import math
    entropy = 0.0
    if total_chars > 0:
        freq = vowel_count / total_chars
        if freq > 0 and freq < 1:
            entropy = - (freq * math.log2(freq) + (1-freq) * math.log2(1-freq))

    # Core logic: count entries with even length and at least one digit
    valid_entries = 0
    has_digit_flag = False
    for entry in cleaned:
        has_digit_flag = any(c.isdigit() for c in entry)
        length_ok = (len(entry) % 2 == 0)
        if has_digit_flag and length_ok:
            valid_entries += 1

    # Secondary filter: must contain 'x' or 'y'
    filtered_valid = 0
    for entry in cleaned:
        has_digit_flag = any(c.isdigit() for c in entry)
        even_length = (len(entry) % 2 == 0)
        contains_xy = 'x' in entry or 'y' in entry
        if has_digit_flag and even_length and contains_xy:
            filtered_valid += 1

    # Final score computation
    bonus = 5 if filtered_valid > 0 else 0
    base_score = valid_entries * 7
    penalty = len(reversed_strings) - len(cleaned)  # Always zero, but looks suspicious
    final_score = base_score + bonus + penalty

    # Dead code path (distractor)
    if False:
        final_score *= 2
        final_score += sum(ord(c) for c in upper_version[0]) if upper_version else 0

    return final_score

# Input data
input_data = [' Abc1 ', 'xy2z', 'nope', 'a4', 'test9x', '1234', 'xYz8']

# Execute
result = calculate_final_score(input_data)
print(f"Result: {result}")