def analyze_text_patterns(input_str):
    char_frequency = {}
    for char in input_str:
        if char.isalpha():
            lower_char = char.lower()
            char_frequency[lower_char] = char_frequency.get(lower_char, 0) + 1

    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    vowels_found = set(char for char in char_frequency if char in vowel_set)
    consonants_found = set(char for char in char_frequency if char not in vowel_set)

    # Distractor: compute redundant statistics
    total_vowel_count = sum(char_frequency[c] for c in vowels_found)
    total_consonant_count = sum(char_frequency[c] for c in consonants_found)
    diversity_ratio = len(vowels_found) / (len(consonants_found) + 1)

    # Semi-relevant transformation
    shifted_counts = {chr((ord(k) - ord('a') + 2) % 26 + ord('a')): v ** 0.5 
                      for k, v in char_frequency.items()}

    # Dummy accumulator with partial use
    temp_sum = 0
    for idx, count in enumerate(char_frequency.values()):
        if idx % 2 == 0:
            temp_sum += count * 1.5
        else:
            temp_sum += count * 0.8

    return vowels_found, consonants_found, total_vowel_count


def generate_combinatorial_weights(n):
    # Irrelevant combinatorics function (red herring)
    weights = [1]
    for i in range(1, n+1):
        next_weight = weights[-1] * i
        weights.append(next_weight)
    trimmed = [w for w in weights if w < 10000]  # unused
    return weights[:5]


def calculate_final_score(text, base_multiplier=3.7):
    # Main logic begins
    cleaned = ''.join(ch for ch in text if ch.isalnum())
    upper_count = sum(1 for ch in cleaned if ch.isupper())
    lower_count = len(cleaned) - upper_count

    # Use analysis function
    vowels, consonants, vowel_total = analyze_text_patterns(text)

    # Key computation branch
    if len(vowels) >= 3 and len(consonants) >= 5:
        size_factor = len(set(cleaned.lower()))
        case_penalty = abs(upper_count - lower_count) * 0.3
        
        # Dummy nested loop (distractor)
        dummy_matrix = [[i * j for j in range(3)] for i in range(2)]
        accumulation_trace = 0
        for row in dummy_matrix:
            for val in row:
                accumulation_trace += val ** 2

        # Another red herring: combinatorics
        comb_weights = generate_combinatorial_weights(6)
        weight_offset = sum(w * 0.1 for w in comb_weights if w % 2 == 0)

        # Core formula
        raw_score = (vowel_total * base_multiplier) + (size_factor * 4.2)
        adjusted_score = raw_score - case_penalty + weight_offset
        final_score = int(round(adjusted_score))
    else:
        final_score = 10  # unreachable in main case

    return final_score

# Execution entry point
input_text = "DynamicProgrammingWithComplexPatternsAndMixedCASE"
result = calculate_final_score(input_text)
print(f"Target result: {result}")