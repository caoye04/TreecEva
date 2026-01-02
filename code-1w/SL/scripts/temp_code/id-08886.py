def analyze_frequency(text):
    # Irrelevant helper: counts character frequencies (not used in final logic)
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char.lower()] = freq.get(char.lower(), 0) + 1
    return freq


def validate_checksum(sequence):
    # Semi-relevant: checksum validation, but only side-effect used
    total = 0
    for i, val in enumerate(sequence):
        total += val * (i + 1)
    remainder = total % 11
    return remainder == 0


def extract_segments(data_string):
    # Splits string into chunks – partially relevant
    segments = data_string.split('-')
    lengths = [len(s) for s in segments]  # Used later
    return segments, lengths


def calculate_modifiers(keys):
    # Computes modifier array using set operations and comparisons
    base_set = {1, 2, 3, 4, 5}
    result_mods = []
    for k in keys:
        temp_set = {x for x in range(k)}
        intersection = base_set & temp_set
        if len(intersection) >= 2:
            result_mods.append(len(intersection) * 0.5)
        else:
            result_mods.append(0.1)
    return result_mods


def calculate_final_score(raw_data, mods):
    # Main scoring logic with dictionary lookups and arithmetic
    scores = {}
    tokens, sizes = extract_segments(raw_data)
    
    temp_tracker = []
    for i, token in enumerate(tokens):
        # Character counting logic
        vowel_count = sum(1 for c in token if c.lower() in 'aeiou')
        const_count = len(token) - vowel_count
        
        # Dictionary accumulation
        key = f"item_{i}"
        scores[key] = {
            'vowels': vowel_count,
            'consonants': const_count,
            'total': len(token),
            'ratio': round(vowel_count / len(token), 3) if len(token) > 0 else 0
        }
        temp_tracker.append(const_count)
    
    # Aggregate base score using consonant totals and sizes (redundant check)
    base_score = sum(entry['consonants'] for entry in scores.values())
    size_bonus = sum(sizes) * 0.2
    
    # Apply modifiers
    adjusted_mods = calculate_modifiers([len(t) for t in tokens])
    mod_adjustment = sum(m for m in adjusted_mods)
    
    # Final computation chain
    intermediate = base_score + size_bonus
    final_score = intermediate * (1 + mod_adjustment)
    
    # Dead code path: never executed due to prior conditions
    if False and validate_checksum([len(t) for t in tokens]):
        final_score *= 0.9
    
    # Key red herring variables
    debug_info = analyze_frequency(raw_data)  # Computed but unused
    checksum_valid = validate_checksum(list(range(len(tokens))))  # Unused boolean
    
    return int(round(final_score))

# Execution block
if __name__ == "__main__":
    raw_input = "Dream-Light-Stream-Zone"
    config_keys = [5, 4, 6, 4]
    modifiers = calculate_modifiers(config_keys)
    final_score = calculate_final_score(raw_input, modifiers)
    print(f"Target result: {final_score}")