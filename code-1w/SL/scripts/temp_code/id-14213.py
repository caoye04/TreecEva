def analyze_text_patterns(text_data):
    char_frequency = {}
    for char in text_data:
        if char.isalpha():
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1

    # Distractor: Compute average length of words (not used later)
    words = text_data.split()
    total_length = sum(len(word) for word in words)
    avg_word_length = total_length / len(words) if words else 0

    # Relevant: Find max frequency and count vowels
    max_freq = max(char_frequency.values()) if char_frequency else 0
    vowel_count = sum(count for char, count in char_frequency.items() if char in 'aeiou')

    # Semi-relevant transformation
    normalized_score = sum(count / max_freq for count in char_frequency.values()) if max_freq > 0 else 0

    return vowel_count, normalized_score, len(char_frequency)


def calculate_final_score(input_string, threshold=3):
    # Intermediate processing with distractors
    reversed_lines = [line[::-1] for line in input_string.split('\n')]
    flat_chars = ''.join(reversed_lines)

    # Call analysis function
    vowels, norm_score, unique_letters = analyze_text_patterns(flat_chars)

    # Distractor: Simulate unused pattern matching
    patterns_found = 0
    for i in range(len(flat_chars) - 1):
        if flat_chars[i] == flat_chars[i+1]:
            patterns_found += 1  # Unused variable

    # Distractor: Unused list comprehension with zip
    paired_data = [(a, b) for a, b in zip(flat_chars, flat_chars[1:]) if a != b]
    entropy_approx = len(paired_data) / len(flat_chars) if flat_chars else 0

    # Core logic: compute score based on vowels and uniqueness
    base_value = vowels * 7
    bonus = unique_letters * 2 if norm_score > threshold else unique_letters
    penalty = len([c for c in flat_chars if not c.isalpha()]) * 3

    final_score = base_value + bonus - penalty

    # Additional irrelevant accumulation
    cumulative_sum = 0
    for index, char in enumerate(flat_chars):
        if char in 'aeiou':
            cumulative_sum += index * ord(char) % 5
    # Not affecting final_score

    return final_score

# Main execution
input_text = "Hello\nWorld This is a Sample Text!\nWith Numbers 123 and Symbols @#$"
final_score = calculate_final_score(input_text)
print(f"Result: {final_score}")